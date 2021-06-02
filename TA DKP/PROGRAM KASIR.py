from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime


def submit():
    datetime.datetime.now()
    x = datetime.datetime.now()    

    pesan1=""
    pesan2=""
    pesan3=""
    pesan4=""
    pesan5=""

    total1=0
    total2=0
    total3=0
    total4=0
    total5=0  
    
    if len(stringnomor.get()) == 0:
        messagebox.showerror("Error","Nomor meja belum terisi")
        return
    if re.search('[a-zA-Z]',stringnomor.get()):
        messagebox.showerror("Error","Nomor meja tidak bisa diisi selain angka")
        return

    if re.search('[a-zA-Z]',stringjml1.get()):
        messagebox.showerror("Error","Pastikan jumlah dalam angka")
        return
    if re.search('[a-zA-Z]',stringjml2.get()):
        messagebox.showerror("Error","Pastikan jumlah dalam angka")
        return
    if re.search('[a-zA-Z]',stringjml3.get()):
        messagebox.showerror("Error","Pastikan jumlah dalam angka")
        return
    if re.search('[a-zA-Z]',stringjml4.get()):
        messagebox.showerror("Error","Pastikan jumlah dalam angka")
        return
    if re.search('[a-zA-Z]',stringjml5.get()):
        messagebox.showerror("Error","Pastikan jumlah dalam angka")
        return
    
    if radio.get()== 0:
        messagebox.showerror("Error","Jenis pesanan belum terisi")
        return
    elif radio.get() == 1:
        JP="Dine In "
    elif radio.get() == 2:
        JP="Take Away "
        
    if re.search('[a-zA-Z]',stringbayar.get()):
        messagebox.showerror("Error","Pastikan input pembayaran dalam angka")
        return
    elif stringbayar.get()== 0:
        messagebox.showerror("Error", "Nominal uang pembayaran belum dimasukkan")
        return
        
    if strpesan1.get()=="Menu yang dipilih":
        messagebox.showerror("Error","Tidak ada menu yang dipesan")
        return
    elif strpesan1.get()== "Paket Blue":
        total1= 19999*int(stringjml1.get())
        pesan1= "\n\tPaket blue @19.999 x "+ str(stringjml1.get())+ "\t" + str(total1)
    elif strpesan1.get()== "Paket Yellow":
        total1= 24999*int(stringjml1.get())
        pesan1= "\n\tPaket yellow @24.999 x "+ str(stringjml1.get())+ "\t" + str(total1)
    elif strpesan1.get()== "Paket Green":
        total1= 28999*int(stringjml1.get())
        pesan1= "\n\tPaket green @28.999 x "+ str(stringjml1.get())+ "\t" + str(total1)
    elif strpesan1.get()== "Paket Mint":
        total1= 33999*int(stringjml1.get())
        pesan1= "\n\tPaket mint @33.999 x "+ str(stringjml1.get())+ "\t" + str(total1)
    elif strpesan1.get()== "Paket Purple":
        total1= 37999*int(stringjml1.get())
        pesan1= "\n\tPaket purple @37.999 x "+ str(stringjml1.get())+ "\t" + str(total1)

    if strpesan2.get()=="Menu yang dipilih":
        messagebox.showerror("Error","Tidak ada menu yang dipesan")
        return
    elif strpesan2.get()== "Paket Blue":
        total2= 19999*int(stringjml2.get())
        pesan2= "\n\tPaket blue @19.999 x "+ str(stringjml2.get())+ "\t" + str(total2)
    elif strpesan2.get()== "Paket Yellow":
        total2= 24999*int(stringjml2.get())
        pesan2= "\n\tPaket yellow @24.999 x "+ str(stringjml2.get())+ "\t" + str(total2)
    elif strpesan2.get()== "Paket Green":
        total2= 28999*int(stringjml2.get())
        pesan2= "\n\tPaket green @28.999 x "+ str(stringjml2.get())+ "\t" + str(total2)
    elif strpesan2.get()== "Paket Mint":
        total2= 33999*int(stringjml2.get())
        pesan2= "\n\tPaket mint @33.999 x "+ str(stringjml2.get())+ "\t" + str(total2)
    elif strpesan2.get()== "Paket Purple":
        total2= 37999*int(stringjml2.get())
        pesan2= "\n\tPaket purple @37.999 x "+ str(stringjml2.get())+ "\t" + str(total2)

    if strpesan3.get()=="Menu yang dipilih":
        messagebox.showerror("Error","Tidak ada menu yang dipesan")
        return
    elif strpesan3.get()== "Paket Blue":
        total3= 19999*int(stringjml3.get())
        pesan3= "\n\tPaket blue @19.999 x "+ str(stringjml3.get())+ "\t" + str(total3)
    elif strpesan3.get()== "Paket Yellow":
        total3= 24999*int(stringjml3.get())
        pesan3= "\n\tPaket yellow @24.999 x "+ str(stringjml3.get())+ "\t" + str(total3)
    elif strpesan3.get()== "Paket Green":
        total3= 28999*int(stringjml3.get())
        pesan3= "\n\tPaket green @28.999 x "+ str(stringjml3.get())+ "\t" + str(total3)
    elif strpesan3.get()== "Paket Mint":
        total3= 33999*int(stringjml3.get())
        pesan3= "\n\tPaket mint @33.999 x "+ str(stringjml3.get())+ "\t" + str(total3)
    elif strpesan3.get()== "Paket Purple":
        total3= 37999*int(stringjml3.get())
        pesan3= "\n\tPaket purple @37.999 x "+ str(stringjml3.get())+ "\t" + str(total3)

    if strpesan4.get()=="Menu yang dipilih":
        messagebox.showerror("Error","Tidak ada menu yang dipesan")
        return
    elif strpesan4.get()== "Paket Blue":
        total4= 19999*int(stringjml4.get())
        pesan4= "\n\tPaket blue @19.999 x "+ str(stringjml4.get())+ "\t" + str(total4)
    elif strpesan4.get()== "Paket Yellow":
        total4= 24999*int(stringjml4.get())
        pesan4= "\n\tPaket yellow @24.999 x "+ str(stringjml4.get())+ "\t" + str(total4)
    elif strpesan4.get()== "Paket Green":
        total4= 28999*int(stringjml4.get())
        pesan4= "\n\tPaket green @28.999 x "+ str(stringjml4.get())+ "\t" + str(total4)
    elif strpesan4.get()== "Paket Mint":
        total4= 33999*int(stringjml4.get())
        pesan4= "\n\tPaket mint @33.999 x "+ str(stringjml4.get())+ "\t" + str(total4)
    elif strpesan4.get()== "Paket Purple":
        total4= 37999*int(stringjml4.get())
        pesan4= "\n\tPaket purple @37.999 x "+ str(stringjml4.get())+ "\t" + str(total4)

    if strpesan5.get()=="Menu yang dipilih":
        messagebox.showerror("Error","Tidak ada menu yang dipesan")
        return
    elif strpesan5.get()== "Paket Blue":
        total5= 19999*int(stringjml5.get())
        pesan5= "\n\tPaket blue @19.999 x "+ str(stringjml5.get())+ "\t" + str(total5)
    elif strpesan5.get()== "Paket Yellow":
        total5= 24999*int(stringjml5.get())
        pesan5= "\n\tPaket yellow @24.999 x "+ str(stringjml5.get())+ "\t" + str(total5)
    elif strpesan5.get()== "Paket Green":
        total5= 28999*int(stringjml5.get())
        pesan5= "\n\tPaket green @28.999 x "+ str(stringjml5.get())+ "\t" + str(total5)
    elif strpesan5.get()== "Paket Mint":
        total5= 33999*int(stringjml5.get())
        pesan5= "\n\tPaket mint @33.999 x "+ str(stringjml5.get())+ "\t" + str(total5)
    elif strpesan5.get()== "Paket Purple":
        total5= 37999*int(stringjml5.get())
        pesan5= "\n\tPaket purple @37.999 x "+ str(stringjml5.get())+ "\t" + str(total5)

    n=0
    y=" "
    z=" terima kasih"
    for n in range (3):
        y=y+ z
        n+=1

    m=0
    p=" "
    q="-"
    for n in range (43):
        p=p+q
        n+=1

    total=total1+total2+total3+total4+total5

    if int(stringbayar.get())>total:
        kembalian=int(stringbayar.get())-total
    else:
        messagebox.showerror("Transaksi Gagal","Maaf Uang Anda Kurang")
        return
            
    header="\t\tVakansi Cafe\t\n\t      Jalan Pemuda No 1, Jepara\t\n\t"+p+ "\n\n"
    #footer="\n\t\t^^Terima Kasih^^\t\t\t"
    teks = ("Waktu\t\t: "+ str(x)+"\nNomor Meja\t: " + str(stringnomor.get()) + "\nJenis Pesanan\t: " + JP +"\n\n\t"+pesan1+pesan2+pesan3+pesan4+pesan5)

    messagebox.showinfo("Konfirmasi Pesanan", header+teks + "\n\t" + p +"\n\tTotal\t\t\t" + str(total) + "\n\tBayar\t\t\t" +str(stringbayar.get()) + "\n\tKembalian\t\t" + str(kembalian)+"\n\n   "+y)
    
