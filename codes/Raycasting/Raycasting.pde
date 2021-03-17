boundary[] bound=new boundary[7];
entity ent;
float xoff=0;
float yoff=0;
void setup()
{
  size(500,500);
  for(int i=0;i<3;i++)
  {
    bound[i]=new boundary(random(500),random(500),random(500),random(500));
  }
  bound[3]=new boundary(0,0,800,0);
  bound[4]=new boundary(800,0,800,800);
  bound[5]=new boundary(800,800,0,800);
  bound[6]=new boundary(0,800,0,0);
  
  ent=new entity(300.0,300.0,bound);
  //ray=new Ray(300,300,PVector.fromAngle(PI/4));
}

void draw()
{ background(0);
  //ent.x=mouseX;
  //ent.y=mouseY;
  //for(int i=0;i<ent.rays.size();i++)
  //{
  //  ent.rays.get(i).x=mouseX;
  //  ent.rays.get(i).y=mouseY;
  //}
  ent.x=mouseX;//noise(xoff)*500;
  ent.y=mouseY;//noise(yoff)*500;
   for(int i=0;i<ent.rays.size();i++)
  {
    ent.rays.get(i).x=ent.x;
    ent.rays.get(i).y=ent.y;
  }
  //ray.setdir(mouseX,mouseY);
  for(int i=0;i<bound.length;i++)
  {
    bound[i].show();
  }
  ent.show();
  xoff+=0.01;
  yoff+=0.01;
  //PVector cast=ray.cast(bound);
//  if(cast.x!=-1)
//  { fill(255);
//    ellipse(cast.x,cast.y,10,10);
//  }
//  else
//  ray.c=color(255,0,0);
//  ray.show();

}
