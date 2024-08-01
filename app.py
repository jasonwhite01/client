from flask import Flask, jsonify
from flask_cors import CORS
from rssfeedreader import newsItems

NEWS_ITEMS = newsItems()

#config
DEBUG = True

#instantiate app
app = Flask(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins':'*'}})

@app.route('/feeds', methods=['GET'])
def all_newsItems():
    return jsonify({
        'status' : 'success',
        'members' : NEWS_ITEMS
    })

if __name__ == '__main__':
    app.run()