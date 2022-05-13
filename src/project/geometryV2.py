import math
import tkinter as tk
# from PIL import ImageTk, Image

# koordinat tengah x = 350, y = 200

def regtxt():
    global playerName, playerNoReg, playerAge, playerAddress, namefile
    playerName = str(player_Name.get())
    playerNoReg = str(player_NoReg.get())
    playerAge = str(player_Age.get())
    playerAddress = str(player_Address.get())
    
    namefile = playerName + playerNoReg
    playerFile = open(namefile + ".txt", "a+")
    playerFile.write("="*5 + "Players" + "="*5 + "\nname: " + playerName +"\nNo Registration: " + playerNoReg + "\nAge: " + playerAge + "\nAddress: " + playerAddress + "\n")

def updatePoint():
    global res
    res = res + 1

def updateFile():
    newPoin = open(namefile + ".txt", "a+")
    newPoin.write("Your point is: " + str(res) + "\n")
    newPoin.close()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        labelMain = tk.Label(self, text="Main Menu",font=("helvetica",25))
        buttonCalc = tk.Button(self, text="Calculator",width=20,height=4,font=("helvetica",15), command=lambda: controller.show_frame(Calculator))
        buttonFormula = tk.Button(self, text="Formula",width=20,height=4,font=("helvetica",15), command=lambda: controller.show_frame(Formula))
        buttonGames = tk.Button(self, text="Games",width=20,height=4,font=("helvetica",15), command=lambda: controller.show_frame(Registration))
        buttonExit = tk.Button(self, text="Exit",width=20,height=4,font=("helvetica",15), command=self.quit)
        labelMain.pack()
        buttonCalc.pack()
        buttonFormula.pack()
        buttonGames.pack()
        buttonExit.pack()

class Square(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var = float(side.get())
                result1 = var * var
                result2 = var * 4
                resArea.config(text=result1)
                resCircum.config(text=result2)
            except Exception as err: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resArea.config(text="")
                resCircum.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelSquare = tk.Label(self, text="Square Calculator", font=("helvetica",25))
        labelSide = tk.Label(self, text="Input Side legth      :", font=("helvetica",15))
        side = tk.Entry(self,font=("helvetica",15))
        labelArea = tk.Label(self, text="Area                      :", font=("helvetica",15))
        labelCircum = tk.Label(self, text="Circumfence leghth :", font=("helvetica",15))
        resArea = tk.Label(self,font=("helvetica",15))
        resCircum = tk.Label(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Tabs2dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",12), command=calculate)

        labelSquare.pack()
        labelSide.place(x=200, y=37)
        side.place(x=382, y=39)
        labelArea.place(x=200, y=70)
        labelCircum.place(x=200, y=100)
        
        resArea.place(x=382, y=70)
        resCircum.place(x=381,y=100)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=165)
        buttonBack.place(x=325,y=400)

class Rectangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try: # run the code
                var1 = float(length.get())
                var2 = float(width.get())
                result1 = var1 * var2
                result2 = 2*(var1+var2)
                resArea.config(text=result1)
                resCircum.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resArea.config(text="")
                resCircum.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelRectangle = tk.Label(self,text="Rectangle calculator", font=("helvetica",25))
        labelLength = tk.Label(self, text="Input Side length    :", font=("helvetica",15))
        labelWidth = tk.Label(self, text="Input Side width     :", font=("helvetica",15))
        length = tk.Entry(self,font=("helvetica",15))
        width = tk.Entry(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        labelArea = tk.Label(self, text="Area                      :", font=("helvetica",15))
        labelCircum = tk.Label(self, text="Circumfence leghth :", font=("helvetica",15))
        resArea = tk.Label(self, font=("helvetica",15))
        resCircum = tk.Label(self, font=("helvetica",15))
        
        buttonBack = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, command=lambda: controller.show_frame(Tabs2dimension), font=("helvetica",12))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, command=calculate, font=("helvetica",12))

        labelRectangle.pack()
        labelLength.place(x=200, y=40)
        labelWidth.place(x=200, y=70)
        length.place(x=382, y=42)
        width.place(x=382, y=72)
        labelArea.place(x=200, y=100)
        labelCircum.place(x=200, y=125)
        
        resArea.place(x=382, y=100)
        resCircum.place(x=381,y=125)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=165)
        buttonBack.place(x=325,y=400)

class Triangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var1  = float(base.get())
                var2 = float(height.get())
                result1 = (var1 * var2)/2
                result2 = math.sqrt(var1 ** 2 + var2 ** 2) + var1 + var2
                resArea.config(text=result1)
                resCircum.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resArea.config(text="")
                resCircum.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")


        labelTriangle = tk.Label(self, text="Triangle calculator", font=("helvetica",25))
        labelBased = tk.Label(self, text="Input Base            :", font=("helvetica", 15))
        labelheight = tk.Label(self, text="Input Height           :",font=("helvetica", 15))
        base = tk.Entry(self,font=("helvetica", 15))
        height = tk.Entry(self,font=("helvetica", 15))
        labelError = tk.Label(self, font=("helvetica",15))

        labelArea = tk.Label(self, text="Area                     :",font=("helvetica", 15))
        labelCircum = tk.Label(self, text="Circumfence leghth :", font=("helvetica", 15))
        resArea = tk.Label(self, font=("helvetica",15))
        resCircum = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, command=lambda: controller.show_frame(Tabs2dimension), font=("helvetica",12))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, command=calculate, font=("helvetica",12))

        labelTriangle.pack()
        labelBased.place(x=220,y=45)
        labelheight.place(x=220,y=85)
        base.place(x=400,y=44)
        height.place(x=400,y=86)
        labelArea.place(x=220,y=120)
        labelCircum.place(x=220,y=150)

        resArea.place(x=400, y=120)
        resCircum.place(x=400,y=150)
        
        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=200)
        buttonBack.place(x=325,y=400)

class Circle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var = float(radius.get())
                result1 = 22/7 * var  * var
                result2 = 2 * 22/7 * var
                resArea.config(text=result1)
                resCircum.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resArea.config(text="")
                resCircum.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")


        labelCircle = tk.Label(self, text="Circle calculator", font=("helvetica",25))
        labelRadius = tk.Label(self, text="Input Radius: ", font=("helvetica", 15))
        radius = tk.Entry(self, font=("helvetica", 15))
        labelError = tk.Label(self, font=("helvetica",15))

        labelArea = tk.Label(self, text="Area: ", font=("helvetica", 15))
        labelCircum = tk.Label(self, text="Circumfence length: ", font=("helvetica",15))
        resArea = tk.Label(self, font=("helvetica",15))
        resCircum = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, command=lambda: controller.show_frame(Tabs2dimension), font=("helvetica",12))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, command=calculate, font=("helvetica",12))

        labelCircle.pack()
        labelRadius.place(x=220,y=45)
        radius.place(x=400,y=45)
        labelArea.place(x=220,y=70)
        labelCircum.place(x=220,y=100)

        resArea.place(x=400, y=70)
        resCircum.place(x=400,y=100)

        labelError.place(x=315,y=300)
        
        buttonRes.place(x=325, y=200)
        buttonBack.place(x=325,y=400) 

class Rhombus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var1 = float(diagonal1.get())
                var2 = float(diagonal2.get())
                var3 = float(side.get())
                result1 = var1 * var2 * 0.5
                result2 = 4 * var3
                resArea.config(text=result1)
                resCircum.config(text=result2)
            except:
                labelError.config(text="Something went wrong",fg="red")
                resArea.config(text="")
                resCircum.config(text="")
            else:
                labelError.config(text="")

        labelRhombus = tk.Label(self, text="Rhombus Calculator", font=("helvetica", 25))
        labelDiagonal1 = tk.Label(self, text="Input Diagonal 1: ", font=("helvetica", 15))
        labelDiagonal2 = tk.Label(self, text="Input Diagonal 2: ", font=("helvetica", 15))
        labelSide = tk.Label(self, text="Input Side: ", font=("helvetica", 15))
        diagonal1 = tk.Entry(self, font=("helvetica", 15))
        diagonal2 = tk.Entry(self, font=("helvetica", 15))
        side = tk.Entry(self, font=("helvetica", 15))
        labelError = tk.Label(self, font=("helvetica",15))

        labelArea = tk.Label(self, text="Area: ", font=("helvetica", 15))
        labelCircum = tk.Label(self, text="Circumfence length: ", font=("helvetica",15))
        resArea = tk.Label(self, font=("helvetica",15))
        resCircum = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, command=lambda: controller.show_frame(Tabs2dimension), font=("helvetica",12))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, command=calculate, font=("helvetica",12))

        labelRhombus.pack()
        labelDiagonal1.place(x=220,y=45)
        labelDiagonal2.place(x=220,y=80)
        labelSide.place(x=220,y=115)
        diagonal1.place(x=405,y=45)
        diagonal2.place(x=405,y=80)
        side.place(x=405,y=115)
        labelArea.place(x=220,y=150)
        labelCircum.place(x=220,y=185)

        resArea.place(x=405, y=150)
        resCircum.place(x=405,y=185)
        
        labelError.place(x=315,y=350)

        buttonRes.place(x=325, y=250)
        buttonBack.place(x=325,y=400)

