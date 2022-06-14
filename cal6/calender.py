from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window 

from helpers import times, split_time

def set_origin(ox, oy):
    def give_point(a,b):
        return 0.0 + ox + a, 0.0 + oy + b
    return give_point

def find_root( widg ):
    if widg != None:
        return [widg] + find_root(widg.parent)
    else:
        return []

class Calender(FloatLayout):
    def setup_grid(self):
        self.windowW, self.windowH = 0,0
        self.xbuff, self.ybuff = .05 * self.windowW, .10 * self.windowH
        self.ygap = (self.windowH - self.ybuff) / len(times)
        self.label_point = set_origin( (-self.windowW/2.0) + self.xbuff, -self.windowH/2.0 + (self.ybuff/2.0) )
        self.canvas_point = set_origin( self.xbuff, self.ybuff/2.0 )
        self.build_border()

    def __init__(self, *args, **kwargs):
        super(Calender, self).__init__(*args, **kwargs)

    def build_border( self ):
        for i in range(len(times)):
            self.add_widget( Label( pos=self.label_point( 0, i * self.ygap ), 
                                    text=times[i], 
                                    font_size=16) )
            with self.canvas:
                Color(0, .5, .5, .5)
                p1, p2 = self.canvas_point(0, i * self.ygap), self.canvas_point( 1000, i * self.ygap )
                Line(points=list( p1 + p2 ), width=1)

    def add_block( self, start, end, color, text ):
        shr, smin = split_time(start.strip()) # 11:53P ---> 11:00P, 53
        ehr, emin = split_time(end.strip())
        y1, y2 = (times.index(shr) + smin/60.0) * self.ygap, \
                 (times.index(ehr) + emin/60.0) * self.ygap
        left_edge = .15 * self.windowW
        r, g, b = color
        with self.canvas:
            Color(r,g,b,.5)
            pos = self.canvas_point(left_edge,y1)
            Rectangle(pos=pos, size=( self.windowW, y2-y1 ) )
            
        pos = self.label_point(2*left_edge, y1 + (y2-y1)/2.0)
        label = Label(text=text, pos=pos, font_size=16)
        self.add_widget( label ) 
