import portion as P
from datetime import datetime, timedelta, time


def difference(start_time, end_time):
    # I have take starting time to its 12:00:00 AM because we needed in separation of night time for particular day.
    start_date_am = datetime.combine(start_time.date(), datetime.min.time())
    night_interval_dt = []
    # i have iterated over loop of date and capture in interval of night time by using timedelta.
    while start_date_am <= end_time:
        night_interval_dt.append(
            P.closed(
                datetime.combine(start_date_am, time()),
                datetime.combine(start_date_am, time()) + timedelta(hours=6),
            )
        )
        start_date_am += timedelta(days=1)
    # Here i have intersection night_time from total_time interval.
    interval_night = [
        P.closed(start_time, end_time).intersection(night_time)
        for night_time in night_interval_dt
    ]
    # i have calculate total time in hours
    total_time = (end_time - start_time).total_seconds() / 3600
    # Here i have calculate total_night_time in hours
    total_night_time = sum(
        [(i.upper - i.lower).total_seconds() / 3600 for i in interval_night]
    )
    return total_time - total_night_time


if __name__ == "__main__":
    user_input_start_time = str(input("Enter the Start Time: "))
    user_input_end_time = str(input("Enter the End Time: "))
    start_time = datetime.strptime(user_input_start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(user_input_end_time, "%Y-%m-%d %H:%M:%S")
    print(
        "The Total Time Difference in Hours is : {}".format(
            difference(start_time, end_time)
        )
    )
