from turtle import back
import pygame
import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS']="300,30"
clock=pygame.time.Clock()
pygame.init()
pygame.mixer.init()
sound=pygame.mixer.Sound("images//music.mp3")
sound.play(-1)
score=0
def quiz_q1():
    print("\nI light the way but burn away.")
    print("I fear the wind but love the dark.\n")
    ans = input("What am I? ").lower()
    return ans == "torch"

def quiz_q2():
    print("""I have keys but no locks.
I have space but no room.
You can enter, but can’t go outside.
What am I?\n""")   
    ans = input("What am I? ").lower()
    return ans == "keyboard" 

def quiz_q3():
   print("""The more you take, the more you leave behind.
What am I?\n""")
   ans = input("What am I? ").lower()
   return ans == "footsteps"

def quiz_q4():
   print("""I speak without a mouth and hear without ears.\n""")
   ans=input("What am I? ").lower()
   return ans=="echo"

test_font=pygame.font.SysFont("Arial",30)
def display_start():
    start=test_font.render("Press SPACE to start",True,(255,255,255))
    window.blit(start,(400,400))
def gameover():
    over=test_font.render("GAME OVER",True,(255,0,0))
    window.blit(over,(400,400))

def winner_screen():
    won_img=pygame.image.load("images\\won.jpg")
    
    window.blit(won_img, (0, 0))
    
    pygame.display.update()
    pygame.time.delay(3000)
    exit()

qn_answered=["none","no","no","no","no"]
lives=0
window=pygame.display.set_mode((1000,500),0,12)
room=1
prev_room=0
x=[pygame.image.load("images\\k09fmpg9ta451.jpg"),pygame.image.load("images\\create a pixel style dungeon with oonly x axis path.jpg"),pygame.image.load("images\\1d dungeon trail pixel trail.jpg"),pygame.image.load("images\\create a pixel style dungeon for 1d.jpg"),pygame.image.load("images\\images.jpg")]
BACK=x[room-1]

Player=pygame.image.load("images\\CREATE A PIXEL  STYLE DUNGEON CHARARER FOR A 1D GAME.png")


player_rect=Player.get_rect(midbottom=(100,350))
game=None
while True:
    if room!=prev_room:
    
       prev_room=room
       if room==2 and qn_answered[1]=="no":
          j=quiz_q1()
          if j:
             score+=1
             print("Correct! Your score is now ",score)
             qn_answered[1]="yes"
          else:
                print("Wrong answer.")
                lives-=1
                print("You lost a life. Lives left:",lives)
       elif room==3 and qn_answered[2]=="no":
          j=quiz_q2()
          if j:
             score+=1
             print("Correct! Your score is now ",score)
             qn_answered[2]="yes"  
          else:
                print("Wrong answer.")
                lives-=1
                print("You lost a life. Lives left:",lives)
       elif room==4 and qn_answered[3]=="no":
          j=quiz_q3()
          if j:
             score+=1
             print("Correct! Your score is now ",score)
             qn_answered[3]="yes"
          else:
                print("Wrong answer.")
                lives-=1
                print("You lost a life. Lives left:",lives)
       elif room==5 and qn_answered[4]=="no":
          j=quiz_q4()
          if j:
             score+=1
             print("Correct! Your score is now ",score)
             qn_answered[4]="yes"
          else:
                print("Wrong answer.")
                lives-=1
                print("You lost a life. Lives left:",lives)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if lives==0:
            display_start()
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            lives=3
            room=2
    window.blit(BACK,(0,0))
     
    if lives>0:
      
      if room==2:#in room 1
        if player_rect.x>=1000:
          room+=1
          player_rect.x=10
        
        #else:
          
         # print("")
      
                 
      elif room==3:#in room 2
        if player_rect.x>=1000:
          room+=1
          player_rect.x=10
        elif player_rect.x<=0:
           player_rect.x=950
           room-=1
       # else:
        #  print("")
               
   
      elif room==4:#in room 3
        if player_rect.x>=1000:
           room+=1
           player_rect.x=10
        elif player_rect.x<=0:
           player_rect.x=950
           room-=1
       # else:
         #  print("")

      elif room==5 :
        if player_rect.x>=1000:
        
          if score==4:

            game="won"
          elif score<4:
             if room==5 and player_rect.x>=1000:
                player_rect.x=950

                print("Not all questions answered correctly. Game Over.")  
          else:
        

            gameover()
            windows.blit(back,(100,100))
            windows.update()
            lives=-1 

        elif player_rect.x<=0:
           
           player_rect.x=950
           room-=1
       # else:
        #   print("")  
      elif  room>2:
        if player_rect.x<=0 :
           room-=1
          
        
           player_rect.x=1000
        
        
      
    
    
      key=pygame.key.get_pressed()
      if key[pygame.K_d] :
          player_rect.x+=10
     
      if key[pygame.K_a]  : 
          if room>2 or player_rect.x>20:
             player_rect.x-=10
    

     

      BACK=x[room-1]
      window.blit(BACK,(-10,-220))
      window.blit(Player,player_rect)
    elif lives==0:
        display_start()
    if game=="won":
    
        winner_screen()
        
        
             
    pygame.display.update()
    clock.tick(60)
 
 