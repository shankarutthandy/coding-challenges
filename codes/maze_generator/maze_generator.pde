int cols=20;
int rows=cols;
int sze=800;
cell[][] cells=new cell[cols][rows];
ArrayList<cell> stack=new ArrayList<cell>();
cell current;
void setup()
{
  size(800,800);
  for(int i=0;i<cols;i++)
  {
   for(int j=0;j<rows;j++)
    {
      cells[i][j]=new cell(i,j);
    }
  }
  current = cells[0][0];
  stack.add(current);
}
void draw()
{background(255);
boolean contin=false;
for(int i=0;i<cols;i++)
 {
for(int j=0;j<rows;j++)
{
 cells[i][j].draw();
 if(contin==false && cells[i][j].visited==false)
   contin=true;
}
 }
 if(contin==true)
 {
  current.visited=true;
  cell next=current.checkNeighbors();
  if(next!=current)
  {stack.add(next);
  current=next;
  }
  else
  {stack.remove(stack.size()-1);
  current=stack.get(stack.size()-1);
  }
 
 }
}

class cell
{
 boolean[] walls={true,true,true,true};// Top Right Bottom Left
 float x;
 float y;
 boolean visited;
 int scale;
 cell(float i,float j)
 {
 visited=false;
 x=i;
 y=j;
 scale=sze/cols;
 }
 
 cell checkNeighbors()
 {
  ArrayList<cell> neighbours=new ArrayList<cell>();
  int[] index=new int[2];
  index[0]=int(this.x);
  index[1]=int(this.y-1);
  //top
  if(index[0]>=0 && index[1]>=0 && index[0]<rows && index[1]<cols && !cells[index[0]][index[1]].visited)
  {
    neighbours.add(cells[index[0]][index[1]]);
  }
  //right
  index[0]=int(this.x+1);
  index[1]=int(this.y);
  if(index[0]>=0 && index[1]>=0 && index[0]<rows && index[1]<cols && !cells[index[0]][index[1]].visited)
  {
    neighbours.add(cells[index[0]][index[1]]);
  }  
  //bottom
  index[0]=int(this.x);
  index[1]=int(this.y+1);  
  if(index[0]>=0 && index[1]>=0 && index[0]<rows && index[1]<cols && !cells[index[0]][index[1]].visited)
  {
    neighbours.add(cells[index[0]][index[1]]);
  }  
  //left
  index[0]=int(this.x-1);
  index[1]=int(this.y);  
  if(index[0]>=0 && index[1]>=0 && index[0]<rows && index[1]<cols && !cells[index[0]][index[1]].visited)
  {
    neighbours.add(cells[index[0]][index[1]]);
  }     
  if(neighbours.size()>0)
  {
    int sel=int(random(neighbours.size()));
    cell selected=neighbours.get(sel);
    if(int(selected.x-this.x)==0)
    {
     if(int(selected.y-this.y)==1)
     {this.walls[2]=false;
      selected.walls[0]=false;
     }
     else
     {
       this.walls[0]=false;
       selected.walls[2]=false;
     }
    }
    else if(selected.y-this.y==0)
    {
    if(int(selected.x-this.x)==1)
     {this.walls[1]=false;
      selected.walls[3]=false;
     }
     else
     {
       this.walls[3]=false;
       selected.walls[1]=false;
     }      
    }
    
    return  selected;
  }
  else
  {
   return cells[int(this.x)][int(this.y)]; 
  }
  
 }
 void draw()
 {
  noStroke();
  if(!this.visited)
  fill(0);
  else
  fill(255,0,255);
  rect(this.x*this.scale,this.y*this.scale,this.scale,this.scale);
  if(walls[0])
    stroke(255);
  else
    stroke(255,0,255);
  line(this.x*this.scale,this.y*this.scale,(this.x+1)*this.scale,this.y*this.scale);
  if(walls[1])
    stroke(255);
  else
    stroke(255,0,255);
  line((this.x+1)*this.scale,this.y*this.scale,(this.x+1)*this.scale,(this.y+1)*this.scale);
  if(walls[2])
    stroke(255);
  else
    stroke(255,0,255);  
  line((this.x+1)*this.scale,(this.y+1)*this.scale,this.x*this.scale,(this.y+1)*this.scale);
  if(walls[3])
    stroke(255);
  else
    stroke(255,0,255);  
  line(this.x*this.scale,(this.y+1)*this.scale,this.x*this.scale,this.y*this.scale);
 }
}
