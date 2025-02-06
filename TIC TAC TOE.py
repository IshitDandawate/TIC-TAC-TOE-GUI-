import tkinter as tk
import messagebox as m

win=tk.Tk()
win.title("X AND O")

turn=True
count=0
winner=False


def restart():
    global lst,count,turn,winner
    winner=False
    count=0
    turn=True
    lst=[[0,0,0],
     [0,0,0],
     [0,0,0]]

    b1["text"]=""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""

    b1["state"] = "normal"
    b2["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "normal"
    b6["state"] = "normal"
    b7["state"] = "normal"
    b8["state"] = "normal"
    b9["state"] = "normal"

    b1.config(bg="#f0f0f0")
    b2.config(bg="#f0f0f0")
    b3.config(bg="#f0f0f0")
    b4.config(bg="#f0f0f0")
    b5.config(bg="#f0f0f0")
    b6.config(bg="#f0f0f0")
    b7.config(bg="#f0f0f0")
    b8.config(bg="#f0f0f0")
    b9.config(bg="#f0f0f0")


def disable():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    b5["state"] = "disabled"
    b6["state"] = "disabled"
    b7["state"] = "disabled"
    b8["state"] = "disabled"
    b9["state"] = "disabled"

def play(b):
    global turn,count
    if b["text"]=="" and turn==True:
        b["text"]="X"
        turn=False
        count+=1
        lst[b.grid_info()['row']][b.grid_info()['column']]=1

    elif b["text"]=="" and turn==False:
        b["text"]="0"
        turn=True
        count+=1
        lst[b.grid_info()['row']][b.grid_info()['column']] = 2

    else:
        m.showerror("X AND 0","CHOOSE ANOTHER BOX...")

    if count>=5:
        wincheck()

def wincheck():
    global winner,count
    if [1,1,1] in lst:
        if lst.index([1,1,1])==0:
            b1.config(bg="blue")
            b2.config(bg="blue")
            b3.config(bg="blue")
            disable()
            winner=True
        elif lst.index([1,1,1])==1:
            b4.config(bg="blue")
            b5.config(bg="blue")
            b6.config(bg="blue")
            disable()
            winner = True
        else:
            b7.config(bg="blue")
            b8.config(bg="blue")
            b9.config(bg="blue")
            disable()
            winner = True

    elif [2,2,2] in lst:
        if lst.index([2,2,2])==0:
            b1.config(bg="blue")
            b2.config(bg="blue")
            b3.config(bg="blue")
            disable()
            winner = True

        elif lst.index([2,2,2])==1:
            b4.config(bg="blue")
            b5.config(bg="blue")
            b6.config(bg="blue")
            disable()
            winner = True

        else:
            b7.config(bg="blue")
            b8.config(bg="blue")
            b9.config(bg="blue")
            disable()
            winner = True

    elif lst[0][0]==lst[1][0]==lst[2][0]!=0:
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        disable()
        winner = True

    elif lst[0][1]==lst[1][1]==lst[2][1]:
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        disable()
        winner = True

    elif lst[0][2]==lst[1][2]==lst[2][2]!=0:
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        disable()
        winner = True

    elif lst[0][0]==lst[1][1]==lst[2][2]:
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        disable()
        winner = True

    elif lst[0][2]==lst[1][1]==lst[2][0]:
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        disable()
        winner = True

    if count==9 and winner==False:
        m.showinfo("X AND 0","TIE NO ONE WINS")


#BOARD
lst=[[0,0,0],
     [0,0,0],
     [0,0,0]]
#BUTTONS AND GRIDS
res=tk.Button(text="Restart",height=2,width=6,bg="red",command=restart)
b1=tk.Button(text="",height=3,width=6,command=lambda: play(b1))
b2=tk.Button(text="",height=3,width=6,command=lambda: play(b2))
b3=tk.Button(text="",height=3,width=6,command=lambda: play(b3))
b4=tk.Button(text="",height=3,width=6,command=lambda: play(b4))
b5=tk.Button(text="",height=3,width=6,command=lambda: play(b5))
b6=tk.Button(text="",height=3,width=6,command=lambda: play(b6))
b7=tk.Button(text="",height=3,width=6,command=lambda: play(b7))
b8=tk.Button(text="",height=3,width=6,command=lambda: play(b8))
b9=tk.Button(text="",height=3,width=6,command=lambda: play(b9))

res.grid(row=3,column=1)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

win.mainloop()
