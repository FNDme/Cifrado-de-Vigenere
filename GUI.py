from tkinter import messagebox, Tk, Canvas, Text, Button, Label, Entry, END, DISABLED, NORMAL
from Vigenere import encrypt, decrypt

base = Tk()

base.title('Vigenere Cipher')
base.resizable(False, False)
base.geometry('500x400')
base.configure(background='#232426')


Canva = Canvas(base, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
Canva.place(x=0, y=335)


def gui_encrypt():
    key = keyText.get()
    if key == '' or key.count(' ') > 1:
        messagebox.showerror('Error', 'Key must be one word')
        return
    key = key.replace('\n', '')
    key = key.replace('\t', '')

    encrypted = encrypt(inputText.get('1.0', END), keyText.get())

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.insert(END, encrypted)
    outputText.config(state=DISABLED)

    return


def gui_decrypt():
    key = keyText.get()
    if key == '' or key.count(' ') > 1:
        messagebox.showerror('Error', 'Key must be one word')
        return
    key = key.replace('\n', '')
    key = key.replace('\t', '')

    decrypted = decrypt(inputText.get('1.0', END), keyText.get())

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.insert(END, decrypted)
    outputText.config(state=DISABLED)

    return


def clear():
    inputText.delete('1.0', END)

    keyText.delete('1.0', END)

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.config(state=DISABLED)


inputTextLabel = Label(base, text='Input Text')
inputTextLabel.place(x=30, y=30)
inputTextLabel.configure(background='#232426', foreground='#F2F2F2')
keyTextLabel = Label(base, text='Key')
keyTextLabel.place(x=30, y=130)
keyTextLabel.configure(background='#232426', foreground='#F2F2F2')
outputTextLabel = Label(base, text='Output Text')
outputTextLabel.place(x=30, y=210)
outputTextLabel.configure(background='#232426', foreground='#BFBFBD')
inputText = Text(base, width=50, height=3)
inputText.place(x=20, y=60)
inputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
keyText = Entry(base, width=25)
keyText.place(x=20, y=160)
keyText.configure(background='#04BF68', foreground='#232426', borderwidth=0)
outputText = Text(base, width=50, height=3)
outputText.place(x=20, y=240)
outputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)
Encrypt = Button(base, text='Encrypt', command=lambda: gui_encrypt())
Encrypt.place(x=30, y=355)
Encrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
Decript = Button(base, text='Decrypt', command=lambda: gui_decrypt())
Decript.place(x=110, y=355)
Decript.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)
Clear = Button(base, text='Clear', command=lambda: clear())
Clear.place(x=410, y=355)
Clear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)


base.mainloop()
