from kivy.base import runTouchApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from course_selector.course_selector import course_selector_layout
from cal6.tabbed_calender import TabbedCalender
from algorithm.schedule_algorithm import generate_schedules

courses_selected = []
number_of_courses_selected = 0

def create_label_callback( dicts, text ):
    global courses_selected, number_of_courses_selected, course_labels
    number_of_courses_selected += 1
    #courses_selected += dicts
    for d in dicts:
        if d['Title'][0] == text:
            courses_selected += [d]
    course_labels.add_widget( Label( text=text ))#" ".join([text, courses_selected[-1]['Title'][0]])))

def generate_callback( button ):
    global tabbed_calender, courses_selected, number_of_courses_selected
    tabbed_calender.schedules = generate_schedules(courses_selected, number_of_courses_selected)
    tabbed_calender.load_next_schedule()

def load_active_widgets():
    global top_level_layout, active_widgets
    top_level_layout.clear_widgets()
    for widg in active_widgets:
        top_level_layout.add_widget(widg)

top_level_layout = FloatLayout()
# Wierd part is that create_label is called when a course is selected. 
course_select = course_selector_layout(create_label_callback, top_per=1, x_per=1, y_per=.1)
course_labels = GridLayout( cols=1, size_hint = (1, .2), pos_hint = {'top':.85} )
tabbed_calender = TabbedCalender( size_hint = (1, .65), pos_hint = {'top':.65} )
tabbed_calender.setup_grid()#Setup grids once tabbed calender has its place in the widget tree.
gen_butt = Button( text="Generate Schedules", 
                   on_press=generate_callback,
                   size_hint=(1, .05),
                   pos_hint = {'top':.9} )
active_widgets = [course_select, course_labels, gen_butt, tabbed_calender]
inactive_widgets = []
load_active_widgets()
runTouchApp(top_level_layout)
