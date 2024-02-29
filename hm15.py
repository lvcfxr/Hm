from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': {
            'EUR': 0.92,
            'UAH': 38.11
        },
        'EUR': {
            'USD': 1.08,
            'UAH': 41.28
        },
        'UAH': {
            'USD': 0.026,
            'EUR': 0.024
        }
    }