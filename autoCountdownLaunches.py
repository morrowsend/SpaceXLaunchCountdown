# #How to make python run the "getLaunchList" function every day at 1am: https://stackoverflow.com/a/15090893

from datetime import datetime, timedelta
from threading import Timer
from datetime import datetime, time, timedelta
from threading import Timer
from time import sleep


def hello_world():
    print ("hello world")


def main():
    launchDate = 'Tue Jun 07, 2022 21:03:00'
    #launchDate = getLaunchList();
    days = countdown(launchDate, datetime.now()) #pass the launch date and current date to the countdown function
    unit = get_days_unit(days) 



# Set up next time to get next rocket launch from website API
    x=datetime.today()

    y = x.replace(day=x.day, hour=15, minute=57, second=10, microsecond=0) + timedelta(days=0) #at 1:00am tomorrow...
    delta_t=y-x #get the difference from now until the next time we want to run the check of launches

    t = Timer(delta_t.total_seconds(), hello_world) # In that number of seconds, run the function named "getLaunchList"
    t.start()
    print("Still working")
    sleep(1)
    print("still...")





if __name__ == "__main__":
    main()