class Cube(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var = float(side.get())
                result1 = var * var * var
                result2 = 6 * var**2
                resVolume.config(text=result1)
                resSurface.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resVolume.config(text="")
                resSurface.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelCube = tk.Label(self, text="Cube Calculator", font=("helvetica",25))
        labelSide = tk.Label(self, text="Input Side length      ", font=("helvetica",15))
        side = tk.Entry(self,font=("helvetica",15))
        labelVolume = tk.Label(self, text="Volume                 :", font=("helvetica",15))
        labelSurface = tk.Label(self, text="Surface Area        :", font=("helvetica",15))
        resVolume = tk.Label(self,font=("helvetica",15))
        resSurface = tk.Label(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 3 dimension page",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Tabs3dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",12),command=calculate)

        labelCube.pack()
        labelSide.place(x=200, y=37)
        side.place(x=382, y=39)
        labelVolume.place(x=200, y=70)
        labelSurface.place(x=200, y=100)
        
        resVolume.place(x=382, y=70)
        resSurface.place(x=381,y=100)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=165)
        buttonBack.place(x=325,y=400)
    
class Cuboids(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var1 = float(length.get())
                var2 = float(width.get())
                var3 = float(height.get())
                result1 = var1 * var2 * var3
                result2 = 2*((var1*var2)+(var1*var3)+(var2*var3))
                resVolume.config(text=result1)
                resSurface.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resVolume.config(text="")
                resSurface.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelCube = tk.Label(self, text="Cuboids Calculator", font=("helvetica",25))
        labelLength = tk.Label(self, text="Input Length      ", font=("helvetica",15))
        labelWidth = tk.Label(self, text="Input Width      ", font=("helvetica",15))
        labelHeight = tk.Label(self, text="Input Height      ", font=("helvetica",15))
        length = tk.Entry(self,font=("helvetica",15))
        width = tk.Entry(self,font=("helvetica",15))
        height = tk.Entry(self,font=("helvetica",15))
        labelVolume = tk.Label(self, text="Volume                 :", font=("helvetica",15))
        labelSurface = tk.Label(self, text="Surface Area        :", font=("helvetica",15))
        resVolume = tk.Label(self,font=("helvetica",15))
        resSurface = tk.Label(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 3 dimension page",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Tabs3dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",12),command=calculate)

        labelCube.pack()
        labelLength.place(x=200, y=37)
        labelWidth.place(x=200, y=65)
        labelHeight.place(x=200, y=93)
        length.place(x=382, y=37)
        width.place(x=382, y=65)
        height.place(x=382, y=93)
        labelVolume.place(x=200, y=121)
        labelSurface.place(x=200, y=149)
        
        resVolume.place(x=382, y=121)
        resSurface.place(x=381,y=149)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=180)
        buttonBack.place(x=325,y=400)

class Ball(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var = float(radius.get())
                result1 = 4 * (22/7 * var**3)/3
                result2 = 4 * 22/7 * var**2
                resVolume.config(text=result1)
                resSurface.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resVolume.config(text="")
                resSurface.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelBall = tk.Label(self, text="Ball Calculator", font=("helvetica",25))
        labelRadius = tk.Label(self, text="Input Radius length      ", font=("helvetica",15))
        radius = tk.Entry(self,font=("helvetica",15))
        labelVolume = tk.Label(self, text="Volume                 :", font=("helvetica",15))
        labelSurface = tk.Label(self, text="Surface Area        :", font=("helvetica",15))
        resVolume = tk.Label(self,font=("helvetica",15))
        resSurface = tk.Label(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 3 dimension page",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Tabs3dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",12),command=calculate)

        labelBall.pack()
        labelRadius.place(x=200, y=37)
        radius.place(x=382, y=39)
        labelVolume.place(x=200, y=70)
        labelSurface.place(x=200, y=100)
        
        resVolume.place(x=382, y=70)
        resSurface.place(x=381,y=100)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=165)
        buttonBack.place(x=325,y=400)

