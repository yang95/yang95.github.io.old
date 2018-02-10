package zuobiao

import( 
    "os"  
)
 
 
func Exist(filename string) bool { 
	_,err := os.Stat(filename) 
	if err != nil {
       return false
    }
	return true
}
func Remove(filename string){
	os.Remove(filename)   
}
func abs(a int)int{
	if(a<0){
		a=-1*a
	}
	return a
}
func Er(img [][][]uint8) (img_ [][]int) {  
	img_ = make([][]int,100,100) //建议第一维
	defer func() {
		if r := recover(); r != nil {
		   
		}
	}()
	width:=100
	height:=100
	for i:=0;i<width;i++{
		m2 := make([]int,100) //可用循环对m2赋值，默认建立初值为0
		for j:=0;j<height;j++{ 
			m2[j] = int(img[i][j][0]) 
			if m2[j]>10{
				m2[j] = 0
			}else{
				m2[j] = 1
			}
		}
		img_[i]=m2
	}
	return img_
} 

func Jian(img1 [][]int,img2 [][]int) (img_ [][]int){
	img_ = make([][]int,100,100) //建议第一维
	width:=len(img1[0])
	height:=len(img1)
	for i:=0;i<width;i++{ 
	    m2 := make([]int,100) //可用循环对m2赋值，默认建立初值为0
		defer func() {
			if r := recover(); r != nil {
			   
			}
		}()
		for j:=0;j<height;j++{
			 m2[j] = img1[i][j]-img2[i][j]
			 if m2[j]< 0{
				m2[j] = 0
			 }
		} 
		img_[i]=m2
	}
	return img_
}
func Position(img1 [][]int)(int,int){
	width:=len(img1[0])
	height:=len(img1)
	for i:=1;i<width-1;i++{ 
		for j:=1;j<height-1;j++{ 
			 if(  img1[i+1][j]>0 &&  img1[i][j+1]>0 &&  img1[i-1][j]>0 &&  img1[i][j-1]>0   ) { 
				return j,i
			 }
		} 
	} 
	return 0,0
}
func Bilisuofang(c_x int,c_y int,x int,y int)(int,int){

	 tmp_y :=  int(c_y*y/100)
	 tmp_x :=  int(c_x*x/100)
	return tmp_x,tmp_y
}