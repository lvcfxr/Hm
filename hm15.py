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
    
    if from_currency == to_currency:
        return amount

    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return None

    rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * rate
    return converted_amount