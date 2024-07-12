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
        messagebox.showerror("Note This Point", "Username or Password cannot be empty")
    else:
        print(f"ok your login is done and you can proceed to the next step. Username: {user_name}")

def sign():
    if not entry1tab2.get() or not entry2tab2.get() or not c_entry2tab2.get():
        messagebox.showerror("Note This Point", "Username or Password cannot be empty")
    elif entry2tab2.get() != c_entry2tab2.get():
        messagebox.showerror("Note This Point", "Password and Confirm Password Should be Same ")
    else:
        print("You are good to login now..")
tabview = customtkinter.CTkTabview(master=root)
tabview.pack(pady=20, padx=20, fill="both", expand=True)


tabview.add("Tab 1")
tabview.add("Tab 2")
frame_1=customtkinter.CTkFrame(master=tabview.tab("Tab 1"))
frame_1.pack(pady=50,padx=50,fill="both",expand=True)
label=customtkinter.CTkLabel(master=frame_1, text="Login System")
label.pack(pady=12,padx=10)
entry1=customtkinter.CTkEntry(master=frame_1,placeholder_text="User_name")
entry1.pack(pady=15,padx=12)
entry2=customtkinter.CTkEntry(master=frame_1,placeholder_text="Pasword",show="-")
entry2.pack(pady=15,padx=13)
button=customtkinter.CTkButton(master=frame_1,text="Login",command=ok)
button.pack(pady=15,padx=13)
check=customtkinter.CTkCheckBox(master=frame_1,text="Remeber me always")
check.pack(pady=15,padx=13)


# -------


frame_2=customtkinter.CTkFrame(master=tabview.tab("Tab 2"))
frame_2.pack(pady=20,padx=50,fill="both",expand=True)
labeltab2=customtkinter.CTkLabel(master=frame_2, text="Signup System")
labeltab2.pack(pady=12,padx=10)
entry1tab2=customtkinter.CTkEntry(master=frame_2,placeholder_text="Create Username")
entry1tab2.pack(pady=15,padx=12)
label2=customtkinter.CTkLabel(master=frame_2, text="Create a Password")
label2.pack(pady=5,padx=4)
entry2tab2=customtkinter.CTkEntry(master=frame_2,placeholder_text="Pasword",show="-")
entry2tab2.pack(pady=15,padx=13)
c_entry2tab2=customtkinter.CTkEntry(master=frame_2,placeholder_text="Confirm Password",show="-")
c_entry2tab2.pack(pady=15,padx=13)
button2=customtkinter.CTkButton(master=frame_2,text="sign up",command=sign)
button2.pack(pady=15,padx=13)




root.mainloop()

