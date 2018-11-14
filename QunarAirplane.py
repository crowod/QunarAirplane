import requests
import json
import time
import re
from sha import MySHA
from md5 import MyMD5
from my_function import *
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests import RequestException
from selenium import webdriver
from sendemail import SendMali
from urllib import parse

MIN_PRICE = 900
token_str = 'qunar_api_token'
qtTime_str = 'QN668'
cookieToken_str = 'QN48'
md5_hash = [1732584193, 4023233417, 2562383102, 271733878]
sha_hash = [1732584193, 4023233417, 2562383102, 271733878, 3285377520]
token = {}
searchDepartureAirport = '北京'
searchArrivalAirport = '贵阳'
searchDepartureTime = '2019-01-08'
searchArrivalTime = ''
nextNDays = '0'
startSearch = 'true'
fromCode = 'BJS'
toCode = 'KWE'
from_ = 'flight_dom_search'
lowestPrice = 'null'


def get_cookie():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    query = {
        'searchDepartureAirport': searchDepartureAirport,
        'searchArrivalAirport': searchArrivalAirport,
        'searchDepartureTime': searchDepartureTime,
        'searchArrivalTime': searchDepartureTime,
        'nextNDays': nextNDays,
        'startSearch': startSearch,
        'fromCode': fromCode,
        'toCode': toCode,
        'from': from_,
        'lowestPrice': lowestPrice,
    }
    url = 'https://flight.qunar.com/site/oneway_list.htm?' + urlencode(query)
    driver.get(url)
    time.sleep(0.5)
    driver.refresh()
    cookie_list = driver.get_cookies()
    pre_cookies_value = ''
    for cookie in cookie_list:
        pre_cookies_value += cookie['name'] + '=' + cookie['value'] + ';'
    time.sleep(0.5)
    driver.refresh()
    cookie_list = driver.get_cookies()
    post_cookies_value = ''
    for cookie in cookie_list:
        post_cookies_value += cookie['name'] + '=' + cookie['value'] + ';'
    driver.close()
    return pre_cookies_value.strip(';'), post_cookies_value.strip(';')


pre_cookies_value, post_cookies_value = get_cookie()


def getQtTime(qtTime):
    result = qtTime.split(',')
    result = list(map(int, result))
    result = list(map(lambda x: chr(x - 2), result))
    result = "".join(result)
    return result


def getTokenStr(token_str, cookies_value):
    return s_default(cookieToken_str, cookies_value)


def getRandomKey(token_str):
    n = ''
    r = '' + token_str[4:]
    for i in r:
        n += str(ord(i))
    my_md5 = MyMD5(n)
    my_md5.start()
    md5 = my_md5.md5
    return md5[-6:]


def s_default(token, cookies_value):
    cookies_value = re.split(';\s*', cookies_value)
    cookies_value = list(map(parse.unquote, cookies_value))
    cookies_value = list(map(lambda x: x.split('='), cookies_value))
    cookies_value = {x[0]: x[1] for x in cookies_value}
    result = cookies_value[token]
    return result


def encrypt():
    t = getTokenStr(token_str, pre_cookies_value)
    n = getQtTime(s_default(qtTime_str, pre_cookies_value))
    r = int(n) % 2
    return encryptFunction()[r](t + n), n


def first_function(token):
    my_sha = MySHA(token)
    my_sha.start()
    sha = my_sha.sha
    my_md5 = MyMD5(sha)
    my_md5.start()
    return my_md5.md5


def second_function(token):
    my_md5 = MyMD5(token)
    my_md5.start()
    md5 = my_md5.md5
    my_sha = MySHA(md5)
    my_sha.start()
    return my_sha.sha


def encryptFunction():
    return [first_function, second_function]


def get_m_():
    __m__, n = encrypt()
    token[getRandomKey(n)] = __m__
    my_md5 = MyMD5(__m__)
    my_md5.start()
    __m__ = my_md5.md5
    return __m__


def cookie_cov():
    if re.search('QN271=.*?;', post_cookies_value) and re.search(
            'QN271=.*?;', pre_cookies_value):
        return re.sub('QN271=.*?;',
                      re.search('QN271=.*?;', post_cookies_value)[0],
                      pre_cookies_value)
    else:
        return pre_cookies_value


