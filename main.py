import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        host = 'https://cloud-api.yandex.net:443/'
        uri = 'v1/disk/resources/upload/'
        url = host + uri
        params = {'path': f'/{file_path}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        upload_link = response.json()['href']
        response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))
        return response.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    if result == 201:
        print("Успешно загружено.")
