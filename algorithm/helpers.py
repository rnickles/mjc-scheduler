def name( course ): return course['Name'][0].strip()
def days( course ): return course['Days']
def times( course ): return course['Times']
def section( course ): return course['Section'][0].strip()

def convert12to24(split_time):
    half = split_time[1][2:].strip()
    split_time[0] = int(split_time[0]) % 12
    if half == 'A':
        return
    else:
        split_time[0] += 12

def strToFloats( tstring ):
    "11:00A - 12:00P"
    start, end = tstring.split(" - ")
    start, end = start.split(":"), end.split(":")
    convert12to24(start); convert12to24(end) 
    shr, smin = map( float, [start[0],start[1][:2]] )
    ehr, emin = map( float, [end[0],end[1][:2]] )
    return shr + smin / 60.0, ehr + emin / 60.0

def overlap(t1, t2):
    t1, t2 = strToFloats(t1), strToFloats(t2)
    # Considers exactly-adjacent times as overlapping, 
    # e.g. overlap(11:00-12:00, 12:00-1:00) == True
    return t2[0] <= t1[0] <= t2[1] or \
        t2[0] <= t1[1] <= t2[1] 

def weekly_calender( course ):
    "[[ [M,F], 11:00AM - 12:00PM ], [ [M, TH], 01:00AM - 02:00AM ]]"
    weekly_calender = {}
    daysAndTimes = zip(days(course), times(course))
    for dys, tmes in daysAndTimes:
        for d in dys:
            if not weekly_calender.has_key( d ):
                weekly_calender[ d ] = [tmes]
            else:
                weekly_calender[ d ] += [tmes]
    return weekly_calender
