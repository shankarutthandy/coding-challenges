from p5 import *
import numpy as np
import math as m
import random
game=None

def setup():   
    global game
    size(600,600)
    game=GAME()

def draw():       
    global game
    game.run()

class GAME:
    def __init__(self):
        self.blocks=-1*np.ones((3,3))   
        self.human=0                    
        self.computer=1                 
        self.flag=self.human            
    def run(self):
        self.update()
        self.render()
    def not_filled(self):
        for i in range(3):
            for j in range(3):
                if self.blocks[i][j]==-1:
                    return True
        return False
    def check_winner(self):
        for i in range(3):
            if self.blocks[i][0]==self.blocks[i][1]==self.blocks[i][2]:
                if self.blocks[i][1]!=-1:
                    return self.blocks[i][0]
        for i in range(3):
            if self.blocks[0][i]==self.blocks[1][i]==self.blocks[2][i]:
                if self.blocks[1][i]!=-1:
                    return self.blocks[1][i]
        if self.blocks[0][0]==self.blocks[1][1]==self.blocks[2][2]:
            if self.blocks[1][1]!=-1:    
                return self.blocks[1][1]
        if self.blocks[0][2]==self.blocks[1][1]==self.blocks[2][0]:
            if self.blocks[1][1]!=-1:    
                return self.blocks[1][1]
        return -1
    def minimax(self,depth,ismax):
        score=self.check_winner()
        if score==self.computer:
            score=10
            return score
        if score==self.human:
            score=-10
            return score
        if not self.not_filled():
            return 0.5
        if ismax:
            best=-1000
            for i in range(3):
                for j in range(3):
                    if self.blocks[i][j]==-1:
                        self.blocks[i][j]=self.computer
                        best=max(best-depth,self.minimax(depth+1,not ismax))
                        self.blocks[i][j]=-1
            return best
        else:
            best=1000
            for i in range(3):
                for j in range(3):
                    if self.blocks[i][j]==-1:
                        self.blocks[i][j]=self.human
                        best=min(best+depth,self.minimax(depth+1,not ismax))
                        self.blocks[i][j]=-1
            return best  
    def get_ai_move(self):
        best_value=-1000
        best_move=(-1,-1)
        for i in range(3):
            for j in range(3):
                if self.blocks[i][j]==-1:
                    self.blocks[i][j]=self.computer
                    value=self.minimax(0,False)
                    self.blocks[i][j]=-1
                    if value > best_value:
                        best_value=value
                        best_move=(i,j)
        if self.not_filled():
            self.blocks[best_move[0]][best_move[1]]=self.computer                            
    def get_move(self):
        if not self.not_filled():
            return
        else:
            possible_choices=[]
            for i in range(3):
                for j in range(3):
                    if self.blocks[i][j]==-1:
                        possible_choices.append((i,j))
            choice=random.choice(possible_choices)
            self.blocks[choice[0]][choice[1]]=self.computer
    def update(self):
        if self.flag==self.human:
            if mouse_is_pressed:
                x=m.floor(float(mouse_x)/200)
                y=m.floor(float(mouse_y)/200)
                if self.blocks[y][x]==-1:   
                    self.blocks[y][x]=0 
                    self.flag=self.computer
        else:
            self.flag=self.human
            self.get_ai_move()
    def render(self):
        res=self.check_winner()
        background(255)
        stroke_weight(10)
        stroke(0)
        line(200,0,200,600)
        line(400,0,400,600)
        line(0,200,600,200)
        line(0,400,600,400) 
        stroke_weight(30)
        if res==-1 and self.not_filled():
            for i in range(1,4):
                 for j in range(1,4):
                    y,x=(2*i-1)*100,(2*j-1)*100
                    if self.blocks[i-1][j-1]==1:
                        stroke(255,0,0)
                        line(x-60,y-60,x+60,y+60)
                        line(x-60,y+60,x+60,y-60)
                    elif self.blocks[i-1][j-1]==0:
                        stroke(0,0,255)
                        ellipse(x,y,150,150)
        else:
            background(0)
            stroke_weight(30)
            fill(0)
            if res==1:
                stroke(255,0,0)
                line(100,100,500,500)
                line(100,500,500,100)
            elif res==0:
                stroke(0,0,255)
                ellipse(300,300,400,400)
            else:
                stroke(255,255,255)
                line(200,250,400,250)
                line(200,350,400,350)
run()