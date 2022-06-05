


##########################################################################

# from datetime import datetime
# import os
# import sys
# import time
# import requests # for rocket website API


# def countdown(launchDate, now): #reference: https://www.sololearn.com/Discuss/1530780/how-can-i-get-python-to-countdown-to-a-set-date-in-the-future
#    
    
#     dateFormat = '%a %b %d, %Y %H:%M:%S'      # Tell python how launch date is formatted useing the symbols described here: https://www.geeksforgeeks.org/how-to-format-date-using-strftime-in-python/
                  
#     futuredate = datetime.strptime(launchDate, dateFormat)

#     nowdate = datetime.now()
#     count = int((futuredate-nowdate).total_seconds())

#     days = count//86400
#     hours = (count-days*86400)//3600
#     minutes = (count-days*86400-hours*3600)//60
#     seconds = count-days*86400-hours*3600-minutes*60
#     print("{} days {} hours {} minutes {} seconds left".format(days, hours, minutes, seconds))

#     #If you want to convert to EST and take care of calculating daylight 
#     # savings time, add this: https://stackoverflow.com/questions/48416511/how-to-convert-utc-to-est-with-python-and-take-care-of-daylight-saving-automatic

# def getLaunchList():
#     # This is the rocket code
#     response = requests.get("https://fdo.rocketlaunch.live/json/launches/next/5")
#     json = response.json()
#     jsonResults = json['result']

#     # print(jsonResults['result'])

#     numSpaceXlaunches=0
#     for launch in jsonResults:
#         # print (launch['name'])
#         if not numSpaceXlaunches and launch['provider']['name']=='SpaceX':
#             numSpaceXlaunches+=1
#             print('Next SpaceX Launch:')           
#             print(launch['launch_description']+"\n")          # The 'quicktext' gives similar info as 'launch_description' but also has a link to stream the launch live
            
#             # print(launch['quicktext']) 
#             quicktextDateString = launch['quicktext']
#             launchDateString = quicktextDateString.split(' - ')[2]  #split the quicktext description to only return the launch date
#             launchDate = launchDateString.split(' U')[0]
#             # print("Launch T0 = ",launch["t0"])
#             # print("Est Date: ",launch["est_date"])
#             # print('current launch time is ', launch['win_open'])
#             return (launchDate)
#             break

#     if numSpaceXlaunches==0:
#         print("Womp womp, no SpaceX in the next 5 expected launches")
#         return ()



# def main():
#     launchDate = 'Tue Jun 07, 2022 21:03:00'
#     #launchDate = getLaunchList();
#     days = countdown(launchDate, datetime.now()) #pass the launch date and current date to the countdown function
#     unit = get_days_unit(days)
    
    




# def get_days_unit(count):
#     if count == 1:
#         return "day"

#     return "days"


# if __name__ == "__main__":
#     main()






##########################################################################
# #How to make python run the "getLaunchList" function every day at 1am: https://stackoverflow.com/a/15090893
# from datetime import datetime, timedelta
# from threading import Timer
# from datetime import datetime, time, timedelta
# from threading import Timer
# from time import sleep


# def hello_world():
#     print ("hello world")
#     #...

# x=datetime.today()

# y = x.replace(day=x.day, hour=15, minute=54, second=0, microsecond=0) + timedelta(days=0) #at 1:00am tomorrow...
# delta_t=y-x #get the difference from now until the next time we want to run the check of launches

# t = Timer(delta_t.total_seconds(), hello_world) 
# t.start()
# print("Still working")
# sleep(1)
# print("still...")


##########################################################################








# # Countdown timer reference: https://gist.github.com/morion4000/3866374?permalink_comment_id=2852932#gistcomment-2852932
# from datetime import datetime, time, timedelta
# from threading import Timer
# from time import sleep

# def dateDiffInSeconds(date1, date2):
#   timedelta = date2 - date1
#   return timedelta.days * 24 * 3600 + timedelta.seconds

# def daysHoursMinutesSecondsFromSeconds(seconds):
# 	minutes, seconds = divmod(seconds, 60)
# 	hours, minutes = divmod(minutes, 60)
# 	days, hours = divmod(hours, 24)
# 	return (days, hours, minutes, seconds)


# dateFormat = '%a %b %d, %Y %H:%M:%S'      # Tell python how launch date is formatted useing the symbols described here: https://www.geeksforgeeks.org/how-to-format-date-using-strftime-in-python/
# launchDate = 'Tue Jun 07, 2022 21:03:00'


# req = datetime.strptime(launchDate, dateFormat)
# now = datetime.now()

# while req>now:
#     print("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
#     sleep(1)
#     now = datetime.now()

# print("Done")