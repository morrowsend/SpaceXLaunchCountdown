from datetime import datetime, timedelta
from pickle import TRUE
from threading import Timer
from datetime import datetime, time, timedelta
from threading import Timer
from time import sleep
import os
import sys
import time
import requests # for rocket website API


debug = False #<-- Set to True so you don't make too many requests from the server. False when you are ready to run for real
launchDate = None #Create a global variable to hold the launch date. (Not the best way to handle this, but simple and effective...)
firstDate = 'Tue Jun 04, 2022 19:14:00'
secondDate = 'Tue Jun 04, 2022 20:00:00'



# function to get difference in seconds between 2 dates
def dateDiffInSeconds(date1, date2): 
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

# out days, hours, minutes, and seconds 
def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)


#function to request next 5 rocket launches in the world, strip out the next one from SpaceX
def getLaunchList():
    response = requests.get("https://fdo.rocketlaunch.live/json/launches/next/5")
    json = response.json()
    jsonResults = json['result']

    # print(jsonResults['result'])

    numSpaceXlaunches=0
    for launch in jsonResults:
        # print (launch['name'])
        if not numSpaceXlaunches and launch['provider']['name']=='SpaceX':
            numSpaceXlaunches+=1
           # print('Next SpaceX Launch:')           
            #print(launch['launch_description']+"\n")          # The 'quicktext' gives similar info as 'launch_description' but also has a link to stream the launch live
            
            # print(launch['quicktext']) 
            quicktextDateString = launch['quicktext']
            launchDateString = quicktextDateString.split(' - ')[2]  #split the quicktext description to only return the launch date
            launchDate = launchDateString.split(' U')[0]
            # print("Launch T0 = ",launch["t0"])
            # print("Est Date: ",launch["est_date"])
            # print('current launch time is ', launch['win_open'])
            return (launchDate)
            break

    if numSpaceXlaunches==0:
        launchDate = None
        print("Womp womp, no SpaceX in the next 5 expected launches")
        return (None)


#This function is used for testing so you don't overrun the rocket server
def FAKEgetLaunchList():
    x=datetime.today()
    x = x.replace(day=x.day, hour=x.hour, minute=x.minute, second=x.second)+ timedelta(seconds=30) # TESTING PURPOSES
    launchDate = None #x.strftime('%a %b %d, %Y %H:%M:%S')
    #print ("FAKE launch date = " +launchDate)
    return (launchDate)



# main funciton here
def main():
    
    #Flow of this code:
    # 1. Start a "forever loop" (while(1))
    # 2. As soon as this script runs, get the next launch date
    # 3. Set up the next time to update the launch date to 1am the next day
    # 4. Display the countdown
    # 5. Once countdown ends, delay for an hour and then check for next launch
    
    # Step 1:
    while(1):
        
        # Step 2:
        if(debug):
            launchDate = FAKEgetLaunchList()
            print("\n loop stated")
        else:
            launchDate = getLaunchList()

        # Set up next time to get next rocket launch from website API
        x=datetime.today()
        
        
        #  Step 3
        if(debug):
            y = x.replace(day=x.day, hour=x.hour, minute=x.minute, second=x.second)+ timedelta(seconds=30) # TESTING PURPOSES
            #print("today is "+str(x))
            delta_t=y-x #get the difference from now until the next time we want to run the check of launches
            t = Timer(delta_t.total_seconds(), FAKEgetLaunchList) #<-- use this so as not to make too many requests from the server

        else:
            y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1) #at 1:00am 1 day from now
            delta_t=y-x #get the difference from now until the next time we want to run the check of launches            
            t = Timer(delta_t.total_seconds(), getLaunchList) # In that number of seconds, run the function named "getLaunchList"

        
        delta_t=y-x #get the difference from now until the next time we want to run the check of launches
        t.start()  # Actually start this thread in the background
       # print("checking next launch at "+str(y))



        #  Step 4:
        if launchDate == None:
            print("No launches scheduled") #<-- Replace with Display code
            sleep(86400) #sleep for 24 hours = 86400 seconds
        else:            
        # Now set up the countdown timer to the next launch. Reference: https://gist.github.com/morion4000/3866374?permalink_comment_id=2852932#gistcomment-2852932
            dateFormat = '%a %b %d, %Y %H:%M:%S'      # Tell python how launch date is formatted useing the symbols described here: https://www.geeksforgeeks.org/how-to-format-date-using-strftime-in-python/
            req = datetime.strptime(launchDate, dateFormat)
            now = datetime.now()
            #print(str(req) + " now = "+ str(now))
            while req>now:
                #This is where you would write to your display
                print("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
                sleep(1)
                now = datetime.now()
            
            print("we have liftoff!") #<-- Replace with Display code
        
            #print("sleep for an hour after liftoff, then start over")
            sleep(3600) #  delay for an hour then get next launch time from the server


if __name__ == "__main__":
    main()
