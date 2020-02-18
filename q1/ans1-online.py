#Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​ to the source IP)
#Step 2. count the number of countries
import requests
import re

counter = dict()

file = open('ip-test.txt', 'r')
Lines = file.readlines()
for line in Lines:
    if line not in ['\n', '\r\n']:
        count = line.split()[0]
        ip = line.split()[1]
        url = 'http://api.hostip.info/get_html.php?ip={0}'.format(ip)
        req = requests.get(url)

        regex = re.findall(r'\(([A-Z]{2})\)',req.text)

        if regex[0] in counter:
            counter[regex[0]] += int(count)
        else:
            counter[regex[0]] = 1
print(counter)
