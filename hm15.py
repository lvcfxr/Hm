from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': {
            'EUR': 0.89,
            'UAH': 27.50
        },
        'EUR': {
            'USD': 1.12,
            'UAH': 31.00
        },
        'UAH': {
            'USD': 0.036,
            'EUR': 0.032
        }
    }