int MaxIterations=10000000;
float Dist=10;
RRT path=null;
ArrayList<obstacle> obs=new ArrayList<obstacle>();
PVector strt=null;
PVector endPoint=null;
menu m=new menu();
void setup()
{
  size(800,800);
  background(120);
 
}

void mousePressed()
{
  m.mousePressed();
}
void mouseDragged()
{
  m.mouseDragged();
}
void draw()
{
 if(m.run)
 {
 m.render();
 }
 else
 {
   background(120);
   m.render();
 }
}
class vertx
{
  PVector pose;
  float weight;
  vertx previous;
  vertx(PVector pose_,float wgt,vertx prev)
  {
    pose=pose_;
    weight=wgt; 
    previous=prev;
  }
}
class menu
{
  boolean start;
 boolean end;
 boolean run;
 boolean addObs;
 boolean clearObs;
 menu()
 {
  start=false;
  end=false;
  run=false;
 }
 void render()
 {

 fill(color(240,220,220),100);
 stroke(0);
 rectMode(CENTER);
 rect(50,20,100,40);
 rect(150,20,100,40);
 rect(250,20,100,40);
 rect(350,20,100,40);
 rect(450,20,100,40);
 fill(0);
 text("START",30,25);
 text("END",140,25);
 text("RUN",240,25);
 text("add obstacles",310,25);
 text("clear obstacles",410,25);
 
if(this.run)
   {
     if(path==null)
     {  
     path=new RRT(MaxIterations,Dist,strt,endPoint,obs);
     }
     else
     {
       path.show();
     }
   }
   else
   {
     if(strt!=null)
     {
    fill(color(0,255,0));
    ellipse(strt.x,strt.y,20,20);
     }
     if(endPoint!=null)
     {
    fill(color(255,0,0));
    ellipse(endPoint.x,endPoint.y,20,20);
     }
     
     for(obstacle o:obs)
     {
       o.show();
     }
   }

 }
 void mousePressed()
 {
   if(mouseX>0 && mouseX<100 && mouseY<40 && mouseY>0)
   {
     this.start=true;
     this.end=false;
      
      this.addObs=false;
   }
   else if (mouseX>100 && mouseX<200 && mouseY<40 && mouseY>0)
   {
     this.start=false;
     this.end=true;
     this.clearObs=false;
      this.addObs=false;
   }
  else if (mouseX>200 && mouseX<300 && mouseY<40 && mouseY>0)
   {
     this.start=false;
     this.end=false;
      this.run=true;
      this.addObs=false;
      this.clearObs=false;
   }
   else if (mouseX>300 && mouseX<400 && mouseY<40 && mouseY>0)
   {
     this.start=false;
     this.end=false;
      this.addObs=true;
      this.clearObs=false;
   }
   else if (mouseX>400 && mouseX<500 && mouseY<40 && mouseY>0)
   {
     this.start=false;
     this.end=false;
      this.addObs=false;
      this.clearObs=true;
   }
   if(this.start)
   {
    strt=new PVector(mouseX,mouseY);
   }
   else if(this.end)
   {
     endPoint=new PVector(mouseX,mouseY);
   }
   else if(this.clearObs)
   {
     obs=new ArrayList<obstacle>();
   }
 }
 void mouseDragged()
 {
  if(this.addObs)
  {
    obs.add(new obstacle(new PVector(mouseX,mouseY),10));
  }
 }
}
