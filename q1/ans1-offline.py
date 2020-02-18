#Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​ to the source IP)
#Step 2. count the number of countries
import requests
import re
import MySQLdb
import pandas as pd

DB_IP='127.0.0.1'
DB_user='crypto'
DB_pass='good-firm'
DB_name='crypto'
db = MySQLdb.connect(host=DB_IP, user=DB_user, passwd=DB_pass, db=DB_name, charset='utf8')

counter = dict()
file = open('ip4.txt', 'r')
Lines = file.readlines()

country_count = {}
for line in Lines:
    if line not in ['\n', '\r\n']:
        count = int(line.split()[0])
        ip = line.split()[1]

        regex = re.compile('([\d+]{1,3}).([\d+]{1,3}).([\d+]{1,3}).([\d+]{1,3})')
        matched = regex.match(ip)
        ip_num = int(matched.group(1))*pow(256,3) + int(matched.group(2))*pow(256,2) \
                + int(matched.group(3))*pow(256,1) + int(matched.group(4))*pow(256,0) #display for clarity
        df = pd.read_sql("select country from ip where `from` <= {0} and `to` >= {0}".format(ip_num), con=db) #assume no risk of sql injection

        try:
            country_count[df['country'][0]]
        except KeyError:
            country_count[df['country'][0]] = 0
        finally:
            country_count[df['country'][0]] += count

print(country_count)