window=Tk()

window.title("Kasir Vakansi Cafe")
window.geometry("500x500")

tab = ttk.Notebook(window)
tab1 = ttk.Frame(tab)
tab2 = ttk.Frame(tab)
tab.add(tab1, text='Daftar Menu')
tab.add(tab2, text='Pembayaran')

lbl=Label(tab1,text="Vakansi Cafe",fg="dark blue",font=("Keep on Truckin", 25)).pack()
lbl=Label(tab1,text="Jalan Permuda No 1, Jepara",fg="dark blue", font=("Futura BK BT", 10)).pack()
lbl=Label(tab1,text="===================================",fg="dark blue", font=("Futura BK BT", 5)).pack()
lbl=Label(tab1,text="\nDaftar Menu",fg="dark blue", font=("Futura BK BT", 10)).pack()
lbl=Label(tab1,text="\n Paket Blue\t\t Rp19.999/porsi \n Paket Yellow\t\t Rp24.999/porsi \n Paket Green\t\t Rp28.999/porsi \n Paket Mint\t\t Rp33.999/porsi \n Paket Puple\t\t Rp37.999/porsi",fg="dark blue", font=("Futura BK BT", 12)).pack()

lbl=Label(tab2,text="Vakansi Cafe",fg="dark blue",font=("Keep on Truckin", 25)).pack()
lbl=Label(tab2,text="Jalan Permuda No 1, Jepara",fg="dark blue", font=("Futura BK BT", 10)).pack()
lbl=Label(tab2,text="===================================",fg="dark blue", font=("Futura BK BT", 5)).pack()

