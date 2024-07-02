import threading
import requests
import os


def download_file(url, folder):
    local_filename = os.path.join(folder, url.split('/')[-1])
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"Download {local_filename}")


urls = [
    "https://learnsql.com/blog/sql-window-functions-cheat-sheet/Window_Functions_Cheat_Sheet.pdf",
    "https://learnsql.com/blog/mysql-cheat-sheet/mysql-cheat-sheet-a4.pdf",
    "https://learnsql.com/blog/sql-basics-cheat-sheet/sql-basics-cheat-sheet-a4.pdf"
]

download_folder = "/home/abdallah/Desktop/learnSQL"
os.makedirs(download_folder, exist_ok=True)

threads = []

for url in urls:
    thread = threading.Thread(target=download_file, args=(url, download_folder))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All files have been downloaded!")
