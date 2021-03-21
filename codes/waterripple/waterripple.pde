float damping=0.99;
float[][] buffer1;
float[][] buffer2;

void setup()
{
  size(800,800);
  buffer1=new float[width][height];
  buffer2=new float[width][height];
  
}
void mouseDragged()
{
  buffer1[mouseX][mouseY]=255;
}
void draw()
{
  loadPixels();
  for(int i=1;i<width-1;i++)
  {for(int j=1;j<height-1;j++)
  {
    buffer1[i][j]=(buffer2[i+1][j]+buffer2[i-1][j]+buffer2[i][j+1]+buffer2[i][j-1])/2 - buffer1[i][j];
    buffer1[i][j]*=damping;
    int index=i+j*width;
     pixels[index]=color(buffer1[i][j]*255); 
    
    
  }}
  updatePixels();
  float[][] temp=buffer2;
  buffer2=buffer1;
  buffer1=temp;
}
