# import random
# import tkinter as tk
#
#
# root = tk.Tk()
# photo = tk.PhotoImage(file='home.png')
# root.iconphoto(False, photo)
#
# root.title('Home program')
# root.geometry('300x400+550+185')
# root.config(bg='#A4B96C')
# label_name = tk.Label(root, text='Nick', font=('Arial', 15), bg='#B4A23A', fg='#000000', width=5, height=2, anchor='se', relief= tk.RAISED, bd=10 )
# label_name.pack()
#
# def print_text():
#     print(random.randint(1, 5))
#
#
# first = 0
# def add_label():
#     global first
#     random_col =['red', 'green', 'blue', 'yellow', ]
#     first_l = tk.Label(text=' new', bg=random.choices(random_col), font=('Arial', random.randint(5, 25)))
#     first_l.pack()
#     first += 1
#     if first >= 5:
#         root.destroy()
# Button_name = tk.Button(root, text='Random', font=('Time New Roman', 15), bg='#451AB9', fg='black', padx=10, pady=5, anchor='sw', relief=tk.RAISED, bd=30, command=print_text)
# Button_name.pack()
#
# add_button = tk.Button(root, text='Label', font=30, relief=tk.RAISED, bd=20, bg='#FF4536', command=add_label)
# add_button.pack()
#
# def add_cbt():
#     global count
#     count += 1
#     add_counter_button['text'] = f'Counter: {count}'
#
#
# count = 0
# add_counter_button = tk.Button(root, text=f'Counter:{count}', font=30, relief=tk.RAISED, bd=5, bg='yellow', activebackground='blue', command=add_cbt)
# add_counter_button.pack()
#
# root.minsize(200, 300)
# root.maxsize(400, 500)
#
# root.mainloop()
#
#
# import random
# import tkinter as tk
#
# root = tk.Tk()
#
# root.geometry(f'350x350+400+182')
# root.title('GRID')
# #root.resizable(False, False
#
# def get_NUM():
#     get_your_num = your_num.get()
#     if get_your_num:
#         list_c = ['green', '#35AC65', '#AA00AA', '#123456']
#         create_label = tk.Label(root, text=get_your_num, bg=random.choice(list_c))
#         create_label.grid(column=1, row=5, sticky='ne')
#
# def del_NUM():
#     your_num.delete(0, tk.END)
#
# user = tk.PhotoImage(file='user.png')
# root.iconphoto(False, user)
# root['bg'] = '#56AB98'
# tk.Label(root, text='Your_num',bg='#657814', font=('Arial', 12)).grid(row=0, column=0)
# your_num = tk.Entry(root)
# your_num.grid(row=0, column=1)
#
# tk.Button(text='Get', activebackground='#89AC04', command=get_NUM, font=('Arial', 12)).grid(row=1, column=0, sticky='we')
# tk.Button(text='Delate', activebackground='#1278AC', command=del_NUM, font=('Arial', 12)).grid(row=1, column=1, sticky='we')
# tk.Button(text='Qwerty', activebackground='#1FF189', command=lambda: your_num.insert(0, 'qwerty'), font=('Arial', 12)).grid(row=1, column=2, sticky='we')
#
#
# # root.minsize(height=290, width=250)
# # root.maxsize(height=460, width=560)
# root.mainloop()
# import random
# import tkinter as tk
#
# root = tk.Tk()
# root.geometry('380x220+400+108')
# photo = tk.PhotoImage(file='user.png')
# root.iconphoto(False, photo)
# root.title('Date of user')
#
#
#
#
# def send_data():
#     name_A = name_entry.get()
#     name_B = second_name_entry.get()
#     name_C = addres_entry.get()
#     name_D = city_entry.get()
#     name_E = country_entry.get()
#     name_F = postal_code_entry.get()
#
#
#     if name_A or name_B or name_C or name_D or name_D or name_E or name_F:
#         data_user_file = open('Data of user.txt', 'a')
#
#         data_user_file.write('-----------------' + '\n')
#         data_user_file.write('Name: ' + name_A + '\n')
#         data_user_file.write('Second name: ' + name_B + '\n')
#         data_user_file.write('Addres: ' + name_C + '\n')
#         data_user_file.write('City: ' + name_D + '\n')
#         data_user_file.write('Country: ' + name_E + '\n')
#         data_user_file.write('Postal code: ' + name_F + '\n')
#
#         data_user_file.close()
#     else:
#         print('Entry not found')
#
#
#
#
# name = tk.Label(text='Name:', font=14, fg='#FF4500', width=10)
# name.grid(row=0, column=0, sticky='e')
# name_entry = tk.Entry(root, width=35)
# name_entry.grid(row=0, column=1, sticky='we')
#
# second_name = tk.Label(text='Second name:', font=14, fg='#FF4500', width=10, padx= 5).grid(row=1, column=0, sticky='e')
# second_name_entry = tk.Entry(root, width=40)
# second_name_entry.grid(row=1, column=1, sticky='we')
#
# addres = tk.Label(text='Addres:', font=14, fg='#FF4500', width=10).grid(row=2, column=0, sticky='e')
# addres_entry = tk.Entry(root, width=40)
# addres_entry.grid(row=2, column=1, sticky='we')
#
# city = tk.Label(text='City:', font=14, fg='#FF4500', width=10).grid(row=3, column=0, sticky='e')
# city_entry = tk.Entry(root, width=40)
# city_entry.grid(row=3, column=1, sticky='we')
#
# country = tk.Label(text='Country:', font=14, fg='#FF4500', width=10).grid(row=4, column=0, sticky='e')
# country_entry = tk.Entry(root, width=40)
# country_entry.grid(row=4, column=1, sticky='we')
#
# postal_code = tk.Label(text='Postal code:', font=14, fg='#FF4500', width=10).grid(row=5, column=0, sticky='e')
# postal_code_entry = tk.Entry(root, width= 40)
# postal_code_entry.grid(row=5, column=1, sticky='we')
#
#
#
# Button_send = tk.Button(text='Send', font=14, bg='#7CFC00', command=send_data).grid(row=7, column=0)
#
# all_entry = [name_entry, second_name_entry, addres_entry, city_entry, country_entry, postal_code_entry]
#
# def clear_all():
#     i = 0
#     while i <= 5:
#         all_entry[i].delete(0, 'end')
#         i += 1
#
#
# Button_clear = tk.Button(text='Clear', font=16, bg='#DC143C', command=clear_all).grid(row=7, column=1)
#
# root.maxsize(390, 250)
# root.minsize(350, 200)
#
# root.mainloop()

