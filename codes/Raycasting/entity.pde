class entity
{PVector Center;
 boundary[] bounds;
 int fov;
 float heading;
 ArrayList<Ray> rays=new ArrayList<Ray>();
  entity(PVector c,boundary[] walls)
  {
    Center=c;
    bounds=walls;
    fov=60;
    heading=0;
    for(int f=-fov;f<fov;f+=1)
    {
    rays.add(new Ray(Center,PVector.fromAngle(radians(f))));
    }
  }
  
  void keyUpdate(char k)
  {
    
   if(k=='a')
   {
     this.heading-=0.02;
   }
   else if(k=='d')
   {
     this.heading+=0.02;
   }
   else if(k=='w')
   {
    PVector vel=PVector.fromAngle(this.heading);
    vel.mult(2);
    vel.add(this.Center);
     
    this.update(vel.x,vel.y);
    }
   
   else if(k=='s')
   {
     PVector vel=PVector.fromAngle(this.heading);
     vel.mult(2);
     vel=PVector.sub(this.Center,vel);
     
    this.update(vel.x,vel.y);
    
   }
   if(k=='a'|| k=='d')
   {
   ArrayList<Ray> newRays=new ArrayList<Ray>();
   for(int f=-this.fov;f<this.fov;f+=1)
   {
       newRays.add(new Ray(this.Center,PVector.fromAngle(radians(f)+this.heading)));
   }
  this.rays=newRays;
   }
  }
  void update(float a,float b)
  {

    if(a>sceneW)
    {
      a=0;
    }
    else if(a<0)
    {
     a=sceneW;
    }
    if(b>sceneH)
    {
      b=0;
    }
    else if(b<0)
    {
     b=sceneH;
    }
    ent.Center=new PVector(a,b);
    for(Ray ray:rays)
    {
      ray.Center.x=a;
      ray.Center.y=b;
    }
    }
  void show()
  {
    FloatList scene=this.hit();
    noStroke();
    fill(100);
   ellipse(this.Center.x,this.Center.y,20,20);
   this.render(scene);
   
   
   }
  void render(FloatList scenes)
  {
    float sceneW=400;
    float sceneH=400;
    float w=sceneW/scenes.size();
    float projPlane=sceneW/2.0/tan(this.fov/2.0);
    pushMatrix();
    translate(sceneW,0);
    for(int i=0;i<scenes.size();i++)
    {
      noStroke();
      float sq=scenes.get(i)*scenes.get(i);
      float wsq=sceneW*sceneW;
      float b=map(sq,0,wsq,255,0);
      float h=(sceneW/scenes.get(i))*projPlane;
      fill(b);
      rectMode(CENTER);
      rect((i*w)+w/2,sceneH/2,w,h);
    }
    popMatrix();
       
      
    }
    
  
FloatList hit()
{
  FloatList dist=new FloatList();
  for(int i=0;i<this.rays.size();i++)
   {
    Ray ray=this.rays.get(i);
    PVector bestPoint=null;
    float WorldRecord=500000000;
    for(int j=0;j<bounds.length;j++)
     {
       PVector point=ray.cast(bounds[j]);
       if(point!=null)
       { 
         if(PVector.dist(point,this.Center)<WorldRecord)
         {
           WorldRecord=PVector.dist(point,this.Center);
           bestPoint=point;
         }
      
       }
       dist.append(WorldRecord);
     }
       if(bestPoint!=null)   
        {stroke(255,100);
         strokeWeight(5);
         line(this.Center.x,this.Center.y,bestPoint.x,bestPoint.y);
         }  }
         return dist;
}
  }
