import requests, json

def get_stock_current_info(stock):

    headr = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "www.settrade.com",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1"
            }

    r = requests.get(f'https://www.settrade.com/api/set/stock/{stock}/info', headers=headr)
    output = json.loads(r.text)
    return output

def get_stock_historical_info(stock):

    headr = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "www.settrade.com",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Upgrade-Insecure-Requests": "1"
            }

    r = requests.get(f'https://www.settrade.com/api/set/stock/{stock}/historical-trading', headers=headr)
    output = json.loads(r.text)
    return output

logfile = open("log.txt", "w")
json.dump(get_stock_historical_info("AP"), logfile ,indent=2)