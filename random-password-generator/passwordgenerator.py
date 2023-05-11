# pip install tkinter
# pip install pyperclip
# pip install random
# pip install strings


from tkinter import *
import random, string
import pyperclip



# Tkinter penceresi
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

# Başlık
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()

# Alt bilgi
Label(root, text ='github.com/enesakahs', font ='Consolas 15 bold').pack(side = BOTTOM)



# Şifre uzunluğunu seçin
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()



# Şifre üretme fonksiyonunu tanımla
pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   



Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

# Şifre alanı
Entry(root , textvariable = pass_str).pack()


# Şifreyi kopyalamak için fonksiyon
def Copy_password():
    pyperclip.copy(pass_str.get())

# Kopyala butonu
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)



# döngü
root.mainloop()