lbl=Label(tab2,text="Nomor Meja:\t",font=("Futura BK BT", 12)).place(x=5, y=100)
stringnomor= StringVar()
nomorEntry = Entry(tab2, width=5, textvariable=stringnomor).place(x=120,y=105)

lbl=Label(tab2,text="Menu 1:\t",font=("Futura BK BT", 12)).place(x=5, y=200)
strpesan1 = StringVar(value="Menu yang Dipilih") 
Cb1 = ttk.Combobox(tab2, width = 20, textvariable = strpesan1, state="readonly")
Cb1.place(x=70, y=205)
Cb1["values"] = ("Paket Blue",
                 "Paket Yellow",
                 "Paket Green",
                 "Paket Mint",
                 "Paket Purple") 
lbl=Label(tab2,text="Jumlah Porsi:\t",font=("Futura BK BT", 12)).place(x=250, y=200)
stringjml1= StringVar()
jml1= Entry(tab2, width=5, textvariable=stringjml1).place(x=355,y=205)

lbl=Label(tab2,text="Menu 2:\t",font=("Futura BK BT", 12)).place(x=5, y=230)
strpesan2 = StringVar(value="Menu yang Dipilih") 
Cb2 = ttk.Combobox(tab2, width = 20, textvariable = strpesan2, state="readonly")
Cb2.place(x=70, y=235)
Cb2["values"] = ("Paket Blue",
                 "Paket Yellow",
                 "Paket Green",
                 "Paket Mint",
                 "Paket Purple") 
