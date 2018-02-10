#include <opencv2\opencv.hpp> 
#include <iostream>
#include <stdio.h>
#include <windows.h>

using namespace cv;
using namespace std;

#define threshold_diff1 25 //设置简单帧差法阈值  
#define threshold_diff2 25 //设置简单帧差法阈值 



int threshold_value = 0;
int threshold_type = 3;
char* window_name = "img";

char* trackbar_type = "越小灵敏";
char* trackbar_value = "Value";

#define FILE_NAME "D:\\poisture.yml"

int  x_1;
int  y_1;
int  x_2;
int  y_2;
int  x_3;
int  y_3;
int  x_4;
int  y_4;
//配置文件 
void my_write(char* key, int value) {
	cv::FileStorage fs(FILE_NAME, FileStorage::WRITE);
	if (key == "x_1") {
		x_1 = value;
	}
	if (key == "y_1") {
		y_1 = value;
	}
	if (key == "x_2") {
		x_2 = value;
	}
	if (key == "y_2") {
		y_2 = value;
	}
	if (key == "x_3") {
		x_3 = value;
	}
	if (key == "y_3") {
		y_3 = value;
	}
	if (key == "x_4") {
		x_4 = value;
	}
	if (key == "y_4") {
		y_4 = value;
	}
	if (key == "threshold") {
		threshold_value = value;
	}
	fs << "x_1" << x_1;
	fs << "y_1" << y_1;
	fs << "x_2" << x_2;
	fs << "y_2" << y_2;
	fs << "x_3" << x_3;
	fs << "y_3" << y_3;
	fs << "x_4" << x_4;
	fs << "y_4" << y_4;
	fs << "threshold" << threshold_value;

	fs.release();
}
void my_read_all() {
	cv::FileStorage fs(FILE_NAME, FileStorage::READ);
	fs["x_1"] >> x_1;
	fs["y_1"] >> y_1;
	fs["x_2"] >> x_2;
	fs["y_2"] >> y_2;
	fs["x_3"] >> x_3;
	fs["y_3"] >> y_3;
	fs["x_4"] >> x_4;
	fs["y_4"] >> y_4;
	fs["threshold"] >> threshold_value;
	fs.release();
}

//配置文件  
double Distance(Point p, Point p2) {
	return sqrt(pow((p.x - p2.x), 2) + pow((p.y - p2.y), 2));
}
Mat frame1;
void my_mouse_event(int event, int x, int y, int flags, void *ustc)//event鼠标事件代号，x,y鼠标坐标，flags拖拽和键盘操作的代号  
{
	static int move = 0;
	static Point po1 = Point(x_1, y_1);
	static Point po2 = Point(x_2, y_2);
	static Point po3 = Point(x_3, y_3);
	static Point po4 = Point(x_4, y_4);
	Point cur_pt = Point(x, y);//实时坐标  
	Point move_pt = Point(0, 0);//实时坐标  
	if (event == CV_EVENT_LBUTTONDOWN)//左键按下
	{
		if (Distance(cur_pt, po1)<80) {
			po1.x = cur_pt.x;
			po1.y = cur_pt.y;
			my_write("x_1", po1.x);
			my_write("y_1", po1.y);
		}
		else if (Distance(cur_pt, po2)<80) {
			po2.x = cur_pt.x;
			po2.y = cur_pt.y;
			my_write("x_2", po2.x);
			my_write("y_2", po2.y);
		}
		else if (Distance(cur_pt, po3)<80) {
			po3.x = cur_pt.x;
			po3.y = cur_pt.y;
			my_write("x_3", po3.x);
			my_write("y_3", po3.y);
		}
		else if (Distance(cur_pt, po4)<80) {
			po4.x = cur_pt.x;
			po4.y = cur_pt.y;
			my_write("x_4", po4.x);
			my_write("y_4", po4.y);
		}
	}
	Mat tmp = frame1.clone();
	putText(tmp, "1", po1, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 0));
	putText(tmp, "2", po2, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 0));
	putText(tmp, "3", po3, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 0));
	putText(tmp, "4", po4, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 0));
	line(tmp, po1, po2, Scalar(255, 0, 0), 2, 8);
	line(tmp, po2, po3, Scalar(0, 255, 0), 2, 8);
	line(tmp, po3, po4, Scalar(255, 0, 255), 2, 8);
	line(tmp, po4, po1, Scalar(0, 0, 255), 2, 8);
	imshow(window_name, tmp);
}

/**
* @自定义的阈值函数
*/
void Threshold_Demo(int, void*)
{
	/* 0: 二进制阈值
	1: 反二进制阈值
	2: 截断阈值
	3: 0阈值
	4: 反0阈值
	*/

	threshold(frame1, frame1, threshold_value, 255, threshold_type);

	my_write("threshold", threshold_value);
	//imshow("threshold_value", frame1);
}

 

int config() {
	my_read_all();
	/// 创建滑动条来控制阈值

	namedWindow(window_name);//定义一个img窗口   
	createTrackbar(trackbar_type,
		window_name, &threshold_value,
		255, Threshold_Demo);

	//读取视频或摄像头  
	VideoCapture capture(0);
	if (capture.isOpened() == false) {
		MessageBox(NULL, TEXT("未检测到摄像头"), NULL, MB_OK);
		return false;
	}
	setMouseCallback(window_name, my_mouse_event, 0);//调用回调函数  
	while (true)
	{
		capture >> frame1;
		
		imshow(window_name, frame1);
		if (waitKey(30) == 'q') {
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
	config();
	return 0;
}
