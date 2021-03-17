class boundary
{ float x1,x2,y1,y2;
  boundary(float i,float j,float k,float l)
  {
    x1=i;
    y1=j;
    x2=k;
    y2=l;
  }
  void show()
  {
    stroke(255);
    strokeWeight(4);
    //noFill();
    line(this.x1,this.y1,this.x2,this.y2);
  }
  }
