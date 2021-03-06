from kivy.uix.scrollview import ScrollView

from calender import Calender
from helpers import times, split_time

class ScrollableCalender( ScrollView ):
    def __init__(self, *args, **kwargs):
        super(ScrollableCalender, self).__init__(*args, **kwargs)
        self.calender = Calender( size_hint=(1,2) )
        self.add_widget( self.calender )
        #self.calender.setup_grid()
        #self.calender.build_border()

if __name__ == '__main__':
    from kivy.app import App

    class Main(App):
        def build(self):
            #scrollable_calender = ScrollableCalender( size_hint = (1, 1), pos_hint = {'top': 1} )
            scrollable_calender = ScrollableCalender( size_hint=(1, .65) )
            start, end = "03:45A", "01:25P"
            scrollable_calender.calender.add_block(start, end, (0, 255, 0), end + "\n" + start)
            return scrollable_calender

    Main().run()


