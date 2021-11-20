from tkinter import *
from random import *
from time import *
from timer import Timer
from playsound import playsound

root=Tk()

height_of_monitor=root.winfo_screenheight()
width_of_monitor=root.winfo_screenwidth()

width_game=1000
height_game=700

x = (width_of_monitor/2)-(width_game/2)
y = (height_of_monitor/2)-(height_game/1.75) 

root.geometry(f'{width_game}x{height_game}+{int(x)}+{int(y)}')
root.title('Space Intruders')

canvas=Canvas(width=width_game, height=height_game, bg='black')
canvas.config(cursor="none")
canvas.pack()

t=Timer(logger=None)

playsound('kevin_soundtrack.mp3', block = False)



for i in range(180):
    x=randint(0, 1000)
    y=randint(0, 700)
    canvas.create_oval(x,y,x+1,y+1)

score = 0

def mys_release(event):
    pass

spaceship_state='normal'

def motion(event):
    global spaceship, spaceship_img, bullet, spaceship_coordsX1, spaceship_coordsY1, spaceship_coordsX2, spaceship_coordsY2, img, canon, sniperX, sniperY, score
    global spaceship_state
    canvas.delete(spaceship)
    canvas.delete(canon)
    canvas.delete(spaceship_img)
    #canvas.update()
    #print(event.x, event.y)
    spaceship_img = canvas.create_image(event.x-35,630, anchor=NW, image=img, state=spaceship_state)
    spaceship = canvas.create_rectangle(event.x-25,680,event.x+25,670, state='hidden')
    canon = canvas.create_rectangle(event.x-7,680,event.x+7, 650, state='hidden')
    #canvas.update()
    spaceship_coordsX1=int(canvas.coords(spaceship)[0])
    spaceship_coordsX2=int(canvas.coords(spaceship)[2])
    spaceship_coordsY1=int(canvas.coords(spaceship)[1])
    spaceship_coordsY2=int(canvas.coords(spaceship)[3])
    #canvas.update()
    
    canvas.delete(sniperX)
    canvas.delete(sniperY)
    sniperX=canvas.create_line(event.x-10,event.y-10,event.x+10,event.y+10, state=spaceship_state)
    sniperY=canvas.create_line(event.x+10,event.y-10,event.x-10,event.y+10, state=spaceship_state)
    
    canvas.update()
    
bullet_coordsY=0
bullet_coordsX1=0
bullet_coordsX2=0

