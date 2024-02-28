from tkinter import *
from tkinter import messagebox
import time
import datetime as dt

  
window = Tk()
window.title('Sego Bebek Mentok')
window.resizable(0,0)
window.geometry('700x600') # membuat ukuran
window.configure(bg='#4169E1') # membuat background warna
#window.iconbitmap(r'logo.ico') # membuat logo atas kiri


# Variabel Manu
SegoBebek = StringVar()
SegoAyam = StringVar()
SegoUsus = StringVar()
EsTeh = StringVar()
EsJeruk = StringVar()
EsDegan = StringVar()
TehAnget = StringVar()
DeganAnget = StringVar()
tekstotal = StringVar()
teksuang = StringVar()
uang = 0
total = 0
tax = 0.11

# buat function
def totalbeli():
    global SegoBebek, SegoAyam, SegoUsus, EsTeh, TehAnget, DeganAnget, tekstotal , total
    hSegoBebek = int(SegoBebek.get()) * 25000
    hSegoAyam = int(SegoAyam.get()) * 15000
    hSegoUsus = int(SegoUsus.get()) * 10000
    hEsTeh = int(EsTeh.get()) * 5000
    hTehAnget = int(TehAnget.get()) * 4000
    hDeganAnget = int(DeganAnget.get()) * 6000
    total = (hSegoBebek + (hSegoBebek * tax)) + (hSegoAyam + (hSegoAyam * tax)) + (hSegoUsus + (hSegoUsus * tax)) + (hEsTeh + (hEsTeh* tax)) + (hTehAnget + (hTehAnget * tax)) + (hDeganAnget + (hDeganAnget * tax))
    tekstotal.set(int(total))
   
def kembalian():
    uang = int(teksuang.get())
    
    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian kamu sebesar Rp. {}'.format(int(kembalian)))
    else:
        messagebox.showerror(message='Mohon Maaf Kurang Ya Mas Atau Mbak e.')
    

def clear():
        SegoBebek.set('0')
        SegoAyam.set('0')
        SegoUsus.set('0')
        EsTeh.set('0')
        TehAnget.set('0')
        DeganAnget.set('0')
        tekstotal.set('0')
        teksuang.set('0')

# membuat TULISAN
Label(window, text='Sego Bebek Mentok', bg='#4169E1', fg='#fef5ac', font='arialblack 20 bold').place(x=220,y=30)

# membuat label nama menu
Label(window, text='1. SegoBebek', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=100,y=100)
Label(window, text='2. SegoAyam', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=100,y=140)
Label(window, text='3. SegoUsus', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=100,y=180)
Label(window, text='4. EsTeh', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=100,y=220)
Label(window, text='5. TehAnget', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=100,y=260)
Label(window, text='6. DeganAnget', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=100,y=300)

# membuat label harga
Label(window, text='Rp.25.000', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=350,y=100)
Label(window, text='Rp.15.000', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=350,y=140)
Label(window, text='Rp.10.000', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=350,y=180)
Label(window, text='Rp.5.000', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=350,y=220)
Label(window, text='Rp.4.000', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=350,y=260)
Label(window, text='Rp.6.000', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12').place(x=350,y=300)

# membuat spinbox
Spinbox(window, from_=0, to=100, width=4, font='timesnewroman 11', textvariable=SegoBebek, command=totalbeli).place(x=550,y=100)
Spinbox(window, from_=0, to=100, width=4, font='timesnewroman 11', textvariable=SegoAyam, command=totalbeli).place(x=550,y=140)
Spinbox(window, from_=0, to=100, width=4, font='timesnewroman 11', textvariable=SegoUsus, command=totalbeli).place(x=550,y=180)
Spinbox(window, from_=0, to=100, width=4, font='timesnewroman 11', textvariable=EsTeh, command=totalbeli).place(x=550,y=220)
Spinbox(window, from_=0, to=100, width=4, font='timesnewroman 11', textvariable=TehAnget, command=totalbeli).place(x=550,y=260)
Spinbox(window, from_=0, to=100, width=4, font='timesnewroman 11', textvariable=DeganAnget, command=totalbeli).place(x=550,y=300)

# membuat label pembayaran
Label(window, text='Masukan uang anda:', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12 ').place(x=100,y=340)

# Label Pembayaran Transfer
Label(window, text='Pembayaran Transfer\nBCA 1991490812',bg='#4169E1', fg='#fef5ac', font='timesnewroman 12 ').place(x=100,y=450)
Label(window, text='Info Pemesanan Catering\nWa081243447272',bg='#4169E1', fg='#fef5ac', font='timesnewroman 12 ').place(x=100,y=500)
Label(window, text='Tersedia\n "Sego Bebek Mentok"\n GOJEK\nSHOPEE FOOD\n GRAB\n MAXIM FOOD',bg='#4169E1', fg='#fef5ac', font='timesnewroman 12 ').place(x=300,y=450)

# membuat entry jumlah uang
Entry(window, textvariable=teksuang).place(x=100,y=370) 

# membuat label total
Label(window, text='Total Harga Rp.', bg='#4169E1', fg='#fef5ac', font='timesnewroman 12 bold').place(x=390,y=370)
Label(window, textvariable=tekstotal, bg='#4169E1', fg='#fef5ac', font='timesnewroman 12 bold').place(x=510,y=370)

# membuat tombol
Button(window, text='Bayar', fg='black', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=400)
Button(window, text='Selesai', fg='black', bg='#ff1e1e', width=10, command=clear).place(x=250,y=400)

def waktu():
    x = time.strftime("%H:%M:%S %p \n %x")
    label.config(text=x)
    label.after(200, waktu)

label = Label(window, bg="#4169E1", fg="#fef5ac", font='timesnewroman 20 bold')
label.place(x=540,y=0)

waktu ()
window.mainloop() 