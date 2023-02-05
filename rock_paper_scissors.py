import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk,Image
import os.path
import random
import time
from tkinter import messagebox

class Page1():

    computer_score=0
    user_score=0
    second=0
    minute=1
    total_clicks=0
    
    def get_winner(self,button_no):
       
        Page1.total_clicks+=1

        self.user_choice_display=tk.Label(self.page1)
        self.user_choice_display.place(relx=0.22,rely=0.45,relwidth=0.08,relheight=0.11)

        self.computer_choice_display=tk.Label(self.page1)
        self.computer_choice_display.place(relx=0.68,rely=0.45,relwidth=0.08,relheight=0.11)        
        
        if(button_no=="1"):
            self.user_choice="Rock"
            self.user_choice_display.configure(image=self.base_rock1)
        elif(button_no=="2"):
            self.user_choice="Paper"
            self.user_choice_display.configure(image=self.base_paper1)
        else:
            self.user_choice="Scissor"
            self.user_choice_display.configure(image=self.base_scissors1)

        options=["Rock","Paper","Scissor"]
        self.computer_choice=random.choice(options)
        if(self.computer_choice=="Rock"):
            self.computer_choice_display.configure(image=self.base_rock1)
        elif(self.computer_choice=="Paper"):
            self.computer_choice_display.configure(image=self.base_paper1)
        else:
            self.computer_choice_display.configure(image=self.base_scissors1)

        if(self.user_choice==self.computer_choice):

            self.user_score_label.configure(text=f"{Page1.user_score}")
            self.computer_score_label.configure(text=f"{Page1.computer_score}")

        elif(button_no=="1"):
            if(self.computer_choice=="Paper"):
                Page1.computer_score+=1
                self.computer_score_label.configure(text=f"{Page1.computer_score}")    
            else:
                Page1.user_score+=1
                self.user_score_label.configure(text=f"{Page1.user_score}")
        elif(button_no=="2"):
            if(self.computer_choice=="Scissor"):
                Page1.computer_score+=1
                self.computer_score_label.configure(text=f"{Page1.computer_score}")    
            else:
                Page1.user_score+=1
                self.user_score_label.configure(text=f"{Page1.user_score}")
        else:
            if(self.computer_choice=="Rock"):
                Page1.computer_score+=1
                self.computer_score_label.configure(text=f"{Page1.computer_score}")    
            else:
                Page1.user_score+=1
                self.user_score_label.configure(text=f"{Page1.user_score}")
    
    def update(self):
        if(self.minute<0):
            Page1.minute=0
            Page1.second=59
            self.winner_label=tk.Label(self.page1,bg="#eb144c",font=("Segoe UI Black",14,"bold"))
            self.winner_label.place(relx=0.42,rely=0.6,relwidth=0.16,relheight=0.06)
            if(Page1.total_clicks>=15):
                if(self.computer_score>self.user_score):
                    self.winner_label.configure(text="You Lose!")
                elif(self.user_score>self.computer_score):
                    self.winner_label.configure(text="You Win!")
                else:
                    self.winner_label.configure(text="It\'s Tie!")           
            else:
                self.winner_label.configure(text="Computer Won")
            self.page1.after(2000,self.page1.destroy)

        if(self.second==0):
            Page1.second=59
            Page1.minute-=1
        else:
            Page1.second-=1

        self.timer_label.configure(text=f"{Page1.minute} : {Page1.second}")
        self.timer_label.after(1000,self.update)

    def end(self):
        Page1.second=59
        Page1.minute=0
        self.page1.destroy()

    def __init__(self):
        self.page1=tk.Toplevel()
        
        self.page1.geometry("900x695")
        self.page1.title("Rock Paper Scissor")
        self.page1.resizable(False,False)
        self.page1.configure(bg="#9900ef")


        self.label_frame=tk.Frame(self.page1)
        self.label_frame.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=0.1)
        self.label_frame.configure(background="#eb144c")

        self.label_top=tk.Label(self.label_frame,text="Rock Paper Scissor",font=("Segoe UI Black",20,"bold"),bg="#eb144c")
        self.label_top.place(relx=0.20,rely=0.2,relwidth=0.6,relheight=0.6)

        self.score_label=tk.Label(self.page1,text="Score",font=("Segoe UI Black",17,"bold"),bg="#eb144c")
        self.score_label.place(relx=0.43,rely=0.25,relwidth=0.15,relheight=0.06)

        self.timer_label=tk.Label(self.page1,font=("Segoe UI Black",15,"bold"),bg="#eb144c")
        self.timer_label.place(relx=0.43,rely=0.15,relwidth=0.15,relheight=0.06)

        self.update()

        self.user_score_label=tk.Label(self.page1,font=("Segoe UI Black",15,"bold"),bg="#eb144c")
        self.user_score_label.place(relx=0.43,rely=0.32,relwidth=0.07,relheight=0.05)

        self.computer_score_label=tk.Label(self.page1,font=("Segoe UI Black",15,"bold"),bg="#eb144c")
        self.computer_score_label.place(relx=0.51,rely=0.32,relwidth=0.07,relheight=0.05)

        self.base_rock=ImageTk.PhotoImage(Image.open(r"rock2.jpg"))
        self.base_rock1=ImageTk.PhotoImage(Image.open(r"rock3.jpg"))

        self.rock_button=tk.Button(self.page1,image=self.base_rock,command=lambda button_no="1":self.get_winner(button_no))
        self.rock_button.place(relx=0.05,rely=0.30,relheight=0.09,relwidth=0.07)

        self.base_paper=ImageTk.PhotoImage(Image.open(r"paper2.jpg"))
        self.base_paper1=ImageTk.PhotoImage(Image.open(r"paper3.jpg"))

        self.paper_button=tk.Button(self.page1,image=self.base_paper,command=lambda button_no="2":self.get_winner(button_no))
        self.paper_button.place(relx=0.05,rely=0.45,relheight=0.09,relwidth=0.07)

        self.base_scissors=ImageTk.PhotoImage(Image.open(r"scissors2.jpg"))
        self.base_scissors1=ImageTk.PhotoImage(Image.open(r"scissors3.jpg"))

        self.scissors_button=tk.Button(self.page1,image=self.base_scissors,command=lambda button_no="3":self.get_winner(button_no))
        self.scissors_button.place(relx=0.05,rely=0.60,relheight=0.09,relwidth=0.07)

        self.user_choice_label=tk.Label(self.page1,text="You:",font=("Segoe UI Black",14,"bold"),bg="#eb144c")
        self.user_choice_label.place(relx=0.05,rely=0.15,relwidth=0.10,relheight=0.06)

        self.computer_choice_label=tk.Label(self.page1,text="Computer:",font=("Segoe UI Black",14,"bold"),bg="#eb144c")
        self.computer_choice_label.place(relx=0.85,rely=0.15,relwidth=0.12,relheight=0.06)

        self.rock_computer=tk.Label(self.page1,image=self.base_rock)
        self.rock_computer.place(relx=0.85,rely=0.30,relwidth=0.07,relheight=0.09)

        self.paper_computer=tk.Label(self.page1,image=self.base_paper)
        self.paper_computer.place(relx=0.85,rely=0.45,relwidth=0.07,relheight=0.09)

        self.scissor_computer=tk.Label(self.page1,image=self.base_scissors)
        self.scissor_computer.place(relx=0.85,rely=0.60,relwidth=0.07,relheight=0.09)

        self.button=tk.Button(self.page1,text="Home",font=("Segoe UI Black",14,"bold"),bg="#eb144c",command=self.end)
        self.button.place(relx=0.45,rely=0.85,relwidth=0.10,relheight=0.05)

class StartWindow():
    def __init__(self,master):
        self.master=master

        self.master.geometry("900x600")
        self.master.title("Rock Paper Scissor")
        self.master.resizable(False,False)
        self.master.configure(bg="#9900ef")
        
        self.image_background=ImageTk.PhotoImage(Image.open(r"home_rock_paper_scissors.jpg"))
        
        self.label=tk.Label(self.master,image=self.image_background)
        self.label.place(relx=0.30,rely=0.2,relheight=0.4,relwidth=0.4)

        self.start=tk.Button(self.master,text="Start",font=("Segoe UI Black",14,"bold"),bg="#eb144c",command=self.open_window)
        self.start.place(relx=0.47,rely=0.65,relheight=0.05,relwidth=0.10)

    def open_window(self):
        self.obj=Page1()
        self.obj.page1.mainloop()

root=tk.Tk()
app=StartWindow(root)
root.mainloop()