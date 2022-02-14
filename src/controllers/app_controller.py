from src.managers import SpreadSheetManager
from src.helpers import RelativePathHelper
import datetime
import random
import pandas

class AppController(object):
    #date should be mm-dd-yyyy
    def generate_schedule_for_day(self,date):
        pn = [1,-1]
        self.lunch = datetime.timedelta(hours=5, minutes=45)
        self.lunch_noise = datetime.timedelta(minutes=random.randrange(1, 30))  # minutes
        self.start_end_noise = datetime.timedelta(minutes=random.randrange(1, 10))
        self.break_length = datetime.timedelta(minutes=30)  # minutes
        self.work_time = datetime.timedelta(hours=8)
        self.break_noise = datetime.timedelta(minutes=random.randrange(1, 10))
        self.end_noise = datetime.timedelta(minutes=random.randrange(1, 10))

        day = datetime.datetime.strptime(date, "%m-%d-%Y") + datetime.timedelta(hours=6)
        start_time = day + (random.choice(pn) * self.start_end_noise)
        break_start = day + (self.lunch + (random.choice(pn) * self.lunch_noise))
        break_time = self.break_length + (random.choice(pn) * self.break_noise)
        break_end = break_time + break_start
        end_time = day + (self.work_time + (random.choice(pn) * self.end_noise))

        print("date",day.strftime("%m-%d-%Y"))
        print("start time:", start_time.strftime("%H:%M"))
        print("break start:", break_start.strftime("%H:%M"))
        print("break end:",break_end.strftime("%H:%M"))
        print("break time:", int(break_time.seconds/60))
        print("end time:",end_time.strftime("%H:%M"))
        time_length = int(int(int(break_time.seconds)/60))
        print(time_length)

        return [day.strftime("%m-%d-%Y"),
                start_time.strftime("%H:%M"),
                break_start.strftime("%H:%M"),
                break_end.strftime("%H:%M"),
                end_time.strftime("%H:%M")]


    def __init__(self):
        table = [["date", "start time", "break start", "break end", "end time"]]

        date_list = pandas.date_range(datetime.datetime(year=2022,month=1,day=5), datetime.datetime(year=2022,month=5,day=1) - datetime.timedelta(days=1), freq='d')
        for date in date_list:
            table.append(self.generate_schedule_for_day((date.strftime("%m-%d-%Y"))))
        with SpreadSheetManager("text.xlsx") as spreadsheet:
            spreadsheet.write_2dlist_to_table(table)

