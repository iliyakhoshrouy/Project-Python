from iliyaint import*
from random import choice
import string

class App:
    def __init__(self):
        self.window = il()
        self.window.title('PG')
        self.window.geometry('500x255')
        self.window.config(bg='black')

        #component creation
        self.label()
        self.entry()
        self.button()

    def label(self):
        label_title = Label(self.window, text='Welcome to PG APP', font=('Courrier', 20), bg='black', fg='white')
        label_title.pack()

    def entry(self):
        self.password_entry = Entry(self.window, font=('Courrier', 25), bg='red', fg='white', width=30, relief='solid')
        self.password_entry.pack(pady=50)

    def button(self):
        pg = Button(self.window, text="Generate Password",  font=('Courrier', 12), bg='gray', fg='white', width=25, command=self.generate_password)
        pg.pack()

    def generate_password(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ""
        for x in range(28):
            password+=choice(characters)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        
#display
app = App()
app.window.mainloop()
