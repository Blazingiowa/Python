import tkinter
import random

FNT=("Times New Roman",20,"bold")

key=""
keyoff=False
idx=0
tmr=0
stage=0
score=0
bar_x=0
bar_y=0
ball_x=0
ball_y=0
ball_xp=0
ball_yp=0
is_clr=True

block=[]
for i in range(5):
    block.append([1]*10)
for i in range(10):
    block.append([0]*10)

def key_down(e):
    global key
    key=e.keysym

def key_up(e):
    global keyoff
    keyoff=True