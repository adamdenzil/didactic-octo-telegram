from tkinter import *
import random
root=Tk()
root.title("password generator")
root.geometry("324x424")

label_1=Label(root)

array_3d=[[[2,4,2,4,3,2,1,3,4],["Head","tail"],["A","B","C","D","E","F","G","H"]]]

print(array_3d[0][2][3])
def new_password():
  random1=random.randint(0,8)   
  random2=random.randint(0,1)
  random3=random.randint(0,7) 
  
  letter1=str(array_3d[0][0][random1])
  letter2=(array_3d[0][1][random2])
  letter3=(array_3d[0][2][random3])
  
  label_1["text"]=letter1+""+letter2+""+letter3
  
btn=Button(root,text="Generate password",command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_1.place(relx=0.5,rely=0.6,anchor=CENTER)
  
root.mainloop()