import customtkinter
from tkinter import messagebox
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("500x500")
def ok():
    user_name =entry1.get()
    password =entry2.get()
    if not user_name or not password:
        messagebox.showerror("Error", "Username or Password cannot be empty")
    else:
        print(f"ok your login is done and you can proceed to the next step. Username: {user_name}")
frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=50,padx=50,fill="both",expand=True)
label=customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12,padx=10)
entry1=customtkinter.CTkEntry(master=frame,placeholder_text="User_name")
entry1.pack(pady=15,padx=12)
entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Pasword",show="-")
entry2.pack(pady=15,padx=13)
button=customtkinter.CTkButton(master=frame,text="Login",command=ok)
button.pack(pady=15,padx=13)
check=customtkinter.CTkCheckBox(master=frame,text="Remeber me always")
check.pack(pady=15,padx=13)
root.mainloop()