class Cone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var1 = float(radius.get())
                var2 = float(height.get())
                result1 = ((22/7 * var1**2)*var2)/3
                hypotenusa = math.sqrt(var1**2 + var2**2)
                result2 = (22/7 * var1)*(var1+hypotenusa)
                resVolume.config(text=result1)
                resSurface.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resVolume.config(text="")
                resSurface.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelBall = tk.Label(self, text="Cone Calculator", font=("helvetica",25))
        labelRadius = tk.Label(self, text="Input Radius", font=("helvetica",15))
        labelHeight = tk.Label(self, text="Input Height", font=("helvetica",15))
        radius = tk.Entry(self,font=("helvetica",15))
        height = tk.Entry(self,font=("helvetica",15))
        labelVolume = tk.Label(self, text="Volume                 :", font=("helvetica",15))
        labelSurface = tk.Label(self, text="Surface Area        :", font=("helvetica",15))
        resVolume = tk.Label(self,font=("helvetica",15))
        resSurface = tk.Label(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 3 dimension page",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Tabs3dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",12),command=calculate)

        labelBall.pack()
        labelRadius.place(x=200, y=37)
        labelHeight.place(x=200, y=65)
        radius.place(x=382, y=37)
        height.place(x=382, y=65)
        labelVolume.place(x=200, y=93)
        labelSurface.place(x=200, y=121)
        
        resVolume.place(x=382, y=93)
        resSurface.place(x=381,y=121)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=165)
        buttonBack.place(x=325,y=400)

class Pyramids(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            try:
                var1 = float(side.get())
                var2 = float(height.get())
                result1 = 1/3 * var1**2 * var2
                slant = math.sqrt((var1**2)/4 + (var2**2))
                result2 = var1**2 + 4*(0.5 * var1 * slant)
                resVolume.config(text=result1)
                resSurface.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="Something went wrong",fg="red")
                resVolume.config(text="")
                resSurface.config(text="")
            else: # if the code above not error then run else:
                labelError.config(text="")

        labelPyramids = tk.Label(self, text="Pyramids Calculator", font=("helvetica",25))
        labelSide = tk.Label(self, text="Input Side", font=("helvetica",15))
        labelHeight = tk.Label(self, text="Input Height", font=("helvetica",15))
        side = tk.Entry(self,font=("helvetica",15))
        height = tk.Entry(self,font=("helvetica",15))
        labelVolume = tk.Label(self, text="Volume                 :", font=("helvetica",15))
        labelSurface = tk.Label(self, text="Surface Area        :", font=("helvetica",15))
        resVolume = tk.Label(self,font=("helvetica",15))
        resSurface = tk.Label(self,font=("helvetica",15))
        labelError = tk.Label(self, font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 3 dimension page",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Tabs3dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",12),command=calculate)

        labelPyramids.pack()
        labelSide.place(x=200, y=37)
        labelHeight.place(x=200, y=65)
        side.place(x=382, y=37)
        height.place(x=382, y=65)
        labelVolume.place(x=200, y=93)
        labelSurface.place(x=200, y=121)
        
        resVolume.place(x=382, y=93)
        resSurface.place(x=381,y=121)

        labelError.place(x=315,y=300)

        buttonRes.place(x=325, y=165)
        buttonBack.place(x=325,y=400)

class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelCalc = tk.Label(self, text="Choose Dimension",font=("helvetica",25))
        button2d = tk.Button(self, text="2 Dimensional shapes",width=20,height=4, font=("helvetica",15), command=lambda: controller.show_frame(Tabs2dimension))
        button3d = tk.Button(self, text="3 Dimensional shapes",width=20,height=4, font=("helvetica",15), command=lambda: controller.show_frame(Tabs3dimension))

        buttonBackMain = tk.Button(self, text="Back to main menu",width=20,height=4, font=("helvetica",15), command=lambda: controller.show_frame(MainMenu))
        labelCalc.pack()
        button2d.pack()
        button3d.pack()
        buttonBackMain.pack()

