from tkinter import *

class Calculator:
    def __init__(self):
        #Configuration
        self.buttonColour = "#323333"
        self.defaultScreenSize = "400x509"
        self.backgroundColour = "#323333"
        self.activeBackgroundColour="#666666"
        self.fontInfo = ["arial", 18,"bold"]
        self.fontColour = "#c9c9c9"

        #Creates window with basic information.
        self.root = Tk()
        self.root.title("L3 DIT Calculator - Shae West")
        self.root.geometry(self.defaultScreenSize)
        self.root.resizable(width=False, height=False)
        self.app = Frame(self.root, bg=self.backgroundColour)
        self.operation=""

        #Creates the input field string var and sets it to the text
        self.inputField = StringVar()
        self.inputField.set("Please press CLS to start")

        #Creates display window for calculator
        self.entry = Entry(self.app,validate="key",font=self.fontInfo,textvariable=self.inputField, bg="gray" , width=29, bd=4, justify="center")
        self.entry.grid(row=0, column=0, columnspan=6, ipady=10, pady=5, padx=4)

        def keyPress(event):
            self.operationList = ["1","2","3","4","5","6","7","8","9","0","+","-", "/", "*"]
            if(event.char in self.operationList):
                self.operation = self.operation + event.char
            elif(event.char == "="):
                answer(self)
            elif(event.keysym == "Return"):
                answer(self)

        self.entry.bind("<Key>", keyPress)

        #Creating buttons
        def createButton(self, textDisplay, rowLocation, columnLocation, command):
            self.button=Button(self.app,padx=14,pady=14, bd=4, bg=self.buttonColour, command=command,text=textDisplay, font=self.fontInfo, width=4, height=2, activebackground=self.activeBackgroundColour)
            self.button.grid(row=rowLocation, column=columnLocation)

        #Adds specified text to the operation variable
        def addToOperation(self, toAdd):
            self.operation = self.operation + toAdd
            self.inputField.set(self.operation)

        #Calculates the answer and sets the input fieldn and operation string
        def answer(self):
            self.answer = eval(self.operation)
            self.inputField.set(self.answer)
            self.operation = str(self.answer)
        
        #Clears the input field, operation string and answer string
        def clear(self):
            self.inputField.set("")
            self.operation = ("")
            self.answer = ("")

        #Creates number buttons
        createButton(self, "1", 1,0, lambda: addToOperation(self, "1"))
        createButton(self, "2", 1,1, lambda: addToOperation(self, "2"))
        createButton(self, "3", 1,2, lambda: addToOperation(self, "3"))
        createButton(self, "4", 2,0, lambda: addToOperation(self, "4"))
        createButton(self, "5", 2,1, lambda: addToOperation(self, "5"))
        createButton(self, "6", 2,2, lambda: addToOperation(self, "6"))
        createButton(self, "7", 3,0, lambda: addToOperation(self, "7"))
        createButton(self, "8", 3,1, lambda: addToOperation(self, "8"))
        createButton(self, "9", 3,2, lambda: addToOperation(self, "9"))
        createButton(self, "0", 4,0, lambda: addToOperation(self, "0"))

        #Creates operation buttons
        createButton(self, "+", 1,3, lambda: addToOperation(self, "+"))
        createButton(self, "-", 2,3, lambda: addToOperation(self, "-"))
        createButton(self, "*", 3,3, lambda: addToOperation(self, "*"))
        createButton(self, "/", 4,3, lambda: addToOperation(self, "/"))
        createButton(self, "=", 4, 2, lambda: answer(self))
        createButton(self, "CLR", 4,1, lambda: clear(self))
        

        #Packs the app
        self.app.pack()

        #Runs the mainloop
        self.root.mainloop()

        

#Ensures that the file run is the main file.
if __name__ == "__main__":
    #Runs the calculator class
    Calculator()
