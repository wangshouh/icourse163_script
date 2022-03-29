import requests
import json
import time
import re
import pickle


def get_qr_info(s):
    '''
    获取二维码url和pollkey
    '''
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
    '''
    获取二维码图片并保存
    '''
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
    '''.
    获取二维码结果
    '''
    url = f"https://www.icourse163.org/logonByQRCode/poll.do?pollKey={pollkey}"

    headers = {
        'Host': 'www.icourse163.org',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    response = s.get(url, headers=headers)
    response_json = json.loads(response.text)

    return response_json['result']


def scan_qr_code(s, pollkey):
    '''
    根据不同结果给出不同终端提示
    如果成功后则提取token并返回
    '''
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
    '''
    中国大学MOOC存在一个cookies跳转页面,该页面url见下
    '''
    url = f"https://www.icourse163.org/passport/logingate/mocMobChangeCookie.htm?token={login_token}&returnUrl="

    headers = {
        'Host': 'www.icourse163.org',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    response = s.get(url, headers=headers)

    return response.text


def get_cookie_url(cookie_text):
    '''
    接上述函数的返回值,跳转页面中的link标签内存在cookie url
    点击后即可获取cookie
    '''
    cookie_url_list = re.findall(r'href="(.*?)"', cookie_text)

    return cookie_url_list


def get_cookie(s, cookie_url_list):
    '''
    通过访问cookies url获取cookie
    '''
    for cookie_url in cookie_url_list:
        url = cookie_url

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        }

        response = s.get(url, headers=headers)
        print(response.text)


def save_session(s):
    '''
    保存session
    '''
    with open('session.pickle', 'wb') as f:
        pickle.dump(s, f)


def login_session():
    s = requests.Session()
    qr_info = get_qr_info(s)
    print(qr_info)
    qr_url = qr_info['codeUrl']
    pollkey = qr_info['pollKey']
    get_qr_img(qr_url)
    login_token = scan_qr_code(s, pollkey)
    cookie_text = get_cookie_text(s, login_token)
    cookie_url_list = get_cookie_url(cookie_text)
    get_cookie(s, cookie_url_list)
    save_session(s)

    return s
