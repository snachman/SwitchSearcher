import os
import json
import datetime
from pushbullet import Pushbullet

key = "o.qACW2GLOdscAvYTw5DASY1PeTPsHw1Zt"


def push(alert_title, alert_text):
    # return os.popen("curl --header 'Access-Token: "+ key + "' https://api.pushbullet.com/v2/users/me")
    pb = Pushbullet(key)
    pb.push_note(alert_title, alert_text)


def get_timestamp():
    return str(datetime.datetime.now())


def get_product_description(product_id):
    if product_id == str(77464002):
        return "Gray Switch"
    elif product_id == str(77464001):
        return "Neon Switch"


def get_data(list_of_zips):
        for zip_code in list_of_zips:
                gray_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464002?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
                neon_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464001?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/s?searchTerm=nintendo+switch' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
                list_of_items = [gray_switch_in_stock_only, neon_switch_in_stock_only]
                for item in list_of_items:
                    dat = os.popen(item).read()
                    dat = json.loads(dat)
                    # f = open("log.txt", "a")
                    number_of_locations = len(dat['products'][0]['locations'])
                    for x in range(number_of_locations):
                        product_id = (dat['products'][0]['product_id'])
                        location = (dat['products'][0]['locations'][x]['store_name'])
                        count = (dat['products'][0]['locations'][x]['location_available_to_promise_quantity'])
                        # entry = (location + ": " + str(count))
                        # f.write(entry + "\n")
                        if count > 0.0:
                            # push(get_product_description(product_id), location)
                            print(location)



if __name__ == '__main__':
    get_data([21076])



