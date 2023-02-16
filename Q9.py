from datetime import datetime, timedelta

def difference(start_time, end_time):

    night_interval_hr = []
    while end_time > start_time:
        if datetime(start_time.year, start_time.month, start_time.day,0,0,0) < start_time < datetime(start_time.year, start_time.month, start_time.day,6,0,0):
            night_interval_hr.append((start_time, start_time + timedelta(hours=1)))
        start_time += timedelta(hours=1)

    night_hr = [(date[-1]-date[0]).total_seconds() for date in night_interval_hr]
    total_night_hr = sum(night_hr)/3600
    time_difference_seconds = (end_time - start_time).total_seconds()
    time_difference_hours = time_difference_seconds / 3600
    return time_difference_hours-total_night_hr

if __name__ == "__main__":
    start_time =  datetime.strptime("2022-10-18 02:00:00", "%Y-%m-%d %H:%M:%S")
    end_time =  datetime.strptime("2022-10-18 08:00:00", "%Y-%m-%d %H:%M:%S")

    print(difference(start_time, end_time))


