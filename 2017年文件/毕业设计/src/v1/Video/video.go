package video
import( 
    "os/exec"
)
 
func Init(){ 
      exec.Command("cmd", "/C", `ffmpeg -f dshow -i video="USB2.0 PC CAMERA" %d.jpg`)
} 
