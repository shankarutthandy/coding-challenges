class cell
{
  PVector pos;
  float r;
  
  cell(PVector pose,float radius)
  {
   pos=pose;
   r=radius;
  }
  void move()
  {
    this.pos.add(PVector.random2D().mult(3));
  }
  boolean clicked(float x,float y)
  {
   float d=dist(x,y,this.pos.x,this.pos.y);
   if(d<this.r)
     return true;
   else
     return false;
  }
  void show()
  {
    this.move();
    noStroke();
    fill(color(255,0,255,100));
    ellipse(this.pos.x,this.pos.y,this.r*2,this.r*2);
  }
  cell child()
  {
    PVector newPose = this.pos.copy().add(PVector.random2D().mult(15));
    cell child=new cell(newPose,this.r/1.414);
    return child;
  }
}
