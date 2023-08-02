from tkinter import *
from tkinter import messagebox
import os
import pickle


root = Tk()
root.title("Todo List App")
root.geometry('600x580')

#frame_task = Frame(root)
#frame_task.pack()

def add_task():
    task = text_entry.get()
    if task == '':
        messagebox.showwarning('warning','You must enter a task')
    else:
    #print(task)
        text_box.insert(END,task)
        text_entry.delete(0,END)

def delete_task():
    try:
        task_index = text_box.curselection()[0]
        text_box.delete(task_index)
    except:
        messagebox.showwarning('warning', 'You must select a task')

#if not os.path.exists('Tasks'):
 #   os.mkdir('Tasks')      
def save_task():
    if text_box.get(0) == '':
        messagebox.showwarning('warning','No available task to save')
        
    #print(task)
    else:
        task = text_box.get(0,text_box.size())
        pickle.dump(task, open("tasks.txt", "wb"))
        messagebox.showinfo('Success',f'Task {task} is Saved Successfully')
        
    #task_content = str(text_box.get(0,END))
    #print(task_content)
    #file = open('Tasks.txt', 'w')
    #file.write(task_content)
    #file.close()
   
def load_task():
    tasks = pickle.load(open("tasks.txt", "rb"))
    text_box.delete(0,END)
    for task in tasks:
        text_box.insert(END,task)
        
def delete_all_task():
    text_box.delete(0,END)

text_box = Listbox(root,relief=GROOVE,bd=7,fg='white',bg='black',width=98,height=25,
                   font=('ariel',12,'bold'))
text_box.place(x=0,y=0)

text_scroll = Scrollbar(root,orient=VERTICAL)
text_scroll.pack(side=RIGHT,fill=Y)
text_box.config(yscrollcommand=text_scroll.set)
text_scroll.config(command=text_box.yview)

 
text_entry = Entry(root,width=100,bd=6,relief=SUNKEN,font=('ariel',13,'bold'),
                   bg='white')
text_entry.place(x=0,y=400)
 
add_button = Button(root,text="Add Task",bg='firebrick2',width=100,cursor='hand2',
                    activebackground='firebrick2',bd=4,
                    relief=GROOVE,justify='center',command=add_task)
add_button.place(x=0,y=430)

delete_button = Button(root,text="Delete Task",bg='firebrick2',width=100,cursor='hand2',
                    activebackground='firebrick2',bd=4,
                    relief=GROOVE,command=delete_task)
delete_button.place(x=0,y=460)

load_button = Button(root,text="Load Task",bg='firebrick2',width=100,cursor='hand2',
                    activebackground='firebrick2',bd=4,
                    relief=GROOVE,command=load_task)
load_button.place(x=0,y=490)

save_button = Button(root,text="Save Task",bg='firebrick2',width=100,cursor='hand2',
                    activebackground='firebrick2',bd=4,
                    relief=GROOVE,command=save_task)
save_button.place(x=0,y=520) 

delete_all_button = Button(root,text="Delete all Task",bg='firebrick2',width=100,cursor='hand2',
                    activebackground='firebrick2',bd=4,
                    relief=GROOVE,command=delete_all_task)
delete_all_button.place(x=0,y=550) 


root.mainloop()