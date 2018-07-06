import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

while 1 == 1:
    list1 = []

    file = open("Hours.txt", "a") # opens a file or if doesnt exists makes it.
    file.write("--------------------------"+str(datetime.now())+"---------------------------------------------"+" \n" )

    r  = requests.get("STEAM PROFILE URL HERE")# enter steam url

    data = r.content

    soup = BeautifulSoup(data)

    number = ""
    hours = (soup.find_all("div", {"class": "recentgame_quicklinks recentgame_recentplaytime"}))
    for item in hours:
        number = item.text
        file.write(str(number) +"\n" )




    a  = requests.get("STEAM PROFILE URL HERE")# enter steam url
    soup = BeautifulSoup(a.content)



    games = (soup.find_all("div", {"class": "game_name"}))

    for item in games:
        number = item.text
        list1.append(number)


    games = (soup.find_all("div", {"class": "game_info_details"}))
    count = 0
    for item in games:
        number = str(item.text)
        file.write(str(number) + list1[count]+ "\n" )
        print(list1[count])
        count = count + 1 
    file.close()
    time.sleep(3600)


