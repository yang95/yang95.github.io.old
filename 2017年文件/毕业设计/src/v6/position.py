 
def textture(x0,y0,x1,y1,x2,y2,x3,y3):
    global a
    global b 
    global c
    global d
    global e
    global f
    global g
    global h
    x0 = x0*1.0
    y0 = y0*1.0
    x1 = x1*1.0
    y1 = y1*1.0
    x2 = x2*1.0
    y2 = y2*1.0
    x3 = x3*1.0
    y3 = y3*1.0
    c = x0
    f = y0
    g = (x0-x1+x2-x3)*(y3-y2)-(y0-y1+y2-y3)*(x3-x2)
    tmp_g = (x1-x2)*(y3-y2)-(y1-y2)*(x3-x2)
    print x1,x2,y3,y2,y1,x3,x2
    g = g/tmp_g
    h = (x0-x1+x2-x3)*(y1-y2)-(y0-y1+y2-y3)*(x1-x2)
    tmp_h = (x3-x2)*(y1-y2)-(y3-y2)*(x1-x2)
    h = h/tmp_h
    b = x3-x0+h*x3
    e = y3-y0+h*y3
    a = x1-x0+g*x1
    d = y1-y0+g*y1
    print a,b,c,d,e,f,g,h 

def position(u,v):
    y=((f*g-d)*u+(a-c*g)*v+c*d-a*f)/((h*d-e*g)*u+(b*g-a*h)*v+a*e-b*d)
    x=((e-f*h)*u+(c*h-b)*v-e*c+b*f)/((h*d-e*g)*u+(b*g-a*h)*v+a*e-b*d)
    if(x<0 or y<0 or x>1 or y>1):
        return None
    return (x,y)
def view_position(a0,b0,x_m,y_m,x,y): 
    x = a0+x_m*x
    y = b0+y_m*y
    return (x,y)


if __name__ == "__main__":
    textture(10,10,20,10,20,20,10,30); 
    print position(18,19)
