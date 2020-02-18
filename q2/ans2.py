import subprocess
import json
import argparse
import sys
import os
import pathlib
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("USERNAME")

currpath = pathlib.Path(__file__).parent.absolute()
parser = argparse.ArgumentParser(description='Take name tag and return public ip with ssh login.')
parser.add_argument('nametag',
                    metavar='nametag',
                    default=None,
                    action='store',
                    help='input valid aws name tag into the system')
args = parser.parse_args()
nametag = sys.argv[1]
#nametag = '0005-nagios-kpex-asia'

ip = ''
with open(os.path.join(currpath, 'addresses.txt')) as json_file:
    data = json.load(json_file)

    for i in range(len(data['Addresses'])):
        try:
            if data['Addresses'][i]['Tags'][0]['Value'] == nametag and \
            data['Addresses'][i]['Tags'][0]['Key'] == 'Name':
                ip = data['Addresses'][i]['PublicIp']
                break
        except KeyError:
            pass

if ip:
    awssh_path = os.path.join(currpath, 'awssh.sh')
    script = "{0} {1} {2}".format(awssh_path,username,ip)

    print('ssh {0}@{1}'.format(username,ip))
    subprocess.call(script, shell=True)
else:
    print('Host​ not​ found')
