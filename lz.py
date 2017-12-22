import random
point=100
c1=2
c2=2
w=1
r1=round(random.random(),2)
r2=round(random.random(),2)
X=[random.randint(-2,5) for i in range(0,point)]  #uniform
PbestX=X
def f(a):
    return a**3-5*a**2-2*a+3
def G_Max(l):
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
def P_Max(l):
    global PbestX,X
    if l[0]>l[1]:
        return PbestX[l[2]],l[0]
    else:
        return X[l[2]],l[1]
v=[random.randint(-2,2) for i in range(0,point)]  #uniform
PbestY=[f(X[i]) for i in range(0,point)]
GbestX,GbestY=G_Max(PbestY)
def up_v(v,x,p):
    global c1,c2,r1,r2,GbestX
    return w*v+c1*r1*(p-x)+c2*r2*(GbestX-x)
def up_x(v,x):
    return x+v
def get_position():
    global PbestX,X,PbestY0,PbestY1,PbestY2,PbestY3
    global v,point
    n=0
    flag=1
    turn=0
    tempX=0
    #temp_PY=0
    while turn<100 and flag:
        for i in range(0,point):
            temp_PY=f(X[i])
            PbestX[i],PbestY[i]=P_Max([PbestY[i],temp_PY,i])
        GbestX,GbestY=G_Max(PbestY)
        for i in range(0,point):
            v[i]=up_v(v[i],X[i],PbestX[i])
        for i in range(0,point):
            X[i]=up_x(X[i],v[i])
        turn+=1
        if tempX==GbestX:
            n+=1
        else:
            #print(tempX)
            n=0
        if n>5:
            print('aasaas')
            break
        tempX=int(GbestX)
if __name__=="__main__":
    get_position()
    print('(',GbestX,',',GbestY,')')
