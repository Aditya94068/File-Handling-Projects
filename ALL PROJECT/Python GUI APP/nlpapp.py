from tkinter import *
from mydb import *
from tkinter import messagebox
from myApi import *
class NLPApp:
    def __init__(self):
        #Create a db object
        self.dbo = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title('NLPAPP') # Add title Of aur App
        self.root.iconbitmap('resources/favicon.ico') # Changing Icon Of aur app
        self.root.geometry('350x600') # Adjusting aur the size of the software
        self.root.config(bg="#39648F") # Add the Background Color
        self.login_gui() 
        self.root.mainloop() # This statement is used for showing GUI window

    def login_gui(self):
        self.clear()
        
        heading = Label(self.root,text='NLPApp') # This is used for labeling our window
        heading.pack(pady=(30,30)) # This is used to add padding 
        heading.config(font=('verdana',20,'bold'),bg='#39648F',fg='white') # Here we are adjusting with fonts

        label1 = Label(self.root,text='Enter Email ')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=40)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=40,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text="Login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))


        label3 = Label(self.root,text='Not a member ?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))


    def register_gui(self):
        self.clear()
        
        heading = Label(self.root,text='NLPApp') 
        heading.pack(pady=(30,30))
        heading.config(font=('verdana',20,'bold'),bg='#39648F',fg='white') 

        label0 = Label(self.root,text='Enter name ')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=40)
        self.name_input.pack(pady=(5,5),ipady=4)


        label1 = Label(self.root,text='Enter Email ')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=40)
        self.email_input.pack(pady=(5,5),ipady=4)

        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=40,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn = Button(self.root,text="register",width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))


        label3 = Label(self.root,text='Already a member ?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    def clear(self):
         #clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()
    def perform_registration(self):
        #Fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration Successfull. You can login now')
        else:
            messagebox.showinfo('Error','Email already Exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else:
            messagebox.showinfo('error','Incorrect email or password')
        
    def home_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp') 
        heading.pack(pady=(30,30))
        heading.config(font=('verdana',20,'bold'),bg='#39648F',fg='white') 


        sentiment_btn = Button(self.root,text='Sentiment Analysis',width=40,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn = Button(self.root,text='Name Entity Recognisation',width=40,height=4,command=self.login_gui)
        ner_btn.pack(pady=(10,10))

        emotion_btn = Button(self.root,text='Emotion Predicion',width=40,height=4,command=self.login_gui)
        emotion_btn.pack(pady=(10,10))


        logout_btn = Button(self.root,text='Login Out',command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp') 
        heading.pack(pady=(30,30))
        heading.config(font=('verdana',20,'bold'),bg='#39648F',fg='white') 

        heading = Label(self.root,text='Sentiment Analysis') 
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',16,'bold'),bg='#39648F',fg='white') 


        label1 = Label(self.root,text="Enter the text")
        label1.pack(pady=(10,20))

        self.sentiment_input = Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

        sentiment_btn = Button(self.root,text='Analyze Sentiment',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root,text="",bg='#39648F',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.config(font=('verdana',16))

        goback_btn = Button(self.root,text="Go Back",command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        txt = ''
        for key , value in result.items():
            txt = txt +  key + ' ' + str(value) + '\n'
            self.sentiment_result['text'] = txt



nlp = NLPApp()