from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
class sorting_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Application | Developed by Vishal | techashlabs")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # Resize image
        img = Image.open("images/folder.png")
        img = img.resize((80, 80))   # adjust size as needed
        self.logo_icon = ImageTk.PhotoImage(img)

        title = Label(
            self.root,
            text="File Sorting Application",
            image=self.logo_icon,
            compound=LEFT,
            padx=10,
            font=("impact", 40),
            bg="#023548",
            fg="white",
            anchor="w"
        )
        title.place(x=0, y=0, relwidth=1)

        #==========Section-1==========#

        lbl_Select_folder=Label(self.root,text="Select Folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        txt_folder_name=Entry(self.root,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=250,y=100,height=40,width=600)
        btn_browse=Button(self.root,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=900,y=95,height=45,width=150)
        hr=Label(self.root,bg="lightgray").place(x=50,y=160,height=2,width=1250)

        #==========Section-2==========#
        #==========All Extensions==========#
        self.image_extensions=["Image Extensions",".png",".jpg"]
        self.audio_extensions=["Audio Extensions",".amr",".mp3"]
        self.video_extensions=["Video Extensions",".mp4",".avi",".mpeg4",".3gp"]
        self.doc_extensions=["Document Extensions",".doc",".xlsx",".ppt",".pptx",".xls",".pdf",".zip",".rar",".csv",".docx",".txt"]
        lbl_Support_ext=Label(self.root,text="Various Support Extensions",font=("times new roman",25),bg="white").place(x=50,y=170)
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.image_box.place(x=60,y=230,width=270,height=35)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.video_box.place(x=360,y=230,width=270,height=35)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.audio_box.place(x=700,y=230,width=270,height=35)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.doc_box.place(x=1010,y=230,width=270,height=35)
        self.doc_box.current(0) 

         #==========Section-3==========#
        #==========All Image Icons==========#
        self.image_icon=PhotoImage(file="images/im.png")
        self.audio_icon=PhotoImage(file="images/im.png")
        self.video_icon=PhotoImage(file="images/im.png")
        self.document_icon=PhotoImage(file="images/im.png")
        self.other_icon=PhotoImage(file="images/im.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)
        self.lbl_total_files=Label(Frame1,text="Total Files:150",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)

        img = Image.open("images/image.png")
        img = img.resize((70, 70))
        self.image_icon = ImageTk.PhotoImage(img)

        self.lbl_total_image = Label(
            Frame1,
            text="Total Images\n250",
            image=self.image_icon,
            compound=TOP,
            font=("times new roman",18,"bold"),
            bg='#0875B7',
            fg="white",
            pady=10
        )
        self.lbl_total_image.place(x=10,y=60,width=230,height=200)


        img = Image.open("images/im.png")
        img = img.resize((70, 70))
        self.audio_icon = ImageTk.PhotoImage(img)

        self.lbl_audio_image = Label(
            Frame1,
            text="Total Audio\n250",
            image=self.audio_icon,
            compound=TOP,
            font=("times new roman",18,"bold"),
            bg='#008EA4',
            fg="white",
            pady=10
        )
        self.lbl_audio_image.place(x=260,y=60,width=230,height=200)


        img = Image.open("images/Video.png")
        img = img.resize((70, 70))
        self.Videos_icon = ImageTk.PhotoImage(img)

        self.lbl_Video_image = Label(
            Frame1,
            text="Total Videos\n250",
            image=self.Videos_icon,
            compound=TOP,
            font=("times new roman",18,"bold"),
            bg='#DF002A',
            fg="white",
            pady=10
        )
        self.lbl_Video_image.place(x=510,y=60,width=230,height=200)


        img = Image.open("images/Document.png")
        img = img.resize((70, 70))
        self.document_icon = ImageTk.PhotoImage(img)

        self.lbl_document_image = Label(
            Frame1,
            text="Total Documents\n250",
            image=self.document_icon,
            compound=TOP,
            font=("times new roman",18,"bold"),
            bg='#008EA4',
            fg="white",
            pady=10
        )
        self.lbl_document_image.place(x=760,y=60,width=230,height=200)


        img = Image.open("images/Other.png")
        img = img.resize((70, 70))
        self.other_icon = ImageTk.PhotoImage(img)

        self.lbl_other_image = Label(
            Frame1,
            text="Other Files\n250",
            image=self.other_icon,
            compound=TOP,
            font=("times new roman",18,"bold"),
            bg='gray',
            fg="white",
            pady=10
        )
        self.lbl_other_image.place(x=1005,y=60,width=230,height=200)

root = Tk()
obj = sorting_App(root)
root.mainloop()