# import tkinter as tk
#
# def random_drop():
#     random_num = random.randint(1, 6)
#
#     label_Number = tk.Label(text=random_num, font=25, fg='#00FA9A').grid(row=1, column=1, padx=30)
# root = tk.Tk()
# root.geometry('140x70+400+108')
# photo = tk.PhotoImage(file='instagram.png')
# root.iconphoto(False, photo)
# root.title('Cube')
#
# Button_DROP = tk.Button(text='Drop cube', font=20, command=random_drop, activebackground='#0000CD', activeforeground='#FF00FF').grid(padx=30, sticky='we', row=0, column=1)
# label_Number = tk.Label(text='*', font=20).grid(row=1, column=1, sticky='s')
#
# root.mainloop()

# import tkinter as tk
#
#
# def select():
#     for check in [test, over_year, rools]:
#         check.select()
#
#
# def deselect():
#     for check in [test, over_year, rools]:
#         check.deselect()
#
# def show_what():
#     print('Флажок тест', test_STR.get())
#
#
# root = tk.Tk()
#
# test_STR = tk.StringVar()
# test_STR.set('0')
# our_year_INT = tk.IntVar()
# root.geometry('380x220+400+108')
# photo = tk.PhotoImage(file='user.png')
# root.iconphoto(False, photo)
# root.title('Learn of user')
#
# test = tk.Checkbutton(root, text='TEST', variable=test_STR, offvalue=0, onvalue=1)
# test.pack()
# over_year = tk.Checkbutton(root, text='Тебе уде есть 18?', variable=our_year_INT)
# over_year.pack()
# rools = tk.Checkbutton(root, text='Правила знаешь?')
# rools.pack()
#
# tk.Button(root, text='select all', command=select).pack()
# tk.Button(root, text='deselect all', command=deselect).pack()
# tk.Button(root, text='show', command=show_what).pack()
#
# if test_STR.get() == 1:
#     tk.Label(root, font=15, foreground='#454565')
# else:
#     tk.Label(root, background='#AAAA43')
#
#
#
#
# root.minsize(height=300, width=190)
# root.maxsize(height=400, width=300)
# root.mainloop()

