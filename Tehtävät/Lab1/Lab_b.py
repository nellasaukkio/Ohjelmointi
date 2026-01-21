from tkinter import Tk, Frame, Label, Button, Entry, messagebox
#luo ohjelman ikkuna
window = Tk()
window.title('hello')
#luo Frame, jonne tulee riville label ja entry
frame = Frame(window)
Label(frame,text='"mikä on sinun nimesi"',padx=10, pady=10).pack(side='left')
entry = Entry(frame)
entry.pack(side='right')
#show frame and Button
frame.pack(side='top')
Button(window, text='lähetä',command=lambda : [messagebox.showinfo("Hello",f'Hauska tavata, {entry.get()}'), entry.delete(0,'end')]).\
    pack(side='bottom')
#start the event loop
window.mainloop()
