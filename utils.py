import os
import time


def wait_for_download_complete(folder: str, expected_filename: str, timeout: int = 30) -> str:
    """
    Ждёт, пока не исчезнут .crdownload-файлы и не появится нужный файл.
    """
    expected_path = os.path.join(folder, expected_filename)
    start = time.time()

    while time.time() - start < timeout:
        files = os.listdir(folder)
        downloading = any(f.endswith('.crdownload') for f in files)
        if not downloading and expected_filename in files:
            return expected_path
        time.sleep(0.5)

    raise TimeoutError(f"Файл {expected_filename} не был скачан за {timeout} секунд.")


def get_file_size_mb(path: str) -> float:
    size_bytes = os.path.getsize(path)
    size_mb = size_bytes / (1024 * 1024)
    return round(size_mb, 2)
