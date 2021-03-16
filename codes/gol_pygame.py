import pygame
import numpy as np 

class game:
    def __init__(self,width,height):
        self.width=width;self.height=height
        self.rows=int(self.height/20)
        self.cols=int(self.width/20)
        self.matrix=np.zeros((self.rows,self.cols),dtype=np.int)
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]=np.random.randint(0,2,dtype=np.int)
    def update(self):
        temp=self.matrix.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours=0
                for k in range(-1,2):
                    for l in range(-1,2):
                        m=i+k
                        n=j+l
                        if m==self.rows:m=0
                        if n==self.cols:n=0
                        neighbours+=self.matrix[m][n]
                neighbours-=self.matrix[i][j]
                temp[i][j]=self.rule(K=self.matrix[i][j],N=neighbours)
        self.matrix=temp
    def rule(self,K,N):
        if K==1 and N<2:
            return 0
        elif K==1 and N>3:
            return 0
        elif K==0 and N==3:
            return 1
        else:
            return K
    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j]==1:
                    pygame.draw.rect(WIN,(0,0,0),pygame.Rect(j*20,i*20,20,20)) 
                    
                else:
                    pygame.draw.rect(WIN,(255,255,255),pygame.Rect(j*20,i*20,20,20)) 
                    
pygame.init()
HEIGHT=800
WIDTH=800
WIN=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Game of Life')
ga=game(WIDTH,HEIGHT)
clk=pygame.time.Clock()
def main():
    run=True
    while run:
        clk.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        WIN.fill((255,255,255))
        ga.display()
        ga.update()
        pygame.display.flip()
if __name__=='__main__':
    main()