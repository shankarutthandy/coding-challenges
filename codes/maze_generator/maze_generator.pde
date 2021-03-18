int cols=20;
int rows=cols;
Astar path;
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
 if(contin==false)
 {
  path=new Astar(cells);
  path.display();
  noLoop();
  //float posx=cells[0][0].x;
  //float posy=cells[0][0].y;
  //noStroke();
  //fill(0,255,0);
  //ellipseMode(CORNER);
  //ellipse(posx*width/cols,posy*height/rows,width*0.8/cols,height*0.8/rows);
  //fill(255,0,0);
  //posx=cells[cols-1][rows-1].x;
  //posy=cells[cols-1][rows-1].y;
  //ellipse(posx*width/cols,posy*height/rows,width*0.8/cols,height*0.8/rows);
  //noLoop();
 }
}

class cell
{
 boolean[] walls={true,true,true,true};// Top Right Bottom Left
 float x;
 float y;
 boolean visited;
 int scale;
 float g;
 float h,f;
 cell previous;
 cell(float i,float j)
 {
 visited=false;
 x=i;
 y=j;
 scale=width/cols;
 g=0;
 h=0;
 previous=null;
 f=g+h;
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
  fill(255);
  rect(this.x*this.scale,this.y*this.scale,this.scale,this.scale);
  if(walls[0])
    stroke(0);
  else
    stroke(255);
  line(this.x*this.scale,this.y*this.scale,(this.x+1)*this.scale,this.y*this.scale);
  if(walls[1])
    stroke(0);
  else
    stroke(255);
  line((this.x+1)*this.scale,this.y*this.scale,(this.x+1)*this.scale,(this.y+1)*this.scale);
  if(walls[2])
    stroke(0);
  else
    stroke(255);  
  line((this.x+1)*this.scale,(this.y+1)*this.scale,this.x*this.scale,(this.y+1)*this.scale);
  if(walls[3])
    stroke(0);
  else
    stroke(255);  
  line(this.x*this.scale,(this.y+1)*this.scale,this.x*this.scale,this.y*this.scale);
 }
}
class Astar
{
 ArrayList<cell> OpenList;
 ArrayList<cell> ClosedList;
 int scale;
 cell[][] grid;
 Astar(cell[][] grid_)
 {
 grid=grid_;
 OpenList=new ArrayList<cell>();
 ClosedList=new ArrayList<cell>();
 OpenList.add(grid[0][0]);
 scale=width/cols;
 }
 void display()
 {
   

  while(this.OpenList.size()>0 )
  { int q=0;
    for(int i=0;i<this.OpenList.size();i++)
    {
      if(this.OpenList.get(i).f<this.OpenList.get(q).f)
      {
        q=i;
      }
    }
     cell curr=this.OpenList.get(q);
     this.OpenList.remove(q);
     
     
     ArrayList<cell> neighbours=this.neighbours(curr);
     for(int i=0;i<neighbours.size();i++)
    {
     cell neighbour=neighbours.get(i);
     if(!this.isIn(neighbour,this.ClosedList))
     {
      float tempG=curr.g+1;
      boolean isNewPath=false;
      if(this.isIn(neighbour,this.OpenList))
      {
        if(tempG<neighbour.g)
        {neighbour.g=tempG;
        isNewPath=true;
        }}
        
        else{
          neighbour.g=tempG;
          isNewPath=true;
          this.OpenList.add(neighbour);
          
        }
        if(isNewPath)
        {
          neighbour.h=abs(cols-1-neighbour.x)+abs(cols-1-neighbour.y);
          neighbour.f=neighbour.g+neighbour.h;
          neighbour.previous=curr;
          
        }
      }
       
     }
     this.ClosedList.add(curr);
     
    }
  stroke(0);
  strokeWeight(4);
 cell temp=this.grid[cols-1][rows-1];
 while(temp.previous!=null)
 {
  line(temp.x*this.scale+this.scale/2,temp.y*this.scale+this.scale/2,temp.previous.x*this.scale+this.scale/2,temp.previous.y*this.scale+this.scale/2); 
  temp=temp.previous;
 }
 
  
 }
 boolean isIn(cell check,ArrayList<cell> in)
 {
  for(cell c:in)
  {
   if(c.x==check.x && c.y==check.y)
   {
     return true;
   }
  }
  return false;
 }
ArrayList<cell> neighbours(cell q)
{
  ArrayList<cell> neighbours=new ArrayList<cell>();
  int i=int(q.x);
  int j=int(q.y);
  cell current=this.grid[i][j];
  int indexi=0;
  int indexj=0;
  indexi=i+1;
  indexj=j;
  if(!(indexi<0 || indexi>cols-1 || indexj>cols-1 || indexj<0))
  {
    if(!current.walls[1])
      neighbours.add(this.grid[indexi][indexj]);
  }
  indexi=i;
  indexj=j+1;
  if(!(indexi<0 || indexi>cols-1 || indexj>cols-1 || indexj<0))
  {
    if(!current.walls[2])
      neighbours.add(this.grid[indexi][indexj]);
  }
  indexi=i-1;
  indexj=j;
  if(!(indexi<0 || indexi>cols-1 || indexj>cols-1 || indexj<0))
  {
    if(!current.walls[3])
      neighbours.add(this.grid[indexi][indexj]);
  }
  indexi=i;
  indexj=j-1;
  if(!(indexi<0 || indexi>cols-1 || indexj>cols-1 || indexj<0))
  {
    if(!current.walls[0])
      neighbours.add(this.grid[indexi][indexj]);
  }
  return neighbours;
  
}
}
