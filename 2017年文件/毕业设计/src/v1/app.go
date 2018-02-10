package main

import(
    "github.com/Comdex/imgo"
    "os" 
    "fmt" 
    "strconv" 
    "net"
)
func byteString(p []byte) string {        
	for i := 0; i < len(p); i++  {                
		if p[i] == 0 {                        
			return string(p[0:i])                
		}        
	}        
	return string(p)
}
func Init(){
	listen,err := net.ListenTCP("tcp", &net.TCPAddr{net.ParseIP(""), 1024, ""})  
    if err != nil {  
        fmt.Println("监听端口失败:", err.Error())  
        return  
    }  
    fmt.Println("已初始化连接，等待客户端连接...")  
    Server(listen)  
}
var zuobiao string = "0,0";
func Server(listen *net.TCPListener) {  
    for {  
        conn, err := listen.AcceptTCP()  
        if err != nil {  
            fmt.Println("接受客户端连接异常:", err.Error())  
            continue  
        }  
        fmt.Println("客户端连接来自:", conn.RemoteAddr().String())  
        defer conn.Close()  
		go func(){
			for {  
				if(zuobiao != "0,0"){
					conn.Write([]byte(zuobiao)) 
				}
			}
		}()
        /*
		go func() {  
            data := make([]byte, 128)  
            for {  
                i, err := conn.Read(data)  
                fmt.Println("客户端发来数据:", string(data[0:i]))  
                if err != nil {  
                    fmt.Println("读取客户端数据错误:", err.Error())  
                    break  
                }  
                //conn.Write([]byte{'f', 'i', 'n', 'i', 's', 'h'})  
                conn.Write([]byte("1024,768"))  
            }  
  
        }()  
		*/
    }  
}  
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
func er(img [][][]uint8) (img_ [][]int) {  
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
			if m2[j]>80{
				m2[j] = 0
			}else{
				m2[j] = 1
			}
		}
		img_[i]=m2
	}
	return img_
} 

func jian(img1 [][]int,img2 [][]int) (img_ [][]int){
	img_ = make([][]int,100,100) //建议第一维
	width:=len(img1[0])
	height:=len(img1)
	for i:=0;i<width;i++{ 
	    m2 := make([]int,100) //可用循环对m2赋值，默认建立初值为0
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
func position(img1 [][]int)(int,int){
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
func bilisuofang(c_x int,c_y int,x int,y int)(int,int){

	 tmp_y :=  int(c_y*y/100)
	 tmp_x :=  int(c_x*x/100)
	return tmp_x,tmp_y
}
func main(){
    //如果读取出错会panic,返回图像矩阵img
    //img[height][width][4],height为图像高度,width为图像宽度
    //img[height][width][4]为第height行第width列上像素点的RGBA数值数组，值范围为0-255
    //如img[150][20][0]是150行20列处像素的红色值,img[150][20][1]是150行20列处像素的绿
    //色值，img[150][20][2]是150行20列处像素的蓝色值,img[150][20][3]是150行20列处像素
    //的alpha数值,一般用作不透明度参数,如果一个像素的alpha通道数值为0%，那它就是完全透明的.
	go func(){
		img,_:=imgo.ResizeForMatrix("img/0.jpg", 100,100)
		img_ := er(img); 
		var i int
		i=1
		for true {  
			path := "img/"+strconv.Itoa(i)+".jpg"
			if Exist(path) { 
				img2,_:=imgo.ResizeForMatrix(path, 100,100)
				img_2 := er(img2);  
				img_2 = jian(img_2,img_);  
				x,y:=position(img_2)
				x,y = bilisuofang(1366,768,x,y)
				zuobiao=strconv.Itoa(x)+","+strconv.Itoa(y)
				fmt.Println(zuobiao)
				i++	 
				Remove(path)			
			}
				fmt.Println("wait",path)
		} 
	}()
	Init() 
	
    //保存为jpeg,100为质量，1-100
	//err:=imgo.SaveAsJPEG("2-5-new.jpg",img,100) 
	//if err!=nil {
	//	panic(err)
	//} 
}
