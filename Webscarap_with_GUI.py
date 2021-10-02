from tkinter import *

window=Tk()                                                                                         #opening window

window.geometry("550x400")                                                                          #window size

label1 =Label(window,text="Entente Project",font="times 24 bold")                                   #labels used to create label of type text
label1.grid(row=0,column=4)

label2 = Label(window,text="choose any one",font="times 20 italic")
label2.grid(row=3,column=4)

item_list=["lamps","chandlier","ships","coffee table","animal lamps","all products"]
item_listbox=StringVar(window)
item_listbox.set("select product")
menu=OptionMenu(window,item_listbox,*item_list)                                                     #labeled of type item_listbox and imported all
menu.grid(row=5,column=4)

listbox1=Listbox(window,height=15,width=80)
listbox1.grid(row=10,column=3,rowspan=6,columnspan=3,pady=10,padx=20)

sb1=Scrollbar(window)
sb1.grid(row=10,column=6,sticky='ns',rowspan=6)

listbox1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox1.yview)

b1=Button(window,text="search",width=12,bg="grey")                                                  #create button
b1.grid(row=7,column=4)

window.mainloop()
