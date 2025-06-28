import os
import urllib.request
from urllib.parse import urlparse

def download_function(url, directory_path):

    try:
        # urlの分解
        parsed_url = urlparse(url)
        # pathの最後の文字列を取得
        filename = os.path.basename(parsed_url.path)

        if not filename:
            filename = "downloaded_file"
        
        # ファイルパスの作成directory_path/filename
        full_path = os.path.join(directory_path, filename)
        print("ダウンロード開始")
        with urllib.request.urlopen(url) as web_file:
            content = web_file.read()
        with open(full_path, 'wb') as local_file:
            local_file.write(content)
        print("ダウンロード済み")
        return f"{directory_path}にダウンロード完了"
    except Exception as e:
        error_message = f"ダウンロードに失敗しました。({e})"
        print(error_message)
