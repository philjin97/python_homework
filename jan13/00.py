import requests 

# URL = 'https://api.bithumb.com/public/ticker/BTC_KRW'
# response = requests.get(URL).json()
# print(type(response))

# data = response['data']
# print(type(data))

# prev_closing_price = data['prev_closing_price']
# print(prev_closing_price)


def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

    res = requests.get(url=url).json()
    data = res["data"]
    prev_closing_price = data["prev_closing_price"]

    return prev_closing_price

if __name__ == "__main__":
    print(get_btc_krw())