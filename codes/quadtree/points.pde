class pts
{
  int x,y;
  pts(int x_,int y_)
  {

    x=x_;
    y=y_; 
}
void show()
{
  strokeWeight(3);
  point(this.x,this.y);
}
void highlight()
{
  strokeWeight(6);
  stroke(color(255,0,0));
  point(this.x,this.y);
}
}
