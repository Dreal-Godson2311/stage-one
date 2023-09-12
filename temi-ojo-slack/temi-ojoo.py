import pprint
from flask import *
import json, time
import datetime
from flask import Flask, request, jsonify



app = Flask(__name__)
utc_time = datetime.datetime.utcnow()
weekday = datetime.datetime.today().weekday()
weekday_str = "Monday" if weekday == 0 else "Tuesday" if weekday == 1 else "Wednesday" if weekday == 2 else "Thursday" if weekday == 3 else "Friday" if weekday == 4 else "Saturday" if weekday == 5 else "Sunday"

@app.route('/', methods=['GET'])
def home_page():
    data_set ={'Page':'Home', 
               'Message':'Successfully loaded the home page',
               'current_day': weekday_str, 
               'utc_time': utc_time.isoformat().split('.')[0]}
    
    
    
    return jsonify(data_set)

@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    data_set ={'Slack_name':f'{user_query}',
               'current_day': weekday_str,'utc_time': utc_time.isoformat().split('.')[0],
               'track':'backend',
               "github_file_url": "https://github.com/Dreal-Godson2311/stage-one.git",
               "github_repo_url": "https://github.com/Dreal-Godson2311/stage-one/blob/main/temi-ojo-slack/temi-ojoo.py",
               "status_code": 200}
    
    
    
    
    return jsonify(data_set)

if __name__ == '__main__':
    app.run(port=2307)
