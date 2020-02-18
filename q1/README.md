sudo apt update
sudo apt install python3 awscli pip3 -y
sudo pip3 install requests
sudo pip3 install re
sudo pip3 install MySQLdb
sudo pip3 install pandas
#for formal development, a separate venv is created, pip3 freeze > requirements.txt and pip3 install -r requirements.txt is used.

#run ans1.sh on bash to get the results of
#1a. Count​ the total​ number​ ​ of HTTP​ requests​ recorded​ by​ this​ access​ logfile using ans1.sh
cat access.log | grep -c HTTP
#85951

#1b. Find​ the top-10​ (host)​ hosts​ makes​ most​ requests​ from​ 2019-06-10​ 00:00:00​ to 2019-06-19​ 23:59:59,​ inclusively using ans1.sh
cat access.log | grep '1[0-9]/Jun/2019' | awk '{print $1}' | uniq -c | sort -n -r | head -n 10
#    730 118.24.71.239
#    637 1.222.44.52
#    371 119.29.129.76
#    352 119.29.129.76
#    177 136.243.70.151
#    143 148.251.41.239
#    139 5.9.152.73
#    137 95.216.38.186
#    119 148.70.14.32
#    109 5.9.71.213

#1c. Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​ to the source IP)
#My thought process is to first have a list of ip in one file and use uniq -c to speed up the execution process, using ans1.sh
cat access.log | awk '{print $1}' | grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}" | uniq -c | sort -n -r > ip.txt

#Then I found a public available api for geoip (http://api.hostip.info/) and use regex to extract the country info at ans1-offline.py
#I made ip-test.txt to test the system is indeed working
#After a while, the cli is not returning correct values the request probably due to a high request frequency.

#Then I downloaded IP2LOCATION-LITE-DB1.CSV from http://download.ip2location.com/lite/ and renamed the columns as "from","to","short","country" for clarity and transfer to mysql
#Then I transferred into mysql database using ans1.sql
#Then I used ans1-offline.py to find out all the requests originating countries using global maximum method.
#After waiting some time, here is the result.
#{'China': 23482, 'Russian Federation': 1038, 'Hong Kong': 3869, 'Thailand': 942, 'Korea (Republic of)': 963, 'United States of America': 29527, 'Germany': 15148, 'Finland': 3244, 'Poland': 220, 'Netherlands': 439, 'Taiwan (Province of China)': 185, 'United Kingdom of Great Britain ': 575, 'Norway': 156, 'Ukraine': 383, 'Indonesia': 89, 'France': 3307, 'Ireland': 69, 'Canada': 228, 'Romania': 135, 'Australia': 80, 'Spain': 58, 'United Arab Emirates': 13, 'Belgium': 14, 'Switzerland': 29, 'Bangladesh': 35, 'Japan': 127, 'Angola': 8, 'Singapore': 32, 'Bulgaria': 8, 'Latvia': 13, 'Sweden': 16, 'Macao': 12, 'Austria': 5, 'India': 42, 'Algeria': 4, 'Brazil': 72, 'Viet Nam': 64, 'Cambodia': 4, 'Jordan': 4, 'Iran (Islamic Republic of)': 44, 'Estonia': 2, 'Denmark': 2, 'Italy': 27, 'Czechia': 5, 'Turkey': 760, 'Belize': 2, 'Mexico': 4, 'Hungary': 1, 'Belarus': 2, 'Greece': 3, 'Lebanon': 3, 'Saint Vincent and The Grenadines': 1, 'Luxembourg': 1, 'Argentina': 7, 'South Africa': 5, 'Lesotho': 1, 'Saint Kitts and Nevis': 4, 'Portugal': 1, 'Colombia': 5, 'Kenya': 1, 'Nigeria': 2, 'Egypt': 2, 'Pakistan': 1, 'Slovenia': 1, 'Peru': 3, 'Chile': 3, '-': 1, 'Ecuador': 1, 'Saint Martin (French Part)': 1, 'Morocco': 1, 'Malaysia': 1}

#Hence, USA has the most requests originating from.
