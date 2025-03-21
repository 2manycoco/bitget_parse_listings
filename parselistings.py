import requests

def get_bitget_listings():
    url = "https://api.bitget.com/api/spot/v1/public/products"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['symbol'] for coin in data['data']]
    return []

if __name__ == "__main__":
    listings = get_bitget_listings()
    print("Bitget New Listings:", listings)
