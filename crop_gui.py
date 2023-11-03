from tkinter import *
import pickle
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image

root = Tk()
root.geometry('1000x700')
root.title("Crop Prediction")

# Background Image
bg = ImageTk.PhotoImage(file='farm.jpg')
bg_label = Label(image=bg).place(x=0,y=0,relwidth=1,relheight=1)

def get_data():
    l ={20: 'rice',11: 'maize',3: 'chickpea',9: 'kidneybeans',18: 'pigeonpeas',
        13: 'mothbeans',14: 'mungbean',2: 'blackgram',10: 'lentil',19: 'pomegranate',
        1: 'banana',12: 'mango',7: 'grapes',21: 'watermelon',15: 'muskmelon',0: 'apple',
        16: 'orange',17: 'papaya',4: 'coconut',6: 'cotton',8: 'jute',5: 'coffee'
        }
    with open('D:\P\What-Crop-To-Grow-master\croppred.sav','rb') as f:
        mp = pickle.load(f) 
        result = l[mp.predict([[int(n_val.get()),
                                int(p_val.get()),
                                int(k_val.get()),
                                float(t_val.get()),
                                float(h_val.get()),
                                float(ph_val.get()),
                                float(r_val.get())
                                ]])[0]]
        tmsg.showinfo(title='Prediction Result',message=f"Your Plant  is {result}.")


f1 = Frame(root, bg='snow')
f1.place(x=70, y=50, height=540, width=800)
main_labl = Label(f1,text="Crop Prediction Using Support Vector Machine",font="comicsansms 20 bold",bg='lightblue',fg='red')
n = Label(f1,text="Nitrogen",font="comicsansms 15 bold")
p = Label(f1,text="Phosphorus",font="comicsansms 15 bold")
k = Label(f1,text="Potassium",font="comicsansms 15 bold")
temp = Label(f1,text="Temperature",font="comicsansms 15 bold")
humidity = Label(f1,text="Humidity",font="comicsansms 15 bold")
ph = Label(f1,text="PH",font="comicsansms 15 bold")
rainfall = Label(f1,text="Rainfall",font="comicsansms 15 bold")

main_labl.place(x=70,y=20)
p.place(x=70,y=100)
n.place(x=70,y=150)
k.place(x=70,y=190)
temp.place(x=70,y=250)
humidity.place(x=70,y=300)
ph.place(x=70,y=350)
rainfall.place(x=70,y=400)


n_val = StringVar()
p_val = StringVar()
k_val = StringVar()
t_val = StringVar()
h_val = StringVar()
ph_val = StringVar()
r_val = StringVar()

n_entry = Entry(root,textvariable=n_val,font = "Helvetica 18 bold",bg="lightyellow")
p_entry = Entry(root,textvariable=p_val,font = "Helvetica 18 bold",bg="lightyellow")
k_entry = Entry(root,textvariable=k_val,font = "Helvetica 18 bold",bg="lightyellow")
t_entry = Entry(root,textvariable=t_val,font = "Helvetica 18 bold",bg="lightyellow")
h_entry = Entry(root,textvariable=h_val,font = "Helvetica 18 bold",bg="lightyellow")
ph_entry = Entry(root,textvariable=ph_val,font = "Helvetica 18 bold",bg="lightyellow")
r_entry = Entry(root,textvariable=r_val,font = "Helvetica 18 bold",bg="lightyellow")

n_entry.place(x=330,y=150)
p_entry.place(x=330,y=200)
k_entry.place(x=330,y=250)
t_entry.place(x=330,y=300)
h_entry.place(x=330,y=350)
ph_entry.place(x=330,y=400)
r_entry.place(x=330,y=450)

Button(text="Submit", width=10, height=2,fg='black',command=get_data).place(x=450,y=500)
root.mainloop()