class Formula(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFormula = tk.Label(self, text="Choose Geometry",font=("helvetica",25))
        # 2 dimension shapes
        buttonSquare = tk.Button(self, text="Square",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fsquare))
        buttonRectangle = tk.Button(self, text="Rectangle",width=20,height=3,font=("helvetica",12), command=lambda: controller.show_frame(Frectangle))
        buttonTriangle = tk.Button(self, text="Triangle",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Ftriangle))
        buttonCircle = tk.Button(self, text="Circle",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fcircle))
        buttonRhombus = tk.Button(self, text="Rhombus",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Frhombus))
        
        # 3 dimension shapes
        buttonCube = tk.Button(self, text="Cube",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fcube))
        buttonCuboids = tk.Button(self, text="Cuboids",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fcuboids))
        buttonBall = tk.Button(self, text="Ball",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fball))
        buttonCone = tk.Button(self, text="Cone",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fcone))
        buttonPyramids = tk.Button(self, text="Pyramids",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Fpyramids))

        buttonBackMain = tk.Button(self, text="Back to main menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(MainMenu))
        labelFormula.pack()
        # 2 diemsionshapes
        buttonSquare.place(x=200,y=50)
        buttonRectangle.place(x=200,y=125)
        buttonTriangle.place(x=200,y=200)
        buttonCircle.place(x=200,y=275)
        buttonRhombus.place(x=200,y=350)
        # # 3 dimension shapes
        buttonCube.place(x=400,y=50)
        buttonCuboids.place(x=400,y=125)
        buttonBall.place(x=400,y=200)
        buttonCone.place(x=400,y=275)
        buttonPyramids.place(x=400,y=350)

        buttonBackMain.place(x=300,y=425)

class Fsquare(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFsquare = tk.Label(self, text="Square Formula",font=("helvetica",25))
        labelArea = tk.Label(self, text="Area = S x S",font=("helvetica",15))
        labelCircumfence = tk.Label(self, text="Circumfence = S+S+S+S / 4S",font=("helvetica",15))
        label_Legend = tk.Label(self, text="S = Side",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFsquare.pack()
        labelArea.place(x=300,y=50)
        labelCircumfence.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)
        
class Frectangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFrectagle = tk.Label(self, text= "Rectangle Formula",font=("helvetica",25))
        labelArea = tk.Label(self, text="Area = W x L",font=("helvetica",15))
        labelCircumfence = tk.Label(self, text="Circumfence = 2W + 2L",font=("helvetica",15))
        label_Legend = tk.Label(self, text="W = Wide\n L = Length",font=("helvetica",15))
        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFrectagle.pack()
        labelArea.place(x=300,y=50)
        labelCircumfence.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)
     
class Ftriangle (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFtriangle = tk.Label(self, text= "Triangle Formula",font=("helvetica",25))
        labelArea = tk.Label(self, text="Area = (B x H)/2",font=("helvetica",15))
        labelCircumfence = tk.Label(self, text="Circumfence = A + B + C",font=("helvetica",15))
        label_Legend = tk.Label(self, text="B = Base\nH = Height\nA,B,C = Sides",font=("helvetica",15))
        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFtriangle.pack()
        labelArea.place (x=300,y=50)
        labelCircumfence.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)

class Fcircle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFcircle = tk.Label(self, text= "Circle Formula",font=("helvetica",25))
        labelArea = tk.Label(self, text="Area = π x r x r ",font=("helvetica",15))
        labelCircumfence = tk.Label(self, text="Circumfence = 2πr / πd",font=("helvetica",15))
        label_Legend = tk.Label(self, text="π = Phi(22/7)\n r = Radius \n d = Diameter",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFcircle.pack()
        labelArea.place (x=300,y=50)
        labelCircumfence.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)
        
class Frhombus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFrhombus = tk.Label(self, text= "Rhombus Formula",font=("helvetica",25))
        labelArea = tk.Label(self, text="Area = (d1 x d2)/2 ",font=("helvetica",15))
        labelCircumfence = tk.Label(self, text="Circumfence = 4S/S+S+S+S",font=("helvetica",15))
        label_Legend = tk.Label(self, text="d1 = Diagonal 1\n d2 = Diagonal 2 \n S = Side",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=10, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFrhombus.pack()
        labelArea.place (x=300,y=50)
        labelCircumfence.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)

class Fcube(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFcube = tk.Label(self, text="Cube Formula",font=("helvetica",25))
        labelVolume = tk.Label(self, text="Volume = S x S x S",font=("helvetica",15))
        labelSurfaceArea = tk.Label(self, text="Surface Area = 6 x S x S",font=("helvetica",15))
        label_Legend = tk.Label(self, text="S = Side",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFcube.pack()
        labelVolume.place(x=300,y=50)
        labelSurfaceArea.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)
        
class Fcuboids(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFcuboids = tk.Label(self, text="Cuboids Formula",font=("helvetica",25))
        labelVolume = tk.Label(self, text="Volume = L x W x H",font=("helvetica",15))
        labelSurfaceArea = tk.Label(self, text="Surface Area = 2 x (L x W) + (L x H) + (W x H)",font=("helvetica",15))
        label_Legend = tk.Label(self, text="L = length\nW = Width\nH = Height",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFcuboids.pack()
        labelVolume.place(x=300,y=50)
        labelSurfaceArea.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)

class Fball(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFball = tk.Label(self, text="Cuboids Formula",font=("helvetica",25))
        labelVolume = tk.Label(self, text="Volume = 4/3 x 22/7 x r x r x r",font=("helvetica",15))
        labelSurfaceArea = tk.Label(self, text="Surface Area = 4 x 22/7 x r x r",font=("helvetica",15))
        label_Legend = tk.Label(self, text="r = Radius",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFball.pack()
        labelVolume.place(x=300,y=50)
        labelSurfaceArea.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)

class Fcone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFcone = tk.Label(self, text="Cone Formula",font=("helvetica",25))
        labelVolume = tk.Label(self, text="Volume = (π x r x r x h)/3 ",font=("helvetica",15))
        labelSurfaceArea = tk.Label(self, text="Surface Area = π x r x (r + s) ",font=("helvetica",15))
        label_Legend = tk.Label(self, text="π = Phi (22/7)\n r = Radius\n h = Height\n s = slant Height",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFcone.pack()
        labelVolume.place(x=300,y=50)
        labelSurfaceArea.place(x=300,y=100)
        label_Legend.place(x=300, y=150)
        
        buttonBackMain.place(x=300,y=425)

class Fpyramids(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelFpyramids = tk.Label(self, text="Pyramid Formula",font=("helvetica",25))
        labelVolume = tk.Label(self, text="Volume = (a x a x h)/3 ",font=("helvetica",15))
        labelSurfaceArea = tk.Label(self, text="Surface Area = A+(p x s)/2 ",font=("helvetica",15))
        label_Legend = tk.Label(self, text="a = Side Lenght h = Height\n p = Perimeter Of Base A = Area Of Base\n s = Slant Height",font=("helvetica",15))

        buttonBackMain = tk.Button(self, text="Back To Formula Menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Formula))

        labelFpyramids.pack()
        labelVolume.place(x=300,y=50)
        labelSurfaceArea.place(x=300,y=100)
        label_Legend.place(x=230, y=150)
        
        buttonBackMain.place(x=300,y=425)

class Tabs2dimension(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label2d = tk.Label(self, text="Choose 2 dimensional shapes",font=("helvetica",25))
        buttonSquare = tk.Button(self, text="Square",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Square))
        buttonRectangle = tk.Button(self, text="Rectangle",width=20,height=4,font=("helvetica",12), command=lambda: controller.show_frame(Rectangle))
        buttonTriangle = tk.Button(self, text="Triangle",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Triangle))
        buttonCircle = tk.Button(self, text="Circle",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Circle))
        buttonRhombus = tk.Button(self, text="Rhombus",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Rhombus))
        buttonBackCalc1 = tk.Button(self, text="Back to Calculator menu", font=("helvetica",12), width=20,height=4, command=lambda: controller.show_frame(Calculator))
        label2d.pack()
        buttonSquare.place(x=150,y=50)
        buttonRectangle.place(x=150,y=150)
        buttonTriangle.place(x=150,y=250)
        buttonCircle.place(x=450,y=50)
        buttonRhombus.place(x=450,y=150)
        buttonBackCalc1.place(x=450, y=250)

class Tabs3dimension(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label3d = tk.Label(self, text="Choose 3 dimensional shapes", font=("helvetica",25))
        buttonCube = tk.Button(self, text="Cube",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Cube))
        buttonCuboids = tk.Button(self, text="Cuboids",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Cuboids))
        buttonBall = tk.Button(self, text="Ball",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Ball))
        buttonCone = tk.Button(self, text="Cone",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Cone))
        buttonPyramids = tk.Button(self, text="Pyramids",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Pyramids))
        buttonBackCalc2 = tk.Button(self, text="Back to Calculator menu",width=20,height=4, font=("helvetica",12), command=lambda: controller.show_frame(Calculator))
        label3d.pack()
        buttonCube.place(x=150,y=50)
        buttonCuboids.place(x=150,y=150)
        buttonBall.place(x=150,y=250)
        buttonCone.place(x=450,y=50)
        buttonPyramids.place(x=450,y=150)
        buttonBackCalc2.place(x=450,y=250)

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='Tomato')

        Button = tk.Button(self, text="Home", font=("helvetiva", 15), command=lambda: controller.show_frame(MainMenu))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("helvetiva", 15), command=lambda: controller.show_frame(Calculator))
        Button.place(x=100, y=450)

