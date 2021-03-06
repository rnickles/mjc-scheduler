from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel 
from kivy.core.window import Window 
from random import random
from helpers import extract_times
from scrollable_calender import ScrollableCalender

class TabbedCalender(TabbedPanel):
    def setup_grid(self):
        for item in self.ids:
            self.ids[item].content.calender.setup_grid()
        
    def __init__(self, *args, **kwargs):
        super(TabbedCalender, self).__init__(*args, **kwargs)
        self.schedule_index = -1
        self.schedules = []

    def load_next_schedule( self ):
        self.schedule_index += 1
        self.add_schedule( self.schedules[ self.schedule_index ] )

    def add_blocks( self, d_list, start, end, color, text ):
        for day in d_list:
            if day == 'M':
                self.ids.mon.content.calender.add_block( start, end, color, text )
            if day == 'T':
                self.ids.tues.content.calender.add_block( start, end, color, text )
            if day == 'W':
                self.ids.wed.content.calender.add_block( start, end, color, text )
            if day == 'TH':
                self.ids.thurs.content.calender.add_block( start, end, color, text )
            if day == 'F':
                self.ids.fri.content.calender.add_block( start, end, color, text )

    def add_course( self, course_dict ):
        color = 0, random(), random()
        time_data = zip(course_dict['Days'], course_dict['Times'], course_dict['Type'])
        for d_list, t, ty in time_data:
            start, end = extract_times(t)
            text = " ".join([course_dict['Name'][0], ty, start, end])
            self.add_blocks( d_list, start, end, color, text )

    def add_schedule( self, schedule ):
        for course in schedule:
            self.add_course( course )
    

if __name__ == '__main__':
    course_dict = {'Name': ['MCHEM-101'], 'Title': ['General Chemistry 1', '08/25/14-12/13/14'], 'Section': ['1704'], 'Days': [['W'], ['F'], ['M'], ['TH'], ['ARR']], 'Times': ['11:40A - 01:05P', '01:40P - 02:30P', '11:40A - 12:45P', '08:25A - 11:30A', '1.7 hrs/wk'], 'Avail': ['Wait/11'], 'Location': ['MSCC 114, West', 'MSCC 305, West', 'MSCC 114, West', 'MSCC 312, West', 'MONL, West'], 'Units': ['5'], 'Instructor': ['Maki, Lau'], 'Type': ['LEC', 'LEC', 'LAB', 'LAB', 'DINT'], 'Important Notes': ['HYBRID.  Part of Lecture is online.  Required on-campus lecture and laboratory class attendance.  Contact instructor makil@mjc.ed   u'], 'Max/': ['24/2']}
    course_dict2 = {'Name': ['MPHYS-102'], 'Title': ['Ge\
neral Phys: Waves, Ther & Op', '08/25/14-12/13/14'], 'Section': ['3712'], 'Days': [['T', 'TH'], ['T'], ['T']], 'Times': [\
'11:40A - 01:05P', '02:50P - 03:40P', '03:50P - 06:55P'], 'Avail': ['Open'], 'Location': ['MSCC 351, West', 'MSCC 311, We\
st', 'MSCC 311, West'], 'Units': ['5'], 'Instructor': ['Gariety, Mic'], 'Type': ['LEC', 'LEC', 'LAB'], 'Important Notes':\
 [''], 'Max/': ['24/7']}

    class TabbedPanelApp(App): 
        def setup_grid(self):
            self.tabcal.setup_grid()
            sched = [course_dict,course_dict2]
            self.tabcal.add_schedule(sched)

        def build(self):
            self.tabcal = TabbedCalender( size_hint=(1,.65) )
            self.setup_grid()
            return self.tabcal

    app = TabbedPanelApp()
    app.run()
