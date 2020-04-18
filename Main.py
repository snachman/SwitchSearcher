import os
import json
import datetime
from pushbullet import Pushbullet

key= "o.qACW2GLOdscAvYTw5DASY1PeTPsHw1Zt"
neon_switch = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464001?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + zip_code + "&limit=20&requested_quantity=1&radius=50&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
gray_switch = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464002?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=21030&limit=20&requested_quantity=1&radius=50&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
gray_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464002?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=21030&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"
neon_switch_in_stock_only = "curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464001?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=21030&limit=20&requested_quantity=1&radius=5000&include_only_available_stores=true&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/s?searchTerm=nintendo+switch' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed"

def push(alert_title, alert_text):
    # return os.popen("curl --header 'Access-Token: "+ key + "' https://api.pushbullet.com/v2/users/me")
    pb = Pushbullet(key)
    push = pb.push_note(alert_title, alert_text)


def get_timestamp():
    return str(datetime.datetime.now())


def get_data(list_of_zips):

    for zip in list_of_zips:
        time = get_timestamp()

        dat = os.popen("curl 'https://api.target.com/fulfillment_aggregator/v1/fiats/77464001?key=eb2551e4accc14f38cc42d32fbc2b2ea&nearby=" + str(zip) + "&limit=20&requested_quantity=1&radius=50&fulfillment_test_mode=grocery_opu_team_member_test' -H 'authority: api.target.com' -H 'accept: application/json' -H 'dnt: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'origin: https://www.target.com' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://www.target.com/c/nintendo-switch-consoles-video-games/-/N-piakr?lnk=NintendoSwitchc' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7' --compressed").read()
        dat = json.loads(dat)
        f = open("test.txt", "a")
        for x in range(19):
            location = (dat['products'][0]['locations'][x]['store_name'])
            distance = (dat['products'][0]['locations'][x]['distance'])
            count = (dat['products'][0]['locations'][x]['location_available_to_promise_quantity'])
            entry = (location + ": " + str(count))
            f.write(entry + "\n")
            if count > 0.0:
                push("SWITCH FOUND", location)



if __name__ == '__main__':
    get_data([21136, 21076])



