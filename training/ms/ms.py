
import requests
from pprint import pprint



url = "https://api.moysklad.ru/api/remap/1.2/entity/metadata?filter=type=paymentout=states"
headers = {
    "Authorization": "9c10e0dc4b1b681143e68c18a5f647e9b6480216",
    "Accept-Encoding": "gzip"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('успех')
    pprint(response.json())
else:
    # Обработка ошибки, если запрос не удался
    print(f"Ошибка запроса: {response.status_code} - {response.reason}")
