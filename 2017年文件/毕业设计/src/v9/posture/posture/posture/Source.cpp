#include <opencv2\opencv.hpp> 
#include <iostream>
#include <stdio.h>
#include <windows.h> 
#include "AKWPosition.cpp" 
 
#define FILE_NAME "D:\\poisture.yml"

using namespace cv;
using namespace std;


static int threshold_diff = 25;//���ü�֡���ֵ   

AKWPosition *poi = new AKWPosition;

double width = GetSystemMetrics(SM_CXSCREEN);
double height = GetSystemMetrics(SM_CYSCREEN);


//��ȡ����
int my_read(char* key) {
	int result;
	cv::FileStorage fs(FILE_NAME, FileStorage::READ);
	fs[key] >> result;
	fs.release();
	return result;
}
//��������¼�
void  my_click(double x, double y) {
	x = int(x*width);
	y = int(y*height);
	SetCursorPos(x, y);
	//mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, x, y, 0, 0);
}
//�ɹ���������
void callback_success(double x, double y) {
	poi->poi(x, y);
	if (x > 0 && y > 0 && x < 1 && y < 1) {
		my_click(x, y);
	}
}
//û�з�������
void callback_error() {
	MessageBox(NULL, TEXT("δ��⵽����ͷ"), NULL, MB_OK);
}


int app(int threshold_diff) { 
	Mat frame1, frame2, frame3, gray_3, gray_2, gray_1;
	Mat gray, gray_diff1, gray_diff2;//�洢2�������ͼƬ  
	Mat gray_diff11, gray_diff12;
	Mat gray_diff21, gray_diff22;
	//��ȡ��Ƶ������ͷ  
	VideoCapture capture(0);
	if (capture.isOpened() == false) {
		callback_error();
		return false;
	}

	capture >> frame1;
	/// תΪ�Ҷ�ͼ
	cvtColor(frame1, gray_1, CV_BGR2GRAY);

	capture >> frame2;
	cvtColor(frame2, gray_2, CV_BGR2GRAY);


	while (capture.isOpened())
	{
		Mat dst, thre, pre, demo;

		double x, y;
		capture >> frame3;

		imshow("foreground", frame3);
		//imshow("frame", frame3);
		/// תΪ�Ҷ�ͼ
		cvtColor(frame3, gray_3, CV_BGR2GRAY);


		subtract(gray_2, gray_1, gray_diff11);//�ڶ�֡����һ֡  gray_diff11=gray_2-gray_1
		subtract(gray_1, gray_2, gray_diff12);
		add(gray_diff11, gray_diff12, gray_diff1);
		subtract(gray_3, gray_2, gray_diff21);//����֡���ڶ�֡  
		subtract(gray_2, gray_3, gray_diff22);
		add(gray_diff21, gray_diff22, gray_diff2);
		for (int i = 0; i<gray_diff1.rows; i++)
			for (int j = 0; j<gray_diff1.cols; j++)
			{
				if (abs(gray_diff1.at<unsigned char>(i, j)) >= threshold_diff)//����ģ�����һ��Ҫ��unsigned char�������һֱ����  
					gray_diff1.at<unsigned char>(i, j) = 255;            //��һ�������ֵ����  
				else gray_diff1.at<unsigned char>(i, j) = 0;

				if (abs(gray_diff2.at<unsigned char>(i, j)) >= threshold_diff)//�ڶ��������ֵ����  
					gray_diff2.at<unsigned char>(i, j) = 255;
				else gray_diff2.at<unsigned char>(i, j) = 0;
			}
		bitwise_and(gray_diff1, gray_diff2, gray);

		//dilate(gray, gray, Mat()); //ͼ������
		erode(gray, gray, Mat());  //ͼ��ʴ

		medianBlur(gray, dst, 15);




		vector<vector<Point>> contours;
		findContours(dst, contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);

		for (int i = 0; i < (int)contours.size(); i++)
		{

			int x_max = 0;
			int y_max = 0;
			int x_min = 0;
			int y_min = 0;
			//�����������
			double mianji = contourArea(contours[i]);
			if (mianji>(width*height) / 4) {
				continue;
			}
			for (int j = 0; j < (int)contours[i].size(); j++) {
				if (j == 0) {
					x_min = contours[i][j].x;
					y_min = contours[i][j].y;
				}
				if (x_min > contours[i][j].x) {
					x_min = contours[i][j].x;
				}
				if (y_min > contours[i][j].y) {
					y_min = contours[i][j].y;
				}
				if (x_max < contours[i][j].x) {
					x_max = contours[i][j].x;
				}
				if (y_max < contours[i][j].y) {
					y_max = contours[i][j].y;
				}
			}
			if (x_max - x_min == 0 || y_max - y_min == 0) {
				continue;
			}
			//���ݱ�������
			if ((y_max - y_min) / (x_max - x_min) > 4 || (x_max - x_min) / (y_max - y_min) > 4) {
				continue;
			}

			//�ҵ����ĵ�ת������
			x = int((x_max + x_min) / 2);
			y = int((y_max + y_min) / 2);
			callback_success(x,y); 
		}


		gray_1 = gray_2.clone();
		gray_2 = gray_3.clone();
		if (waitKey(10) == 'q') {
			return 0;
		}
	}
	return 0;
}




int _stdcall WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow
) {

	HANDLE hMutex = CreateMutex(NULL, FALSE, TEXT("XXX_0D0DDD11-5E3F-4287-BB74-7E3D2C7720EF"));
	//��ʵ��
	if (WaitForSingleObject(hMutex, 100) == WAIT_TIMEOUT) { 
		return FALSE; 
	} 
	double x0 = my_read("x_1");
	double y0 = my_read("y_1");
	double x_1 = my_read("x_2");
	double y_1 = my_read("y_2");
	double x_2 = my_read("x_3");
	double y_2 = my_read("y_3");
	double x_3 = my_read("x_4");
	double y_3 = my_read("y_4");
	threshold_diff = my_read("threshold"); 
	poi->init(x0, y0, x_1, y_1, x_2, y_2, x_3, y_3, width, height); 
	app(threshold_diff);
}
