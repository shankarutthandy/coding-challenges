boundary[] bound=new boundary[7];
entity ent;
float xoff=0;
float yoff=0;
int sceneW=0;
int sceneH=0;
void setup()
{
  size(800,400);
  sceneW=width/2;
  sceneH=height;
  for(int i=0;i<3;i++)
  {
    bound[i]=new boundary(random(sceneW),random(sceneH),random(sceneW),random(sceneH));
  }
  bound[3]=new boundary(0,0,sceneW,0);
  bound[4]=new boundary(sceneW,0,sceneW,sceneH);
  bound[5]=new boundary(sceneW,sceneH,0,sceneH);
  bound[6]=new boundary(0,sceneH,0,0);
  
  ent=new entity(new PVector(300,300),bound);

}

void draw()
{ background(0);
if(keyPressed)
{
  ent.keyUpdate(key);
}
//ent.update(mouseX,mouseY);

  for(int i=0;i<bound.length;i++)
  {
    bound[i].show();
  }
  ent.show();
  xoff+=0.01;
  yoff+=0.01;


}
