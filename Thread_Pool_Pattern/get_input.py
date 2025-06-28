import os

def get_input():
    print("ダウンロードしたいurlを一行ずつ入力してください。終了する場合は'DONE'と入力してください")
    print("-" * 20)
    urls = []
    while True:
        url = input().strip()
        # strip(): 文字列と先頭と末尾にある空白文字をすべて削除
        if url.upper() == 'DONE':
            if not urls:
                print("URLが入力されていません。終了します。")
                return None, None
            break
        if url.startswith('http'):
            urls.append(url)
        elif url:
            print(f"{url}は無効なURLです。")

    while True:
        local_path = input("ダウンロード先のディレクトリパスを入力してください： ").strip()
        # 入力されたパスが実際に存在するパスかどうかをチェック
        if os.path.isdir(local_path):
            return urls, local_path
        else:
            print("Error: 有効なディレクトリではありません。")
