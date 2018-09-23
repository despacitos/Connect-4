import kivy as kivy
from kivy.app import App
import time
kivy.require("1.10.1")
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Line
from kivy.graphics.vertex_instructions import Ellipse
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color
                                               
class Game(FloatLayout):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        with self.canvas:
            Window.clearcolor = (0,.2,1,1)
            Window.size = (800,880)
            self.Red = [1, 0, 0, 1]
            self.Yellow = [1, 1, 0, 1]
            self.White = [1, 1, 1, 1]
            
            self.A1 = Ellipse(size=self.size, pos=(6,666))
            self.B1 = Ellipse(size=self.size, pos=(121,666))
            self.C1 = Ellipse(size=self.size, pos=(235,666))
            self.D1 = Ellipse(size=self.size, pos=(349,666))
            self.E1 = Ellipse(size=self.size, pos=(463,666))
            self.F1 = Ellipse(size=self.size, pos=(578,666))
            self.G1 = Ellipse(size=self.size, pos=(692,666))

            self.A2 = Ellipse(size=self.size, pos=(6,556))
            self.B2 = Ellipse(size=self.size, pos=(121,556))
            self.C2 = Ellipse(size=self.size, pos=(235,556))
            self.D2 = Ellipse(size=self.size, pos=(349,556))
            self.E2 = Ellipse(size=self.size, pos=(463,556))
            self.F2 = Ellipse(size=self.size, pos=(578,556))
            self.G2 = Ellipse(size=self.size, pos=(692,556))

            self.A3 = Ellipse(size=self.size, pos=(6,446))
            self.B3 = Ellipse(size=self.size, pos=(121,446))
            self.C3 = Ellipse(size=self.size, pos=(235,446))
            self.D3 = Ellipse(size=self.size, pos=(349,446))
            self.E3 = Ellipse(size=self.size, pos=(463,446))
            self.F3 = Ellipse(size=self.size, pos=(578,446))
            self.G3 = Ellipse(size=self.size, pos=(692,446))

            self.A4 = Ellipse(size=self.size, pos=(6,336))
            self.B4 = Ellipse(size=self.size, pos=(121,336))
            self.C4 = Ellipse(size=self.size, pos=(235,336))
            self.D4 = Ellipse(size=self.size, pos=(349,336))
            self.E4 = Ellipse(size=self.size, pos=(463,336))
            self.F4 = Ellipse(size=self.size, pos=(578,336))
            self.G4 = Ellipse(size=self.size, pos=(692,336))

            self.A5 = Ellipse(size=self.size, pos=(6,226))
            self.B5 = Ellipse(size=self.size, pos=(121,226))
            self.C5 = Ellipse(size=self.size, pos=(235,226))
            self.D5 = Ellipse(size=self.size, pos=(349,226))
            self.E5 = Ellipse(size=self.size, pos=(463,226))
            self.F5 = Ellipse(size=self.size, pos=(578,226))
            self.G5 = Ellipse(size=self.size, pos=(692,226))

            self.A6 = Ellipse(size=self.size, pos=(6,116))
            self.B6 = Ellipse(size=self.size, pos=(121,116))
            self.C6 = Ellipse(size=self.size, pos=(235,116))
            self.D6 = Ellipse(size=self.size, pos=(349,116))
            self.E6 = Ellipse(size=self.size, pos=(463,116))
            self.F6 = Ellipse(size=self.size, pos=(578,116))
            self.G6 = Ellipse(size=self.size, pos=(692,116))
            
            self.btn1 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':0, 'y':.875})
            self.add_widget(self.btn1)
            self.btn1.bind(on_press=self.clk1)
            self.btn2 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':.14285714285, 'y':.875})
            self.add_widget(self.btn2)
            self.btn2.bind(on_press=self.clk2)
            self.btn3 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':.28571428571, 'y':.875})
            self.add_widget(self.btn3)
            self.btn3.bind(on_press=self.clk3)
            self.btn4 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':.42857142857, 'y':.875})
            self.add_widget(self.btn4)
            self.btn4.bind(on_press=self.clk4)
            self.btn5 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':.57142857142, 'y':.875})
            self.add_widget(self.btn5)
            self.btn5.bind(on_press=self.clk5)
            self.btn6 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':.71428571428, 'y':.875})
            self.add_widget(self.btn6)
            self.btn6.bind(on_press=self.clk6)
            self.btn7 = Button(text='Drop Here', size_hint=(.14285714285, .125), pos_hint={'x':.85714285714, 'y':.875})
            self.add_widget(self.btn7)
            self.btn7.bind(on_press=self.clk7)
            
            self.ResetScores = Button(text='Reset Scores', size_hint=(.14285714285, .125), pos_hint={'x':0, 'y':0})
            self.add_widget(self.ResetScores)
            self.RedScore = Button(text='Red: ', pos_hint={'x':.28571428571, 'y':0}, size_hint=(.14285714285, .125), background_down='', background_normal='', background_color=[0,.2,1,1])
            self.add_widget(self.RedScore)
            self.YellowScore = Button(text='Yellow: ', pos_hint={'x':.57142857142, 'y':0}, size_hint=(.14285714285, .125), background_down='', background_normal='', background_color=[0,.2,1,1])
            self.add_widget(self.YellowScore)
            self.NewGame = Button(text='New Game', size_hint=(.14285714285, .125), pos_hint={'x':.85714285714, 'y':0})
            self.add_widget(self.NewGame)
            self.NewGame.bind(on_press=self.ClearBoard)
            self.WinCondition = Button(text='Declare Winner', size_hint=(.14285714285, .125), pos_hint={'x':.42857142857, 'y':0})
            self.add_widget(self.WinCondition)
            self.WinCondition.bind(on_press=self.winDeclare)
            
            self.btnclk1 = 6
            self.btnclk2 = 6
            self.btnclk3 = 6
            self.btnclk4 = 6
            self.btnclk5 = 6
            self.btnclk6 = 6
            self.btnclk7 = 6

            self.redturn = 1
            self.yellowturn = 0

            self.redCount = 0
            self.yellowCount = 0
            
            self.CheckerPlacement=["A1","B1","C1","D1","E1","F1","G1","A2","B2","C2","D2","E2","F2","G2","A3","B3","C3","D3","E3","F3","G3","A4","B4","C4","D4","E4","F4","G4","A5","B5","C5","D5","E5","F5","G5","A6","B6","C6","D6","E6","F6","G6"]
                                #   0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41
    def winDeclare(self, obj):
        if(self.CheckerPlacement[35]=="red" and self.CheckerPlacement[36]=="red" and self.CheckerPlacement[37]=="red" and self.CheckerPlacement[38]=="red"):
            self.RedScore = Button(text='Red: ', pos_hint={'x':.28571428571, 'y':0}, size_hint=(.14285714285, .125), background_down='', background_normal='', background_color=[0,.2,1,1])
            self.add_widget(self.RedScore)
        else:
            pass
        
    def clk1(self, obj):                                                    
        if(self.btnclk1==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.A6 = Ellipse(size=(100,100), pos=(6,116))
            self.btnclk1=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[35]="red"
        elif(self.btnclk1==5 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.A5 = Ellipse(size=(100,100), pos=(6,226))
            self.btnclk1=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk1==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.A4 = Ellipse(size=(100,100), pos=(6,336))
            self.btnclk1=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk1==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.A3 = Ellipse(size=(100,100), pos=(6,446))
            self.btnclk1=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk1==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.A2 = Ellipse(size=(100,100), pos=(6,556))
            self.btnclk1=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk1==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.A1 = Ellipse(size=(100,100), pos=(6,666))
            self.btnclk1=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk1==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.A6 = Ellipse(size=(100,100), pos=(6,116))
            self.btnclk1=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk1==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.A5 = Ellipse(size=(100,100), pos=(6,226))
            self.btnclk1=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk1==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.A4 = Ellipse(size=(100,100), pos=(6,336))
            self.btnclk1=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk1==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.A3 = Ellipse(size=(100,100), pos=(6,446))
            self.btnclk1=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk1==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.A2 = Ellipse(size=(100,100), pos=(6,556))
            self.btnclk1=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk1==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.A1 = Ellipse(size=(100,100), pos=(6,666))
            self.btnclk1=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass
    def clk2(self, obj):                                                    
        if(self.btnclk2==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.B6 = Ellipse(size=(100,100), pos=(121,116))
            self.btnclk2=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[36]="red"
        elif(self.btnclk2==5 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.B5 = Ellipse(size=(100,100), pos=(121,226))
            self.btnclk2=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk2==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.B4 = Ellipse(size=(100,100), pos=(121,336))
            self.btnclk2=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk2==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.B3 = Ellipse(size=(100,100), pos=(121,446))
            self.btnclk2=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk2==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.B2 = Ellipse(size=(100,100), pos=(121,556))
            self.btnclk2=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk2==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.B1 = Ellipse(size=(100,100), pos=(121,666))
            self.btnclk2=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk2==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.B6 = Ellipse(size=(100,100), pos=(121,116))
            self.btnclk2=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk2==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.B5 = Ellipse(size=(100,100), pos=(121,226))
            self.btnclk2=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk2==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.B4 = Ellipse(size=(100,100), pos=(121,336))
            self.btnclk2=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk2==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.B3 = Ellipse(size=(100,100), pos=(121,446))
            self.btnclk2=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk2==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.B2 = Ellipse(size=(100,100), pos=(121,556))
            self.btnclk2=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk2==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.B1 = Ellipse(size=(100,100), pos=(121,666))
            self.btnclk2=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass
    def clk3(self, obj):                                                    
        if(self.btnclk3==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.C6 = Ellipse(size=(100,100), pos=(235,116))
            self.btnclk3=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[37]="red"
        elif(self.btnclk3==5 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.C5 = Ellipse(size=(100,100), pos=(235,226))
            self.btnclk3=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk3==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.C4 = Ellipse(size=(100,100), pos=(235,336))
            self.btnclk3=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk3==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.C3 = Ellipse(size=(100,100), pos=(235,446))
            self.btnclk3=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk3==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.C2 = Ellipse(size=(100,100), pos=(235,556))
            self.btnclk3=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk3==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.C1 = Ellipse(size=(100,100), pos=(235,666))
            self.btnclk3=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk3==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.C6 = Ellipse(size=(100,100), pos=(235,116))
            self.btnclk3=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk3==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.C5 = Ellipse(size=(100,100), pos=(235,226))
            self.btnclk3=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk3==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.C4 = Ellipse(size=(100,100), pos=(235,336))
            self.btnclk3=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk3==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.C3 = Ellipse(size=(100,100), pos=(235,446))
            self.btnclk3=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk3==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.C2 = Ellipse(size=(100,100), pos=(235,556))
            self.btnclk3=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk3==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.C1 = Ellipse(size=(100,100), pos=(235,666))
            self.btnclk3=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass
    def clk4(self, obj):                                                    
        if(self.btnclk4==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.D6 = Ellipse(size=(100,100), pos=(349,116))
            self.btnclk4=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[38]="red"
        elif(self.btnclk4==5 and self.redturn==1):                                                                                                                                              
            with self.canvas:
                Color(rgba=self.Red)
                self.D5 = Ellipse(size=(100,100), pos=(349,226))
            self.btnclk4=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk4==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.D4 = Ellipse(size=(100,100), pos=(349,336))
            self.btnclk4=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk4==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.D3 = Ellipse(size=(100,100), pos=(349,446))
            self.btnclk4=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk4==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.D2 = Ellipse(size=(100,100), pos=(349,556))
            self.btnclk4=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk4==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.D1 = Ellipse(size=(100,100), pos=(349,666))
            self.btnclk4=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk4==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.D6 = Ellipse(size=(100,100), pos=(349,116))
            self.btnclk4=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk4==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.D5 = Ellipse(size=(100,100), pos=(349,226))
            self.btnclk4=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk4==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.D4 = Ellipse(size=(100,100), pos=(349,336))
            self.btnclk4=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk4==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.D3 = Ellipse(size=(100,100), pos=(349,446))
            self.btnclk4=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk4==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.D2 = Ellipse(size=(100,100), pos=(349,556))
            self.btnclk4=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk4==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.D1 = Ellipse(size=(100,100), pos=(349,666))
            self.btnclk4=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass
    def clk5(self, obj):                                                    
        if(self.btnclk5==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.E6 = Ellipse(size=(100,100), pos=(463,116))
            self.btnclk5=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[39]="red"
        elif(self.btnclk5==5 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.E5 = Ellipse(size=(100,100), pos=(463,226))
            self.btnclk5=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk5==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.E4 = Ellipse(size=(100,100), pos=(463,336))
            self.btnclk5=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk5==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.E3 = Ellipse(size=(100,100), pos=(463,446))
            self.btnclk5=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk5==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.E2 = Ellipse(size=(100,100), pos=(463,556))
            self.btnclk5=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk5==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.E1 = Ellipse(size=(100,100), pos=(463,666))
            self.btnclk5=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk5==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.E6 = Ellipse(size=(100,100), pos=(463,116))
            self.btnclk5=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk5==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.E5 = Ellipse(size=(100,100), pos=(463,226))
            self.btnclk5=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk5==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.E4 = Ellipse(size=(100,100), pos=(463,336))
            self.btnclk5=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk5==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.E3 = Ellipse(size=(100,100), pos=(463,446))
            self.btnclk5=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk5==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.E2 = Ellipse(size=(100,100), pos=(463,556))
            self.btnclk5=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk5==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.E1 = Ellipse(size=(100,100), pos=(463,666))
            self.btnclk5=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass
    def clk6(self, obj):                                                    
        if(self.btnclk6==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F6 = Ellipse(size=(100,100), pos=(578,116))
            self.btnclk6=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[40]="red"
        elif(self.btnclk6==5 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F5 = Ellipse(size=(100,100), pos=(578,226))
            self.btnclk6=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk6==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F4 = Ellipse(size=(100,100), pos=(578,336))
            self.btnclk6=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk6==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F3 = Ellipse(size=(100,100), pos=(578,446))
            self.btnclk6=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk6==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F2 = Ellipse(size=(100,100), pos=(578,556))
            self.btnclk6=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk6==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F1 = Ellipse(size=(100,100), pos=(578,666))
            self.btnclk6=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk6==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F6 = Ellipse(size=(100,100), pos=(578,116))
            self.btnclk6=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk6==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F5 = Ellipse(size=(100,100), pos=(578,226))
            self.btnclk6=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk6==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F4 = Ellipse(size=(100,100), pos=(578,336))
            self.btnclk6=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk6==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F3 = Ellipse(size=(100,100), pos=(578,446))
            self.btnclk6=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk6==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F2 = Ellipse(size=(100,100), pos=(578,556))
            self.btnclk6=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk6==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F1 = Ellipse(size=(100,100), pos=(578,666))
            self.btnclk6=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass
    def clk7(self, obj):                                                    
        if(self.btnclk7==6 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F6 = Ellipse(size=(100,100), pos=(692,116))
            self.btnclk7=5
            self.redturn=0
            self.yellowturn=1
            self.CheckerPlacement[41]="red"
        elif(self.btnclk7==5 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F5 = Ellipse(size=(100,100), pos=(692,226))
            self.btnclk7=4
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk7==4 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F4 = Ellipse(size=(100,100), pos=(692,336))
            self.btnclk7=3
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk7==3 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F3 = Ellipse(size=(100,100), pos=(692,446))
            self.btnclk7=2
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk7==2 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F2 = Ellipse(size=(100,100), pos=(692,556))
            self.btnclk7=1
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk7==1 and self.redturn==1):
            with self.canvas:
                Color(rgba=self.Red)
                self.F1 = Ellipse(size=(100,100), pos=(692,666))
            self.btnclk7=0
            self.redturn=0
            self.yellowturn=1
        elif(self.btnclk7==6 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F6 = Ellipse(size=(100,100), pos=(692,116))
            self.btnclk7=5
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk7==5 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F5 = Ellipse(size=(100,100), pos=(692,226))
            self.btnclk7=4
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk7==4 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F4 = Ellipse(size=(100,100), pos=(692,336))
            self.btnclk7=3
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk7==3 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F3 = Ellipse(size=(100,100), pos=(692,446))
            self.btnclk7=2
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk7==2 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F2 = Ellipse(size=(100,100), pos=(692,556))
            self.btnclk7=1
            self.redturn=1
            self.yellowturn=0
        elif(self.btnclk7==1 and self.yellowturn==1):
            with self.canvas:
                Color(rgba=self.Yellow)
                self.F1 = Ellipse(size=(100,100), pos=(692,666))
            self.btnclk7=0
            self.redturn=1
            self.yellowturn=0
        else:
            pass

    def ClearBoard(self, obj):
        with self.canvas:
            Color(rgba=self.White)
            self.A1 = Ellipse(size=(100,100), pos=(6,666))
            self.B1 = Ellipse(size=(100,100), pos=(121,666))
            self.C1 = Ellipse(size=(100,100), pos=(235,666))
            self.D1 = Ellipse(size=(100,100), pos=(349,666))
            self.E1 = Ellipse(size=(100,100), pos=(463,666))
            self.F1 = Ellipse(size=(100,100), pos=(578,666))
            self.G1 = Ellipse(size=(100,100), pos=(692,666))

            self.A2 = Ellipse(size=(100,100), pos=(6,556))
            self.B2 = Ellipse(size=(100,100), pos=(121,556))
            self.C2 = Ellipse(size=(100,100), pos=(235,556))
            self.D2 = Ellipse(size=(100,100), pos=(349,556))
            self.E2 = Ellipse(size=(100,100), pos=(463,556))
            self.F2 = Ellipse(size=(100,100), pos=(578,556))
            self.G2 = Ellipse(size=(100,100), pos=(692,556))

            self.A3 = Ellipse(size=(100,100), pos=(6,446))
            self.B3 = Ellipse(size=(100,100), pos=(121,446))
            self.C3 = Ellipse(size=(100,100), pos=(235,446))
            self.D3 = Ellipse(size=(100,100), pos=(349,446))
            self.E3 = Ellipse(size=(100,100), pos=(463,446))
            self.F3 = Ellipse(size=(100,100), pos=(578,446))
            self.G3 = Ellipse(size=(100,100), pos=(692,446))

            self.A4 = Ellipse(size=(100,100), pos=(6,336))
            self.B4 = Ellipse(size=(100,100), pos=(121,336))
            self.C4 = Ellipse(size=(100,100), pos=(235,336))
            self.D4 = Ellipse(size=(100,100), pos=(349,336))
            self.E4 = Ellipse(size=(100,100), pos=(463,336))
            self.F4 = Ellipse(size=(100,100), pos=(578,336))
            self.G4 = Ellipse(size=(100,100), pos=(692,336))

            self.A5 = Ellipse(size=(100,100), pos=(6,226))
            self.B5 = Ellipse(size=(100,100), pos=(121,226))
            self.C5 = Ellipse(size=(100,100), pos=(235,226))
            self.D5 = Ellipse(size=(100,100), pos=(349,226))
            self.E5 = Ellipse(size=(100,100), pos=(463,226))
            self.F5 = Ellipse(size=(100,100), pos=(578,226))
            self.G5 = Ellipse(size=(100,100), pos=(692,226))

            self.A6 = Ellipse(size=(100,100), pos=(6,116))
            self.B6 = Ellipse(size=(100,100), pos=(121,116))
            self.C6 = Ellipse(size=(100,100), pos=(235,116))
            self.D6 = Ellipse(size=(100,100), pos=(349,116))
            self.E6 = Ellipse(size=(100,100), pos=(463,116))
            self.F6 = Ellipse(size=(100,100), pos=(578,116))
            self.G6 = Ellipse(size=(100,100), pos=(692,116))

        self.btnclk1 = 6
        self.btnclk2 = 6
        self.btnclk3 = 6
        self.btnclk4 = 6
        self.btnclk5 = 6
        self.btnclk6 = 6
        self.btnclk7 = 6

        self.redturn = 1
        self.yellowturn = 0
        
class Connect4a(App):
    def build(self):
        return Game()
    
if __name__ == "__main__":
    Connect4a().run()