class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global player_Name, player_Age, player_NoReg, player_Address

        def clearEntry():
            player_Name.delete(0,'end')
            player_Age.delete(0,'end')
            player_NoReg.delete(0,'end')
            player_Address.delete(0,'end')
        
        def resetPoin():
            global res
            res = int(0)

        labelReg = tk.Label(self, text="Games Registration",font=("helvetica",25))
        
        labelName = tk.Label(self, text="Name",font=("helvetica",15))
        labelAge = tk.Label(self, text="Age",font=("helvetica",15))
        labelNoReg = tk.Label(self, text="No. Registration",font=("helvetica",15))
        labelAddress = tk.Label(self, text="Address",font=("helvetica",15))
        player_Name = tk.Entry(self,font=("helvetica",15))
        player_Age = tk.Entry(self,font=("helvetica",15))
        player_NoReg = tk.Entry(self,font=("helvetica",15))
        player_Address = tk.Entry(self,font=("helvetica",15))
        buttonBackMain = tk.Button(self, text="Back to main menu",width=20,height=3, font=("helvetica",12), command=lambda: controller.show_frame(MainMenu))
        buttonLanjut = tk.Button(self, text="Next",width=20,height=3, font=("helvetica",12), command=lambda:[controller.show_frame(Question1), regtxt(), clearEntry(), resetPoin()])

        labelReg.pack()
        labelName.place(x=200,y=150)
        labelAge.place(x=200,y=200)
        labelNoReg.place(x=200,y=250)
        labelAddress.place(x=200, y=300)
        player_Name.place(x=400, y=150)
        player_Age.place(x=400, y=200)
        player_NoReg.place(x=400, y=250)
        player_Address.place(x=400, y=300)
        buttonBackMain.place(x=200, y=400)
        buttonLanjut.place(x=400, y=400)

