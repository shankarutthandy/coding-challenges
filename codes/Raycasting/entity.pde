class entity
{float x,y;
 boundary[] bounds;
 ArrayList<Ray> rays=new ArrayList<Ray>();
  entity(float i,float j,boundary[] walls)
  {
    x=i;
    y=j;
    bounds=walls;
    for(int f=0;f<360;f+=1)
    {
    rays.add(new Ray(x,y,PVector.fromAngle(radians(f))));
    }
    print(rays.size());
  }
  void show()
  {
    fill(255);
   ellipse(this.x,this.y,20,20);
  for(int i=0;i<this.rays.size();i++)
   {
    Ray ray=this.rays.get(i);
    //ray.show();
    PVector bestPoint=null;
    float WorldRecord=500000000;
    for(int j=0;j<bounds.length;j++)
     {
       PVector point=ray.cast(bounds[j]);
       if(point!=null)
       { 
         if(PVector.dist(point,new PVector(this.x,this.y))<WorldRecord)
         {
           WorldRecord=PVector.dist(point,new PVector(this.x,this.y));
           bestPoint=point;
         }
         //stroke(255);
         //strokeWeight(0.5);
         //line(this.x,this.y,point.x,point.y);
       }
     }
     //print(WorldRecord);
      if(bestPoint!=null)   
         {stroke(255,100);
         strokeWeight(1);
         line(this.x,this.y,bestPoint.x,bestPoint.y);
         }
   }
  //for(int j=0;j<bounds.length;j++)
  //{
  //  for(int i=0;i<this.rays.size();i++)
  //  {
  //    Ray ray=this.rays.get(i);
  //    PVector point=ray.cast(bounds[j]);
  //    if(point.x!=-1)
  //    {
  //      stroke(255);
  //      strokeWeight(1);
  //      line(this.x,this.y,point.x,point.y);
  //    }
  //  }
    
  }}
