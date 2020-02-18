from flask import Flask, redirect, url_for, request, jsonify
import string
from random import choices
app = Flask(__name__)

url_dict = {}
def generate_short_link():
    characters = string.digits + string.ascii_letters
    short_url = ''.join(choices(characters, k=9))
    return short_url

@app.route('/newurl', methods=['POST'])
def shorturl():
    url = request.json['url']
    short_url = generate_short_link()
    url_dict[short_url] = url
    return jsonify({'url':url, 'shortenUrl':'https://shortenurl.org/'+short_url}), 201

@app.route('/<shorturl>', methods=['GET'])
def geturl(shorturl):
    return redirect(url_dict[shorturl]), 304

if __name__ == '__main__':
   app.run(debug = True, host= '0.0.0.0')

#curl -i -H "Content-Type: application/json" -X POST -d '{"url":"google.com"}' http://localhost:5000/newurl
#curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/<shorturl>
