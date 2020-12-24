import tkinter
import datetime
import file_system
from tkinter import ttk


def spisok():
    load = file_system.logs()
    try:
        timestart=datetime.datetime(int(ys.get()),int(ms.get()),int(ds.get()),int(ts.get()[:2]),int(ts.get()[3:]))
        timeend=datetime.datetime(int(ye.get()),int(me.get()),int(de.get()),int(te.get()[:2]),int(te.get()[3:]))
    except :
        try:
            timestart=datetime.datetime(int(ys.get()),int(ms.get()),int(ds.get()))
            timeend=datetime.datetime(int(ye.get()),int(me.get()),int(de.get()))
        except:
            timestart=datetime.datetime(2000,1,1)
            timeend=datetime.datetime(9999,1,1)
    if load:
        text.delete(1.0, 'end')
        for elem in load:
            if timestart <= elem.time <= timeend:
                if name_file.get():
                    if name_file.get() == elem.src_path[elem.last + 1:]:
                        text.insert('end','Time: ' + str(elem.time.strftime("%d-%m-%Y %H:%M")) + ' File: ' + elem.src_path[elem.last + 1:] +' File_action: '+ elem.event_type + '\n')
                else:
                    text.insert('end','Time: ' + str(elem.time.strftime("%d-%m-%Y %H:%M")) + ' File: ' + elem.src_path[elem.last + 1:] +' File_action: '+ elem.event_type + '\n')
            
       
def start():
    file_system.start()
    l1.config(bd = 20, bg = '#00ff00', text = 'Логи записываются! :)')

def stop():
    file_system.stop()
    l1.config(bd = 20, bg = '#ff0000',text = 'Логи не записываются! :(')

def exxit():
    top.destroy()

top=tkinter.Tk()
top.title('File_Control')
top.geometry('1100x370')

startButton = tkinter.Button(top, height = 2, width = 20,text ="Начать запись.", command = start)
startButton.grid(row = 1, column = 0)

stopButton = tkinter.Button(top, height = 2, width = 20,text ="Остановить запись.", command = stop)
stopButton.grid(row = 2, column = 0)

stopButton = tkinter.Button(top, height = 2, width = 20,text ="Просмотр логов.", command = spisok)
stopButton.grid(row = 3, column = 0)

exitButton = tkinter.Button(top, height = 2, width = 20,text ="Выход?", command = exxit)
exitButton.grid(row = 4, column = 0)

text = tkinter.Text(width=100, height = 20)
text.grid(row = 0, column = 6, rowspan = 10, columnspan = 5)

l1 = tkinter.Label(top, text = 'Логи не записываются :(')
l1.grid(row=0, column = 0)
l1.config(bd = 20, bg = '#ff0000')

l2 = tkinter.Label(top, text = 'Выберите время начала и конца логов:')
l2.grid(row=0, column = 1,columnspan = 5)

ld = tkinter.Label(top, text = 'День:')
ld.grid(row=1, column = 2)
lm = tkinter.Label(top, text = 'Месяц:')
lm.grid(row=1, column = 3)
ly = tkinter.Label(top, text = 'Год:')
ly.grid(row=1, column = 4)
ly = tkinter.Label(top, text = 'Время(hh:mm):')
ly.grid(row=1, column = 5)

lm = tkinter.Label(top, text = 'Начало:')
lm.grid(row=2, column = 1)
ly = tkinter.Label(top, text = 'Конец:')
ly.grid(row=3, column = 1)
ln = tkinter.Label(top, text = 'Название файла:')
ln.grid(row=4,column=1,columnspan=2)

ds = ttk.Combobox(top,height = 2, width = 3, values=['01','02','03','04','05','06','07','08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
ds.grid(row=2,column=2)
ms = ttk.Combobox(top,height = 2, width = 3, values=[1,2,3,4,5,6,7,8,9,10,11,12])
ms.grid(row=2,column=3)
ys = ttk.Combobox(top,height = 2, width = 5, values=[2020,2021,2022,2023,2024])
ys.grid(row=2,column=4)
ts = tkinter.Entry(top,width = 6,bd=2)
ts.grid(row=2,column=5)

de = ttk.Combobox(top,height = 2, width = 3, values=['01','02','03','04','05','06','07','08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
de.grid(row=3,column=2)
me = ttk.Combobox(top,height = 2, width = 3, values=[1,2,3,4,5,6,7,8,9,10,11,12])
me.grid(row=3,column=3)
ye = ttk.Combobox(top,height = 2, width = 5, values=[2020,2021,2022,2023,2024])
ye.grid(row=3,column=4)
te = tkinter.Entry(top,width = 6,bd=2)
te.grid(row=3,column=5)

name_file = tkinter.Entry(top,width = 10,bd=2)
name_file.grid(row=4,column=3,columnspan=2)

top.mainloop()
