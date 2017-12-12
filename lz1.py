import random
c1=2
c2=2
w=1
r1=round(random.random(),2)
r2=round(random.random(),2)
X=[random.uniform(-2,5) for i in range(0,4)]
PbestX=X
def f(a):
    return a**3-5*a**2-2*a+3
def Max(l):
    global PbestX
    temp=l[0]
    X=0
    x=0
    for value in l[1:]:
        x+=1
        if value>temp:
            temp=value
            X=x
    return PbestX[X],temp
#x0=random.randint(-2,5)
#x1=random.randint(-2,5)
#x2=random.randint(-2,5)
#x3=random.randint(-2,5)
#v0=random.randint(-2,2)
#v1=random.randint(-2,2)
#v2=random.randint(-2,2)
#v3=random.randint(-2,2)
v=[random.uniform(-2,2) for i in range(0,4)]
PbestY0=f(X[0])
PbestY1=f(X[1])
PbestY2=f(X[2])
PbestY3=f(X[3])
GbestX,GbestY=Max([PbestY0,PbestY1,PbestY2,PbestY3])
def up_v(v,x,p):
    global c1,c2,r1,r2,GbestX
    return w*v+c1*r1*(p-x)+c2*r2*(GbestX-x)
def up_x(v,x):
    return x+v
def get_position():
    global PbestX,X,PbestY0,PbestY1,PbestY2,PbestY3
    global v
    n=0
    flag=1
    turn=0
    tempX=0
    while turn<100000 and flag:
        temp_PY0=f(X[0])
        temp_PY1=f(X[1])
        temp_PY2=f(X[2])
        temp_PY3=f(X[3])
        PbestX[0],PbestY0=Max([PbestY0,temp_PY1])
        PbestX[1],PbestY1=Max([PbestY0,temp_PY0])
        PbestX[2],PbestY2=Max([PbestY0,temp_PY2])
        PbestX[3],PbestY3=Max([PbestY0,temp_PY3])
        GbestX,GbestY=Max([PbestY0,PbestY1,PbestY2,PbestY3])
        v[0]=up_v(v[0],X[0],PbestX[0])
        v[1]=up_v(v[1],X[1],PbestX[1])
        v[2]=up_v(v[2],X[2],PbestX[2])
        v[3]=up_v(v[3],X[3],PbestX[3])
        for i in range(0,4):
            X[i]=up_x(X[i],v[i])
        turn+=1
        if tempX==GbestX:
            n+=1
        else:
            n=0
        if n>5:
            print('aasaas')
            break
        tempX=GbestX
if __name__=="__main__":
    get_position()
    print('(',GbestX,',',GbestY,')')
