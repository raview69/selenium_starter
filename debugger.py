from seleniumwire import webdriver  # Import from seleniumwire

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the Google home page
driver.get("https://www.google.com")

# Access and print requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers["Content-Type"],
        )


headers = {
    "authority": "www.binance.com",
    "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?0",
    "content-type": "application/json",
    "sec-ch-ua-platform": '"Windows"',
    "origin": "https://www.binance.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.binance.com/en/futures/WIFUSDT",
    "accept-language": "en-US,en;q=0.9",
    "cookie": 'theme=dark; se_sd=w1RAQUR0NQAFBQKMQDFcgZZVgHRYEEUU1tQFeUEZFRQVgB1NWUAR1; bnc-uuid=1fd2b633-4231-4d00-be80-2a390a11e492; sajssdk_2015_cross_new_user=1; BNC_FV_KEY=333437f913a8a665b6ef939f4d5b4aad55829236; BNC_FV_KEY_T=101-zA5Ug6x04EhsUiBY0fAfr%2F8yme%2FlTa0DoYlujjok8RvNqCu%2FofvLoGaINW4Ydzr0Fd7oGvgfhOxQuaVkTQKK7A%3D%3D-WYRAA0n2umAYVB47f5SnsQ%3D%3D-72; BNC_FV_KEY_EXPIRE=1727036428465; se_gd=w8AVFRgQJENVxxXgPUxYgZZBwFlITBSVVQL9cUE5FZUUgDVNWUMQ1; se_gsd=VTI2FQpvISw3BjMpNCIxFVskChRXAgdRU1REUlxWUVZSHVNT1; cr00=172CDB26B95271E39B1B13F804569586; d1og=web.135729561.E17290713776C6407C5F1F789A4F99A5; r2o1=web.135729561.16AE03B28498EEF49FC227A1592375FB; f30l=web.135729561.1A005BC58DB9E0797CE0499B736B9692; logined=y; BNC-Location=BINANCE; __BNC_USER_DEVICE_ID__={"d41d8cd98f00b204e9800998ecf8427e":{"date":1727018518060,"value":""}}; p20t=web.135729561.CF0F37026DFFE97BD5ADF210E204B655; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22135729561%22%2C%22first_id%22%3A%221921a1af5fe22b3-09c3ab70717f31-16525637-1188412-1921a1af5ff2753%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMWExYWY1ZmUyMmIzLTA5YzNhYjcwNzE3ZjMxLTE2NTI1NjM3LTExODg0MTItMTkyMWExYWY1ZmYyNzUzIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTM1NzI5NTYxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22135729561%22%7D%2C%22%24device_id%22%3A%221921a1af5fe22b3-09c3ab70717f31-16525637-1188412-1921a1af5ff2753%22%7D; userPreferredCurrency=USD_USD; lang=en; futures-layout=pro',
}


# post order
"https://www.binance.com/bapi/futures/v1/private/future/order/place-order"

{
    "symbol": "WIFUSDT",
    "type": "LIMIT",
    "side": "BUY",
    "positionSide": "LONG",
    "quantity": 31,
    "timeInForce": "GTC",
    "price": "1.6636",
    "placeType": "order-form",
}

# close order

"https://www.binance.com/bapi/futures/v1/private/future/order/place-order"

# {
#     "symbol": "WIFUSDT",
#     "type": "MARKET",
#     "side": "SELL",
#     "quantity": 31,
#     "positionSide": "LONG",
#     "leverage": 14,
#     "isolated": false,
#     "newOrderRespType": "RESULT",
#     "placeType": "position",
# }
