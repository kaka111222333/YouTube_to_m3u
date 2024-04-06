#! /usr/bin/python3

TW = r'''
🌏  台湾新闻,#genre#
'''


CCTV = r'''

📺 CCTV,#genre#
日照综合,http://192.168.23.1:4000/udp/239.253.224.254:8000
山东卫视,http://192.168.23.1:4000/udp/239.253.224.78:8000
CCTV-1 综合,http://192.168.23.1:4000/udp/239.253.224.77:8000
CCTV-4K 超高清,http://192.168.23.1:4000/udp/239.253.224.122:8000
CCTV-3 综艺,http://192.168.23.1:4000/udp/239.253.224.191:8000
CCTV-4 亚洲,http://192.168.23.1:4000/udp/239.253.224.111:8000
CCTV-4 欧洲,http://192.168.23.1:4000/udp/239.253.224.186:8000
CCTV-4 美洲,http://192.168.23.1:4000/udp/239.253.224.187:8000
CCTV-5 体育,http://192.168.23.1:4000/udp/239.253.224.192:8000
CCTV-5+体育赛事,http://192.168.23.1:4000/udp/239.253.224.80:8000
CCTV-6 电影,http://192.168.23.1:4000/udp/239.253.224.193:8000
CHC家庭影院,http://192.168.23.1:4000/udp/239.253.224.152:8000
CHC动作电影,http://192.168.23.1:4000/udp/239.253.224.153:8000
CHC高清电影,http://192.168.23.1:4000/udp/239.253.224.154:8000
CCTV-7 国防军事,http://192.168.23.1:4000/udp/239.253.224.233:8000
CCTV-8 电视剧,http://192.168.23.1:4000/udp/239.253.224.194:8000
CCTV-9 纪录,http://192.168.23.1:4000/udp/239.253.224.79:8000
CCTV-10 科教,http://192.168.23.1:4000/udp/239.253.224.234:8000
CCTV-11 戏曲,http://192.168.23.1:4000/udp/239.253.224.169:8000
CCTV-12 社会与法,http://192.168.23.1:4000/udp/239.253.224.235:8000
CCTV-13 新闻,http://192.168.23.1:4000/udp/239.253.224.175:8000
CCTV-14 少儿,http://192.168.23.1:4000/udp/239.253.224.236:8000
CCTV-15 音乐,http://192.168.23.1:4000/udp/239.253.224.170:8000
CCTV-16 奥林匹克,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000002395/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-17 农业农村,http://192.168.23.1:4000/udp/239.253.224.168:8000
CCTV-2 财经,http://192.168.23.1:4000/udp/239.253.224.232:8000

CCTV-1 综合,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001331/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-1 综合,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001331/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-1 综合,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001068/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-2 财经,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001332/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-2 财经,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001332/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-2 财经,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001293/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-3 综艺,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001598/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-4 亚洲,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001333/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-4 亚洲,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001290/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-5 体育,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001850/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-5+体育赛事,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001334/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-5+体育赛事,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001008/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-5+体育赛事,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001334/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-5+体育赛事,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001334/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-6 电影,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001859/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-6 电影,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001275/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-7 国防军事,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001291/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-8 电视剧,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001869/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-9 纪录,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001294/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-10 科教,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001288/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-11 戏曲,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001327/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-12 社会与法,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001289/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-13 新闻,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001328/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-14 少儿,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001292/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-15 音乐,http://[2409:8087:1a01:df::4077]/PLTV/88888888/224/3221225513/index.m3u8
CCTV-15 音乐,http://[2409:8087:1a01:df::4077]/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221225601/index.m3u8
CCTV-16 奥林匹克,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000002395/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-17 农业农村,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001295/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
CCTV-17 农业农村,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001301/index.m3u8?virtualDomain=yinhe.live_hls.zte.com


CCTV-1 综合,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226231/index.m3u8
CCTV-2 财经,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226195/index.m3u8
CCTV-3 综艺,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226397/index.m3u8
CCTV-4 亚洲,http://39.134.24.161/dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226191/index.m3u8
CCTV-4 亚洲,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226191/index.m3u8
CCTV-5 体育,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226395/index.m3u8
CCTV-5+体育赛事,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226221/index.m3u8
CCTV-6 电影,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226393/index.m3u8
CCTV-7 国防军事,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226192/index.m3u8
CCTV-8 电视剧,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226391/index.m3u8
CCTV-9 纪录,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226197/index.m3u8
CCTV-10 科教,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226189/index.m3u8
CCTV-11 戏曲,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226240/index.m3u8
CCTV-12 社会与法,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226190/index.m3u8
CCTV-13 新闻,https://live-play.cctvnews.cctv.com/cctv/merge_cctv13.m3u8
CCTV-13 新闻,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226233/index.m3u8
CCTV-14 少儿,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226193/index.m3u8
CCTV-15 音乐,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225785/index.m3u8
CCTV-16 奥林匹克,http://39.134.24.162/dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226921/index.m3u8
CCTV-16 奥林匹克,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226921/index.m3u8
CCTV-17 农业农村,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226198/index.m3u8
CCTV风云剧场,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226950/index.m3u8
CCTV第一剧场,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226959/index.m3u8
CCTV怀旧剧场,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226972/index.m3u8
CCTV风云音乐,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226953/index.m3u8
CCTV兵器科技,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226975/index.m3u8
CCTV风云足球,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226984/index.m3u8
CCTV高尔夫网球,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226978/index.m3u8
CCTV女性时尚,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226969/index.m3u8
CCTV央视文化精品,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226981/index.m3u8
CCTV央视台球,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226956/index.m3u8
CCTV电视指南,http://dbiptv.sn.chinamobile.com/PLTV/88888893/224/3221226987/index.m3u8


📺  卫视,#genre#
山东卫视,http://192.168.23.1:4000/udp/239.253.224.78:8000
江苏卫视,http://192.168.23.1:4000/udp/239.253.224.83:8000
浙江卫视,http://192.168.23.1:4000/udp/239.253.224.84:8000
东方卫视,http://192.168.23.1:4000/udp/239.253.224.86:8000
北京卫视,http://192.168.23.1:4000/udp/239.253.224.85:8000
北京纪实科教,http://192.168.23.1:4000/udp/239.253.224.165:8000
安徽卫视,http://192.168.23.1:4000/udp/239.253.224.87:8000
湖南卫视,http://192.168.23.1:4000/udp/239.253.224.82:8000
金鹰纪实,http://192.168.23.1:4000/udp/239.253.224.103:8000
金鹰卡通,http://192.168.23.1:4000/udp/239.253.224.117:8000
湖北卫视,http://192.168.23.1:4000/udp/239.253.224.88:8000
天津卫视,http://192.168.23.1:4000/udp/239.253.224.89:8000
广东卫视,http://192.168.23.1:4000/udp/239.253.224.90:8000
深圳卫视,http://192.168.23.1:4000/udp/239.253.224.91:8000
黑龙江卫视,http://192.168.23.1:4000/udp/239.253.224.93:8000
辽宁卫视,http://192.168.23.1:4000/udp/239.253.224.92:8000
吉林卫视,http://192.168.23.1:4000/udp/239.253.224.173:8000
东南卫视,http://192.168.23.1:4000/udp/239.253.224.105:8000
河北卫视,http://192.168.23.1:4000/udp/239.253.224.112:8000
河南卫视,http://192.168.23.1:4000/udp/239.253.224.190:8000
梨园频道,http://192.168.23.1:4000/udp/239.253.224.139:8000
武术世界,http://192.168.23.1:4000/udp/239.253.224.140:8000
文物宝库,http://192.168.23.1:4000/udp/239.253.224.141:8000
云南卫视,http://192.168.23.1:4000/udp/239.253.224.196:8000
贵州卫视,http://192.168.23.1:4000/udp/239.253.224.113:8000
青海卫视,http://192.168.23.1:4000/udp/239.253.224.195:8000
重庆卫视,http://192.168.23.1:4000/udp/239.253.224.38:8000
重庆汽摩,http://192.168.23.1:4000/udp/239.253.224.161:8000
江西卫视,http://192.168.23.1:4000/udp/239.253.224.47:8000
广西卫视,http://192.168.23.1:4000/udp/239.253.224.197:8000
海南卫视,http://192.168.23.1:4000/udp/239.253.224.179:8000
四川卫视,http://192.168.23.1:4000/udp/239.253.224.180:8000
甘肃卫视,http://192.168.23.1:4000/udp/239.253.224.74:8000
中国交通,http://192.168.23.1:4000/udp/239.253.224.177:8000
CETV1,http://192.168.23.1:4000/udp/239.253.224.110:8000
CETV2,http://192.168.23.1:4000/udp/239.253.224.107:8000
CETV4,http://192.168.23.1:4000/udp/239.253.224.116:8000
CETV4,http://192.168.23.1:4000/udp/239.253.224.108:8000
山西卫视,http://192.168.23.1:4000/udp/239.253.224.48:8000
陕西卫视,http://192.168.23.1:4000/udp/239.253.224.49:8000
四川卫视,http://192.168.23.1:4000/udp/239.253.224.50:8000
贵州卫视,http://192.168.23.1:4000/udp/239.253.224.51:8000
甘肃卫视,http://192.168.23.1:4000/udp/239.253.224.52:8000
宁夏卫视,http://192.168.23.1:4000/udp/239.253.224.53:8000
青海卫视,http://192.168.23.1:4000/udp/239.253.224.54:8000
CETV1,http://192.168.23.1:4000/udp/239.253.224.55:8000
三沙卫视,http://192.168.23.1:4000/udp/239.253.224.171:8000
延边卫视,http://192.168.23.1:4000/udp/239.253.224.121:8000
内蒙古卫视,http://192.168.23.1:4000/udp/239.253.224.58:8000
西藏卫视,http://192.168.23.1:4000/udp/239.253.224.56:8000
新疆卫视,http://192.168.23.1:4000/udp/239.253.224.60:8000
兵团卫视,http://192.168.23.1:4000/udp/239.253.224.57:8000
农林卫视,http://192.168.23.1:4000/udp/239.253.224.70:8000
大湾区卫视,http://192.168.23.1:4000/udp/239.253.224.69:8000
北京少儿,http://192.168.23.1:4000/udp/239.253.224.66:8000
哈哈炫动,http://192.168.23.1:4000/udp/239.253.224.63:8000
优漫卡通,http://192.168.23.1:4000/udp/239.253.224.64:8000
嘉佳卡通,http://192.168.23.1:4000/udp/239.253.224.65:8000



山东卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001341/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
山东卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001276/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
安徽卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001298/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
安徽卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001346/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
安徽卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001283/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
江苏卫视,http://[2409:8087:2001:20:2800:0:df6e:eb13]:80/ott.mobaibox.com/PLTV/3/224/3221228097/index.m3u8
江苏卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001344/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
江苏卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001032/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
浙江卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001345/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
浙江卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001026/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
东方卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001336/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
东方卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001028/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
北京卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001335/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
北京卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001025/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
广东卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001031/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
广东卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001337/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
深圳卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001342/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
深圳卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001029/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
湖南卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001339/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
黑龙江卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001338/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
黑龙江卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001030/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
黑龙江卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001274/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
辽宁卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001340/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
辽宁卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001296/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
天津卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001343/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
湖北卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001347/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
湖北卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001299/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
湖南卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001027/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
重庆卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000001297/index.m3u8?virtualDomain=yinhe.live_hls.zte.com

山东卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226209/index.m3u8
东方卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226217/index.m3u8
湖南卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226211/index.m3u8
湖北卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226477/index.m3u8
湖北卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226194/index.m3u8
辽宁卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226546/index.m3u8
辽宁卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226201/index.m3u8
江苏卫视,http://39.134.24.166/dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226200/index.m3u8
江苏卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226200/index.m3u8
江西卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226344/index.m3u8
江西卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225764/index.m3u8
广东卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226216/index.m3u8
广西卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225770/index.m3u8
重庆卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226409/index.m3u8
重庆卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226202/index.m3u8
河南卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226480/index.m3u8
河南卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225767/index.m3u8
河北卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226406/index.m3u8
河北卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225750/index.m3u8
贵州卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226474/index.m3u8
贵州卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225793/index.m3u8
北京卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221225728/index.m3u8
北京卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226222/index.m3u8
黑龙江卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226327/index.m3u8
黑龙江卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226215/index.m3u8
浙江卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226199/index.m3u8
安徽卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226391/index.m3u8
安徽卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226203/index.m3u8
深圳卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226205/index.m3u8
四川卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225768/index.m3u8
东南卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226341/index.m3u8
东南卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225766/index.m3u8
海南卫视,http://ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226465/index.m3u8
海南卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221225769/index.m3u8
精彩综艺,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226009/index.m3u8

🌏  凤凰,#genre#
凤凰资讯,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000002187/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
凤凰卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000002275/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
凤凰资讯,https://0472.org/hls/youzaiSB/fhzx.m3u8
凤凰卫视,https://0472.org/hls/youzaiSB/fhzw.m3u8
凤凰香港,https://0472.org/hls/youzaiSB/fhhk.m3u8
凤凰卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888888/224/3221226547/1.m3u8
凤凰资讯,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226546/index.m3u8
凤凰卫视,http://210.210.155.37/uq2663/h/h157/index2.m3u8
凤凰卫视, https://edge2.laotv.la/live/PhxChinese/index.m3u8
凤凰资讯, https://edge1.laotv.la/live/PhoenixNews/index.m3u8
凤凰资讯,http://playtv-live.ifeng.com/live/06OLEEWQKN4_audio.m3u8
凤凰卫视,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000002275/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
凤凰卫视,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226547/index.m3u8
凤凰资讯,http://dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226546/index.m3u8

纬来体育,rtmp://f13h.mine.nu/sat/tv721
纬来育乐,rtmp://f13h.mine.nu/sat/tv701
纬来日本,rtmp://f13h.mine.nu/sat/tv771
东森超视,rtmp://f13h.mine.nu/sat/tv331
民视,rtmp://f13h.mine.nu/sat/tv051
中视,rtmp://f13h.mine.nu/sat/tv091
华视,rtmp://f13h.mine.nu/sat/tv111
MOMO综合,rtmp://f13h.mine.nu/sat/tv761


4K修复,http://[2409:8087:2001:20:2800:0:df6e:eb15]/wh7f454c46tw1958249448_-1314265822/ott.mobaibox.com/PLTV/3/224/3221228141/index.m3u8?icpid=3&RTS=1659435587&from=1&hms_devid=2115&vqe=3
华数4K影视,http://zteres.sn.chinamobile.com:6060/000000001000/6000000003000004748/index.m3u8?channel-id=wasusyt&Contentid=6000000003000004748&livemode=1&stbId=3
华数4K影视,http://r.jdshipin.com/Lqdwf
欢笑剧场4K,http://[2409:8087:7000:20:1000::22]:6060/yinhe/2/ch00000090990000002156/index.m3u8?virtualDomain=yinhe.live_hls.zte.com
苏州4k,http://liveshowbak2.kan0512.com/ksz-norecord/csztv4k_4k.m3u8
黑莓电影,http://[2409:8087:2001:20:2800:0:df6e:eb09]:80/wh7f454c46tw1557681271_-1627945614/ott.mobaibox.com/PLTV/3/224/3221227520/index.m3u8?icpid=3&RTS=1674385968&from=40&popid=40&hms_devid=2037&prioritypopid=40&vqe=3
爱上4K,http://[2409:8087:5e01:34::23]:6610/ZTE_CMS/00000001000000060000000000000459/index.m3u8?IAS

爱自然 4K,https://d18dyiwu97wm6q.cloudfront.net/playlist2160p.m3u8
法国时装 4K,https://fash2043.cloudycdn.services/slive/ftv_ftv_4k_hevc_73d_42080_default_466_hls.smil/playlist.m3u8
法国时装,http://lb.streaming.sk/fashiontv/stream/playlist.m3u8
法国时装,http://lb.streaming.sk/fashiontv/stream/chunklist_w1702070444.m3u8?zshijd
法国时装,http://lb.streaming.sk/fashiontv/stream/chunklist_w1906011378.m3u8
FashionTV,https://fashs043.cloudycdn.services/scte/africa/playlist.m3u8
世界时装,https://live-3.otcnet.ru/wfc-int-master/index.m3u8
俄罗斯时装,https://live-3.otcnet.ru/wfc-rus-master/index.m3u8
澳亚卫视,https://live.mastvnet.com/lsdream/lY44pmm/2000/live.m3u8
俄罗斯中文,http://brics.bonus-tv.ru/cdn/brics/chinese/tracks-v1a1/index.m3u8
新加坡亚洲新闻,https://d2e1asnsl7br7b.cloudfront.net/7782e205e72f43aeb4a48ec97f66ebbe/index_5.m3u8
新加坡亚洲新闻,http://d2e1asnsl7br7b.cloudfront.net/7782e205e72f43aeb4a48ec97f66ebbe/index_4.m3u8
半岛电视台,https://live-hls-web-aje.getaj.net/AJE/01.m3u8
半岛电视台,http://live-hls-web-aje.getaj.net/AJE/01.m3u8
半岛电视台2,http://live-hls-web-aja.getaj.net/AJA/02.m3u8
BesTV 4K,http://[2409:8087:5e01:34::30]:6610/ZTE_CMS/00000001000000060000000000000202/index.m3u8?IAS
prod/amgclarity4k/playlist.m3u8
Clarity 4K,https://d6s2o8so4wk28.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-2vzmnn0zl3exh-


'''

