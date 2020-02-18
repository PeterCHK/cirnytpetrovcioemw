#unzip compressed gz file
gunzip -k access.log.gz

#Count​ the total​ number​ ​ of HTTP​ requests​ recorded​ by​ this​ access​ logfile
cat access.log | grep -c HTTP
#85951

#Find​ the top-10​ (host)​ hosts​ makes​ most​ requests​ from​ 2019-06-10​ 00:00:00​ to 2019-06-19​ 23:59:59,​ inclusively
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

#Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​ to the source IP)
# Step 1. make a list of ip
cat access.log | awk '{print $1}' | grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}" | uniq -c | sort -n -r > ip.txt
