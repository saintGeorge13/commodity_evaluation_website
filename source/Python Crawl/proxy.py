# -*- coding:utf-8 -*-
import requests
import random

items = [
    {"ip_address": "124.112.171.165", "ip_port": "16625"},
    {"ip_address": "27.30.22.43", "ip_port": "15367"},
    {"ip_address": "120.39.238.194", "ip_port": "22403"},
    {"ip_address": '122.4.49.248', "ip_port": '21001'},
    {"ip_address": '59.63.37.107', "ip_port": "20494"},
    {"ip_address": '49.88.63.94', "ip_port": '18323'},
    {"ip_address": '14.20.188.42', "ip_port": '18015'},
    {"ip_address": '113.58.229.244', "ip_port": '17013'},
    {"ip_address": '171.216.90.203', "ip_port": '22066'},
    {"ip_address": '113.120.25.223', "ip_port": '16957'},
]

def check_ip(item):
    url = 'https://rate.tmall.com/'
    proxies = {
        'http': f'http://{item["ip_address"]}:{item["ip_port"]}',
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.text:
            print("代理ip可用", proxies)
            return True
    except Exception as e:
        print("代理ip不可用", e)
        return False

def return_ip():
    while True:
        proxy = random.choice(items)
        if check_ip(proxy):
            break
    proxies = {
        'http': f'http://{proxy["ip_address"]}:{proxy["ip_port"]}',
    }
    return proxies.get('http')

print(return_ip())