lbl=Label(tab2,text="Jumlah Porsi:\t",font=("Futura BK BT", 12)).place(x=250, y=230)
stringjml2= StringVar()
jml2 = Entry(tab2, width=5, textvariable=stringjml2).place(x=355,y=235)

lbl=Label(tab2,text="Menu 3:\t",font=("Futura BK BT", 12)).place(x=5, y=260)
strpesan3 = StringVar(value="Menu yang Dipilih") 
Cb3 = ttk.Combobox(tab2, width = 20, textvariable = strpesan3, state="readonly")
Cb3.place(x=70, y=265)
Cb3["values"] = ("Paket Blue",
                 "Paket Yellow",
                 "Paket Green",
                 "Paket Mint",
                 "Paket Purple") 
lbl=Label(tab2,text="Jumlah Porsi:\t",font=("Futura BK BT", 12)).place(x=250, y=260)
stringjml3= StringVar()
jml3 = Entry(tab2, width=5, textvariable=stringjml3).place(x=355,y=265)

lbl=Label(tab2,text="Menu 4:\t",font=("Futura BK BT", 12)).place(x=5, y=290)
strpesan4 = StringVar(value="Menu yang Dipilih") 
Cb4 = ttk.Combobox(tab2, width = 20, textvariable = strpesan4, state="readonly")
Cb4.place(x=70, y=295)
Cb4["values"] = ("Paket Blue",
                 "Paket Yellow",
                 "Paket Green",
                 "Paket Mint",
                 "Paket Purple") 
lbl=Label(tab2,text="Jumlah Porsi:\t",font=("Futura BK BT", 12)).place(x=250, y=290)
stringjml4= StringVar()
jml4 = Entry(tab2, width=5, textvariable=stringjml4).place(x=355,y=295)

lbl=Label(tab2,text="Menu 5:\t",font=("Futura BK BT", 12)).place(x=5, y=320)
strpesan5 = StringVar(value="Menu yang Dipilih") 
Cb5 = ttk.Combobox(tab2, width = 20, textvariable = strpesan5, state="readonly")
Cb5.place(x=70, y=325)
Cb5["values"] = ("Paket Blue",
                 "Paket Yellow",
                 "Paket Green",
                 "Paket Mint",
                 "Paket Purple") 
lbl=Label(tab2,text="Jumlah Porsi:\t",font=("Futura BK BT", 12)).place(x=250, y=320)
stringjml5= StringVar()
jml5 = Entry(tab2, width=5, textvariable=stringjml5).place(x=355,y=325)

radio= IntVar()
radio1= Radiobutton(tab2, text="Dine In", variable=radio, value=1). place(x=5, y=150)
radio2= Radiobutton(tab2, text="Take Away", variable=radio, value=2). place(x=100, y=150)

lbl=Label(tab2,text="Bayar:\t",font=("Futura BK BT", 12)).place(x=5, y=370)
stringbayar= StringVar()
bayar= Entry(tab2, width=25, textvariable=stringbayar).place(x=70,y=375)

btn1 = Button(tab2, command = submit, text="SUBMIT").place(x=355,y=375)
#btn2 = Button (tab2, command = clear, text="CLEAR"). place (x=330, y=375)
tab.pack(expand=1, fill='both')
window.mainloop()
