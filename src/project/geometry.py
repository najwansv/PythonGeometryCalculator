import tkinter as tk

class menu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        # self.window.resizable(0,0)
        self.window.title("Geometry calculator")

    def run(self):
        self.window.mainloop()

def tabMainMenu(): # Main Menu
    def tabCalc(): # Calculator Page
        labelMain.destroy()
        buttonCalc.destroy()
        buttonFormula.destroy()
        buttonGames.destroy()

        def tabDimension2(): # 2 dimension page
            labelCalc.destroy()
            button2d.destroy()
            button3d.destroy()
            buttonBackMain.destroy()
            def backCalc1(): # back from 2 dimension page to calculator menu
                label2d.destroy()
                buttonSquare.destroy()
                buttonRectangle.destroy()
                buttonTriangle.destroy()
                buttonCircle.destroy()
                buttonRhombus.destroy()
                buttonBackCalc1.destroy()
                tabCalc()
            label2d = tk.Label(text="Choose 2 dimensional shapes")
            buttonSquare = tk.Button(text="Square",width=20,height=4)
            buttonRectangle = tk.Button(text="Rectangle",width=20,height=4)
            buttonTriangle = tk.Button(text="Triangle",width=20,height=4)
            buttonCircle = tk.Button(text="Circle",width=20,height=4)
            buttonRhombus = tk.Button(text="Rhombus",width=20,height=4)
            buttonBackCalc1 = tk.Button(text="Back to Calculator menu",width=20,height=4, command=backCalc1)
            label2d.pack()
            buttonSquare.pack()
            buttonRectangle.pack()
            buttonTriangle.pack()
            buttonCircle.pack()
            buttonRhombus.pack()
            buttonBackCalc1.pack()

        def tabDimension3(): # 3 dimension page
            labelCalc.destroy()
            button2d.destroy()
            button3d.destroy()
            buttonBackMain.destroy()
            def backCalc2(): # back from 2 dimension page to calculator menu
                label3d.destroy()
                buttonCube.destroy()
                buttonCuboids.destroy()
                buttonBall.destroy()
                buttonCone.destroy()
                buttonPyramids.destroy()
                buttonBackCalc2.destroy()
                tabCalc()
            label3d = tk.Label(text="Choose 3 dimensional shapes")
            buttonCube = tk.Button(text="Cube",width=20,height=4)
            buttonCuboids = tk.Button(text="Cuboids",width=20,height=4)
            buttonBall = tk.Button(text="Ball",width=20,height=4)
            buttonCone = tk.Button(text="Cone",width=20,height=4)
            buttonPyramids = tk.Button(text="Pyramids",width=20,height=4)
            buttonBackCalc2 = tk.Button(text="Back to Calculator menu",width=20,height=4, command=backCalc2)
            label3d.pack()
            buttonCube.pack()
            buttonCuboids.pack()
            buttonBall.pack()
            buttonCone.pack()
            buttonPyramids.pack()
            buttonBackCalc2.pack()

        button2d = tk.Button(text="2 Dimensional shapes",width=20,height=4,command=tabDimension2)
        button3d = tk.Button(text="3 Dimensional shapes",width=20,height=4,command=tabDimension3)

        def backCalcMain(): # back from calculator menu to main menu
            labelCalc.destroy()
            button2d.destroy()
            button3d.destroy()
            buttonBackMain.destroy()
            tabMainMenu()
        
        labelCalc = tk.Label(text="Choose Dimension")
        buttonBackMain = tk.Button(text="Back to main menu",width=20,height=4, command=backCalcMain)
        labelCalc.pack()
        button2d.pack()
        button3d.pack()
        buttonBackMain.pack()

    labelMain = tk.Label(text="Main Menu")
    buttonCalc = tk.Button(text="Calculator",width=20,height=4, command=tabCalc)
    buttonFormula = tk.Button(text="Formula",width=20,height=4)
    buttonGames = tk.Button(text="Games",width=20,height=4)
    labelMain.pack()
    buttonCalc.pack()
    buttonFormula.pack()
    buttonGames.pack()

if __name__ == "__main__":
    calc = menu()
    tabMainMenu()
    calc.run()

