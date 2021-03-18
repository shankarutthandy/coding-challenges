ArrayList<Circle> circles=new ArrayList<Circle>();
PImage img;
ArrayList<PVector> validPoints=new ArrayList<PVector>();
void setup()
{
  size(478,500);
  img=loadImage("monkey.png","png");
  img.loadPixels();
  
  for(int i=0;i<width;i++)
  {
    for(int j=0;j<height;j++)
    {
      int pos=i+ j*pixelWidth;
      if(brightness(img.pixels[pos])>1)
      {
        validPoints.add(new PVector(i,j));
      }
    }
  }

}

void draw()
{
  background(0);
  //float randx=random(width);
  //float randy=random(height);
  //int count=0;
  //while(true)
  //{ if(count>1000)
  //  break;
  //  boolean isValid=true;
  //  for(Circle c:circles)
  //  {
  //    if(dist(c.c.x,c.c.y,randx,randy)<c.r+4)
  //    {
  //      isValid=false;
  //      break;
  //    }
  //  }
  //  if(isValid)
  //  {
  //    break;
  //  }
  //  randx=random(width);
  //  randy=random(height);
  //  count++;
  //}
  float rand=random(validPoints.size());
  float randx=validPoints.get(floor(rand)).x;
  float randy=validPoints.get(floor(rand)).y;
  int count=0;

  while(true)
  {
    if(count>1000)
    break;
    boolean isValid=true;
    for(Circle c:circles)
    {
    if(dist(c.c.x,c.c.y,randx,randy)<c.r+4)
    {
      isValid=false;
      break;
    }
    }
    if(isValid)
    {
      break;
    }
    rand=random(validPoints.size());
    randx=validPoints.get(floor(rand)).x;
    randy=validPoints.get(floor(rand)).y;
    count++;
    
  }
  if(count>1000)
  {
   print("finished");
  for(Circle c:circles)
  {
    c.show();
 
  }
   noLoop();
    
  }
  circles.add(new Circle(new PVector(randx,randy)));
  for(Circle c:circles)
  {
    collision(c);
    c.show();
    c.grow();
 
  }
  //if(count>=1000)
  //{
  //  print("finished");
  //  noLoop();
  //}
}

void collision(Circle k)
{
  boolean growth=true;
 for(Circle c:circles)
 {
   if(k==c) 
   continue;
  if(dist(k.c.x,k.c.y,c.c.x,c.c.y)<k.r+c.r+4)
  {
    growth=false;
    break;
  }
 }
 k.grow=growth;
 
}
class Circle
{
  PVector c;
  int r;
  boolean grow;
  Circle(PVector j)
{
  c=j;
  r=1;
  grow=true;
  }
  void grow()
  {
    this.edges();
    if(grow)
    this.r+=1;
  }
  void show()
  {
    fill(255);
    stroke(255);
    strokeWeight(3);
    ellipse(this.c.x,this.c.y,this.r*2,this.r*2);
  }
  void edges()
  {
    if(this.c.x+this.r>width || this.c.x-this.r<0 || this.c.y+this.r>height || this.c.y-this.r<0 || this.r>5)
    {
      this.grow=false;
    }
  }
  
}
  
