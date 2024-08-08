import requests

async def search_nessesary(dictionary: dict, *args: str) -> dict | list | str:
    key = dictionary
    for i in args:
        key = key[i]
    return key

async def list_button(token_ms: str = 'fd381c6be45d058539a1f5638ba484ecdd8df885'):
    try:
        url = "https://api.moysklad.ru/api/remap/1.2/entity/paymentout/metadata"
        headers = {
            "Authorization": f"{token_ms}",
            "Accept-Encoding": "gzip"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print('успех')
            states = search_nessesary(response.json(), 'states')
            kbbutton = [i['name'] for i in states]
            return kbbutton
    except Exception as ex:
            print(ex)
