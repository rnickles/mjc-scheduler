half = [ i +':00'for i in ['12', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']] 
curry_me = lambda s: lambda i: i + s 
am = curry_me('A')
pm = curry_me('P')
times = map(am, half) + map(pm, half) 
relevant_times = times[6:23]
days = dict( zip( ['M','T','W','TH','F'], range(5) ) )

def split_time(hour):
    colon = hour.find(':')
    return hour[:colon] + ":00" + hour[-1], int(hour[colon+1:-1])

def set_origin(ox, oy):
    def give_point(day,hour):
        hour, min = split_time(hour)
        x_gap, y_gap = 110, 40
        return \
            [days[day]*x_gap + ox, relevant_times.index(hour)*y_gap + (y_gap*(min/60.0)) + oy]
    return give_point

def extract_times( time_string ):
    spl = time_string.split()
    if len(spl) >= 3:
        return spl[0], spl[2]
    else:
        return '06:00A', '06:00A'

def find_critical_time(schedule, f):
    all_times = []
    for item in map(lambda d: d['Times'], schedule):
        all_times += item
    get_start_hour = lambda t: split_time(extract_times(t)[0])[0]
    start_hours = map( get_start_hour, all_times )
    get_int_from_hour = lambda t: int(t[:2])
    return f(start_hours, key=get_int_from_hour)

def earliest_time(schedule):
    return find_critical_time(schedule, min)

def latest_time(schedule):
    return find_critical_time(schedule, max)
