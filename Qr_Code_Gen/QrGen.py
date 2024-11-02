import tkinter as tk
from datetime import datetime
import qrcode
from tkinter import messagebox
from PIL import Image

root =tk.Tk()
root.geometry("400x350")
root.title("QR Code Generator")
label = tk.Label(root, text="ENTER THE TEXT TO CONVERT",font=("Arial"))
text = tk.Text(root, height=1.5, width=50)
label.pack()
text.pack()
root.configure(background="#800080")

def get_input():
    input_text = text.get("1.0", "end-1c")
    if text.get("1.0", "end-1c") == "":
        messagebox.showinfo("Message", "the code contain nothing")
    img = qrcode.make(input_text)
    current_time = datetime.now()
    formatted_time = current_time.strftime("%I_%M_%S")
    global Name
    Name = 'qrcodr'+formatted_time+'.png'
    img.save(Name)



button_1 = tk.Button(root, text="GENERATE MY CODE ", command = get_input)
button_1.pack()

def clear_ex():
    text.delete("1.0","end")


button_2= tk.Button(root, text="Clear", command=clear_ex, font=('Helvetica bold',10)).pack(pady=5)



root.mainloop()
