package main

import(
    "github.com/Comdex/imgo"
    I "./Image"
    socket_server "./Server" 
   // video "./Video" 
    "fmt" 
    "strconv"  
)


func main(){ 
	go func(){ 
		//video.Init()
		socket_server.Init() 
	}() 
	img,_:=imgo.ResizeForMatrix("img/0.jpg", 100,100)
	img_ := I.Er(img); 
	var i int; 
	i=1; 
	
	for  {   
		path := "img/"+strconv.Itoa(i)+".jpg"
		path2 := "img/"+strconv.Itoa(i+1)+".jpg"
		if I.Exist(path) {  
			i++ 
			img2,_:=imgo.ResizeForMatrix(path, 100,100)
			img_2 := I.Er(img2);  
			img_2 = I.Jian(img_2,img_);  
			x,y:=I.Position(img_2)
			x,y = I.Bilisuofang(1366,768,x,y)
			zuobiao:=strconv.Itoa(x)+","+strconv.Itoa(y)
			fmt.Println(zuobiao)
			socket_server.Send(zuobiao) 
			I.Remove(path)			
		} 
		if I.Exist(path2) { 
			i++
		}
		//fmt.Println(i)
	}  
}
