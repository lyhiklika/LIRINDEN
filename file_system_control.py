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


