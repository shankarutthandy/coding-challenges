import math as m

class Pvector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,vec):
        self.x=self.x+vec.x
        self.y=self.y+vec.y
    def sub(self,vec):
        self.x=self.x-vec.x
        self.y=self.y-vec.y
    def getAngle(self,vec):
        dot=self.x*vec.x+self.y*vec.y
        mag1=self.mag();mag2=vec.mag();mag2*=mag1
        return m.acos(dot/(mag1*mag2))
    def dot(self,vec):
        dot=self.x*vec.x+self.y*vec.y
        return dot
    def magnitude(self):
        mag=m.sqrt(self.x**2+self.y**2)
        return mag
    def mult(self,K):
        self.x=self.x*K
        self.y=self.y*K
    def limit(self,maxi):
        if self.magnitude()<=maxi:
            return
        else:
            mag=self.magnitude()
            self.mult(maxi/mag)
    def heading(self):
        theta=m.atan2(self.y,self.x)
        return theta
    def setMag(self,newmag):
        mag=self.magnitude()
        if mag!=0:
            self.mult(newmag/mag)
    def norm(self):
        mag=self.magnitude()
        if mag!=0:
            self.mult(1/mag)
    def get_distance(self,a,b):
        k=self.rsub(a,b)
        return k.magnitude()
    def rnorm(self):
        mag=self.magnitude()
        res=Pvector(self.x,self.y)
        mag=1/mag
        res.mult(mag)
        return res
    def rsub(self,vec1,vec2):
        resx=vec1.x-vec2.x
        resy=vec1.y-vec2.y
        res=Pvector(resx,resy)
        return res
    def radd(self,vec1,vec2):
        resx=vec1.x+vec2.x
        resy=vec1.y+vec2.y
        res=Pvector(resx,resy)
        return res
    def get(self):
        res=Pvector(self.x,self.y)
        return res