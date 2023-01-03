#%%
import requests

def get_full_url(input_url):

    proxies = {
            'http': 'http://localhost:9090',
            'https': 'http://localhost:9090',
        }

    cookies = {
        'li_at': 'AQEDAQuoAOQEd1Q0AAABhXStgN0AAAGFmLoE3U4Ahvg7TOKhV9g_z8PtrKN0zeaBR5HVuzeQmIYjR-F0yPnPQTuJe1DrQGB-H7Zj5O8uILSb-km9sK0bBsJ9WFbIV8Fq4-tIGqyUC63GgtbC8yOD7ZU0',
    }

    headers = {
        'Host': 'www.linkedin.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    # input_url = 'https://www.linkedin.com/in/ACwAAAQML5wBUcrTsc3b449Jy7x8SP6O-Fed3ok'
    response = requests.get(
        input_url,
        cookies=cookies,
        headers=headers,
        proxies=proxies,
        verify=False)

    soup = response.text

    with open("output1.html", "w") as file:
        file.write(str(soup))

    soup_ = BeautifulSoup(soup)
    json_code=json.loads(soup_.findAll('code', id=re.compile('^datalet-bpr-guid-'))[-1].text)
    json_code['request']

    parse_result = urlparse(json_code['request'])
    dict_result = parse_qs(parse_result.query)
    lk_id = dict_result['memberIdentity'][0]
    return lk_id

#%%
import pandas as pd
from bs4 import BeautifulSoup
import re, json, csv, time, random
from urllib.parse import urlparse, parse_qs

df = pd.read_csv('linkedin_profile.csv',)
input_url_list=df['url'].values


start_at = 27
i=0
for url in input_url_list[start_at:]:
    data_search=get_full_url(url)
    with open('linkedin_profile_clean.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow([data_search])
        f_object.close()
    i=i+1
    print(f"in request i = {i}")
    time.sleep(random.randrange(1,1000)/1000)


#%%

proxies = {
        'http': 'http://localhost:9090',
        'https': 'http://localhost:9090',
    }

cookies = {
    'li_at': 'AQEDAQuoAOQEd1Q0AAABhXStgN0AAAGFmLoE3U4Ahvg7TOKhV9g_z8PtrKN0zeaBR5HVuzeQmIYjR-F0yPnPQTuJe1DrQGB-H7Zj5O8uILSb-km9sK0bBsJ9WFbIV8Fq4-tIGqyUC63GgtbC8yOD7ZU0',
}

headers = {
    'Host': 'www.linkedin.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}

input_url = 'https://www.linkedin.com/in/ACwAAAQML5wBUcrTsc3b449Jy7x8SP6O-Fed3ok'
response = requests.get(
    input_url,
    cookies=cookies,
    headers=headers,
    proxies=proxies,
    verify=False)

soup = response.text

with open("output1.html", "w") as file:
    file.write(str(soup))

soup_ = BeautifulSoup(soup)
json_code=json.loads(soup_.findAll('code', id=re.compile('^datalet-bpr-guid-'))[-1].text)
json_code['request']

parse_result = urlparse(json_code['request'])
dict_result = parse_qs(parse_result.query)
lk_id = dict_result['memberIdentity'][0]
return lk_id