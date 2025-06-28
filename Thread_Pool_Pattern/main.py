import time
import concurrent.futures

from task import download_function
from get_input import get_input

def main():
    urls, directory_path = get_input()

    if not urls:
        return
    
    print(f"\n{len(urls)}個のファイルをダウンロードします。")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # pathをそのまま第二引数に渡してしまうとエラーをはく可能性がある。mapメソッドはリストを期待しているため。
        results = executor.map(lambda url: download_function(url, directory_path), urls)

        for r in results:
            print(f"受け取った結果: {r}")
    
    end_time = time.time()
    print(f"全タスク完了。所要時間: {end_time - start_time}秒")


if __name__ == '__main__':
    main()

