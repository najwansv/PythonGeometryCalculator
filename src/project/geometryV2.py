import tkinter as tk

# koordinat tengah x = 350, y = 200

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelMain = tk.Label(self, text="Main Menu")
        buttonCalc = tk.Button(self, text="Calculator",width=20,height=4, command=lambda: controller.show_frame(Calculator))
        buttonFormula = tk.Button(self, text="Formula",width=20,height=4)
        buttonGames = tk.Button(self, text="Games",width=20,height=4)
        labelMain.pack()
        buttonCalc.pack()
        buttonFormula.pack()
        buttonGames.pack()

class Square(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def calculate():
            var = float(num1.get())
            result1 = var ** 3
            result2 = var * 4
            resArea.config(text=result1)
            resCircum.config(text=result2)

        labelMain = tk.Label(self, text="Square Calculator")
        sisi = tk.Label(self, text="Input Side legth: ")
        num1 = tk.Entry(self)
        area = tk.Label(self, text="Area: ")
        circum = tk.Label(self, text="Circumfence leghth: ")
        resArea = tk.Label(self)
        resCircum = tk.Label(self)

        buttonCalc = tk.Button(self, text="Back to 2 dimension page",width=20,height=4, command=lambda: controller.show_frame(Tabs2dimension))
        buttonRes = tk.Button(self,text="Calculate",width=20,height=4, command=calculate)

        labelMain.pack()
        sisi.place(x=245, y=20)
        num1.pack()
        area.place(x=245, y=50)
        circum.place(x=245, y=80)
        
        resArea.place(x=375, y=50)
        resCircum.place(x=377,y=80)

        buttonRes.place(x=325, y=125)
        buttonCalc.place(x=325,y=300)

class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button2d = tk.Button(self, text="2 Dimensional shapes",width=20,height=4,command=lambda: controller.show_frame(Tabs2dimension))
        button3d = tk.Button(self, text="3 Dimensional shapes",width=20,height=4,command=lambda: controller.show_frame(Tabs3dimension))

        labelCalc = tk.Label(self, text="Choose Dimension")
        buttonBackMain = tk.Button(self, text="Back to main menu",width=20,height=4, command=lambda: controller.show_frame(MainMenu))
        labelCalc.pack()
        button2d.pack()
        button3d.pack()
        buttonBackMain.pack()

class Tabs2dimension(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label2d = tk.Label(self, text="Choose 2 dimensional shapes")
        buttonSquare = tk.Button(self, text="Square",width=20,height=4,command=lambda: controller.show_frame(Square))
        buttonRectangle = tk.Button(self, text="Rectangle",width=20,height=4)
        buttonTriangle = tk.Button(self, text="Triangle",width=20,height=4)
        buttonCircle = tk.Button(self, text="Circle",width=20,height=4)
        buttonRhombus = tk.Button(self, text="Rhombus",width=20,height=4)
        buttonBackCalc1 = tk.Button(self, text="Back to Calculator menu",width=20,height=4, command=lambda: controller.show_frame(Calculator))
        label2d.pack()
        buttonSquare.pack()
        buttonRectangle.pack()
        buttonTriangle.pack()
        buttonCircle.pack()
        buttonRhombus.pack()
        buttonBackCalc1.pack()

class Tabs3dimension(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label3d = tk.Label(self, text="Choose 3 dimensional shapes")
        buttonCube = tk.Button(self, text="Cube",width=20,height=4)
        buttonCuboids = tk.Button(self, text="Cuboids",width=20,height=4)
        buttonBall = tk.Button(self, text="Ball",width=20,height=4)
        buttonCone = tk.Button(self, text="Cone",width=20,height=4)
        buttonPyramids = tk.Button(self, text="Pyramids",width=20,height=4)
        buttonBackCalc2 = tk.Button(self, text="Back to Calculator menu",width=20,height=4, command=lambda: controller.show_frame(Calculator))
        label3d.pack()
        buttonCube.pack()
        buttonCuboids.pack()
        buttonBall.pack()
        buttonCone.pack()
        buttonPyramids.pack()
        buttonBackCalc2.pack()

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='Tomato')

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(MainMenu))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Calculator))
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
        for F in (MainMenu, Calculator, Tabs2dimension, Tabs3dimension, ThirdPage, Square):
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