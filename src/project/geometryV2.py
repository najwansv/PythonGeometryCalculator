from email.mime import image
from PIL import ImageTk,Image
import math
import tkinter as tk

# koordinat tengah x = 350, y = 200

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelMain = tk.Label(self, text="Main Menu",font=("helvetica",25))
        buttonCalc = tk.Button(self, text="Calculator",width=20,height=4,font=("helvetica",15), command=lambda: controller.show_frame(Calculator))
        buttonFormula = tk.Button(self, text="Formula",width=20,height=4,font=("helvetica",15))
        buttonGames = tk.Button(self, text="Games",width=20,height=4,font=("helvetica",15))
        labelMain.pack()
        buttonCalc.pack()
        buttonFormula.pack()
        buttonGames.pack()

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
            except: # if the code above is there an error then run except:
                labelError.config(text="something went wrong",fg="red")
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
        # self.configure(bg="cyan")

        def calculate():
            try: # run the code
                var1 = float(length.get())
                var2 = float(width.get())
                result1 = var1 * var2
                result2 = 2*(var1+var2)
                resArea.config(text=result1)
                resCircum.config(text=result2)
            except: # if the code above is there an error then run except:
                labelError.config(text="something went wrong",fg="red")
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
                labelError.config(text="something went wrong",fg="red")
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
                labelError.config(text="something went wrong",fg="red")
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
                labelError.config(text="something went wrong",fg="red")
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

        buttonBack = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, command=lambda: controller.show_frame(Tabs2dimension), font=("helvetica",10))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, command=calculate, font=("helvetica",10))

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
            var = float(side.get())
            result1 = var * var * var
            result2 = 6 * var**2
            resArea.config(text=result1)
            resCircum.config(text=result2)

        labelCube = tk.Label(self, text="Cube Calculator", font=("helvetica",25))
        labelSide = tk.Label(self, text="Input Side legth      ", font=("helvetica",15))
        side = tk.Entry(self,font=("helvetica",15))
        labelArea = tk.Label(self, text="Volume                 :", font=("helvetica",15))
        labelCircum = tk.Label(self, text="Surface Area        :", font=("helvetica",15))
        resArea = tk.Label(self,font=("helvetica",15))
        resCircum = tk.Label(self,font=("helvetica",15))

        buttonBack = tk.Button(self, text="Back to 3 dimension page",width=20,height=4, font=("helvetica",10), command=lambda: controller.show_frame(Tabs3dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, font=("helvetica",10),command=calculate)

        labelCube.pack()
        labelSide.place(x=200, y=37)
        side.place(x=382, y=39)
        labelArea.place(x=200, y=70)
        labelCircum.place(x=200, y=100)
        
        resArea.place(x=382, y=70)
        resCircum.place(x=381,y=100)

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
        buttonCuboids = tk.Button(self, text="Cuboids",width=20,height=4, font=("helvetica",12))
        buttonBall = tk.Button(self, text="Ball",width=20,height=4, font=("helvetica",12))
        buttonCone = tk.Button(self, text="Cone",width=20,height=4, font=("helvetica",12))
        buttonPyramids = tk.Button(self, text="Pyramids",width=20,height=4, font=("helvetica",12))
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

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (MainMenu, Calculator, Tabs2dimension, Tabs3dimension, ThirdPage, Square, Rectangle, Triangle, Circle, Rhombus, Cube):
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