# 다음티비팟, 유튜브 영상 다운로더

학문적 호기심일 뿐

사용하면 카카오티비, 유튜브 약관에 의해 제제를 당합니다.

## 제작 목적

영상에서 일정 시각이 되면 행동이 일어나도록 하는 걸 만드려고 raw한 비디오가 필요했다 (video 태그로 넣을).

근데 유튜브는 [이미 있음](https://developers.google.com/youtube/iframe_api_reference) ㄷㄷ 갓...  
카카오는 없음 ㅠㅠ 문의했는데 딴 소리만 답변으로 옴 ㅠㅠ 플레이어 API 만들어주세요.  
유튜브도 사실 시각을 초만 지원해서 좀... 밀리초로 해주면 어디 덧나나!

## 쓰는 법

### run

```sh
pip install -r requirements.txt
python3 webserver.py
```

### routes

```
/tvpot/:clip_id
/youtube/:video_id
```

유튜브는 영상이 바로 나오고,
티비팟은 json으로 줌

이렇게 나눈 이유는 유튜브에 서버의 아이피가 나와서... src르 넣었을 때 안 보이게 하려고 그렇게 함
