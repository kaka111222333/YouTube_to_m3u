#! /usr/bin/python3

banner = r'''
📺 CCTV,#genre#
CCTV-4K 超高清,http://[2409:8087:2001:20:2800:0:df6e:eb10]:80/ott.mobaibox.com/PLTV/4/224/3221228242/index.m3u8
CCTV-8K 超高清,http://[2409:8087:2001:20:2800:0:df6e:eb02]/ott.mobaibox.com/PLTV/3/224/3221228165/index.m3u8
CCTV-1 综合,http://[2409:8087:2001:20:2800:0:df6e:eb02]/ott.mobaibox.com/PLTV/4/224/3221228149/index.m3u8
CCTV-2 财经,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001332/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-3 综艺,http://[2409:8087:2001:20:2800:0:df6e:eb21]/ott.mobaibox.com/PLTV/3/224/3221228499/index.m3u8
CCTV-4 中文国际,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001333/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
📺 凤凰,#genre#
凤凰资讯,http://[2409:8087:2001:20:2800:0:df6e:eb18]:80/ott.mobaibox.com/PLTV/3/224/3221228524/index.m3u8
凤凰卫视,http://[2409:8087:2001:20:2800:0:df6e:eb23]:80/ott.mobaibox.com/PLTV/3/224/3221228527/index.m3u8

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
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
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
    print(f",{link[start : end]}")

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)
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
            print(f'{ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
