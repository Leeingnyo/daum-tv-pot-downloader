import requests

class GetDaumTVPotUrl():
    video_location_url = None;

    def __init__(self, clip_id):
        self.clip_id = clip_id

    def is_valid(self):
        if self.video_location_url is not None:
            r = requests.head(self.video_location_url)
            print(r.status_code)
            print(r.status_code == requests.codes.ok)
            return r.status_code == requests.codes.ok
        else:
            return False

    def get_video_location_url_from_server(self, clip_id):
        get_uuid_tid_url = 'https://tv.kakao.com/api/v1/ft/cliplinks/{clip_id}/impress?player=monet_html5&service=tvpot&section=&dteType=PC'
        get_video_link_url = 'https://tv.kakao.com/api/v1/ft/cliplinks/{clip_id}/raw?player=monet_html5&uuid={uuid}&service=tvpot&tid={tid}&section=&profile=MAIN&dteType=PC'

        params = {'clip_id': clip_id}
        r = requests.get(get_uuid_tid_url.format(**params))
        jr = r.json()
        clip_id = jr['clipLink']['id']
        uuid = jr['uuid']
        tid = jr['tid']

        params = {'clip_id': clip_id, 'uuid': uuid, 'tid': tid}
        r = requests.get(get_video_link_url.format(**params))
        jr = r.json()
        video_location_url = jr['videoLocation']['url']

        self.video_location_url = video_location_url
        return video_location_url

    def get_video_location_url(self):
        if not self.is_valid():
            self.get_video_location_url_from_server(self.clip_id)
        return self.video_location_url
