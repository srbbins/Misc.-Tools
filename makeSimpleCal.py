import datetime

#increment date
startDate=datetime.date.today()
endDateTime=datetime.datetime(2013, 1, 1)
endDate=datetime.date.fromordinal(endDateTime.toordinal())
dayToPrint=startDate
weekdays=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#outFile=open(r"C:\Documents and Settings\srobbins\Desktop\cal.txt")
while dayToPrint.toordinal()<=endDate.toordinal():
    dateString=str(dayToPrint)
    #outFile.write("")
    print dateString.split()[0]+' '+weekdays[dayToPrint.weekday()]+': '
    dayToPrint=datetime.date.fromordinal(dayToPrint.toordinal()+1)
    
