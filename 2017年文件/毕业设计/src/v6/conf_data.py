import sys
import ConfigParser

class conf_data:
    a0 = 0 
    b0 = 0 
    a1 = 0  
    b1 = 0 
    a2 = 0  
    b2 = 0 
    a3 = 0  
    b3 = 0
    x0 = 0
    y0 = 0   
    x1 = 0
    y1 = 0    
    x2 = 0
    y2 = 0    
    x3 = 0
    y3 = 0    
    threshold = 0 
    def load(conf_data):
        cp = ConfigParser.SafeConfigParser()
        cp.read("myapp.conf") 
        conf_data.a0 = cp.get("conf","a0");
        conf_data.b0 = cp.get("conf","b0");
        conf_data.a1 = cp.get("conf","a1");
        conf_data.b1 = cp.get("conf","b1");
        conf_data.a2 = cp.get("conf","a2");
        conf_data.b2 = cp.get("conf","b2");
        conf_data.a3 = cp.get("conf","a3");
        conf_data.b3 = cp.get("conf","b3");
        conf_data.x0 = cp.get("conf","x0");
        conf_data.y0 = cp.get("conf","y0");
        conf_data.x1 = cp.get("conf","x1");
        conf_data.y1 = cp.get("conf","y1");
        conf_data.x2 = cp.get("conf","x2");
        conf_data.y2 = cp.get("conf","y2");
        conf_data.x3 = cp.get("conf","x3");
        conf_data.y3 = cp.get("conf","y3"); 
        conf_data.threshold = cp.get("conf","threshold");

    def save(conf_data):
        cp = ConfigParser.SafeConfigParser()
        cp.read("myapp.conf") 
        cp.set("conf", "a0",str(conf_data.a0)) 
        cp.set("conf", "b0",str(conf_data.b0))
        cp.set("conf", "a1",str(conf_data.a1))
        cp.set("conf", "b1",str(conf_data.b1)) 
        cp.set("conf", "a2",str(conf_data.a2)) 
        cp.set("conf", "b2",str(conf_data.b2)) 
        cp.set("conf", "a3",str(conf_data.a3)) 
        cp.set("conf", "b3",str(conf_data.b3)) 
        cp.set("conf", "x0",str(conf_data.x0)) 
        cp.set("conf", "y0",str(conf_data.y0)) 
        cp.set("conf", "x1",str(conf_data.x1)) 
        cp.set("conf", "y1",str(conf_data.y1)) 
        cp.set("conf", "x2",str(conf_data.x2)) 
        cp.set("conf", "y2",str(conf_data.y2)) 
        cp.set("conf", "x3",str(conf_data.x3)) 
        cp.set("conf", "y3",str(conf_data.y3)) 
        cp.set("conf", "threshold",str(conf_data.threshold))
        cp.write(open("myapp.conf", "w"))
        cp.write(sys.stdout)
    def to_int(conf_data):
        conf_data.a0 = int(conf_data.a0)
        conf_data.b0 = int(conf_data.b0)
        conf_data.a1 = int(conf_data.a1)
        conf_data.b1 = int(conf_data.b1)
        conf_data.a2 = int(conf_data.a2)
        conf_data.b2 = int(conf_data.b2)
        conf_data.a3 = int(conf_data.a3)
        conf_data.b3 = int(conf_data.b3)
        conf_data.x0 = int(conf_data.x0)
        conf_data.y0 = int(conf_data.y0)
        conf_data.x1 = int(conf_data.x1)
        conf_data.y1 = int(conf_data.y1)
        conf_data.x2 = int(conf_data.x2)
        conf_data.y2 = int(conf_data.y2)
        conf_data.x3 = int(conf_data.x3)
        conf_data.y3 = int(conf_data.y3)
        conf_data.threshold = int(conf_data.threshold)

if __name__ == "__main__":
    import sys
    conf = conf_data();
    conf.load()
    print conf.a0 
