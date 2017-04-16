from flask import Flask, jsonify, redirect

from crossdomain import crossdomain
from get_video_location_url import GetDaumTVPotUrl
from get_youtube_raw_url import GetYoutubeUrl

app = Flask(__name__)
t_mcache = {}
y_mcache = {}

@app.route("/")
def hello():
    return '<p>다음티비팟 뽑아내기<br>/tvpot/:clip_id</p><p>youtube 뽑아내기<br>/youtube/:video_id</p>'

@app.route("/tvpot/<int:clip_id>")
@crossdomain(origin='*')
def get_tvpot_video_src(clip_id):
    if clip_id not in t_mcache:
        t_mcache[clip_id] = GetDaumTVPotUrl(clip_id)
    instance = t_mcache[clip_id]
    video_src = instance.get_video_location_url()
    return jsonify(video_src=video_src)

'''
@app.route("/youtube/<video_id>")
@crossdomain(origin='*')
def get_youtube_video_src(video_id):
    if video_id not in y_mcache:
        y_mcache[video_id] = GetYoutubeUrl(video_id)
    instance = y_mcache[video_id]
    video_src = instance.get_youtube_raw_video()
    return redirect(video_src)
'''

if __name__ == '__main__':
    app.secret_key = 'plz, generate secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=19999, debug=False, use_reloader=True)
