import tkinter as tk
import customtkinter as ctk
import prompt

ctk.set_appearance_mode("darkS")
ctk.set_default_color_theme("blue")
appWidth,appLength=500,750

class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Summarize text")
        self.geometry(f"{appWidth}x{appLength} ")

        self.nameLabel=ctk.CTkLabel(self,text="Enter Text to convert")
        self.nameLabel.grid(row=0,column=0,padx=20,pady=20,sticky="ew")

        self.nameEntry=ctk.CTkEntry(self,placeholder_text="Enter Text",width=300,height=100)
        self.nameEntry.grid(row=0,column=1,columnspan=50,padx=20,pady=90,sticky="ew")

        self.displayBox=ctk.CTkTextbox(self,width=300,height=100)
        self.displayBox.grid(row=3,column=1,padx=20,pady=20,sticky="ew")
        self.displayBox.configure(state="disabled")
        
        self.generateButton=ctk.CTkButton(self,text="Generate Summary",command=self.generate_result)
        self.generateButton.grid(row=2,column=1,padx=20,pady=20,sticky="ew")

    def generate_result(self):
        text=self.nameEntry.get()
        summary=prompt.generate_summary_prompt(text)
        self.displayBox.delete("0.0")
        self.displayBox.configure(state="normal")
        self.displayBox.insert("0.0",summary)

if __name__=="__main__":
    app=App()
    app.mainloop()