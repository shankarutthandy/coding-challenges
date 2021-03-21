quadTree qt;
void setup()
{
  size(800,800);
  qt=new quadTree(new boundary(width/2,height/2,width/2,height/2),4);
  
}
void mouseDragged()
{
  for(int i=0;i<5;i++)
  {
  qt.insert(new pts(mouseX+floor(random(-50,50)),mouseY+floor(random(-50,50))));
  }
}
void draw()
{
  background(0);
  qt.show();
  boundary qry=new boundary(mouseX,mouseY,100,100);
  qt.query(qry);
  qry.highlight();
  
}
class quadTree
{
  boundary bound;
  ArrayList<pts> points;
  int capacity;
  boolean divided;
  quadTree tr,tl,br,bl;
  quadTree(boundary bound_,int cap)
  {
    bound=bound_;
    capacity=cap;
    divided=false;
    points=new ArrayList<pts>();
  }
  void insert(pts pnt)
  {
    if(!this.bound.isIn(pnt))
    {
      return;
    }
    if(this.points.size()<this.capacity)
    {
      this.points.add(pnt);
    }
    else
    {
      if(!this.divided)
      {
        this.divide();
        this.divided=true;
      }
      this.tr.insert(pnt);
      this.tl.insert(pnt);
      this.br.insert(pnt);
      this.bl.insert(pnt);
    }
  }
  void divide()
  {
    int x=this.bound.x;
    int y=this.bound.y;
    int w=this.bound.w;
    int h=this.bound.h;
    this.tr=new quadTree(new boundary(x+w/2,y-h/2,w/2,h/2),this.capacity);
    this.tl=new quadTree(new boundary(x-w/2,y-h/2,w/2,h/2),this.capacity);
    this.br=new quadTree(new boundary(x+w/2,y+h/2,w/2,h/2),this.capacity);
    this.bl=new quadTree(new boundary(x-w/2,y+h/2,w/2,h/2),this.capacity);
  }
   void show()
   {
     this.bound.show();
     //for(pts p:this.points)
     //{
     //  p.show();
     //}
     if(this.divided)
     {
       this.tr.show();
       this.tl.show();
       this.br.show();
       this.bl.show();
     }
   }
   void query(boundary range)
   {
    if(!this.bound.intersect(range))
    {
      return;
    }
    else
    {
      for(pts p:this.points)
      {
        if(range.isIn(p))
          {
            p.highlight();
          }
      }
      if(this.divided)
      {
        this.tr.query(range);
        this.tl.query(range);
        this.br.query(range);
        this.bl.query(range);
      }
      
    }
   }
}
