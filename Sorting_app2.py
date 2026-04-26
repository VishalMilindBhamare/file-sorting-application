from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,filedialog,messagebox
import os,shutil
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
        self.var_foldername=StringVar()
        lbl_Select_folder=Label(self.root,text="Select Folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=250,y=100,height=40,width=600)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=900,y=95,height=45,width=150)
        hr=Label(self.root,bg="lightgray").place(x=50,y=160,height=2,width=1250)

        #==========Section-2==========#
        #==========All Extensions==========#
        self.image_extensions=["Image Extensions",".png",".jpg",".jpeg"]
        self.audio_extensions=["Audio Extensions",".amr",".mp3",".wav"]
        self.video_extensions=["Video Extensions",".mp4",".avi",".mpeg4",".3gp",".mkv"]
        self.doc_extensions=["Document Extensions",".doc",".xlsx",".ppt",".pptx",".xls",".pdf",".zip",".rar",".csv",".docx",".txt"]
        
        self.folders={
                'videos':self.video_extensions,
                'audios':self.audio_extensions,
                'images':self.image_extensions,
                'documents':self.doc_extensions,
                
        }

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
        self.image_icon=PhotoImage(file="images/image.png")
        self.audio_icon=PhotoImage(file="images/im.png")
        self.video_icon=PhotoImage(file="images/Video.png")
        self.document_icon=PhotoImage(file="images/Document.png")
        self.other_icon=PhotoImage(file="images/Other.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)
        self.lbl_total_files=Label(Frame1,text="Total Files",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=10)

        img = Image.open("images/image.png")
        img = img.resize((70, 70))
        self.image_icon = ImageTk.PhotoImage(img)

        self.lbl_total_image = Label(
            Frame1,
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
            image=self.other_icon,
            compound=TOP,
            font=("times new roman",18,"bold"),
            bg='gray',
            fg="white",
            pady=10
        )
        self.lbl_other_image.place(x=1005,y=60,width=230,height=200)

    #==========Section-4==========#
        lbl_Status=Label(self.root,text="STATUS",font=("times new roman",20),bg="white").place(x=50,y=620)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",18),bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=620)

        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",18),bg="white",fg="blue")
        self.lbl_st_moved.place(x=500,y=620)

        self.lbl_st_left=Label(self.root,text="",font=("times new roman",18),bg="white",fg="orange")
        self.lbl_st_left.place(x=700,y=620)
    
    #=============Buttons===========#
        self.btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("times new roman",15,"bold"),bg="#607d8b",fg="white",activebackground="#607d8b",cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=880,y=610,height=45,width=200)

        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,text="START",font=("times new roman",15,"bold"),bg="#ff5722",fg="white",activebackground="#ff5722",cursor="hand2",activeforeground="white")
        self.btn_start.place(x=1100,y=610,height=45,width=200)

    def Total_count(self):
        images = 0
        audios = 0
        videos = 0
        documents = 0
        others = 0

        self.count = 0

    # ✅ Combine all extensions once
        all_extensions = []
        for ext_list in self.folders.values():
            all_extensions.extend(ext_list)

        for i in self.all_files:
            file_path = os.path.join(self.directry, i)

            # ✅ Only process FILES (ignore folders)
            if not os.path.isfile(file_path):
                continue

            self.count += 1
            ext = "." + i.split(".")[-1].lower()

            if ext in self.folders['images']:
                images += 1
            elif ext in self.folders['audios']:
                audios += 1
            elif ext in self.folders['videos']:
                videos += 1
            elif ext in self.folders['documents']:
                documents += 1
            else:
                others += 1

        # ✅ Update UI
        self.lbl_total_image.config(text=f"Total Images\n{images}")
        self.lbl_audio_image.config(text=f"Total Audio\n{audios}")
        self.lbl_Video_image.config(text=f"Total Videos\n{videos}")
        self.lbl_document_image.config(text=f"Total Documents\n{documents}")
        self.lbl_other_image.config(text=f"Other Files\n{others}")
        self.lbl_total_files.config(text=f"Total Files: {self.count}")

    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
           # print(op)
           self.var_foldername.set(str(op))
           self.directry =self.var_foldername.get()
           self.other_name ="others"
           self.rename_folder()
           self.all_files = os.listdir(self.directry)
           length=len(self.all_files)
           self.count=1
           self.Total_count()
           self.btn_start.config(state=NORMAL)
               
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                file_path = os.path.join(self.directry, i)

                if os.path.isfile(file_path):
                    c+=1 
                    self.create_move(i.split(".")[-1].lower(), i)
                    self.lbl_st_total.config(text="TOTAL:"+str(self.count))
                    self.lbl_st_moved.config(text="MOVED:"+str(c))
                    self.lbl_st_left.config(text="LEFT:"+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()
            messagebox.showinfo("Success","All Files Has moved Successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please Select folder")
    
    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text=f"")
        self.lbl_audio_image.config(text=f"")
        self.lbl_Video_image.config(text=f"")
        self.lbl_document_image.config(text=f"")
        self.lbl_other_image.config(text=f"")
        self.lbl_total_files.config(text=f"Total Files")


    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
                os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder.lower()))

    def create_move(self,ext, file_name):
        find = False

        for folder_name in self.folders:
            if "." + ext in self.folders[folder_name]:

                folder_path = os.path.join(self.directry, folder_name)

                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                shutil.move(
                    os.path.join(self.directry, file_name),
                    os.path.join(folder_path, file_name)
                )

                find = True
                break

        # 👉 Handle unknown files
        if not find:
            other_path = os.path.join(self.directry, self.other_name)

            if not os.path.exists(other_path):
                os.mkdir(other_path)

            shutil.move(
                os.path.join(self.directry, file_name),
                os.path.join(other_path, file_name)
            )

root = Tk()
obj = sorting_App(root)
root.mainloop()