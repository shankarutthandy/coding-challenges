import java.util.Collections;
int scl=40;
dstra path;
PVector start,end;
ArrayList<obstacle> o=new ArrayList<obstacle>();
boolean strt=false;
void setup()
{
  size(800,800);
  background(255);
}
void keyPressed()
{
  if(key=='r')
  strt=true;
  if(key=='x')
  o=new ArrayList<obstacle>();
  if(key=='s')
  {
  strt=false;
  int x=floor(mouseX/scl);
  int y=floor(mouseY/scl);
  x=x*scl + scl/2;
  y=y*scl + scl/2;
  start=new PVector(x,y);
  }
  if(key=='e')
  {
  strt=false;
  int x=floor(mouseX/scl);
  int y=floor(mouseY/scl);
  x=x*scl + scl/2;
  y=y*scl + scl/2;
  end=new PVector(x,y);
  }
}
void mouseDragged()
{
  int x=floor(mouseX/scl);
  int y=floor(mouseY/scl);
  x=x*scl + scl/2;
  y=y*scl + scl/2;
  o.add(new obstacle(new PVector(x,y)));
}
void draw()
{
  background(255);
  text("\"s\" place start point\n \"e\" place end point\n \"x\" remove obstacles\n \"r\" find path (if any)",10,20);
 gridShow();
 if(strt && start!=null && end!=null)
 {
   if(path==null)
  path=new dstra(start,end,o);
  path.show();
 }
}
void gridShow()
{
  ellipseMode(CENTER);
  if(start!=null)
  {
  fill(color(0,255,0));
  ellipse(start.x,start.y,scl*0.5,scl*0.5);
  }
  if(end!=null)
  {
  fill(color(255,0,0));
  ellipse(end.x,end.y,scl*0.5,scl*0.5);
  }
  stroke(0);
  strokeWeight(1);
  rectMode(CENTER);
  fill(0);
  for(obstacle obs:o)
  {
    rect(obs.pixPose.x,obs.pixPose.y,scl*0.5,scl*0.5);
  }
 for(int j=0;j<=height;j+=scl)
 {
 line(0,j,width,j); 
 }
 for(int i=0;i<=width;i+=scl)
 {
 line(i,0,i,height); 
 }
      

}
class dstra
{
  minHeap pq;
  PVector start,end;
  vertx[][] mat;
  ArrayList<obstacle> obs;
  dstra(PVector start_,PVector end_, ArrayList<obstacle> o)
  {
    pq=new minHeap();
    start= start_;
    end= end_;
    obs=o;
    mat=new vertx[floor(width/scl)][floor(height/scl)];
    for(int i=0;i<floor(width/scl);i++)
    {for(int j=0;j<floor(height/scl);j++)
    {
      int x=floor(i*scl)+(scl/2);
      int y=floor(j*scl)+(scl/2);
      mat[i][j]=new vertx(new PVector(x,y),pq.vertices.size());
      pq.vertices.add(mat[i][j]);
    }
  }
  mat[floor((start.x/scl)-0.5)][floor((start.y/scl)-0.5)].cost=0;
  pq.bubbleUp(mat[floor((start.x/scl)-0.5)][floor((start.y/scl)-0.5)].idx);
  }
  void update()
  {
    while(this.pq.vertices.size()>0)
    {
      vertx u=this.pq.vertices.get(0);
      u.processed=true;
      Collections.swap(this.pq.vertices,0,this.pq.vertices.size()-1);
      u.idx=0;
      this.pq.vertices.remove(this.pq.vertices.size()-1);
      this.pq.bubbleDown(0);
      ArrayList<vertx> neighbours=this.pq.getNeighbours(this.mat,u,this.obs);
      for(vertx n:neighbours)
      {
        if(n.processed)
        continue;
        float d=PVector.dist(n.pose,u.pose);
        if(u.cost+d<n.cost)
        {
          n.cost=u.cost+d;
          n.previous=u;
          int inx=n.idx;
          this.pq.bubbleDown(inx);
          this.pq.bubbleUp(inx);
        }
      }
    }
  }
  void show()
  {
    this.update();
    vertx temp=this.mat[floor((end.x/scl)-0.5)][floor((end.y/scl)-0.5)];
    stroke(color(0,0,255));
    strokeWeight(2);
    if(temp.previous==null)
    {
      background(255);
      textMode(CENTER);
      text("NO SOLUTION",350,400);
      noLoop();
    }
    while(temp.previous!=null)
    {
      line(temp.pose.x,temp.pose.y,temp.previous.pose.x,temp.previous.pose.y);
      temp=temp.previous;
    }
    noLoop();
    //saveFrame("diljikstra.png");
  }
}
class obstacle
{
  PVector pose;
  PVector pixPose;
  obstacle(PVector pix)
  {
    pose=new PVector(floor((pix.x/scl)-0.5),floor((pix.y/scl)-0.5));
    pixPose=pix;
  }
}
