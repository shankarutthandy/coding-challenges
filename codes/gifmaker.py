'''
Create gif of ur processing session:

How to Use =>

    1.create a createGif object
    2.inside the draw method of ur sketch call the record function
    3.keep pressing 'r' to record or keep clicking it to generate continous images
    4.press 's' or click the square block icon once to generate gif in the image directory or image_path

'''
from p5 import *
import os
import imageio
import pygame
class createGifPygame:
    def __init__(self,surface,gif_name,img_name,image_path=os.getcwd(),duration=0.10):
            self.gif_name=gif_name
            self.count=0
            self.img_name=img_name.split('.')[0]
            self.image_path=image_path+'/images'
            self.duration=duration
            self.surface=surface
            self.curr_key=None
    def record(self):
        if self.curr_key=='r':
            print('recording')
            pygame.image.save(self.surface,self.image_path+'/'+self.img_name+str(self.count)+'.png')
        if self.curr_key=='s':    
            print('#------GIF-CREATED-------#')
            self.create_gif()
            self.curr_key=None
        self.count+=1
    def create_gif(self):
        image_list=[]
        kargs={ 'duration': self.duration }
        file_list=sorted([f for f in os.listdir(self.image_path)if (f.endswith('.jpg') or f.endswith('.png')) and f.startswith(self.img_name)])    
        for f in file_list:
            image_list.append(imageio.imread(os.path.join(self.image_path,f)))
        imageio.mimsave(os.path.join(self.image_path,self.gif_name),image_list,**kargs)
        for f in file_list:
            os.remove(os.path.join(self.image_path,f)) 
class createGif:
    def __init__(self,gif_name,img_name,image_path=os.getcwd(),duration=0.10):
        self.gif_name=gif_name
        self.img_path=image_path+'/images'
        self.duration=duration
        self.store=self.img_path+'/'+img_name
        self.name=img_name.split('.')[0]
    def record(self):
        k=200
        k1=200
        if (key_is_pressed and key=='r') or (mouse_is_pressed and mouse_x<50 and mouse_x>0 and mouse_y<50 and mouse_y>0):
            k=50
            save_frame(self.store)
        if (key_is_pressed and key=='s') or (mouse_is_pressed and mouse_x<100 and mouse_x>50 and mouse_y<50 and mouse_y>0):
            print('...................GIF-saved.....................')
            self.createGif()
        no_stroke()
        fill(k)
        ellipse(25,25,50,50)
        fill(Color(255,30,30))
        triangle((12,10),(12,40),(42,25))
        fill(k1)
        ellipse(75,25,50,50)
        fill(0)
        rect_mode('CENTER')
        rect(75,25,25,25)
    def createGif(self):
        image_list=[]
        kargs={ 'duration': self.duration }
        file_list=sorted([f for f in os.listdir(self.img_path)if (f.endswith('.jpg') or f.endswith('.png')) and f.startswith(self.name)])    
        for f in file_list:
            image_list.append(imageio.imread(os.path.join(self.img_path,f)))
        imageio.mimsave(os.path.join(self.img_path,self.gif_name),image_list,**kargs)
        for f in file_list:
            os.remove(os.path.join(self.img_path,f))