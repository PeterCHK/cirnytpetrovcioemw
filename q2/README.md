sudo apt update
sudo apt install python3 awscli pip3 -y
sudo pip3 install subprocess
sudo pip3 install json
sudo pip3 install argparse
sudo pip3 install pathlib
sudo pip3 install dotenv
#for formal development, a separate venv is created, pip3 freeze > requirements.txt and pip3 install -r requirements.txt is used.

aws configure
#obtain the credentials from AWS IAM > Users > 'user' > Security Credentials > Create access key
#AWS Access Key ID [****************6G2G]:
#AWS Secret Access Key [****************2LaZ]:

#input the commonly used region
#Default region name [ap-southeast-1]:
#Default output format [None]:

bash ans2.sh

#in the terminal, type the correct path that has the ans2.py
alias awssh='python3 /home/pc/projects/interview/crypto.com/q2/ans2.py'

#set the default username at .env file, e.g. 'ec2-user'

#Then run in terminal, e.g.
awssh 0005-nagios-kpex-asia
