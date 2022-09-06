from tkinter import *
from tkinter import ttk
import vk_api

vk_session = vk_api.VkApi(vk_login, vk_password)
vk_session.auth()

vk = vk_session.get_api()


root = Tk()
root.title('vk.com scripts')
root.geometry('500x300')

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text='Программа пока ничего не делает. Но можно нажать кнопку и выйти.').grid(column=0, row=0)
ttk.Button(frm, text='Выход', command=root.destroy).grid(column=0, row=1)

root.mainloop()