LAST = r'''

📺  日照,#genre#
日照新闻综合,http://192.168.23.1:4000/udp/239.253.224.254:8000
日照科教,http://192.168.23.1:4000/udp/239.253.224.253:8000
日照公共,http://192.168.23.1:4000/udp/239.253.224.250:8000
岚山,http://192.168.23.1:4000/udp/239.253.224.252:8000

山东体育,http://192.168.23.1:4000/udp/239.253.224.22:8000
山东生活,http://192.168.23.1:4000/udp/239.253.224.151:8000
山东齐鲁,http://192.168.23.1:4000/udp/239.253.224.114:8000
山东新闻,http://192.168.23.1:4000/udp/239.253.224.23:8000
山东综艺,http://192.168.23.1:4000/udp/239.253.224.159:8000
山东文旅,http://192.168.23.1:4000/udp/239.253.224.160:8000
山东农科,http://192.168.23.1:4000/udp/239.253.224.24:8000
山东少儿,http://192.168.23.1:4000/udp/239.253.224.25:8000
山东教育,http://192.168.23.1:4000/udp/239.253.224.59:8000
海洋频道,http://192.168.23.1:4000/udp/239.253.224.67:8000
莒县,http://192.168.23.1:4000/udp/239.253.224.251:8000
直播中国,http://gctxyc.liveplay.myqcloud.com/gc/wgw05_1/index.m3u8?contentid=2820180516001
青岛五四广场,http://video11.qtv.com.cn/aqdwsgc2022/manifest.m3u8
青岛奥帆中心,http://video10.qtv.com.cn/aqdafzx2022/manifest.m3u8
青岛太平角,http://video10.qtv.com.cn/aqdtp2022/manifest.m3u8
青岛太平湾,http://video10.qtv.com.cn/sxt203/manifest.m3u8
青岛胶州湾,http://video10.qtv.com.cn/sxt200/manifest.m3u8
青岛浮山湾,http://video10.qtv.com.cn/sxt202/manifest.m3u8
青岛快速路1,http://video10.qtv.com.cn/sxt1/manifest.m3u8
青岛快速路2,http://video10.qtv.com.cn/sxt3/manifest.m3u8
青岛快速路3,http://video10.qtv.com.cn/sxt2/manifest.m3u8
青岛QTV-1,http://221.0.78.198:2381/hls/20220/index.m3u8
青岛QTV-2,http://221.0.78.198:2381/hls/20221/index.m3u8
青岛QTV-3,http://221.0.78.198:2381/hls/20222/index.m3u8

📺  IPTV,#genre#
都市剧场,http://192.168.23.1:4000/udp/239.253.224.98:8000
都市剧场,http://192.168.23.1:4000/udp/239.253.224.178:8000
精彩影视,http://192.168.23.1:4000/udp/239.253.224.142:8000
乐游,http://192.168.23.1:4000/udp/239.253.224.97:8000
纪实人文,http://192.168.23.1:4000/udp/239.253.224.120:8000
生活时尚,http://192.168.23.1:4000/udp/239.253.224.99:8000
法治天地,http://192.168.23.1:4000/udp/239.253.224.96:8000
金色学堂,http://192.168.23.1:4000/udp/239.253.224.101:8000
东方财经,http://192.168.23.1:4000/udp/239.253.224.94:8000
游戏风云,http://192.168.23.1:4000/udp/239.253.224.95:8000
动漫秀场,http://192.168.23.1:4000/udp/239.253.224.115:8000
魅力足球,http://192.168.23.1:4000/udp/239.253.224.100:8000
四海钓鱼,http://192.168.23.1:4000/udp/239.253.224.118:8000
先锋乒羽,http://192.168.23.1:4000/udp/239.253.224.155:8000
茶频道,http://192.168.23.1:4000/udp/239.253.224.143:8000
快乐垂钓,http://192.168.23.1:4000/udp/239.253.224.144:8000
先锋乒羽,http://192.168.23.1:4000/udp/239.253.224.145:8000
书画频道,http://192.168.23.1:4000/udp/239.253.224.146:8000
财富天下,http://192.168.23.1:4000/udp/239.253.224.147:8000
家庭理财,http://192.168.23.1:4000/udp/239.253.224.148:8000
新动漫,http://192.168.23.1:4000/udp/239.253.224.149:8000
新动漫,http://192.168.23.1:4000/udp/239.253.224.157:8000
发现之旅,http://192.168.23.1:4000/udp/239.253.224.162:8000
中学生,http://192.168.23.1:4000/udp/239.253.224.163:8000
老故事,http://192.168.23.1:4000/udp/239.253.224.164:8000
环球旅游,http://192.168.23.1:4000/udp/239.253.224.71:8000
优优宝贝,http://192.168.23.1:4000/udp/239.253.224.72:8000
车迷频道,http://192.168.23.1:4000/udp/239.253.224.73:8000
生态环境,http://192.168.23.1:4000/udp/239.253.224.75:8000
中华特产,http://192.168.23.1:4000/udp/239.253.224.76:8000
IPTV5,http://192.168.23.1:4000/udp/239.253.224.109:8000
IPTV3,http://192.168.23.1:4000/udp/239.253.224.124:8000
IPTV电视剧,http://192.168.23.1:4000/udp/239.253.224.125:8000
IPTV电影,http://192.168.23.1:4000/udp/239.253.224.126:8000
IPTV电影2,http://192.168.23.1:4000/udp/239.253.224.127:8000
IPTV电影3,http://192.168.23.1:4000/udp/239.253.224.128:8000
IPTV综艺,http://192.168.23.1:4000/udp/239.253.224.129:8000
IPTV电影4,http://192.168.23.1:4000/udp/239.253.224.130:8000
IPTV体育,http://192.168.23.1:4000/udp/239.253.224.131:8000
IPTV电视剧2,http://192.168.23.1:4000/udp/239.253.224.132:8000
IPTV电视剧3,http://192.168.23.1:4000/udp/239.253.224.135:8000
IPTV综艺2,http://192.168.23.1:4000/udp/239.253.224.136:8000
IPTV科教,http://192.168.23.1:4000/udp/239.253.224.137:8000
IPTV法制,http://192.168.23.1:4000/udp/239.253.224.138:8000
财富天下,http://192.168.23.1:4000/udp/239.253.224.230:8000
IPTV 201,http://192.168.23.1:4000/udp/239.253.224.201:8000
IPTV 202,http://192.168.23.1:4000/udp/239.253.224.202:8000
IPTV 203,http://192.168.23.1:4000/udp/239.253.224.203:8000
IPTV 204,http://192.168.23.1:4000/udp/239.253.224.204:8000
IPTV 205,http://192.168.23.1:4000/udp/239.253.224.205:8000
IPTV 207,http://192.168.23.1:4000/udp/239.253.224.207:8000
IPTV 208,http://192.168.23.1:4000/udp/239.253.224.208:8000
IPTV 209,http://192.168.23.1:4000/udp/239.253.224.209:8000
IPTV 210,http://192.168.23.1:4000/udp/239.253.224.210:8000
IPTV 211,http://192.168.23.1:4000/udp/239.253.224.211:8000
IPTV 212,http://192.168.23.1:4000/udp/239.253.224.212:8000
IPTV 213,http://192.168.23.1:4000/udp/239.253.224.213:8000
IPTV 214,http://192.168.23.1:4000/udp/239.253.224.214:8000
IPTV 215,http://192.168.23.1:4000/udp/239.253.224.215:8000
IPTV 216,http://192.168.23.1:4000/udp/239.253.224.216:8000
IPTV 217,http://192.168.23.1:4000/udp/239.253.224.217:8000
IPTV 218,http://192.168.23.1:4000/udp/239.253.224.218:8000
IPTV 219,http://192.168.23.1:4000/udp/239.253.224.219:8000
IPTV 220,http://192.168.23.1:4000/udp/239.253.224.220:8000
IPTV 221,http://192.168.23.1:4000/udp/239.253.224.221:8000
IPTV 222,http://192.168.23.1:4000/udp/239.253.224.222:8000
IPTV 223,http://192.168.23.1:4000/udp/239.253.224.223:8000
IPTV 224,http://192.168.23.1:4000/udp/239.253.224.224:8000
IPTV 225,http://192.168.23.1:4000/udp/239.253.224.225:8000
IPTV 226,http://192.168.23.1:4000/udp/239.253.224.226:8000
IPTV 227,http://192.168.23.1:4000/udp/239.253.224.227:8000
IPTV 228,http://192.168.23.1:4000/udp/239.253.224.228:8000
IPTV 229,http://192.168.23.1:4000/udp/239.253.224.229:8000
CGTN 西语,http://192.168.23.1:4000/udp/239.253.224.182:8000
CGTN 法语,http://192.168.23.1:4000/udp/239.253.224.183:8000
CGTN 中东,http://192.168.23.1:4000/udp/239.253.224.184:8000
CGTN 俄语,http://192.168.23.1:4000/udp/239.253.224.185:8000
CGTN 纪录,http://192.168.23.1:4000/udp/239.253.224.188:8000
CGTN,http://192.168.23.1:4000/udp/239.253.224.189:8000

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

print(CCTV)
print(LAST)

