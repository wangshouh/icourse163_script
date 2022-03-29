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
