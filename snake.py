import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time
import os
from pynput.keyboard import Key, Listener, KeyCode

def on_press(key):
    global direction

    if key == KeyCode.from_char('q'):
        os._exit(1)
    elif key is key.up and direction!='d':
        direction='u'
    elif key is key.down and direction!='u':
        direction='d'
    elif key is key.right and direction!='l':
        direction='r'
    elif key is key.left and direction!='r':
        direction='l'

def update_world(world,snake,food,w,h):
    global score
    img=[[0 for i in range(w)] for j in range(h)]
    for i in snake:
        if i[0]<0 or i[0]>=h or i[1]<0 or i[1]>=w:
            os._exit(0)
        img[i[0]][i[1]]=1
    img[food[0]][food[1]]=1
    if snake[-1][0] == food[0] and snake[-1][1] == food[1]:
        score+=1
        snake.insert(0,[food[0],food[1]])
        f=put_food(w,h)
        food[0]=f[0]
        food[1]=f[1]
    for i in range(h):
        for j in range(w):
            world[i][j]=img[i][j]


def render(world,im):
    im.set_data(world)
    plt.pause(0.01)


def move(snake):
    global direction
    res=[]
    if direction=='r':
        for i in range(1,len(snake)):
            res.append(snake[i])
        res.append([snake[-1][0],snake[-1][1]+1])
    elif direction=='l':
        for i in range(1,len(snake)):
            res.append(snake[i])
        res.append([snake[-1][0],snake[-1][1]-1])
    elif direction=='d':
        for i in range(1,len(snake)):
            res.append(snake[i])
        res.append([snake[-1][0]+1,snake[-1][1]])
    elif direction=='u':
        for i in range(1,len(snake)):
            res.append(snake[i])
        res.append([snake[-1][0]-1,snake[-1][1]])
    return res


def put_food(w,h):
    y=int(random.random()*w)
    x=int(random.random()*h)
    return [x,y]


def main():
    global score
    w=60
    h=40
    snake=[[int(h/2),int(w/2)],[int(h/2),int(w/2+1)],[int(h/2),int(w/2+2)]]
    world=[[0 for i in range(w)] for j in range(h)]
    food=put_food(w,h)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_axis_off()
    ax.set_title("Pyt{{PYTHON}}hon")
    im=ax.imshow(world,cmap='gray',vmin=-0, vmax=1)
    txt=ax.text(5, 38, 'Score : '+str(score),color='white')
    ax.text(45, 38, 'Press Q to exit ',color='white')
    listener=Listener(on_press=on_press)
    listener.start()
    while(True):
        txt.set_text("Score : "+str(score))
        snake=move(snake)
        update_world(world,snake,food,w,h)
        render(world,im)
        time.sleep(0.1)

score=0
direction='r'

if __name__=='__main__':
    main()
