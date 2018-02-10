import sys
import ConfigParser

class conf_data:
    a0 = 0
    a1 = 0
    b0 = 0
    b1 = 0
    width=640
    height=480
    threshold = 20 
    def __init__(self):
        self.cp = ConfigParser.SafeConfigParser()
        self.cp.read('myapp.conf') 
        a0 = self.cp.get("conf","a0");
        a1 = self.cp.get("conf","a1");
        b0 = self.cp.get("conf","b0");
        b1 = self.cp.get("conf","b1");
        width=self.cp.get("conf","width");
        height=self.cp.get("conf","height");
        threshold = self.cp.get("conf","threshold");

    def save(self):
        self.cp.set('conf', 'a0',str(self.a0)) 
        self.cp.set('conf', 'a1',str(self.a1))
        self.cp.set('conf', 'b0',str(self.b0))
        self.cp.set('conf', 'b1',str(self.b1))
        self.cp.set('conf', 'width',str(self.width))
        self.cp.set('conf', 'height',str(self.height))
        self.cp.set('conf', 'threshold',str(self.threshold))
        self.cp.write(open('myapp.conf', 'w'))
        self.cp.write(sys.stdout)  
if __name__ == "__main__":
    import sys
    conf = conf_data() 
    conf.save()