def úvodný_nákres():
    
    global cas, bullet, bullet_coordsX1, bullet_coordsX2, bullet_coordsY, target1, target2, target3, target4, target5, target6, target7, target8, target9, target10, target1_status, target2_status, target3_status, target4_status, target5_status, target6_status, target7_status, target8_status, target9_status, target10_status
    global tg1x1,tg1y1,tg1x2,tg1y2
    global tg2x1,tg2y1,tg2x2,tg2y2
    global tg3x1,tg3y1,tg3x2,tg3y2
    global tg4x1,tg4y1,tg4x2,tg4y2, canon
    global tg5x1,tg5y1,tg5x2,tg5y2
    global tg6x1,tg6y1,tg6x2,tg6y2
    global tg7x1,tg7y1,tg7x2,tg7y2
    global tg8x1,tg8y1,tg8x2,tg8y2
    global tg9x1,tg9y1,tg9y2,tg9x2
    global tg10x1,tg10y1,tg10y2,tg10x2
    global alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10
    global score, skore
    global premium_state1, premium_state2, premium_state3, premium_state4, premium_state5, premium_state6, premium_state7, premium_state8, premium_state9, premium_state10
    global poloha_skoreY, poloha_skoreX
    global sniperX, sniperY
    global spaceship_state
    global spaceship,  spaceship_img, choose_state, skst, img
    global premium_alienimg, alienimg
    
    choose_state ='hidden'
    spaceship_state='normal'

    img = PhotoImage(file='rocket6.png')
    spaceship_img = canvas.create_image(465,630, anchor=NW, image=img, state=spaceship_state)
    spaceship = canvas.create_rectangle(470,680,530,670, state='hidden')
    canon = canvas.create_rectangle(495,680,505,650, state='hidden')

    sniperX=canvas.create_line(490,340,510,360, state=spaceship_state)
    sniperY=canvas.create_line(510,340,490,360, state=spaceship_state)

    #rozmery stvorcov
    global rbnn, rbnv
    rbnn=500 # random bod najnizsi
    rbnv=60 # random bod najvyssi

    global rbnb, rbnd
    rbnb=10
    rbnd=950

    alienimg = PhotoImage(file='alien.png')
    premium_alienimg = PhotoImage(file='premium_alien4.png')

    skst='hidden' #skryt stvorce ('hidden') alebo zobrazit stvorce ('normal')
    
    #prvy stvorec (od lava)
    tg1x1=200  #ps1x
    tg1y1=300   #ps1y
    tg1x2=tg1x1+30
    tg1y2=tg1y1+30
    target1=canvas.create_rectangle(tg1x1-5,tg1y1-5,tg1x2,tg1y2, state=skst)
    alien1 = canvas.create_image(tg1x1-2.5,tg1y1-2.5, anchor=NW, image=alienimg)

    #druhy stvorec
    tg2x1=265   #ps2x
    tg2y1=300   #ps2y
    tg2x2=tg2x1+30
    tg2y2=tg2y1+30
    target2=canvas.create_rectangle(tg2x1-5,tg2y1-5,tg2x2,tg2y2, state=skst)
    alien2 = canvas.create_image(tg2x1-2.5,tg2y1-2.5, anchor=NW, image=alienimg)

    #treti stvorec
    tg3x1=330
    tg3y1=300
    tg3x2=tg3x1+30
    tg3y2=tg3y1+30
    target3=canvas.create_rectangle(tg3x1-5,tg3y1-5,tg3x2,tg3y2, state=skst)
    alien3 = canvas.create_image(tg3x1-2.5,tg3y1-2.5, anchor=NW, image=alienimg)

    #stvrty stvorec
    tg4x1=395
    tg4y1=300
    tg4x2=tg4x1+30
    tg4y2=tg4y1+30
    target4=canvas.create_rectangle(tg4x1-5,tg4y1-5,tg4x2,tg4y2, state=skst)
    alien4 = canvas.create_image(tg4x1-2.5,tg4y1-2.5, anchor=NW, image=alienimg)

    #piaty stvorec
    #ps5y = randint(rbnv,rbnn)
    #ps5x = randint(rbnb, rbnd)
    
    tg5x1=460
    tg5y1=300
    tg5x2=tg5x1+30
    tg5y2=tg5y1+30
    target5=canvas.create_rectangle(tg5x1-5,tg5y1-5,tg5x2,tg5y2, state=skst)
    alien5 = canvas.create_image(tg5x1-2.5,tg5y1-2.5, anchor=NW, image=alienimg)

    #siesty stvorec
    tg6x1=525
    tg6y1=300
    tg6x2=tg6x1+30
    tg6y2=tg6y1+30
    target6=canvas.create_rectangle(tg6x1-5,tg6y1-5,tg6x2,tg6y2, state=skst)
    alien6 = canvas.create_image(tg6x1-2.5,tg6y1-2.5, anchor=NW, image=alienimg)

    #siedmy stvorec
    tg7x1=590
    tg7y1=300
    tg7x2=tg7x1+30
    tg7y2=tg7y1+30
    target7=canvas.create_rectangle(tg7x1-5,tg7y1-5,tg7x2,tg7y2, state=skst)
    alien7 = canvas.create_image(tg7x1-2.5,tg7y1-2.5, anchor=NW, image=alienimg)

    #osmy stvorec
    tg8x1=655
    tg8y1=300
    tg8x2=tg8x1+30
    tg8y2=tg8y1+30
    target8=canvas.create_rectangle(tg8x1-5,tg8y1-5,tg8x2,tg8y2, state=skst)
    alien8 = canvas.create_image(tg8x1-2.5,tg8y1-2.5, anchor=NW, image=alienimg)

    #deviaty stvorec
    tg9x1=720
    tg9y1=300
    tg9x2=tg9x1+30
    tg9y2=tg9y1+30
    target9=canvas.create_rectangle(tg9x1-5,tg9y1-5,tg9x2,tg9y2, state=skst)
    alien9 = canvas.create_image(tg9x1-2.5,tg9y1-2.5, anchor=NW, image=alienimg)

    #desiaty stvorec
    tg10x1=785
    tg10y1=300
    tg10x2=tg10x1+30
    tg10y2=tg10y1+30
    target10=canvas.create_rectangle(tg10x1-5,tg10y1-5,tg10x2,tg10y2, state=skst)
    alien10 = canvas.create_image(tg10x1-2.5,tg10y1-2.5, anchor=NW, image=alienimg)

    score=0
    
    poloha_skoreX=500
    poloha_skoreY=40
    skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score))


canvas.config(cursor="none")

target1_status=0
target2_status=0
target3_status=0
target4_status=0
target5_status=0
target6_status=0
target7_status=0
target8_status=0
target9_status=0
target10_status=0

cas = 0

#hodnoty stvorcov

premium_state1 = 0
premium_state2 = 0
premium_state3 = 0
premium_state4 = 0
premium_state5 = 0
premium_state6 = 0
premium_state7 = 0
premium_state8 = 0
premium_state9 = 0
premium_state10 = 0

alien_state = 'normal'

