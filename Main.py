import os
import json
import datetime
from pushbullet import Pushbullet
import keys
from Tweeter import tweet




def push(key, alert_title, alert_text):
    pb = Pushbullet(key)
    pb.push_note(alert_title, alert_text)


def get_timestamp():
    return str(datetime.datetime.now())


def get_product_description(product_id):
    if product_id == str(77464002):
        return "Gray Switch"
    elif product_id == str(77464001):
        return "Neon Switch"
    elif product_id == str(50218991):
        return "Witch Hazel" # added for testing
    elif product_id ==str():
        return "Purple/Orange Joy-Con" # added for testing
    else:
        return "unk product"


def get_order_pickup(data):
    if data == "UNAVAILABLE":
        return False
    elif data == "IN_STOCK":
        return True


def get_data(list_of_zips):
    for zip_code in list_of_zips:
        gray_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464002?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
        neon_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464001?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/s?searchTerm=nintendo+switch' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
        witch_hazel_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/50218991?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/t-n-dickinson-s-witch-hazel-cleansing-cloths-25ct/-/A-50218991' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
        purple_orange_joycon = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77333077?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=21030&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/s?searchTerm=nintendo+switch&tref=typeahead%7Cterm%7C2%7Cnintendo+switch%7C%7C%7C%7Chistory&category=0%7CAll%7Cmatchallpartial%7Call+categories&Nao=24' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
        list_of_items = [gray_switch_in_stock_only, neon_switch_in_stock_only, purple_orange_joycon]
        for item in list_of_items:
            dat = os.popen(item).read()
            dat = json.loads(dat)
            number_of_locations = len(dat['products'][0]['locations'])
            for x in range(number_of_locations):
                product_id = (dat['products'][0]['product_id'])
                location = (dat['products'][0]['locations'][x]['store_name'])
                count_in_stock = (dat['products'][0]['locations'][x]['location_available_to_promise_quantity'])
                available_to_order_ahead = get_order_pickup(
                    dat['products'][0]['locations'][x]['order_pickup']['availability_status'])
                if count_in_stock > 0.0: # even when it shows limited availability on the website, it may say 0 in stock, limited availablity might mean they only have a display unit which is not for sale
                    if available_to_order_ahead:
                        push(keys.pushbullet_key, get_product_description(product_id) + " FOUND", location + "\n" + "IT IS AVAILABLE FOR ORDER AHEAD!")
                        # response = (get_product_description(product_id) + " available for order ahead: " + location)
                        # print(response)
                        tweet(get_product_description(product_id) + " available at " + location + ". They are reporting " + str(count_in_stock)) + "."
                    else:
                        push(keys.pushbullet_key, get_product_description(product_id) + " found", location + "\n" + "not available for order ahead.")
                        # response = (get_product_description(product_id) + " found at: " + location + " but is not available for order ahead")
                        # print(response)
                        tweet(get_product_description(product_id) + " available at " + location + ". They are reporting " + str(count_in_stock)) + "."


if __name__ == '__main__':
    get_data([21076])
