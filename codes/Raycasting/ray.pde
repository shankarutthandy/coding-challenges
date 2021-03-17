class Ray
{
  float x;
  float y;
  PVector dir;
  //color c;
  Ray(float i,float j,PVector dirxn)
  {
    x=i;y=j;
    dir=dirxn;
    //c=color(0,0,0);
  }
  //void show()
  //{
  //  //noStroke();
  //  //fill(c);
  //  fill(255);
  //  ellipse(this.x,this.y,10,10);
  //  pushMatrix();
  //  translate(this.x,this.y);
  //  stroke(255,100);
  //  strokeWeight(1);
  //  line(0,0,this.dir.x*20,this.dir.y*20);
  //  popMatrix();
  //}
  //void setdir(float x,float y)
  //{
  //  this.dir.x=x-this.x;
  //  this.dir.y=y-this.y;
  //  this.dir.normalize();
  //}
  PVector cast(boundary wall)
  {
   float x1=wall.x1;
   float x2=wall.x2;
   float y1=wall.y1;
   float y2=wall.y2;
   float x3=this.x;
   float x4=this.x+this.dir.x;
   float y3=this.y;
   float y4=this.y+this.dir.y;
   float den=(x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
   if(den==0)
   {
     return null;
   }
   float t=((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
   float u=-((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den;
   if(t>0 && t<1 && u>0)
   {
    PVector point=new PVector();
    point.x=x1+ (t*(x2-x1));
    point.y=y1+ (t*(y2-y1));
    return point;
   }
   else
   return null;
   
   
  }
}
