ArrayList<cell> cells=new ArrayList<cell>();

void setup()
{
  size(800,800);
  for(int i=0;i<5;i++)
  {
  cells.add(new cell(new PVector(random(800),random(800)),60));
  }
}
void draw()
{
  background(0);
  for(cell c:cells)
  {
    c.show();
  }
}

void mousePressed()
{
  for(int i=cells.size()-1;i>=0;i--)
  {
    if(cells.get(i).clicked(mouseX,mouseY))
    {
           cell cellA=cells.get(i).child();
           cell cellB=cells.get(i).child();
           cells.remove(i);
           cells.add(cellA);
           cells.add(cellB);
           
    }
  }
  
}
