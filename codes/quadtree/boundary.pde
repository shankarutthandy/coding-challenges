class boundary
{
  int x,y,w,h;
  boundary(int x_,int y_,int w_,int h_)
  {
    x=x_;
    y=y_;
    w=w_;
    h=h_;
  }
  boolean isIn(pts pnt)
  {
    if(pnt.x>=this.x-this.w && pnt.x<=this.x+this.w && pnt.y>=this.y-this.h && pnt.y<=this.y+this.h)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  void show()
  {
   noFill();
   stroke(255);
   strokeWeight(1);
   rectMode(CENTER);
   rect(this.x,this.y,this.w*2,this.h*2);
  }
  void highlight()
  {
   fill(100,100);
   stroke(color(0,255,0));
   strokeWeight(4);
   rectMode(CENTER);
   rect(this.x,this.y,this.w*2,this.h*2);
  
  }
  boolean intersect(boundary range)
  {
    PVector c=new PVector(this.x-range.x,this.y-range.y);
    float dx=abs(c.dot(1,0,0));
    float dy=abs(c.dot(0,1,0));
    if(dx<this.w+range.w && dy<this.h+range.h)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
}
