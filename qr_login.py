import requests
import json
import time
import re


def get_qr_info(s):
    url = "https://www.icourse163.org/logonByQRCode/code.do?width=182&height=182"

    payload = {}
    headers = {
        'Host': 'www.icourse163.org',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    response = s.request("GET", url, headers=headers, data=payload)

    response_json = json.loads(response.text)
    return response_json['result']


def get_qr_img(qr_url):
    url = qr_url

    payload = {}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }

    with open('qr.png', 'wb') as f:
        response = requests.request("GET", url, headers=headers, data=payload)
        img_data = response.content
        f.write(img_data)


def get_qr_result(s, pollkey):
    url = f"https://www.icourse163.org/logonByQRCode/poll.do?pollKey={pollkey}"

    headers = {
        'Host': 'www.icourse163.org',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    response = s.get(url, headers=headers)
    response_json = json.loads(response.text)

    return response_json['result']


def scan_qr_code(s, pollkey):
    while True:
        time.sleep(1)
        result = get_qr_result(s, pollkey)
        if result['codeStatus'] == 0:
            print('请使用手机扫描qr.png登录')
            print(result)
        elif result['codeStatus'] == 1:
            print('请在手机上确认登录')
            print(result)
        elif result['codeStatus'] == 2:
            login_token = result['token']
            print('登录成功')
            print(result)
            break
        else:
            print("二维码过期")
            print(result)

    return login_token


def get_cookie_text(s, login_token):

    url = f"https://www.icourse163.org/passport/logingate/mocMobChangeCookie.htm?token={login_token}&returnUrl="

    headers = {
        'Host': 'www.icourse163.org',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    response = s.get(url, headers=headers)
    with open('example.html', 'w') as f:
        f.write(response.text)

    return response.text


def get_cookie_url(cookie_text):
    cookie_url_list = re.findall(r'href="(.*?)"', cookie_text)

    return cookie_url_list


def get_cookie(s, cookie_url_list):
    for cookie_url in cookie_url_list:
        url = cookie_url

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        }

        response = s.get(url, headers=headers)
        print(response.text)
