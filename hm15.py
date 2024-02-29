from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return result

amount = float(input("Введите сумму для конвертации: "))
from_currency = input("Введите код валюты, из которой хотите конвертировать: ").upper()
to_currency = input("Введите код валюты, в которую хотите конвертировать: ").upper()