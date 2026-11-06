from tkinter import *
from speedtest import Speedtest

root = Tk()
root.title('MY_Speed_test')
root.geometry('300x420')
root['bg'] = '#6495ED'
root.resizable(False, False)

def test_speed():
    dowload = Speedtest().download()
    upload = Speedtest().upload()
    dowload_speed = round(dowload/(10**6), 2)
    upload_speed = round(upload / (10 ** 6), 2)

    dowloaad_input.config(text='Speed of dowload: \n' + str(dowload_speed) + 'MbPs')
    dowloaad_output.config(text='Speed of upload: \n'+ str(upload_speed) + 'MbPs')

button = Button(root, text='Click to start', font=('Arial', 15), command=test_speed, background='#00FF00')
button.pack(side=BOTTOM, pady= 10)

dowloaad_input = Label(root, text='Speed of dowload: \n-', font=('Arial', '15'), bg='#4169E1')
dowloaad_input.pack(pady=(20, 0))


dowloaad_output = Label(root, text='Speed of upload: \n-', font=('Arial, 15'), bg='#4169E1')
dowloaad_output.pack(pady=(20, 0))



root.mainloop()