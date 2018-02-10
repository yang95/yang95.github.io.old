#include <opencv2\opencv.hpp> 
#include <iostream>
#include <stdio.h>
#include <windows.h>

using namespace cv;
using namespace std; 

String window_name = "frame";
Mat frame1;
Point cur_pt2 = Point(0,0);//ʵʱ����   
String poistr = "(0,0)";
int init(int index);
void int2str(const int &int_temp, string &string_temp)
{
	stringstream stream;
	stream << int_temp;
	string_temp = stream.str();   //�˴�Ҳ������ stream>>string_temp  
}

void my_mouse_event(int event, int x, int y, int flags, void *ustc)//event����¼����ţ�x,y������꣬flags��ק�ͼ��̲����Ĵ���  
{
	static int move = 0;
	Point cur_pt = Point(x, y);//ʵʱ����   
	string s_x, s_y;
	if (event == CV_EVENT_LBUTTONDOWN)//�������
	{
		cur_pt2.x = cur_pt.x;
		cur_pt2.y = cur_pt.y;
		int2str(cur_pt2.x, s_x);
		int2str(cur_pt2.y, s_y);
		poistr = "("+ s_x +","+ s_y + ")";
	}
	Mat tmp = frame1.clone();
	putText(tmp, poistr, cur_pt2, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 0));
	line(tmp, cur_pt2, cur_pt2, Scalar(255,255, 0), 2, 8);
	 
	imshow(window_name, tmp);
}
void show(VideoCapture capture)
{
	namedWindow(window_name);//����һ��img����   
	setMouseCallback(window_name, my_mouse_event, 0);//���ûص�����  
	while (true) {
		capture >> frame1;   
		resize(frame1, frame1, Size(640, 480));
		imshow(window_name, frame1);
		if (waitKey(1) == 27) {
			return;
		}
		if (waitKey(1) == '0') {
			init(0);
			return;
		}
		if (waitKey(1) == '1') {
			init(1);
			return;
		}
		if (waitKey(1) == '2') {
			init(2);
			return;
		}
		if (waitKey(1) == '3') {
			init(3);
			return;
		}
	}
}
int init(int index) {
	VideoCapture capture(index);
	if (capture.isOpened()) {
		show(capture);
	}
	return 0;
}
 
int _stdcall WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow
) {
	init(0);
	return 0;
}
