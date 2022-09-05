import os
import time
import tkinter as tk

banner = """
 ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗
██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║
██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║
╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝  Programming Language
"""

print(banner)

print("Welcome To Ground Programming Language!")

print("""
Run Ground File - run
Create Ground File - create      
""")
selectground = input("---> ")

if selectground == "create":
    filenameforgnd = input("File Name ---> ")
    with open(filenameforgnd + ".gnd", "w") as file:
        file.write("gndstart\n\n\n\ngndend")
    print("Your File was Created Successfully", " File --->",filenameforgnd,".gnd") 
    time.sleep(9999)
if selectground == "run":
    filenamegnd = input("File Name ---> ")
    try:
        with open(filenamegnd + ".gnd") as filegnd1:
            pass
    except:
        print("There is no such file!")
        filenamegnd = input("File Name ---> ")
    
    with open(filenamegnd + ".gnd") as filegnd2:
        print("Your File is Running...\n---------------------------")
        read = filegnd2.readlines()
        i = 0
        ifmain = False
        while True:
            try:
                rood = read[i]
                if rood == "gndstart\n":
                    ifmain = True
                if rood == "gndend\n":
                    break
                
                
                if "printg() = " in rood and ifmain == True:
                        rood = rood.replace("printg() = ","")
                        rood = rood.replace("\n","")
                        print(rood)
                        time.sleep(9999)
                        
                if "pug() = " in rood and ifmain == True:
                        rood = rood.replace("pug() = ","")
                        rood = rood.replace("\n","")
                        popupground = tk.Tk()
                        popupground.title(rood)
                        popupground.mainloop()
                        
                if "gndclose()" in rood:
                    break
                if "errorg()" in rood and ifmain == True:
                    print("Error!!!")
                    time.sleep(9999)
                if "groundnormalpopup()" in rood and ifmain == True:
                    groundnormalpopup = tk.Tk()
                    groundnormalpopup.title("Ground")
                    groundnormalpopup.geometry("500x500")
                    groundnormalpopup.mainloop()
                if "depositg(a) = " in rood and ifmain == True:
                    rood = rood.replace("depositg(a) = ","")
                    rood = rood.replace("\n","")
                    depositga = rood
                if "depositg(b) = " in rood and ifmain == True:
                    rood = rood.replace("depositg(b) = ","")
                    rood = rood.replace("\n","")
                    depositgb = rood
                if "depositg(c) = " in rood and ifmain == True:
                    rood = rood.replace("depositg(c) = ","")
                    rood = rood.replace("\n","")
                    depositgc = rood
                if "depositg(d) = " in rood and ifmain == True:
                    rood = rood.replace("depositg(d) = ","")
                    rood = rood.replace("\n","")
                    depositgd = rood
                if "depositg(e) = " in rood and ifmain == True:
                    rood = rood.replace("depositg(e) = ","")
                    rood = rood.replace("\n","")
                    depositge = rood
                if "printg(depositg(a))" in rood and ifmain == True:
                    print(depositga)
                    time.sleep(9999)
                if "printg(depositg(b))" in rood and ifmain == True:
                    print(depositgb)
                    time.sleep(9999)
                if "printg(depositg(c))" in rood and ifmain == True:
                    print(depositgc)
                    time.sleep(9999)
                if "printg(depositg(d))" in rood and ifmain == True:
                    print(depositgd)
                    time.sleep(9999)
                if "printg(depositg(e))" in rood and ifmain == True:
                    print(depositge)
                    time.sleep(9999)
                if "pingg() = " in rood and ifmain == True:
                    rood = rood.replace("pingg() = ","")
                    rood = rood.replace("\n","")
                    os.system("ping " + rood)
                    time.sleep(9999)
                if "pingg(depositg(a))" in rood and ifmain == True:
                    os.system("ping " + depositga)
                    time.sleep(9999)
                if "pingg(depositg(b))" in rood and ifmain == True:
                    os.system("ping " + depositgb)
                    time.sleep(9999)
                if "pingg(depositg(c))" in rood and ifmain == True:
                    os.system("ping " + depositgc)
                    time.sleep(9999)
                if "pingg(depositg(d))" in rood and ifmain == True:
                    os.system("ping " + depositgd)
                    time.sleep(9999)
                if "pingg(depositg(e))" in rood and ifmain == True:
                    os.system("ping " + depositge)
                    time.sleep(9999)
                i += 1
            except:
                break       