class Question1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
            quest = open("soal1.txt", 'r')
            a = quest.read()
            
            textSoal.insert(tk.END, a)
            quest.close()

        labelQuest = tk.Label(self, text="Question 1", font=("helvetica",25))
        textSoal = tk.Text(self, width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Question",width=20,height=3, font=("helvetica",12), command=openTxt)
        ansA = tk.Button(self, text="A",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question2))
        ansB = tk.Button(self, text="B",width=5,height=3, font=("helvetica",12), command=lambda:[controller.show_frame(Question2), updatePoint()])
        ansC = tk.Button(self, text="C",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question2))
        ansD = tk.Button(self, text="D",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question2))
        ansE = tk.Button(self, text="E",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question2))
        

        labelQuest.pack()
        textSoal.pack(pady=20)
        openBtn.pack(pady=5)
        ansA.place(x=225,y=400)
        ansB.place(x=300,y=400)
        ansC.place(x=375,y=400)
        ansD.place(x=450,y=400)
        ansE.place(x=525,y=400)

class Question2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
            quest = open("soal2.txt", 'r')
            a = quest.read()
            
            textSoal.insert(tk.END, a)
            quest.close()

        labelQuest = tk.Label(self, text="Question 2", font=("helvetica",25))
        textSoal = tk.Text(self, width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Question",width=20,height=3, font=("helvetica",12), command=openTxt)
        ansA = tk.Button(self, text="A",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question3))
        ansB = tk.Button(self, text="B",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question3))
        ansC = tk.Button(self, text="C",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question3))
        ansD = tk.Button(self, text="D",width=5,height=3, font=("helvetica",12), command=lambda: [controller.show_frame(Question3), updatePoint()])
        ansE = tk.Button(self, text="E",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question3))
        
        labelQuest.pack()
        textSoal.pack(pady=20)
        openBtn.pack(pady=5)
        ansA.place(x=225,y=400)
        ansB.place(x=300,y=400)
        ansC.place(x=375,y=400)
        ansD.place(x=450,y=400)
        ansE.place(x=525,y=400)

class Question3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
            quest = open("soal3.txt", 'r')
            a = quest.read()
            
            textSoal.insert(tk.END, a)
            quest.close()
        
        labelQuest = tk.Label(self, text="Question 3", font=("helvetica",25))
        textSoal = tk.Text(self, width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Question",width=20,height=3, font=("helvetica",12), command=openTxt)
        ansA = tk.Button(self, text="A",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question4))
        ansB = tk.Button(self, text="B",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question4))
        ansC = tk.Button(self, text="C",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question4))
        ansD = tk.Button(self, text="D",width=5,height=3, font=("helvetica",12), command=lambda: [controller.show_frame(Question4), updatePoint()])
        ansE = tk.Button(self, text="E",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question4))

        labelQuest.pack()
        textSoal.pack(pady=20)
        openBtn.pack(pady=5)
        ansA.place(x=225,y=400)
        ansB.place(x=300,y=400)
        ansC.place(x=375,y=400)
        ansD.place(x=450,y=400)
        ansE.place(x=525,y=400)