def get_page_index():
    __m__ = get_m_()
    data_referer = {
        'searchDepartureAirport': searchDepartureAirport,
        'searchArrivalAirport': searchArrivalAirport,
        'searchDepartureTime': searchDepartureTime,
        'searchArrivalTime': searchDepartureTime,
        'nextNDays': nextNDays,
        'startSearch': startSearch,
        'fromCode': fromCode,
        'toCode': toCode,
        'from': from_,
        'lowestPrice': lowestPrice,
    }

    data_path = {
        'departureCity': searchDepartureAirport,
        'arrivalCity': searchArrivalAirport,
        'departureDate': searchDepartureTime,
        'ex_track': '',
        '__m__': __m__,
        'sort': '',
    }
    referer = 'https://flight.qunar.com/site/oneway_list.htm?' + urlencode(
        data_referer)
    token_key, token_value = '', ''
    for key, value in token.items():
        token_key = str(key)
        token_value = value
    cookie = cookie_cov()
    headers = {
        'authority':
        'flight.qunar.com',
        'path':
        '/touch/api/domestic/wbdflightlist?' + urlencode(data_path),
        'dnt':
        '1',
        token_key:
        token_value,
        'cookie':
        cookie,
        'referer':
        referer,
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'x-requested-with':
        'XMLHttpRequest',
    }

    data = {
        'departureCity': searchDepartureAirport,
        'arrivalCity': searchArrivalAirport,
        'departureDate': searchDepartureTime,
        'ex_track': '',
        '__m__': __m__,
        'sort': ''
    }
    url = 'https://flight.qunar.com/touch/api/domestic/wbdflightlist?' + \
        urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            if response.text.find('\"code\":666') != -1:
                time.sleep(1)
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response.text
            else:
                return response.text
    except RequestException:
        print('请求索引页出错')
        return None


def parse_page_detail(html):
    data = json.loads(html)
    flights = []
    if data and 'data' in data.keys():
        flight_data = data.get('data').get('flights')
        for item in flight_data:
            if item.get('minPrice') <= MIN_PRICE:
                if 'binfo1' not in item:
                    binfo = item.get('binfo')
                    flight = {
                        'airCode': binfo.get('airCode'),
                        'arrAirport': binfo.get('arrAirport'),
                        'arrDate': binfo.get('arrDate'),
                        'arrTerminal': binfo.get('arrTerminal'),
                        'arrTime': binfo.get('arrTime'),
                        'depAirport': binfo.get('depAirport'),
                        'depTerminal': binfo.get('depTerminal'),
                        'depTime': binfo.get('depTime'),
                        'name': binfo.get('name'),
                        'planeFullType': binfo.get('planeFullType'),
                        'mealDesc': binfo.get('mealDesc'),
                        'minPrice': item.get('minPrice'),
                    }
                    flights.append(flight)
                else:
                    binfo1 = item.get('binfo1')
                    binfo2 = item.get('binfo2')
                    flight = {
                        "pre": {
                            'airCode': binfo1.get('airCode'),
                            'arrAirport': binfo1.get('arrAirport'),
                            'arrDate': binfo1.get('arrDate'),
                            'arrTerminal': binfo1.get('arrTerminal'),
                            'arrTime': binfo1.get('arrTime'),
                            'depAirport': binfo1.get('depAirport'),
                            'depTerminal': binfo1.get('depTerminal'),
                            'depTime': binfo1.get('depTime'),
                            'name': binfo1.get('name'),
                            'planeFullType': binfo1.get('planeFullType'),
                            'mealDesc': binfo1.get('mealDesc'),
                        },
                        "post": {
                            'airCode': binfo2.get('airCode'),
                            'arrAirport': binfo2.get('arrAirport'),
                            'arrDate': binfo2.get('arrDate'),
                            'arrTerminal': binfo2.get('arrTerminal'),
                            'arrTime': binfo2.get('arrTime'),
                            'depAirport': binfo2.get('depAirport'),
                            'depTerminal': binfo2.get('depTerminal'),
                            'depTime': binfo2.get('depTime'),
                            'name': binfo2.get('name'),
                            'planeFullType': binfo2.get('planeFullType'),
                            'mealDesc': binfo2.get('mealDesc'),
                        },
                        'minPrice': item.get('minPrice'),
                    }
                    flights.append(flight)

    return flights


def main():
    while True:
        html = get_page_index()
        flights = parse_page_detail(html)
        send_mail = SendMali()
        if flights:
            send_mail.send(flights)
            time.sleep(300)


if __name__ == '__main__':
    main()
