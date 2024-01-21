##準備
    python3 manage.py makemigrations
    python3 manage.py migrate

## サーバー起動
    gunicorn mysite.asgi:application -w 4 -k uvicorn.workers.UvicornWorker -t 120

http://http://127.0.0.1:8000

### ホーム画面（アニメリスト）
<img width="1280" alt="Screenshot 2024-01-21 at 17 10 18" src="https://github.com/SeiyaKamata/Mysite/assets/58635523/1e4fd1ac-afe7-4fa0-a636-d76eecc511d7">

### アニメ詳細画面
ジャンルや放送時期、主題歌や聖地などの情報
<img width="1280" alt="Screenshot 2024-01-21 at 17 12 10" src="https://github.com/SeiyaKamata/Mysite/assets/58635523/3e6886a8-2240-4582-9893-7c293001303d">
