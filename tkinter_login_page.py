#author : roman
# this is just a practise file
#fb login page

import tkinter as tk

#create first  window
window=tk.Tk()
window.title("this is window title")




#display "welcome to facebook "
welcome=tk.Label(window,text="welcome to facebook  ",fg="red",bg="blue")  # .pack()
welcome.pack()

#Display  "Enter Your username / email address"
lbl2=tk.Label(window,text="Enter your username /  Email  address :")
lbl2.pack()

#entry field for username / email
entryEmail=tk.Entry(window ,)
entryEmail.pack()



#Display " Enter your password"
lablePass=tk.Label(window,text="Enter your password ")
lablePass.pack()

#entry field for enter  password
entryPass=tk.Entry(window)
entryPass.pack()

#save passward check box
forPass=tk.Checkbutton(window,text="save passward").pack()




#create Login Button
btn=tk.Button(window,text="Login  ",fg="red",bg="blue") #fg="red" can be wriiten before text
btn.pack()

#create sign up  button
btn1=tk.Button(window,text="Sign up  ",fg="red",bg="blue") #fg="red" can be wriiten before text
btn1.pack()

#create forget passward  button
forBtn=tk.Button(window,text="forget passward",fg="red",bg="blue")
forBtn.pack()





#must have at the end for tkinter
window.mainloop()


