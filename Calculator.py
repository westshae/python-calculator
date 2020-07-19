from tkinter import*

window = Tk()
window.title("Calculator")
operation = ""
inputField = StringVar()

# Config
fontInfo = ["arial", 18, "bold"]
backgroundColour = "#c7c7c7"
buttonColour = "#323333"
defaultScreenSize = "400x600"
buttonToCreate = ["1","2","3","4","5","6", "7", "8", "9", "0", "+", "-", "*", "/", "=", "CLR"]


screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()


window.geometry(defaultScreenSize)
displayWindow = Entry(window, font=fontInfo, textvariable=inputField, bg=backgroundColour, justify="right", width=screenWidth).grid()

def createButton(textDisplay, rowLocation, columnLocation):
    Button(window, padx=14, fg=buttonColour, font=fontInfo, text=textDisplay).grid(row=rowLocation, column=columnLocation)

for i in range(buttonToCreate.count):
    print(i)
    


window.mainloop()

# cal = Tk()
# cal.title("Calculator")
# operation=""
# inputField = StringVar()

# textDisplay = Entry(cal, font=("arial", 18, "bold"), textvariable=inputField, insertwidth=5, bg="#c7c7c7", justify="right").grid(columnspan=5)

# button1 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="1").grid(row=1,column=1)
# button2 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="2").grid(row=1, column=2)
# button3 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="3").grid(row=1, column=3)
# button4 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="4").grid(row=1, column=4)
# button5 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="5").grid(row=2, column=1)
# button6 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="6").grid(row=2, column=2)
# button7 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="7").grid(row=2, column=3)
# button5 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="8").grid(row=2, column=4)
# button5 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="9").grid(row=3, column=1)
# button5 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="0").grid(row=3, column=2)
# button5 = Button(cal, padx=14, fg="black", font=("arial", 18, "bold"), text="+").grid(row=3, column=3)

# cal.mainloop()
