import json
import requests

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base_key, sym_key, amount):

        if base_key == sym_key:
            raise APIException(f'Impossible to convert same currencies {base_key}!')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Amount {amount} is not recognised!')

        apikey = 'e2zH2i3Ht6d7Lrai8RZr6nC0140h6bnw'
        result = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?base={base_key}&symbols={sym_key}&apikey={apikey}")
        resp = json.loads(result.content)
        value = resp['rates'][sym_key] * amount
        value = round(value, 3)
        message = f"Result {amount} {base_key} в {sym_key} : {value}"
        return message
