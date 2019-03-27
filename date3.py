# -*- coding: utf-8 -*-
import urllib.request
from time import strftime
from datetime import timedelta, datetime
import matplotlib.pyplot as mp
import re

data = urllib.request.urlopen("http://www.dwa.gov.za/Hydrology/RTData.aspx?Station=C1H006FW&Type=Data")
text = data.read().decode('utf-8')
#text = text.replace("<br>","\n")
lines = re.findall(r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s+(\d+\.\d+)\s+(\d+\.\d+)',text)

value=[]
date=[]
hour=[]

for line in lines:
    ldatetime, ltemp, lflow = line
    ldatetime = datetime.strptime(ldatetime,'%Y-%m-%d %H:%M')
    if (datetime.now() - ldatetime) <= timedelta(1): 
        value.append(ltemp)
        date.append(ldatetime)
mp.plot(date,value)
mp.title("Stream flow for C1H006")
mp.xlabel('Date and Time')
mp.ylabel('Streamflow')
mp.show()
