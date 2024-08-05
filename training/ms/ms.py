
import requests
from pprint import pprint



url = "https://api.moysklad.ru/api/remap/1.2/entity/paymentout/metadata"
headers = {
    "Authorization": "0ab72883c2f0cfea2e92fc4edd45b66a6059d541",
    "Accept-Encoding": "gzip"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('успех')
    a = response.json()
    pprint(len(a['states']))

else:
    # Обработка ошибки, если запрос не удался
    print(f"Ошибка запроса: {response.status_code} - {response.reason}")
