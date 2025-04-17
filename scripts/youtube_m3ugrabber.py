#! /usr/bin/python3

TW = r'''
🌏  台湾新闻,#genre#
'''


CCTV = r'''

🌏  台湾,#genre#
中天新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV28.m3u8
中天亚洲台,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV13.m3u8
东森财经新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV03.m3u8
TVBS新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV31.m3u8
三立新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV01.m3u8
三立新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV32.m3u8
中视新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV09.m3u8
中视,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV42.m3u8
民视新闻台,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV17.m3u8
台视新闻,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV25.m3u8
华视CTS,https://raw.githubusercontent.com/ChiSheng9/iptv/master/TV12.m3u8








'''

LAST = r'''




'''



import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('000000')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('000000')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{ch_name},{link[start : end]}")





print(CCTV)
print(TW)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')

print(LAST)

