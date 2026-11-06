import tkinter as tk
import pyautogui as pag


def iHerb():
    win = tk.Tk()
    win.geometry('335x230+400+108')
    win.title('iHerb data)')

    Label_name = tk.Label(win, text='Number', font=25)
    Label_name.grid(row=0, column=0)

    Entry_name = tk.Entry(win, font=25)
    Entry_name.grid(row=0, column=1)

    Label_password = tk.Label(win, text='Password', font=25)
    Label_password.grid(row=1, column=0)

    Entry_password = tk.Entry(win, font=25, show='*')
    Entry_password.grid(row=1, column=1)

    name = Entry_name.get()
    password = Entry_password.get()
    print(name)
    print(password)

    def Open():
        name = Entry_name.get()
        password = Entry_password.get()
        pag.click(91, 1055)
        pag.hotkey('ctrl', 't')
        pag.write('iHerb.Ua')
        pag.hotkey("enter")
        pag.sleep(8)
        pag.click(1634, 201)
        pag.sleep(3)
        pag.click(570, 478)
        pag.write(name)
        pag.sleep(1)
        pag.doubleClick(592, 557)
        pag.write(password)
        pag.sleep(1)
        pag.doubleClick(642, 757)

    Send_button = tk.Button(win, text='Send data', activebackground='yellow', command=Open)
    Send_button.grid(row=2, column=2)
    win.mainloop()


root = tk.Tk()
root.geometry('335x230+400+108')
photo = tk.PhotoImage(file='../images/user.png')
root.iconphoto(False, photo)
root.title('Choice')

iHerb_Button = tk.Button(text='iHerb', fg='#228B22', activeforeground='#FFFFFF', activebackground='#228B22',
                         font=('Arial', 32), command=iHerb)
iHerb_Button.grid(row=0, column=0, padx=3, pady=5)


def Olx():
    olx = tk.Tk()
    olx.geometry('335x230+400+108')
    olx.title('OLX date)')

    Label_email_or_number = tk.Label(olx, text='Number +380', font=25)
    Label_email_or_number.grid(row=0, column=0)

    Entry_email_or_number = tk.Entry(olx, font=25)
    Entry_email_or_number.grid(row=0, column=1)

    Label_password = tk.Label(olx, text='Password', font=25)
    Label_password.grid(row=1, column=0)

    Entry_password = tk.Entry(olx, font=25, show='*')
    Entry_password.grid(row=1, column=1)

    name = Entry_email_or_number.get()
    password = Entry_password.get()
    print(name)
    print(password)

    def Open_olx():
        name = Entry_email_or_number.get()
        password = Entry_password.get()
        pag.click(91, 1055)
        pag.hotkey('ctrl', 't')
        pag.write('Olx.ua')
        pag.hotkey("enter")
        pag.sleep(4)
        pag.click(1277, 162)
        pag.sleep(2)
        pag.doubleClick(787, 694)
        pag.write(name)
        pag.sleep(1)
        pag.doubleClick(742, 799)
        pag.write(password)
        pag.sleep(1)
        pag.doubleClick(901, 975)

    Send_button = tk.Button(olx, text='Send data', activebackground='yellow', command=Open_olx)
    Send_button.grid(row=2, column=1)
    olx.mainloop()


OLX_Button = tk.Button(text='OLX', fg='#FF6347', activeforeground='#FFFFFF', activebackground='#FF6347',
                       font=('Arial', 32), command=Olx)
OLX_Button.grid(row=0, column=1)


def Prom():
    prom = tk.Tk()
    prom.geometry('335x230+400+108')
    prom.title('Prom date)')

    Label_Number = tk.Label(prom, text='Number +380', font=25)
    Label_Number.grid(row=0, column=0)

    Entry_Number = tk.Entry(prom, font=25)
    Entry_Number.grid(row=0, column=1)

    number = Entry_Number.get()

    def Open_prom():
        number = Entry_Number.get()
        pag.click(91, 1055)
        pag.hotkey('ctrl', 't')
        pag.write('Prom.ua')
        pag.hotkey("enter")
        pag.sleep(5)
        pag.click(1488, 232)
        pag.sleep(1)
        pag.click(1578, 226)
        pag.sleep(0.5)
        pag.doubleClick(1433, 533)
        pag.sleep(1)
        pag.write(number)
        pag.sleep(0.5)
        pag.click(1579, 603)

    Send_button = tk.Button(prom, text='Send data', activebackground='yellow', command=Open_prom)
    Send_button.grid(row=2, column=1)
    prom.mainloop()


Prom_Button = tk.Button(text='Prom', fg='#C71585', activeforeground='#FFFFFF', activebackground='#C71585',
                        font=('Arial', 32), command=Prom)
Prom_Button.grid(row=1, column=0, pady=5)


def site():
    any_site = tk.Tk()
    any_site.geometry('335x230+400+108')
    any_site.title('Site date)')

    Label_name = tk.Label(any_site, text='Number', font=25)
    Label_name.grid(row=0, column=0)

    Entry_name = tk.Entry(any_site, font=25)
    Entry_name.grid(row=0, column=1)

    Label_password = tk.Label(any_site, text='Password', font=25)
    Label_password.grid(row=1, column=0)

    Entry_password = tk.Entry(any_site, font=25, show='*')
    Entry_password.grid(row=1, column=1)

    name = Entry_name.get()
    password = Entry_password.get()
    print(name)
    print(password)

    def Open_site():
        name = Entry_name.get()
        password = Entry_password.get()
        pag.click(91, 1055)
        pag.hotkey('ctrl', 't')
        pag.write('iHerb.Ua')
        pag.hotkey("enter")
        pag.sleep(8)
        pag.click(1634, 201)
        pag.sleep(3)
        pag.click(570, 478)
        pag.write(name)
        pag.sleep(1)
        pag.doubleClick(592, 557)
        pag.write(password)
        pag.sleep(1)
        pag.doubleClick(642, 757)

    Send_button = tk.Button(any_site, text='Send data', activebackground='yellow', command=Open_site)
    Send_button.grid(row=2, column=2)
    any_site.mainloop()


_Button = tk.Button(text='SITE', fg='#FFD700', activeforeground='#FFFFFF', activebackground='#FFD700',
                    font=('Arial', 32), command=site)
_Button.grid(row=1, column=1)

root.mainloop()
