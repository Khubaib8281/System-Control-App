from tkinter import*
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restart_time():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown -l")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
st = Tk()
st.title("ShutDown")
st.geometry("500x500")
st.config(bg="Black")

r_button = Button(st,text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=155,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time(20s)",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=210)

lg_button = Button(st,text="Logout",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

s_button = Button(st,text="Shutdown",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
s_button.place(x=150,y=370,height=50,width=200)


#Run the program
st.mainloop()