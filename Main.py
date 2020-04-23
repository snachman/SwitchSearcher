import os
import json
import datetime
from pushbullet import Pushbullet
import keys
import time
from time import strptime
from Tweeter import tweet
from urllib import parse


def log(message):
    f = open("./log.txt", "a")
    line = str(get_timestamp()) + " - " + message.replace("\n", " ") + "\n"
    f.write(line)
    f.close()


def push(alert_title, alert_text):
    pb = Pushbullet(keys.pushbullet_key)
    pb.push_note(alert_title, alert_text)


def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%c")


def get_product_description(product_id):
    if product_id == str(77464002):
        return "Gray Switch"
    elif product_id == str(77464001):
        return "Neon Switch"
    else:
        return "unk product"


def get_order_pickup(data):
    if data == "UNAVAILABLE":
        return False
    elif data == "IN_STOCK":
        return True


def get_data(list_of_zips):
    for zip_code in list_of_zips:
        gray_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464002?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(
            zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
        neon_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464001?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(
            zip_code) + "&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/s?searchTerm=nintendo+switch' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
        list_of_items = [gray_switch_in_stock_only, neon_switch_in_stock_only]
        for item in list_of_items:
            time.sleep(5)
            dat = os.popen(item).read()
            dat = json.loads(dat)
            product_id = (dat['products'][0]['product_id'])
            number_of_locations = len(dat['products'][0]['locations'])
            log(get_product_description(product_id))
            for x in range(number_of_locations):
                product_id = (dat['products'][0]['product_id'])
                location = (dat['products'][0]['locations'][x]['store_name'])
                store_address = (dat['products'][0]['locations'][x]['store_address'])
                count_in_stock = (dat['products'][0]['locations'][x]['location_available_to_promise_quantity'])
                available_to_order_ahead = get_order_pickup(
                    dat['products'][0]['locations'][x]['order_pickup']['availability_status'])
                log(get_product_description(product_id))
                store_address = store_address.replace(" ", "+")
                google_map = "https://www.google.com/maps/search/?api=1&query=" + parse.quote(store_address, safe='+')

                if count_in_stock > 0.0:
                    if available_to_order_ahead:
                        tweet_message = (get_product_description(
                            product_id) + " available at the " + location + " Target. They are reporting " + str(
                            int(count_in_stock)) + ". IT IS AVAILABLE FOR ORDER AHEAD!" + "\n\n" + google_map)
                        log(tweet_message)
                        tweet(tweet_message)

                    else:
                        tweet_message = (get_product_description(
                            product_id) + " available at the " + location + " Target. They are reporting " + str(
                            int(count_in_stock)) + " but it is not available for ordering ahead so hopefully it's actually there." + "\n\n" + google_map)
                        log(tweet_message)
                        tweet(tweet_message)


if __name__ == '__main__':
    # test comment
    log("begin")
    get_data([21076])
    log("complete")
