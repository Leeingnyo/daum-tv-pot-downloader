import requests
from urllib.parse import unquote

def url_decode(url):
    return unquote(url)

class GetYoutubeUrl():
    youtube_raw_video = None

    def __init__(self, video_id):
        self.video_id = video_id

    def is_valid(self):
        if self.youtube_raw_video is not None:
            r = requests.head(self.youtube_raw_video)
            print(r.status_code)
            print(r.status_code == requests.codes.ok)
            return r.status_code == requests.codes.ok
        else:
            return False

    def get_youtube_raw_video_from_server(self, video_id):
        r = requests.get('http://www.youtube.com/get_video_info?el=detailpage&video_id=%s' % (video_id))
        content = str(r.content)
        index = content.find('url_encoded_fmt_stream_map')
        best_quality = url_decode(content[index:].split('&')[0].split('=')[1]).split(',')[0]
        video_info = dict()
        for items in best_quality.split('&'):
            key, value = items.split('=')
            video_info[key] = url_decode(value)
        youtube_raw_video = video_info.get('url', None)
        self.youtube_raw_video = youtube_raw_video
        return youtube_raw_video

    def get_youtube_raw_video(self):
        if not self.is_valid():
            self.get_youtube_raw_video_from_server(self.video_id)
        return self.youtube_raw_video

if __name__ == '__main__':
    test = GetYoutubeUrl('ZTY6DasUCTM')
    print(test.get_youtube_raw_video())
