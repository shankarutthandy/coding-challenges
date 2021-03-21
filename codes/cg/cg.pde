float offset=-PI/3;
float offsetA=0;
float offsetB=PI/3;
float amplitude=180;
void setup()
{
  size(600,400);
}
void draw()
{
  background(51);
  stroke(255);
  strokeWeight(2);
  fill(color(0,0,255));
  pushMatrix();
  translate(100,0);
  for(int i=0;i<21;i++)
  {
    float ang= i*PI/20;
    
    line(-90*abs(sin(ang+offset)),i*20,90*abs(sin(ang+offset)),i*20);
    
    ellipse(-90*abs(sin(ang+offset)),i*20,10,10);
    ellipse(90*abs(sin(ang+offset)),i*20,10,10);
  }
  //line(0,50,180,50);
  popMatrix();
  pushMatrix();
  translate(300,0);
  for(int i=0;i<21;i++)
  {
    float ang= i*PI/20;
    line(-90*abs(sin(ang+offsetA)),i*20,90*abs(sin(ang+offsetA)),i*20);
    
    ellipse(-90*abs(sin(ang+offsetA)),i*20,10,10);
    ellipse(90*abs(sin(ang+offsetA)),i*20,10,10);
  }
  //line(0,100,180,100);
  popMatrix();
  pushMatrix();
  translate(500,0);
  for(int i=0;i<21;i++)
  {
    float ang= i*PI/20;
    line(-90*abs(sin(ang+offsetB)),i*20,90*abs(sin(ang+offsetB)),i*20);
      
    ellipse(-90*abs(sin(ang+offsetB)),i*20,10,10);
    ellipse(90*abs(sin(ang+offsetB)),i*20,10,10);
  }
  //line(0,200,180,200);
  popMatrix();
  offset+=0.02;
  offsetA+=0.02;
  offsetB+=0.02;
  
}