# import tkinter as tk
#
# def select_lvl():
#     lever_choise = lever.get()
#     #print(lever_choise)
#     user_choise = (f'Your choise {lever_choise} level')
#     lever_text.set(user_choise)
#     if lever_choise == 1:
#         print('Easy')
#     elif lever_choise == 2:
#         print('Middle')
#     else:
#         print('Hard')
#
# def select_age():
#     age_choise = age.get()
#     lever_text_age.set(f'Your choise {age_choise} years')
#     if age_choise == 4:
#         print('Your are tineger')
#     elif age_choise == 5:
#         print('Your are young')
#     elif age_choise == 6:
#         print('Your are old man')
#
# root = tk.Tk()
#
# root.geometry('380x220+400+108')
# photo = tk.PhotoImage(file='user.png')
# root.iconphoto(False, photo)
# root.title('Learn of user')
#
# lever = tk.IntVar()
# age = tk.IntVar()
# lever_text = tk.StringVar()
# lever_text_age = tk.StringVar()
#
# tk.Label(root, text='Choise level', bg='#AA34AA', font=15).pack(pady=4)
# tk.Radiobutton(text='Easy', variable=lever, value=1, command=select_lvl).pack()
# tk.Radiobutton(text='Middle', variable=lever, value=2, command=select_lvl).pack()
# tk.Radiobutton(text='Hard', variable=lever, value=3, command=select_lvl).pack(pady=5)
# tk.Label(root, textvariable=lever_text, bg='#BA0002', font=15).pack(pady=2)
#
# # new class
# tk.Label(root, text='Choise your age', bg='#AA34AA', font=15).pack(pady=8)
# tk.Radiobutton(text='10-18 years', variable=age, value=4, command=select_age).pack()
# tk.Radiobutton(text='19-40 years', variable=age, value=5, command=select_age).pack()
# tk.Radiobutton(text='41-65 years', variable=age, value=6, command=select_age).pack(pady=5)
# tk.Label(root, textvariable=lever_text_age, bg='#00AA45', font=15).pack()
#
# root.minsize(height=300, width=190)
# root.maxsize(height=400, width=300)
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
#
# names = ['Any name',"Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# root.geometry('380x220+400+108')
# photo = tk.PhotoImage(file='user.png')
# root.iconphoto(False, photo)
# root.title('Learn of user')
#
#
# BOX = ttk.Combobox(root,values=names)
# BOX.current(0)
# BOX.pack()
#
#
#
# root.minsize(height=300, width=190)
# root.maxsize(height=400, width=300)
# root.mainloop()

import pyautogui
import tkinter as tk


def make_new_window():
    root = tk.Tk()
    root.geometry('380x220+400+108')
    root.title('iHerb')

    def make_iHerb():
        Name_user = name.get()
        Password_of_user = password.get()

        pyautogui.click(91, 1055, duration=0.8)
        pyautogui.hotkey('ctrl', 't')

        pyautogui.write('iHerb.Ua', 0.8)
        pyautogui.hotkey("enter")
        pyautogui.sleep(6)
        pyautogui.click(1637, 222, duration=0.95)
        pyautogui.sleep(4)
        pyautogui.click(639, 476)
        pyautogui.write(Name_user)
        pyautogui.sleep(1)
        pyautogui.doubleClick(544, 597)
        pyautogui.write(Password_of_user)

    def make_OLX():
        number_user = number.get()
        Password_of_OLX = password_OLX.get()
        print(number_user, Password_of_OLX)

        pyautogui.click(91, 1055, duration=0.8)
        pyautogui.hotkey('ctrl', 't')

        pyautogui.write('iHerb.Ua', 0.8)
        pyautogui.hotkey("enter")
        pyautogui.sleep(6)
        pyautogui.click(1637, 222, duration=0.95)
        pyautogui.sleep(4)
        pyautogui.click(639, 476)
        pyautogui.write(Label_name)
        pyautogui.sleep(1)
        pyautogui.doubleClick(544, 597)
        pyautogui.write(Password_of_OLX)

    Label_name = tk.Label(root, text='Name:')
    Label_name.grid(row=0, column=0)
    Label_pass = tk.Label(root, text='Password:')
    Label_pass.grid(row=1, column=0)

    Label_number = tk.Label()

    name = tk.Entry(root, font=25)
    password = tk.Entry(root, font=25, show='*')

    number = tk.Entry(root, font=25)
    password_OLX = tk.Entry(root, font=25, show='*')

    password.grid(row=1, column=1)
    name.grid(row=0, column=1)

    Button_get = tk.Button(root, text='GET', command=make_iHerb).grid(row=2, column=2)

    root.mainloop()


win = tk.Tk()
win.geometry('600x220')
gif = tk.PhotoImage(file='../images/user.png')
win.iconphoto(False, gif)
win.title('Choice site:')

name_choize = tk.Label(win, text='What site will you want to vizit?', font=35, foreground='#0000CD').grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=50)

iHerb = tk.Button(win, command=make_new_window, text='iHerb, Put here-->', font=25, activebackground='#228B22')
oLX = tk.Button(win, text='OLX, Put here-->', font=25, activebackground='#00FFFF', command=ma)
iHerb.grid(row=1, column=0)
oLX.grid(row=2, column=0)

win.mainloop()