class Question4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
            quest = open("soal4.txt", 'r')
            a = quest.read()
            
            textSoal.insert(tk.END, a)
            quest.close()
        
        labelQuest = tk.Label(self, text="Question 4", font=("helvetica",25))
        textSoal = tk.Text(self, width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Question",width=20,height=3, font=("helvetica",12), command=openTxt)
        ansA = tk.Button(self, text="A",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question5))
        ansB = tk.Button(self, text="B",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question5))
        ansC = tk.Button(self, text="C",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question5))
        ansD = tk.Button(self, text="D",width=5,height=3, font=("helvetica",12), command=lambda: [controller.show_frame(Question5), updatePoint()])
        ansE = tk.Button(self, text="E",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question5))

        labelQuest.pack()
        textSoal.pack(pady=20)
        openBtn.pack(pady=5)
        ansA.place(x=225,y=400)
        ansB.place(x=300,y=400)
        ansC.place(x=375,y=400)
        ansD.place(x=450,y=400)
        ansE.place(x=525,y=400)

class Question5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
            quest = open("soal5.txt", 'r')
            a = quest.read()
            
            textSoal.insert(tk.END, a)
            quest.close()
        
        labelQuest = tk.Label(self, text="Question 5", font=("helvetica",25))
        textSoal = tk.Text(self, width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Question",width=20,height=3, font=("helvetica",12), command=openTxt)
        ansA = tk.Button(self, text="A",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question6))
        ansB = tk.Button(self, text="B",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question6))
        ansC = tk.Button(self, text="C",width=5,height=3, font=("helvetica",12), command=lambda: [controller.show_frame(Question6), updatePoint()])
        ansD = tk.Button(self, text="D",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question6))
        ansE = tk.Button(self, text="E",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Question6))
        
        labelQuest.pack()
        textSoal.pack(pady=20)
        openBtn.pack(pady=5)
        ansA.place(x=225,y=400)
        ansB.place(x=300,y=400)
        ansC.place(x=375,y=400)
        ansD.place(x=450,y=400)
        ansE.place(x=525,y=400)

class Question6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
            quest = open("soal6.txt", 'r')
            a = quest.read()
            
            textSoal.insert(tk.END, a)
            quest.close()
        
        labelQuest = tk.Label(self, text="Question 6", font=("helvetica",25))
        textSoal = tk.Text(self, width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Question",width=20,height=3, font=("helvetica",12), command=openTxt)
        ansA = tk.Button(self, text="A",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Results))
        ansB = tk.Button(self, text="B",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Results))
        ansC = tk.Button(self, text="C",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Results))
        ansD = tk.Button(self, text="D",width=5,height=3, font=("helvetica",12), command=lambda: [controller.show_frame(Results), updatePoint(), updateFile()])
        ansE = tk.Button(self, text="E",width=5,height=3, font=("helvetica",12), command=lambda: controller.show_frame(Results))
        
        labelQuest.pack()
        textSoal.pack(pady=20)
        openBtn.pack(pady=5)
        ansA.place(x=225,y=400)
        ansB.place(x=300,y=400)
        ansC.place(x=375,y=400)
        ansD.place(x=450,y=400)
        ansE.place(x=525,y=400)

class Results(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openTxt():
    
            newPlayerFile = open(namefile + ".txt", "r")
            abc = newPlayerFile.read()
            # newPlayerFile.write("name: " + playerName +"\n"+ "No Registration: " + playerNoReg + "\n" + "Age: " + playerAge + "\n" + "Address: " + playerAddress + "\n" + "Your point is: " + str(res) + "\n")   
            
            textResult.insert(tk.END , abc)
            newPlayerFile.close()
        
        def clearResult():
            textResult.delete("1.0","end")

        textResult = tk.Text(self,width=40, height=10, font=("helvetica",15))
        openBtn = tk.Button(self, text="See Results",width=20,height=3, font=("helvetica",12), command=openTxt)
        buttonBackMain = tk.Button(self, text="Back to main menu",width=20,height=3, font=("helvetica",12), command=lambda: [controller.show_frame(MainMenu), clearResult()])

        buttonBackMain.place(x=300, y=400)  
        textResult.pack(pady=20)
        openBtn.pack(pady=5)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        # window.('-fullscreen',True)
        

        self.frames = {}
        for F in (MainMenu, Calculator, Tabs2dimension, Tabs3dimension, ThirdPage,
                Square, Rectangle, Triangle, Circle, Rhombus, Cube, Cuboids, Ball, Cone, Pyramids,
                Formula, Fsquare, Frectangle, Ftriangle, Fcircle, Frhombus, Fcube, Fcuboids, Fball, Fcone, Fpyramids,
                Registration, Question1, Question2, Question3, Question4, Question5, Question6, Results):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Geometry calculator")

app = Application()
# app.maxsize(800, 500)
app.mainloop()