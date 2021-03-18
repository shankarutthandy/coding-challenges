class Ray
{
  PVector Center;
  PVector dir;

  Ray(PVector c,PVector dirxn)
  {
    Center = c;
    dir=dirxn;

  }

  PVector cast(boundary wall)
  {
   float x1=wall.x1;
   float x2=wall.x2;
   float y1=wall.y1;
   float y2=wall.y2;
   float x3=this.Center.x;
   float x4=this.Center.x+this.dir.x;
   float y3=this.Center.y;
   float y4=this.Center.y+this.dir.y;
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
