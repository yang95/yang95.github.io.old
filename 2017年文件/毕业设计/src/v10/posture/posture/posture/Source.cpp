#include <opencv2\opencv.hpp> 
#include <iostream>
#include <stdio.h>
#include <windows.h> 
#include "AKWPosition.cpp" 
 

using namespace cv;
using namespace std;

LPCWSTR FILE_NAME = L"./posture.conf";
LPCWSTR conf_str = L"posture";
int iread(LPCWSTR key1, LPCWSTR key12) {
	return GetPrivateProfileInt(key1, key12, 0, FILE_NAME);
}

int cap_index = iread(conf_str,L"cap_index");
int a_1 = iread(conf_str, L"a_1");
int b_1 = iread(conf_str, L"b_1");
int width = iread(conf_str, L"width");
int height = iread(conf_str, L"height");
static int threshold_diff = 25;//设置简单帧差法阈值   

AKWPosition *poi = new AKWPosition;
 //产生鼠标事件
void  my_click(double x, double y) {
	poi->poi(x, y);
	if (x*y>0 && x<1 && y< 1) {
		poi->z_poi(x, y, a_1, b_1, width, height);
		SetCursorPos(x, y);
		mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, x, y, 0, 0);
	} 
}
int app() { 
	Mat frame1, frame2, frame3, gray_3, gray_2, gray_1;
	Mat gray, gray_diff1, gray_diff2;//存储2次相减的图片  
	Mat gray_diff11, gray_diff12;
	Mat gray_diff21, gray_diff22;
	//读取视频或摄像头  
	VideoCapture capture(cap_index);
	if (capture.isOpened() == false) { 
		MessageBox(NULL, TEXT("没有摄像头"), NULL, MB_OK);
		exit(0); 
	} 
	capture >> frame1;
	/// 转为灰度图
	cvtColor(frame1, gray_1, CV_BGR2GRAY); 
	capture >> frame2;
	cvtColor(frame2, gray_2, CV_BGR2GRAY); 

	while (capture.isOpened())
	{
		Mat dst, thre, pre, demo;

		double x, y;
		capture >> frame3;

		/// 转为灰度图
		cvtColor(frame3, gray_3, CV_BGR2GRAY);


		subtract(gray_2, gray_1, gray_diff11);//第二帧减第一帧  gray_diff11=gray_2-gray_1
		subtract(gray_1, gray_2, gray_diff12);
		add(gray_diff11, gray_diff12, gray_diff1);
		subtract(gray_3, gray_2, gray_diff21);//第三帧减第二帧  
		subtract(gray_2, gray_3, gray_diff22);
		add(gray_diff21, gray_diff22, gray_diff2);
		for (int i = 0; i<gray_diff1.rows; i++)
			for (int j = 0; j<gray_diff1.cols; j++)
			{
				if (abs(gray_diff1.at<unsigned char>(i, j)) >= threshold_diff)//这里模板参数一定要用unsigned char，否则就一直报错  
					gray_diff1.at<unsigned char>(i, j) = 255;            //第一次相减阈值处理  
				else gray_diff1.at<unsigned char>(i, j) = 0;

				if (abs(gray_diff2.at<unsigned char>(i, j)) >= threshold_diff)//第二次相减阈值处理  
					gray_diff2.at<unsigned char>(i, j) = 255;
				else gray_diff2.at<unsigned char>(i, j) = 0;
			}
		bitwise_and(gray_diff1, gray_diff2, gray);


		//dilate(gray, gray, Mat()); //图像膨胀
		erode(gray, gray, Mat());  //图像腐蚀

		medianBlur(gray, dst, 15);

		imshow("medianBlur", dst);


		vector<vector<Point>> contours;
		findContours(dst, contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);

		for (int i = 0; i < (int)contours.size(); i++)
		{

			int x_max = 0;
			int y_max = 0;
			int x_min = 0;
			int y_min = 0; 
			
		/*
		    //根据面积过滤
		    double mianji = contourArea(contours[i]);
			if (mianji>(width*height) / 4) {
				continue;
			}
		*/
			for (int j = 0; j < (int)contours[i].size(); j++) {
				Point tmp = contours[i][j];
				if (j == 0) {
					x_min = tmp.x;
					y_min = tmp.y;
				}
				if (x_min > tmp.x) {
					x_min = tmp.x;
				}
				if (y_min > tmp.y) {
					y_min = tmp.y;
				}
				if (x_max < tmp.x) {
					x_max = tmp.x;
				}
				if (y_max < tmp.y) {
					y_max = tmp.y;
				}
			} 

			//找到中心点转化坐标
			x = int((x_max + x_min) / 2);
			y = int((y_max + y_min) / 2);  
			my_click(x, y);
		}


		gray_1 = gray_2.clone();
		gray_2 = gray_3.clone();
		if (waitKey(3) == 27) {
			return 0;
		}
	}
	return 0;
}
void init() {
	double  x_1, y_1, x_2, y_2, x_3, y_3,x_4,y_4, ww, hh;
	x_1 = iread(conf_str, L"x_1");
	y_1 = iread(conf_str, L"y_1");
	x_2 = iread(conf_str, L"x_2");
	y_2 = iread(conf_str, L"y_2");
	x_3 = iread(conf_str, L"x_3");
	y_3 = iread(conf_str, L"y_3");
	x_4 = iread(conf_str, L"x_4");
	y_4 = iread(conf_str, L"y_4");
	ww = iread(conf_str, L"width");
	hh = iread(conf_str, L"height");
	threshold_diff = iread(conf_str, L"threshold_diff");
	if (threshold_diff<1) {
		MessageBox(NULL, TEXT("参数错误"), NULL, MB_OK);
		exit(0);
	}
	poi->init(x_1, y_1, x_2, y_2,x_3, y_3, x_4, y_4,ww,hh);
}




int _stdcall WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow
) { 
	HANDLE hMutex = CreateMutex(NULL, FALSE, TEXT("XXX_0D0DDD11-5E3F-4287-BB74-7E3D2C7720EF"));
	//单实例
	if (WaitForSingleObject(hMutex, 100) == WAIT_TIMEOUT) { 
		//return FALSE; 
	}   
	init(); 
	app();
}
