from flask import Flask, jsonify

from get_video_location_url import GetDaumTVPotUrl

app = Flask(__name__)
mcache = {}

@app.route("/")
def hello():
    return '다음티비팟 src url 뽑아내기<br>/:clip_id'

@app.route("/<int:clip_id>")
def get_video_src(clip_id):
    if clip_id not in mcache:
        mcache[clip_id] = GetDaumTVPotUrl(clip_id)
    instance = mcache[clip_id]
    video_src = instance.get_video_location_url()
    return jsonify(video_src=video_src)

if __name__ == '__main__':
    app.secret_key = 'plz, generate secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=19999, debug=False, use_reloader=True)
