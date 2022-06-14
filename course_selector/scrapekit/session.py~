import mechanize
from bs4 import BeautifulSoup as BS
import techie
from compress_items import itemcompress
import listing_test

br = mechanize.Browser()
br.open("http://media.mjc.edu/classsearch/")
assert br.viewing_html()
form = br.forms().next()
relevant_controls = form.controls[2:7]

def get_labels( control ):
    if isinstance(control, mechanize.SelectControl ):
        return \
            [ i.get_labels()[0]._text for i in control.items ]

def set_by_label( text, control ):
    if isinstance(control, mechanize.SelectControl ):
        control.set_value_by_label([ text ])

days = ['M','T','W','TH','F', 'ARR']
def split_days( l_dict ):
    for i in range(len(l_dict['Days'])):
        entry = l_dict['Days'][i]
        thurs = entry.find('TH')
        arr = entry.find('ARR')
        temp = [ d for d in entry ]
        if thurs >= 0:
            temp[thurs] = temp[thurs] + temp[thurs + 1]
            temp.pop(thurs + 1 )
        if arr >= 0:
            temp[arr] = temp[arr] + temp[arr + 1] + temp[arr + 2]
            temp.pop(arr + 1 )
            temp.pop(arr + 1 )
        for d in temp:
            if d not in days:
                print "*" * 100
                print d
                print "*" * 100
        l_dict['Days'][i] = temp

# An attempt at interfacing mechanize with kivy
# I.E. this stuff is meant to be used in outside modules
term_control = relevant_controls[0]
term_labels = get_labels( term_control )
def set_term_value( text ):
    set_by_label( text, term_control )

subject_control = relevant_controls[1]
subject_labels = get_labels( subject_control )
def set_subject_value( text ):
    set_by_label( text, subject_control )

def submit_HTMLform():
    raw_classes = []
    try:
        request = form.click()
        response = mechanize.urlopen(request)
        soup = BS(response.read())
        raw_classes = soup.find_all('tr')
    except mechanize.HTTPError, response2:
        pass
    
    if len(raw_classes) >= 6:
        key = [ str(item) for item in raw_classes[5].strings ][1:-1]
        itemcompress( key, 'U', 's', fill="" )
        
        all_subject_listings = []
        for raw in raw_classes[6:]:
            listing = techie.clean(raw)
            listing_table = dict(zip(key, listing))
            #listing_test.test_suite( listing_table )
            split_days(listing_table)
            all_subject_listings += [listing_table]
        return all_subject_listings
    return [{'Title': ['This department offers no courses for the selected term.']}] 
    


