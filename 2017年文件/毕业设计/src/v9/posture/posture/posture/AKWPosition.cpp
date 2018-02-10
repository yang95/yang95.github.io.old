 
#ifndef I_AM_NOT_REDEFINITION
#define I_AM_NOT_REDEFINITION  
 
class AKWPosition {
	public: 
		double a;
		double b;
		double c;
		double d;
		double e;
		double f;
		double g;
		double h;

		double width;
		double height;

		//坐标处理  
		void init(double x0, double y0, double x_1, double y_1, double x_2, double y_2, double x_3, double y_3, double ww, double hh) {
			width = ww;
			height = hh;
			double tmp_h, tmp_g;
			x0 = x0*1.0;
			y0 = y0*1.0;
			x_1 = x_1*1.0;
			y_1 = y_1*1.0;
			x_2 = x_2*1.0;
			y_2 = y_2*1.0;
			x_3 = x_3*1.0;
			y_3 = y_3*1.0;
			c = x0;
			f = y0;
			g = (x0 - x_1 + x_2 - x_3)*(y_3 - y_2) - (y0 - y_1 + y_2 - y_3)*(x_3 - x_2);
			tmp_g = (x_1 - x_2)*(y_3 - y_2) - (y_1 - y_2)*(x_3 - x_2);
			g = g / tmp_g;
			h = (x0 - x_1 + x_2 - x_3)*(y_1 - y_2) - (y0 - y_1 + y_2 - y_3)*(x_1 - x_2);
			tmp_h = (x_3 - x_2)*(y_1 - y_2) - (y_3 - y_2)*(x_1 - x_2);
			h = h / tmp_h;
			b = x_3 - x0 + h*x_3;
			e = y_3 - y0 + h*y_3;
			a = x_1 - x0 + g*x_1;
			d = y_1 - y0 + g*y_1;
		}
		//返回单位坐标
		void  poi(double &u, double &v) {
			double x, y;
			y = ((f*g - d)*u + (a - c*g)*v + c*d - a*f) / ((h*d - e*g)*u + (b*g - a*h)*v + a*e - b*d);
			x = ((e - f*h)*u + (c*h - b)*v - e*c + b*f) / ((h*d - e*g)*u + (b*g - a*h)*v + a*e - b*d);
			if (x < 0 || y < 0 || x>1 || y>1) {
				u = 0;
				v = 0;
			}
			u = x;
			v = y;
		}
		
};

#endif 
