import webbrowser
import customtkinter
from subprocess import Popen
from detector import detector
from startwindo import createstartwindow
from weaponDetect import weapondetecter
#Creating
def gui_s() :
    Popen(['python', 'app.py'])
    def creat_s():
        # root.destroy()
        createstartwindow()
        # gui_s()
    def detect_face():
        root.destroy()
        detector()
        gui_s()
    def detect_weapon():
        root.destroy()
        weapondetecter()
        gui_s()
    def url():
        url = "http://127.0.0.1:5000"
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(
            "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
        webbrowser.get('edge').open(url)

    root = customtkinter.CTk()
    root.geometry("850x600")
    root.title("UDJAT")
    customtkinter.set_appearance_mode("dark")



    #For checking
    def login():
        print("TEst0")

    #Themes funs
    def light():
        customtkinter.set_appearance_mode("light")
    def dark():
        customtkinter.set_appearance_mode("dark")

    #Locations of buttons
    frame1 = customtkinter.CTkFrame(master=root,fg_color="transparent", width=50, height=50)
    frame1.pack(pady= 10, padx=20)
    frame2=customtkinter.CTkFrame(master=root, width=400)
    frame2.pack(pady= 10, padx=20)
    frame3 = customtkinter.CTkFrame(master=root, width=400)
    frame3.pack(pady= 10, padx=20 )
    frame4 = customtkinter.CTkFrame(master=root,fg_color="transparent", width=300)
    frame4.pack(pady= 10, padx=70, side= "left" )
    frame5 = customtkinter.CTkFrame(master=root,fg_color="transparent", width=300)
    frame5.pack(pady= 10, padx=70, side= "right"  )
    frameT= customtkinter.CTkFrame(master=root,fg_color="transparent")
    frameT.pack(pady=20, padx=20 )


    #UDJAT name
    label1 = customtkinter.CTkLabel(master=frame1, text="UDJAT", font=("Arial",60))
    label1.pack(pady = 1, padx=  10)
    label2 = customtkinter.CTkLabel(master=frame1, text="The Eye Always Watch")
    label2.pack(pady = 0, padx= 10)

    #Main functions
    label3 = customtkinter.CTkLabel(master=frame2, text="Main Functions", font=("Arial",15))
    label3.pack(pady = 12, padx=  10)
    btn1 = customtkinter.CTkButton(master=frame2, text="Create", font=("Arial",20), width=200, height=50,  command =creat_s ) #Create
    btn1.pack(pady = 12, padx = 10)
    btn2 = customtkinter.CTkButton(master=frame2, text="Live Detect", font=("Arial",20),width=200, height=50, command =login) #Detect
    btn2.pack(pady = 12, padx = 10)

    #Additonal functions
    label4 = customtkinter.CTkLabel(master=frame3, text="Additional Functions", font=("Arial",15))
    label4.pack(pady = 12, padx=  10)
    btn3 = customtkinter.CTkButton(master=frame3, text="Live Face Detect",font=("Arial",20), width=200, height=50, command =detect_face ) #Face Recognize
    btn3.pack(pady = 12, padx = 10 ,side="left")
    btn4 = customtkinter.CTkButton(master=frame3, text="Track Person",font=("Arial",20), width=200, height=50, command =login ) #Tracking
    btn4.pack(pady = 12, padx = 10, side="right")
    btn3 = customtkinter.CTkButton(master=frame3, text="Live Waepon Detect",font=("Arial",20), width=200, height=50, command =detect_weapon ) #Weapon Detection
    btn3.pack(pady = 12, padx = 10)

    #Left button web
    btn6 = customtkinter.CTkButton(master=frame4, text="Open Wepsite" ,font=("Arial",20),width=200, height=50,  command =url ) #Website
    btn6.pack(pady = 12, padx = 10)

    #Right button exit
    btn7 = customtkinter.CTkButton(master=frame5, text="Exit" ,font=("Arial",20),width=200, height=50,  command =root.destroy )
    btn7.pack(pady = 12, padx = 10)

    #Themes
    sv1 = customtkinter.StringVar(value="off")
    switch1 = customtkinter.CTkSwitch(frameT, text="Light", command=light, variable=sv1, onvalue="on", offvalue="off")
    switch1.pack()
    sv2 = customtkinter.StringVar(value="on")
    switch2 = customtkinter.CTkSwitch(frameT, text="Dark", command=dark, variable=sv2, onvalue="on", offvalue="off")
    switch2.pack()

    #Run
    root.mainloop()
gui_s()