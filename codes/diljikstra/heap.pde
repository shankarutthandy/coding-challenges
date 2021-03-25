class vertx
{
  PVector pose;
  float cost;
  boolean processed;
  int idx;
  vertx previous;
  vertx(PVector pose_,int index)
  {
    pose=pose_;
    previous=null;
    cost=50000000;
    processed=false;
    idx=index;
  }
}

class minHeap
{
  ArrayList<vertx> vertices;
 minHeap()
 {
 vertices=new ArrayList<vertx>();
 }
 void bubbleUp(int index)
 {
   while(this.hasParent(index) && this.vertices.get(this.getParentIndex(index)).cost>this.vertices.get(index).cost)
   {
     int pindex=this.getParentIndex(index);
     Collections.swap(this.vertices,index,pindex);
     this.vertices.get(index).idx=index;
     this.vertices.get(pindex).idx=pindex;
     index=pindex;
   }
   
 }
 void bubbleDown(int index)
 {
   while(this.hasLeft(index))
   {
     int smallest=this.leftIndex(index);
     if(this.hasRight(index) && this.vertices.get(smallest).cost>this.vertices.get(this.rightIndex(index)).cost)
           smallest=this.rightIndex(index);
     if(this.vertices.get(smallest).cost>this.vertices.get(index).cost)
         break;
     Collections.swap(this.vertices,index,smallest);
     this.vertices.get(smallest).idx=smallest;
     this.vertices.get(index).idx=index;
     index=smallest;
   }
 }
 boolean hasRight(int index)
 {
  if(index*2 +2 > this.vertices.size()-1)
    return false;
  return true;
 }
 boolean hasLeft(int index)
 {
  if(index*2 +1 > this.vertices.size()-1)
    return false;
  return true;
 }
 int leftIndex(int index)
 {
   return (index*2) + 1 ;
 }
 int rightIndex(int index)
 {
   return (index*2) + 2 ;
 }
 boolean hasParent(int index)
 {
  if(index<=0)
     return false;
  else 
     return true;  
 }
 int getParentIndex(int index)
  {
    
    if(index%2==0)
      return floor((index-2)/2);
   else
     return floor((index-1)/2);
  }
  ArrayList<vertx> getNeighbours(vertx[][] matrix,vertx v,ArrayList<obstacle> o)
  {
   ArrayList<vertx> neighb=new ArrayList<vertx>();
   int x=floor((v.pose.x/scl)-0.5);
   int y=floor((v.pose.y/scl)-0.5);
   int tempx,tempy;
   tempx=x+1;
   tempy=y;
   if(tempx<width/scl && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   tempx=x;
   tempy=y+1;
   if(tempy<height/scl && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   tempx=x-1;
   tempy=y;
   if(tempx>0 && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   tempx=x;
   tempy=y-1;
   if(tempy>0 && !this.isObs(tempx,tempy,o))
      neighb.add(matrix[tempx][tempy]);
   tempx=x+1;
   tempy=y+1;
   if(tempx<width/scl && tempy<height/scl && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   tempx=x-1;
   tempy=y-1;
   if(tempx>0 && tempy>0 && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   tempx=x+1;
   tempy=y-1;
   if(tempx<width/scl && tempy>0 && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   tempx=x-1;
   tempy=y+1;
   if(tempy<height/scl && tempx>0 && !this.isObs(tempx,tempy,o))
     neighb.add(matrix[tempx][tempy]);
   return neighb;
  }
  boolean isObs(int x,int y,ArrayList<obstacle> obstacles)
  {
    for(obstacle o:obstacles)
    {
      if(o.pose.x==x && o.pose.y==y)
        return true;
    }
    return false;
  }
}
