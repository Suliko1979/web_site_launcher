
import datetime
import webbrowser

alarmHour = int(input("Час запуска:  "))
alarmMinute = int(input("Минута запуска:  "))
web_site = input('Web-site you want to launch at the assigned time:    ')

while (1==1):
    if (alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
        webbrowser.open(web_site, new=1)
        break


