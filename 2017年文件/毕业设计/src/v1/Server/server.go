package socket_server
import( 
    "fmt"  
    "net"
)
 
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
    }  
}  

func Send(str string){
	zuobiao = str
}