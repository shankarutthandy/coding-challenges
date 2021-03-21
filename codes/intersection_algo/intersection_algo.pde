ArrayList<rectangle> r;
void setup()
{
  size(800,800);
  r=new ArrayList<rectangle>();
}
void mousePressed()
{
  r.add(new rectangle(mouseX,mouseY));
}
void draw()
{
  background(255);
  for(rectangle rec:r)
  {
    rec.intersect(r);
    rec.show();
  }
}
class rectangle
{
  PVector pose;
  int w,h;
  color strk;
 rectangle(int x,int y)
 {
   pose=new PVector(x,y);
   w=100;
   h=190;
   strk=color(0,255,0);
 }
 void show()
 {
   stroke(strk);
   noFill();
   rectMode(CENTER);
   rect(this.pose.x,this.pose.y,this.w,this.h);
 }
 void intersect(ArrayList<rectangle> rectangles)
 {
   for(rectangle rec:rectangles)
   {
     if(rec.pose!=this.pose && this.overlap(rec))
     {
       this.strk=color(255,0,0);
     }
   }
 }
 boolean overlap(rectangle r)
 {
   PVector c=PVector.sub(this.pose,r.pose);
   float dh=c.dot(1,0,0);
   float dv=c.dot(0,1,0);
   if(abs(dh)<=this.w && abs(dv)<=this.h)
   {
     return true;
   }
    else
    {
     return false;
    }
   
 }
}
