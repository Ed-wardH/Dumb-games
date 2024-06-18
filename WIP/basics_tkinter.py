import tkinter as tk
# --- MUST CODE ON TKINTER
# Instance window -> window =Tk()
# Set a refreshing loop -> window.mainloop()
# Print widgets added to the window -> widget.pack

#-------------------------
# - Generate blanck window
# Uses basic constructor
window = tk.Tk()
window.title("Basics")
#window.geometry("300x300")  

# - Add widgets to the window
# A widget is created from the window and some Arguments
# All widgets have a width and height atributes
text_label = tk.Label(text="NEW GAME")
#text_label.grid(row=2,column=0)

def color():
    #ref = str(x)+str(y)
    btn=window.nametowidget("00")
    btn["bg"]="black"
#--- PRUEBAS ---------
imgclear=tk.PhotoImage(width=50,height=50)
for x in range(3):
    for y in range(3):
        frame = tk.Frame(master=window,borderwidth=2)
        frame.grid(row=x,column=y)
    
        btn = tk.Button(master=frame,image=imgclear,name=str(x)+str(y),width=100,height=100,background="white",command=color)
        btn.pack()


instrucciones = tk.Label(master=window,text="Game START",name="instruccion",)
instrucciones.grid(row=3,column=1)




window.mainloop()