def mys_press(event):
    global cakat_casu, cas, bullet, bullet_coordsX1, bullet_coordsX2, bullet_coordsY, target1, target2, target3, target4, target5, target6, target7, target8, target9, target10, target1_status, target2_status, target3_status, target4_status, target5_status, target6_status, target7_status, target8_status, target9_status, target10_status
    global tg1x1,tg1y1,tg1x2,tg1y2
    global tg2x1,tg2y1,tg2x2,tg2y2
    global tg3x1,tg3y1,tg3x2,tg3y2
    global tg4x1,tg4y1,tg4x2,tg4y2
    global tg5x1,tg5y1,tg5x2,tg5y2
    global tg6x1,tg6y1,tg6x2,tg6y2
    global tg7x1,tg7y1,tg7x2,tg7y2
    global tg8x1,tg8y1,tg8x2,tg8y2
    global tg9x1,tg9y1,tg9y2,tg9x2
    global tg10x1,tg10y1,tg10y2,tg10x2
    global alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10, premium_alienimg
    global rbnv,rbnn,rbnb, rbnd, spaceship_state, alien_state
    global score, skore
    global poloha_skoreY, poloha_skoreX, img, skst
    global premium_state1, premium_state2, premium_state3, premium_state4, premium_state5, premium_state6, premium_state7, premium_state8, premium_state9, premium_state10
    global sound_ind
    
    if cas < 1:
        cas +=1
        
        img2 = PhotoImage(file='fireball.png')
        fireball= canvas.create_image(event.x-5,640, anchor=NW, image=img2, state=alien_state)
        bullet=canvas.create_oval(event.x-5, 623, event.x+5, 640, tags='bob', state=skst)
        
        bullet_coordsX1=int(canvas.coords('bob')[0])
        bullet_coordsX2=int(canvas.coords('bob')[2])
        bullet_coordsY=int(canvas.coords('bob')[3])

        if sound_ind ==1:
            
            playsound('vystrel.mp3', block = False)
        else: 
            pass
        
        while True:

            while bullet_coordsY >0:
                
                bullet_coordsX1=int(canvas.coords('bob')[0])
                bullet_coordsX2=int(canvas.coords('bob')[2])
                bullet_coordsY=int(canvas.coords('bob')[3])
                x=0           
                y=-30
                canvas.move('bob', x, y)
                canvas.move(fireball, x, y)
                canvas.update()
            
                if bullet_coordsY<tg1y2+35 and bullet_coordsX1>tg1x1 and bullet_coordsX2<tg1x2:
                    
                    canvas.delete(target1)
                    target1_status+=1
                    #print(target1_status)
                    
                    if target1_status<=1 and premium_state1 == 0 :
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score),state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien1)
                        img3 = PhotoImage(file='explo.png')
                        explosion1= canvas.create_image(tg1x1-25, tg1y1-25, anchor=NW, image=img3,state=alien_state)
                        
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion1)
                        canvas.update()
                        if score < finalne_score:
                            ps1y = randint(rbnv, rbnn)
                            ps1x = randint(rbnb, rbnd)
                            tg1x1=ps1x
                            tg1y1=ps1y
                            tg1x2=tg1x1+30
                            tg1y2=tg1y1+30
                            target1_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target1=canvas.create_rectangle(tg1x1-5,tg1y1-5,tg1x2,tg1y2, state=skst)
                                alien1 = canvas.create_image(tg1x1-2.5,tg1y1-2.5, anchor=NW, image=alienimg, state=alien_state)
                                premium_state1=0
                            else:
                                target1=canvas.create_rectangle(tg1x1-5,tg1y1-5,tg1x2,tg1y2, state=skst)
                                alien1 = canvas.create_image(tg1x1-2.5,tg1y1-2.5, anchor=NW, image=premium_alienimg, state=alien_state)
                                premium_state1 +=1
                        else:
                            zaver()
                                
                    elif target1_status<=1 and premium_state1 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score),state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien1)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion1= canvas.create_image(tg1x1-25, tg1y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion1)
                        canvas.update()
                        if score < finalne_score:
                            ps1y = randint(rbnv, rbnn)
                            ps1x = randint(rbnb, rbnd)
                            tg1x1=ps1x
                            tg1y1=ps1y
                            tg1x2=tg1x1+30
                            tg1y2=tg1y1+30
                            target1_status-=2
                            cas=0
                            
                            target1=canvas.create_rectangle(tg1x1-5,tg1y1-5,tg1x2,tg1y2, state=skst)
                            alien1 = canvas.create_image(tg1x1-2.5,tg1y1-2.5, anchor=NW, image=alienimg, state=alien_state)
                            premium_state1=0
                            canvas.update()
                        else:
                            zaver()

                elif bullet_coordsY<tg2y2+35 and bullet_coordsX1>tg2x1 and bullet_coordsX2<tg2x2:
                    
                    canvas.delete(target2)
                    target2_status+=1
                   
                    if target2_status<=1 and premium_state2 ==0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score),state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien2)
                        img3 = PhotoImage(file='explo.png')
                        explosion2 = canvas.create_image(tg2x1-25, tg2y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion2)
                        canvas.update()
                        if score < finalne_score:
                            ps2y = randint(rbnv, rbnn)
                            ps2x = randint(rbnb, rbnd)
                            tg2x1=ps2x
                            tg2y1=ps2y
                            tg2x2=tg2x1+30
                            tg2y2=tg2y1+30
                            target2_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target2=canvas.create_rectangle(tg2x1-5,tg2y1-5,tg2x2,tg2y2, state=skst)
                                alien2 = canvas.create_image(tg2x1-2.5,tg2y1-2.5, anchor=NW, image=alienimg, state=alien_state)
                                premium_state2=0

                            else:
                                target2=canvas.create_rectangle(tg2x1-5,tg2y1-5,tg2x2,tg2y2, state=skst)
                                alien2 = canvas.create_image(tg2x1-2.5,tg2y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state2 +=1
                        else:
                            zaver()

                    elif target2_status<=1 and premium_state2==1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien2)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion2 = canvas.create_image(tg2x1-25, tg2y1-25, anchor=NW, image=img3)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion2)
                        canvas.update()
                        if score < finalne_score:
                            ps2y = randint(rbnv, rbnn)
                            ps2x = randint(rbnb, rbnd)
                            tg2x1=ps2x
                            tg2y1=ps2y
                            tg2x2=tg2x1+30
                            tg2y2=tg2y1+30
                                
                            cas=0
                                
                            target2=canvas.create_rectangle(tg2x1-5,tg2y1-5,tg2x2,tg2y2, state=skst)
                            alien2 = canvas.create_image(tg2x1-2.5,tg2y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state2=0
                            canvas.update()
                        else:
                            zaver()
                    
                elif bullet_coordsY<tg3y2+35 and bullet_coordsX1>tg3x1 and bullet_coordsX2<tg3x2:
                    canvas.delete(target3)
                    target3_status+=1
                    #print(target3_status)
                    
                    if target3_status<=1 and premium_state3 == 0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien3)
                        img3 = PhotoImage(file='explo.png')
                        explosion3 = canvas.create_image(tg3x1-25, tg3y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion3)
                        canvas.update()
                        if score < finalne_score:

                            ps3y = randint(rbnv, rbnn)
                            ps3x = randint(rbnb, rbnd)
                            tg3x1=ps3x
                            tg3y1=ps3y
                            tg3x2=tg3x1+30
                            tg3y2=tg3y1+30
                            target3_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target3=canvas.create_rectangle(tg3x1-5,tg3y1-5,tg3x2,tg3y2, state=skst)
                                alien3 = canvas.create_image(tg3x1-2.5,tg3y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state3=0
                                    
                            else:
                                target3=canvas.create_rectangle(tg3x1-5,tg3y1-5,tg3x2,tg3y2, state=skst)
                                alien3 = canvas.create_image(tg3x1-2.5,tg3y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state3 +=1
                        else:
                            zaver()

                    elif target3_status<=1 and premium_state3 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20),fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien3)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion3 = canvas.create_image(tg3x1-25, tg3y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion3)
                        canvas.update()
                        if score < finalne_score:

                            ps3y = randint(rbnv, rbnn)
                            ps3x = randint(rbnb, rbnd)
                            tg3x1=ps3x
                            tg3y1=ps3y
                            tg3x2=tg3x1+30
                            tg3y2=tg3y1+30
                            target3_status-=2
                            cas=0
                                
                            target3=canvas.create_rectangle(tg3x1-5,tg3y1-5,tg3x2,tg3y2, state=skst)
                            alien3 = canvas.create_image(tg3x1-2.5,tg3y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state3=0
                            canvas.update()
                        else:
                            zaver()
                                       
                elif bullet_coordsY<tg4y2+35 and bullet_coordsX1>tg4x1 and bullet_coordsX2<tg4x2:
                    canvas.delete(target4)
                    target4_status+=1
                    #print(target4_status)
                    
                    if target4_status<=1 and premium_state4 == 0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien4)
                        img3 = PhotoImage(file='explo.png')
                        explosion4 = canvas.create_image(tg4x1-25, tg4y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion4)
                        canvas.update()
                        if score < finalne_score:

                            ps4y = randint(rbnv, rbnn)
                            ps4x = randint(rbnb, rbnd)
                            tg4x1=ps4x
                            tg4y1=ps4y
                            tg4x2=tg4x1+30
                            tg4y2=tg4y1+30
                            target4_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target4=canvas.create_rectangle(tg4x1-5,tg4y1-5,tg4x2,tg4y2, state=skst)
                                alien4 = canvas.create_image(tg4x1-2.5,tg4y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state4=0
                                    
                            else:
                                target4=canvas.create_rectangle(tg4x1-5,tg4y1-5,tg4x2,tg4y2, state=skst)
                                alien4 = canvas.create_image(tg4x1-2.5,tg4y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state4 +=1
                        else:
                            zaver()

                    elif target4_status<=1 and premium_state4 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien4)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion4 = canvas.create_image(tg4x1-25, tg4y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion4)
                        canvas.update()
                        if score < finalne_score:
                            ps4y = randint(rbnv, rbnn)
                            ps4x = randint(rbnb, rbnd)
                            tg4x1=ps4x
                            tg4y1=ps4y
                            tg4x2=tg4x1+30
                            tg4y2=tg4y1+30
                            target4_status-=2
                            cas=0
                            target4=canvas.create_rectangle(tg4x1-5,tg4y1-5,tg4x2,tg4y2, state=skst)
                            alien4 = canvas.create_image(tg4x1-2.5,tg4y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state4=0
                            canvas.update()
                        else:
                            zaver()
                        
                elif bullet_coordsY<tg5y2+35 and bullet_coordsX1>tg5x1 and bullet_coordsX2<tg5x2:
                    canvas.delete(target5)
                    target5_status+=1
                    
                    if target5_status<=1 and premium_state5 == 0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien5)
                        img3 = PhotoImage(file='explo.png')
                        explosion5 = canvas.create_image(tg5x1-25, tg5y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion5)
                        canvas.update()
                        if score < finalne_score:

                            ps5y = randint(rbnv, rbnn)
                            ps5x = randint(rbnb, rbnd)
                            tg5x1=ps5x
                            tg5y1=ps5y
                            tg5x2=tg5x1+30
                            tg5y2=tg5y1+30                      
                            target5_status-=2
                            cas=0  

                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50:
                                target5=canvas.create_rectangle(tg5x1-5,tg5y1-5,tg5x2,tg5y2, state=skst)
                                alien5 = canvas.create_image(tg5x1-2.5,tg5y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state5=0

                            else:
                                target5=canvas.create_rectangle(tg5x1-5,tg5y1-5,tg5x2,tg5y2, state=skst)
                                alien5 = canvas.create_image(tg5x1-2.5,tg5y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state5 +=1
                        else:
                            zaver()

                    elif target5_status<=1 and premium_state5 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien5)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion5 = canvas.create_image(tg5x1-25, tg5y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion5)
                        canvas.update()
                        if score < finalne_score:

                            ps5y = randint(rbnv, rbnn)
                            ps5x = randint(rbnb, rbnd)
                            tg5x1=ps5x
                            tg5y1=ps5y
                            tg5x2=tg5x1+30
                            tg5y2=tg5y1+30                      
                            target5_status-=2
                            cas=0  
                        
                            target5=canvas.create_rectangle(tg5x1-5,tg5y1-5,tg5x2,tg5y2, state=skst)
                            alien5 = canvas.create_image(tg5x1-2.5,tg5y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state5=0
                            canvas.update()
                        else:
                            zaver()
                                       
                elif bullet_coordsY<tg6y2+35 and bullet_coordsX1>tg6x1 and bullet_coordsX2<tg6x2:
                    canvas.delete(target6)
                    target6_status+=1
                    #print(target6_status)
                    
                    if target6_status<=1 and premium_state6 == 0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien6)
                        img3 = PhotoImage(file='explo.png')
                        explosion6 = canvas.create_image(tg6x1-25, tg6y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion6)
                        canvas.update()
                        if score < finalne_score:

                            ps6y = randint(rbnv, rbnn)
                            ps6x = randint(rbnb, rbnd)
                            tg6x1=ps6x
                            tg6y1=ps6y
                            tg6x2=tg6x1+30
                            tg6y2=tg6y1+30
                            target6_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target6=canvas.create_rectangle(tg6x1-5,tg6y1-5,tg6x2,tg6y2, state=skst)
                                alien6 = canvas.create_image(tg6x1-2.5,tg6y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state6=0

                            else:
                                target6=canvas.create_rectangle(tg6x1-5,tg6y1-5,tg6x2,tg6y2, state=skst)
                                alien6 = canvas.create_image(tg6x1-2.5,tg6y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state6 +=1
                        else:
                            zaver()

                    elif target6_status<=1 and premium_state6 == 1:   
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien6)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion6 = canvas.create_image(tg6x1-25, tg6y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion6)
                        canvas.update()
                        if score < finalne_score:

                            ps6y = randint(rbnv, rbnn)
                            ps6x = randint(rbnb, rbnd)
                            tg6x1=ps6x
                            tg6y1=ps6y
                            tg6x2=tg6x1+30
                            tg6y2=tg6y1+30
                            target6_status-=2
                            cas=0
                            
                            target6=canvas.create_rectangle(tg6x1-5,tg6y1-5,tg6x2,tg6y2, state=skst)
                            alien6 = canvas.create_image(tg6x1-2.5,tg6y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state6=0
                            canvas.update()

                        else:
                            zaver()
                                       
                elif bullet_coordsY<tg7y2+35 and bullet_coordsX1>tg7x1 and bullet_coordsX2<tg7x2:
                    canvas.delete(target7)
                    target7_status+=1
                    #print(target7_status)
                    
                    if target7_status<=1 and premium_state7 == 0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien7)
                        img3 = PhotoImage(file='explo.png')
                        explosion7 = canvas.create_image(tg7x1-25, tg7y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion7)
                        canvas.update()
                        if score < finalne_score:

                            ps7y = randint(rbnv, rbnn)
                            ps7x = randint(rbnb, rbnd)
                            tg7x1=ps7x
                            tg7y1=ps7y
                            tg7x2=tg7x1+30
                            tg7y2=tg7y1+30                       
                            target7_status-=2
                            cas=0

                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target7=canvas.create_rectangle(tg7x1-5,tg7y1-5,tg7x2,tg7y2, state=skst)
                                alien7 = canvas.create_image(tg7x1-2.5,tg7y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state7=0

                            else:
                                target7=canvas.create_rectangle(tg7x1-5,tg7y1-5,tg7x2,tg7y2, state=skst)
                                alien7 = canvas.create_image(tg7x1-2.5,tg7y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state7 +=1
                        else:
                            zaver()

                    elif target7_status<=1 and premium_state7 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien7)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion7 = canvas.create_image(tg7x1-25, tg7y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion7)
                        canvas.update()
                        if score < finalne_score:

                            ps7y = randint(rbnv, rbnn)
                            ps7x = randint(rbnb, rbnd)
                            tg7x1=ps7x
                            tg7y1=ps7y
                            tg7x2=tg7x1+30
                            tg7y2=tg7y1+30                       
                            target7_status-=2
                            cas=0
                            target7=canvas.create_rectangle(tg7x1-5,tg7y1-5,tg7x2,tg7y2, state=skst)
                            alien7 = canvas.create_image(tg7x1-2.5,tg7y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state7=0
                            canvas.update()
                        else:
                            zaver()
                                                          
                elif bullet_coordsY<tg8y2+35 and bullet_coordsX1>tg8x1 and bullet_coordsX2<tg8x2:
                    canvas.delete(target8)
                    target8_status+=1
                    #print(target8_status)
                    
                    if target8_status<=1 and premium_state8 == 0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien8)
                        img3 = PhotoImage(file='explo.png')
                        explosion8 = canvas.create_image(tg8x1-25, tg8y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion8)
                        canvas.update()
                        if score < finalne_score:
                            ps8y = randint(rbnv, rbnn)
                            ps8x = randint(rbnb, rbnd)
                            tg8x1=ps8x
                            tg8y1=ps8y
                            tg8x2=tg8x1+30
                            tg8y2=tg8y1+30
                            target8_status-=2                   
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target8=canvas.create_rectangle(tg8x1-5,tg8y1-5,tg8x2,tg8y2, state=skst)
                                alien8 = canvas.create_image(tg8x1-2.5,tg8y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state8=0

                            else:
                                target8=canvas.create_rectangle(tg8x1-5,tg8y1-5,tg8x2,tg8y2, state=skst)
                                alien8 = canvas.create_image(tg8x1-2.5,tg8y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state8 +=1
                        else:
                            zaver()
                    
                    elif target8_status<=1 and premium_state8 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien8)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion8 = canvas.create_image(tg8x1-25, tg8y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion8)
                        canvas.update()
                        if score < finalne_score:

                            ps8y = randint(rbnv, rbnn)
                            ps8x = randint(rbnb, rbnd)
                            tg8x1=ps8x
                            tg8y1=ps8y
                            tg8x2=tg8x1+30
                            tg8y2=tg8y1+30
                            
                            target8_status-=2                       
                            cas=0
                            
                            target8=canvas.create_rectangle(tg8x1-5,tg8y1-5,tg8x2,tg8y2, state=skst)
                            alien8 = canvas.create_image(tg8x1-2.5,tg8y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state8=0
                            canvas.update()
                        else:
                            zaver()

                                           
                elif bullet_coordsY<tg9y2+35 and bullet_coordsX1>tg9x1 and bullet_coordsX2<tg9x2:
                    canvas.delete(target9)
                    target9_status+=1
                    #print(target8_status)
                    
                    if target9_status<=1 and premium_state9==0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien9)
                        img3 = PhotoImage(file='explo.png')
                        explosion9 = canvas.create_image(tg9x1-25, tg9y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion9)
                        canvas.update()
                        if score < finalne_score:

                            ps9y = randint(rbnv, rbnn)
                            ps9x = randint(rbnb, rbnd)
                            tg9x1=ps9x
                            tg9y1=ps9y
                            tg9x2=tg9x1+30
                            tg9y2=tg9y1+30
                            
                            target9_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target9=canvas.create_rectangle(tg9x1-5,tg9y1-5,tg9x2,tg9y2, state=skst)
                                alien9 = canvas.create_image(tg9x1-2.5,tg9y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state9=0

                            else:
                                target9=canvas.create_rectangle(tg9x1-5,tg9y1-5,tg9x2,tg9y2, state=skst)
                                alien9 = canvas.create_image(tg9x1-2.5,tg9y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state9 +=1
                        else:
                            zaver()
                        
                    elif target9_status<=1 and premium_state9==1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien9)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion9 = canvas.create_image(tg9x1-25, tg9y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion9)
                        canvas.update()
                        if score < finalne_score:

                            ps9y = randint(rbnv, rbnn)
                            ps9x = randint(rbnb, rbnd)
                            tg9x1=ps9x
                            tg9y1=ps9y
                            tg9x2=tg9x1+30
                            tg9y2=tg9y1+30
                            
                            target9_status-=2
                            cas=0
                            
                            target9=canvas.create_rectangle(tg9x1-5,tg9y1-5,tg9x2,tg9y2, state=skst)
                            alien9 = canvas.create_image(tg9x1-2.5,tg9y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state9=0
                            canvas.update()
                        else:
                            zaver()
                                                                  
                elif bullet_coordsY<tg10y2+35 and bullet_coordsX1>tg10x1 and bullet_coordsX2<tg10x2:
                    canvas.delete(target10)
                    target10_status+=1
                    #print(target8_status)
                
                    if target10_status<=1 and premium_state10==0:
                        playsound('trefa_do_cierneho.mp3', block = False)
                        score+=1
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien10)
                        img3 = PhotoImage(file='explo.png')
                        explosion10 = canvas.create_image(tg10x1-25, tg10y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion10)
                        canvas.update()
                        if score < finalne_score:

                            ps10y = randint(rbnv, rbnn)
                            ps10x = randint(rbnb, rbnd)
                            tg10x1=ps10x
                            tg10y1=ps10y
                            tg10x2=tg10x1+30
                            tg10y2=tg10y1+30
                            target10_status-=2
                            cas=0
                            if score != 10 and score != 20 and score != 30 and score != 40 and score !=50 and score != 60 and score != 70 and score != 80 and score !=90:
                                target10=canvas.create_rectangle(tg10x1-5,tg10y1-5,tg10x2,tg10y2, state=skst)
                                alien10 = canvas.create_image(tg10x1-2.5,tg10y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                                premium_state10=0

                            else:
                                target10=canvas.create_rectangle(tg10x1-5,tg10y1-5,tg10x2,tg10y2, state=skst)
                                alien10 = canvas.create_image(tg10x1-2.5,tg10y1-2.5, anchor=NW, image=premium_alienimg,state=alien_state)
                                premium_state10 +=1
                        else:
                            zaver()

                    elif target10_status<=1 and premium_state10 == 1:
                        playsound('premiumH.wav', block = False)
                        score+=5
                        canvas.delete(skore)
                        skore=canvas.create_text(poloha_skoreX,poloha_skoreY,font=('Arial Rounded MT Bold',20), fill='lime', text='skóre: {}'.format(score), state=alien_state)
                        canvas.delete('bob')
                        canvas.delete(fireball)
                        canvas.delete(alien10)
                        img3 = PhotoImage(file='premium_explo3.png')
                        explosion10 = canvas.create_image(tg10x1-25, tg10y1-25, anchor=NW, image=img3,state=alien_state)
                        canvas.update()
                        #sleep(0.05)
                        canvas.delete(explosion10)
                        canvas.update()
                        if score < finalne_score:

                            ps10y = randint(rbnv, rbnn)
                            ps10x = randint(rbnb, rbnd)
                            tg10x1=ps10x
                            tg10y1=ps10y
                            tg10x2=tg10x1+30
                            tg10y2=tg10y1+30
                            
                            target10_status-=2
                            cas=0
                            
                            target10=canvas.create_rectangle(tg10x1-5,tg10y1-5,tg10x2,tg10y2, state=skst)
                            alien10 = canvas.create_image(tg10x1-2.5,tg10y1-2.5, anchor=NW, image=alienimg,state=alien_state)
                            premium_state10=0
                            canvas.update()
                        else:
                            zaver()
                        
            canvas.delete('bob')
            canvas.delete(fireball)
            canvas.update()
            cas=0


    else:
        pass
            


def menu():
    global nadpis, nadpis2, sebachvala, prva_moznost, druha_moznost, tretia_moznost, pointer, finalne_score, ind_pointers, choose_state, pointer, what_army_do_you_dare, prva_moznost_cislo, druha_moznost_cislo, tretia_moznost_cislo, ready_text
    global ind_pocitanie_casu
    choose_state = 'normal'
    
    
    nadpis = canvas.create_text(285, 250, font=('Arial Rounded MT Bold', 70), text='SPACE')
    nadpis2 = canvas.create_text(630, 250, font=('Arial Rounded MT Bold', 70), text='INTRUDERS', fill='lime')
    sebachvala = canvas.create_text(500, 680, font=('Arial Rounded MT Bold', 10), text='developed by Andreas')
    what_army_do_you_dare = canvas.create_text(500, 400,font=('Arial Rounded MT Bold', 20), text='Choose the number of intruders you dare!', state=choose_state)

    prva_moznost = canvas.create_text(350, 440,font=('Arial Rounded MT Bold', 15), text='20 bad guys', fill='white', state=choose_state)
    druha_moznost = canvas.create_text(500, 440,font=('Arial Rounded MT Bold', 15), text='50 gatecrashers', fill='white', state=choose_state)
    tretia_moznost = canvas.create_text(650, 440,font=('Arial Rounded MT Bold', 15), text='70 interlopers', fill='white', state=choose_state)
    
    prva_moznost_cislo = canvas.create_text(350, 465,font=('Arial Rounded MT Bold', 15), text='[1]', fill='white', state=choose_state)
    druha_moznost_cislo = canvas.create_text(500, 465,font=('Arial Rounded MT Bold', 15), text='[2]', fill='white', state=choose_state)
    tretia_moznost_cislo = canvas.create_text(650, 465,font=('Arial Rounded MT Bold', 15), text='[3]', fill='white', state=choose_state)
    
    pointer = canvas.create_polygon(480,520,500, 490, 520, 520, fill='red', state=choose_state)

    ready_text = canvas.create_text(500, 600, font=('Arial Rounded MT Bold', 35), text='Ready? Press Space')
    
    ind_pocitanie_casu = 0
    finalne_score = 50
    ind_pointers = 1

    canvas.update()

def prva(event):
    global pointer, finalne_score, ind_pointers, choose_state
    if ind_pointers ==1:
        canvas.delete(pointer)
        pointer = canvas.create_polygon(330,520,350, 490, 370, 520, fill='red', state=choose_state)
        playsound('choose.wav', block = False)
        finalne_score = 20

def druha(event):
    global pointer, finalne_score, choose_state
    if ind_pointers ==1:
        canvas.delete(pointer)
        pointer = canvas.create_polygon(480,520,500, 490, 520, 520, fill='red', state=choose_state)
        playsound('choose.wav', block = False)
        finalne_score = 50

def tretia(event):
    global pointer, finalne_score, choose_state
    if ind_pointers==1:
        canvas.delete(pointer)
        pointer = canvas.create_polygon(630,520,650, 490, 670, 520, fill='red', state=choose_state)
        playsound('choose.wav', block = False)
        finalne_score = 70

def choose(): 
    canvas.bind_all('<KeyPress-1>', prva)
    canvas.bind_all('<KeyPress-2>', druha)
    canvas.bind_all('<KeyPress-3>', tretia)
    
cass=0

ind_pocitanie_casu = 0
pocitanie_casu=0

def space(event):
    global nadpis, nadpis2, time_do_konca, time_do_konca2, cass, sebachvala, alien_state, spaceship_state
    global premium_state1, premium_state2, premium_state3, premium_state4, premium_state5, premium_state6, premium_state7, premium_state8, premium_state9, premium_state10
    global target1_status, target2_status, target3_status, target4_status, target5_status, target6_status, target7_status, target8_status, target9_status, target10_status
    global zaver_nadpis_na_novu_hru, zaver_skore, skore, cas, ind_pointers, choose_state
    global what_army_do_you_dare, prva_moznost, druha_moznost, tretia_moznost, pointer, prva_moznost_cislo, druha_moznost_cislo, tretia_moznost_cislo, ready_text
    global score, sound_ind
    
    sound_ind=1

    choose_state = 'hidden'
    t.start()
    
    ind_pointers = 0

    canvas.delete(nadpis)
    canvas.delete(sebachvala)
    canvas.delete(nadpis2)
    canvas.delete(what_army_do_you_dare)
    canvas.delete(prva_moznost)
    canvas.delete(druha_moznost)
    canvas.delete(tretia_moznost)
    canvas.delete(pointer)
    canvas.delete(prva_moznost_cislo)
    canvas.delete(druha_moznost_cislo)
    canvas.delete(tretia_moznost_cislo)
    canvas.delete(ready_text)

    playsound('space.wav', block = False)

    úvodný_nákres()
     
    cas=0
    cass+=1
    score=0
    
    klik()

    target1_status=0
    target2_status=0
    target3_status=0
    target4_status=0
    target5_status=0
    target6_status=0
    target7_status=0
    target8_status=0
    target9_status=0
    target10_status=0

    premium_state1=0
    premium_state2=0
    premium_state3=0
    premium_state4=0
    premium_state5=0
    premium_state6=0
    premium_state7=0
    premium_state8=0
    premium_state9=0
    premium_state10=0

    canvas.delete(zaver_nadpis_na_novu_hru)
    canvas.delete(zaver_skore)
    alien_state='normal'
    spaceship_state='normal'
    canvas.update()

canvas.bind_all('<KeyPress-space>', space)

def zaver():
    global premium_state1, premium_state2, premium_state3, premium_state4, premium_state5, premium_state6, premium_state7, premium_state8, premium_state9, premium_state10
    global target1_status, target2_status, target3_status, target4_status, target5_status, target6_status, target7_status, target8_status, target9_status, target10_status
    global skore, alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10, spaceship_state, alien_state, cas, cass
    global zaver_nadpis_na_novu_hru, zaver_skore, ind_pointers, choose_state
    global what_army_do_you_dare, prva_moznost, druha_moznost, tretia_moznost, pointer, prva_moznost_cislo, druha_moznost_cislo, tretia_moznost_cislo, ready_text, sebachvala
    global ind_pocitanie_casu
    global pocitanie_casu, sound_ind
    global t, elapsed_time
    choose_state = 'normal'
    
    cas=0
    
    value = t.stop()
    print(value)
    
    sound_ind = 0

    canvas.delete(skore)
    canvas.delete(alien1)
    canvas.delete(alien2)
    canvas.delete(alien3)
    canvas.delete(alien4) 
    canvas.delete(alien5) 
    canvas.delete(alien6)
    canvas.delete(alien7)
    canvas.delete(alien8)
    canvas.delete(alien9)
    canvas.delete(alien10)
    canvas.delete(sniperX)
    canvas.delete(sniperY)
    canvas.delete(spaceship_img)
    canvas.update()

    ind_pointers = 1

    target1_status+=10
    target2_status+=10
    target3_status+=10
    target4_status+=10
    target5_status+=10
    target6_status+=10
    target7_status+=10
    target8_status+=10
    target9_status+=10
    target10_status+=10

    premium_state1+=10
    premium_state2+=10
    premium_state3+=10
    premium_state4+=10
    premium_state5+=10
    premium_state6+=10
    premium_state7+=10
    premium_state8+=10
    premium_state9+=10
    premium_state10+=10

    playsound('end.wav', block = False)

    alien_state='hidden'
    spaceship_state='hidden'
    canvas.update()
    #zaver_nadpis_na_novu_hru_stvorec = canvas.create_rectangle(300,200,700,300)
    zaver_nadpis_na_novu_hru = canvas.create_text(500, 170, font=('Arial Rounded MT Bold', 80), text='Game Over')
    
    zaver_skore = canvas.create_text(500, 330, font=('Arial Rounded MT Bold', 30), text="You've killed {} intruders in {} seconds".format(score, round(value, 2)))
    
    #sebachvala = canvas.create_text(500, 680, font=('Arial Rounded MT Bold', 10), text='developed by Andreas')

    what_army_do_you_dare = canvas.create_text(500, 400,font=('Arial Rounded MT Bold', 20), text='Choose the number of intruders you dare!', state=choose_state)
    prva_moznost = canvas.create_text(350, 440,font=('Arial Rounded MT Bold', 15), text='20 bad guys', fill='white', state=choose_state)
    druha_moznost = canvas.create_text(500, 440,font=('Arial Rounded MT Bold', 15), text='50 gatecrashers', fill='white', state=choose_state)
    tretia_moznost = canvas.create_text(650, 440,font=('Arial Rounded MT Bold', 15), text='70 interlopers', fill='white', state=choose_state)
    
    prva_moznost_cislo = canvas.create_text(350, 465,font=('Arial Rounded MT Bold', 15), text='[1]', fill='white', state=choose_state)
    druha_moznost_cislo = canvas.create_text(500, 465,font=('Arial Rounded MT Bold', 15), text='[2]', fill='white', state=choose_state)
    tretia_moznost_cislo = canvas.create_text(650, 465,font=('Arial Rounded MT Bold', 15), text='[3]', fill='white', state=choose_state)
    
    
    ready_text = canvas.create_text(500, 600, font=('Arial Rounded MT Bold', 35), text='Ready? Press Space')

    pointer = canvas.create_polygon(480,520,500, 490, 520, 520, fill='red', state=choose_state)
    finalne_score = 50
    ind_pointers = 1


def klik():
    canvas.bind_all('<ButtonPress-1>', mys_press)
    canvas.bind('<Motion>', motion)
    canvas.bind_all('<ButtonRelease-1>', mys_release)
    canvas.bind_all('<KeyPress-space>', space)

menu()
ind_pointers=1
choose()


canvas.mainloop()
