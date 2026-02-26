from psutil import *
from guizero import *

def killProcess(txtBox):
    p = txtBox.value
    p = Process(int(p))
    p.kill()
    
#     try:
#         p = txtBox.selected
#         p = Process(int(result))
#         p.kill()
#     except:
#         app.error("Error!","Invalid PID identified for process elimination.")
    
def refresh(txtBox):
    global processList
    processList = []
    processes = pids()
    for process in processes:
        processList.append(process)
        processList.append(str(Process(process))[14:])  
    for item in txtBox.items:
        txtBox.remove(item)
    for item in processList:
        txtBox.append(item)

def closeApp():
    app.destroy()

app = App()
processList = []
processes = pids()
for process in processes:
    processList.append(process)
    processList.append(str(Process(process))[14:])  

txtBox = ListBox(app, scrollbar = True, items = processList, width = "fill", height = "fill")
#txtBox.repeat(10000, lambda:refresh(txtBox))

sortBox = Box(app, width = "fill")
killbtn = PushButton(sortBox, align = "left", text="Kill Process", height = 1, width = "fill", command=lambda:killProcess(txtBox))
closeBtn = PushButton(sortBox, align = "left", text="Close App", height = 1, width = "fill", command = closeApp)

app.display()