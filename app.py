from flask import Flask, jsonify, request
from flask_cors import CORS
from rssfeedreader import newsItems
from rssfeedsave import saveFeed
import json

NEWS_ITEMS = newsItems()

#config
DEBUG = True

#instantiate app
app = Flask(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins':'*'}})

@app.route('/feeds', methods=['GET','POST'])
def all_newsItems():
    if request.method=='GET':
        return jsonify({
            'status' : 'success',
            'members' : NEWS_ITEMS
        })
    if request.method=='POST':
        print('post received with data: ' + json.dumps(request.json))
        # call persistence function in another python file
        feedDataToPersist = request.json
        print('title data to persist: ' + feedDataToPersist["title"])
        saveFeed(feedDataToPersist["title"], feedDataToPersist["description"], feedDataToPersist["podcasturl"])
        return jsonify({
            'status' : 'success',
            'members' : NEWS_ITEMS
        })

#put data from selected feeds into database
@app.route('/feeds/selectedfeeds', methods=['GET','POST'])
def selected_feeds():
    if request.method=='POST':
        return '--- post ---'
    if request.method=='GET':
        return '--- get ---'

if __name__ == '__main__':
    app.run()