#! /usr/bin/python3

TW = r'''
🌏  台湾新闻,#genre#
'''


CCTV = r'''
📺 CCTV,#genre#
CCTV-1 综合,http://192.168.23.1:4000/udp/239.253.224.77:8000
CCTV-2 财经,http://192.168.23.1:4000/udp/239.253.224.232:8000
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
CCTV-16 奥林匹克,http://39.134.24.162/dbiptv.sn.chinamobile.com/PLTV/88888890/224/3221226921/index.m3u8
CCTV-17 农业农村,http://192.168.23.1:4000/udp/239.253.224.168:8000
CCTV-4K 超高清,http://27.222.3.214/liveali-tp4k.cctv.cn/live/4K10M.stream/playlist.m3u8
CCTV-4K 超高清,http://159.75.85.63:5679/cctv4k.php
CCTV-8K 超高清,https://tv.cry33.com/ys4k.php?id=8k

📺 卫视,#genre#
山东卫视,http://192.168.23.1:4000/udp/239.253.224.78:8000
江苏卫视,http://192.168.23.1:4000/udp/239.253.224.83:8000
浙江卫视,http://192.168.23.1:4000/udp/239.253.224.84:8000
安徽卫视,http://192.168.23.1:4000/udp/239.253.224.87:8000
东方卫视,http://192.168.23.1:4000/udp/239.253.224.86:8000
北京卫视,http://192.168.23.1:4000/udp/239.253.224.85:8000
北京纪实科教,http://192.168.23.1:4000/udp/239.253.224.165:8000
广东卫视,http://192.168.23.1:4000/udp/239.253.224.90:8000
深圳卫视,http://192.168.23.1:4000/udp/239.253.224.91:8000
湖南卫视,http://192.168.23.1:4000/udp/239.253.224.82:8000
金鹰纪实,http://192.168.23.1:4000/udp/239.253.224.103:8000
湖北卫视,http://192.168.23.1:4000/udp/239.253.224.88:8000
天津卫视,http://192.168.23.1:4000/udp/239.253.224.89:8000
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
山西卫视,http://192.168.23.1:4000/udp/239.253.224.48:8000
陕西卫视,http://192.168.23.1:4000/udp/239.253.224.49:8000
四川卫视,http://192.168.23.1:4000/udp/239.253.224.50:8000
贵州卫视,http://192.168.23.1:4000/udp/239.253.224.51:8000
甘肃卫视,http://192.168.23.1:4000/udp/239.253.224.52:8000
宁夏卫视,http://192.168.23.1:4000/udp/239.253.224.53:8000
青海卫视,http://192.168.23.1:4000/udp/239.253.224.54:8000
三沙卫视,http://192.168.23.1:4000/udp/239.253.224.171:8000
延边卫视,http://192.168.23.1:4000/udp/239.253.224.121:8000
内蒙古卫视,http://192.168.23.1:4000/udp/239.253.224.58:8000
西藏卫视,http://192.168.23.1:4000/udp/239.253.224.56:8000
新疆卫视,http://192.168.23.1:4000/udp/239.253.224.60:8000
兵团卫视,http://192.168.23.1:4000/udp/239.253.224.57:8000
农林卫视,http://192.168.23.1:4000/udp/239.253.224.70:8000
CETV1,http://192.168.23.1:4000/udp/239.253.224.110:8000
CETV2,http://192.168.23.1:4000/udp/239.253.224.107:8000
CETV4,http://192.168.23.1:4000/udp/239.253.224.116:8000
CETV4,http://192.168.23.1:4000/udp/239.253.224.108:8000
CETV1,http://192.168.23.1:4000/udp/239.253.224.55:8000
大湾区卫视,http://192.168.23.1:4000/udp/239.253.224.69:8000
金鹰卡通,http://192.168.23.1:4000/udp/239.253.224.117:8000
北京少儿,http://192.168.23.1:4000/udp/239.253.224.66:8000
哈哈炫动,http://192.168.23.1:4000/udp/239.253.224.63:8000
优漫卡通,http://192.168.23.1:4000/udp/239.253.224.64:8000
嘉佳卡通,http://192.168.23.1:4000/udp/239.253.224.65:8000

📺  日照,#genre#
日照新闻综合,http://192.168.23.1:4000/udp/239.253.224.254:8000
日照科教,http://192.168.23.1:4000/udp/239.253.224.253:8000
日照公共,http://192.168.23.1:4000/udp/239.253.224.250:8000
岚山电视台,http://192.168.23.1:4000/udp/239.253.224.252:8000
莒县电视台,http://192.168.23.1:4000/udp/239.253.224.251:8000
海洋频道,http://192.168.23.1:4000/udp/239.253.224.67:8000
山东体育,http://192.168.23.1:4000/udp/239.253.224.22:8000
山东齐鲁,http://192.168.23.1:4000/udp/239.253.224.114:8000
山东生活,http://192.168.23.1:4000/udp/239.253.224.151:8000
山东综艺,http://192.168.23.1:4000/udp/239.253.224.159:8000
山东文旅,http://192.168.23.1:4000/udp/239.253.224.160:8000
山东新闻,http://192.168.23.1:4000/udp/239.253.224.23:8000
山东农科,http://192.168.23.1:4000/udp/239.253.224.24:8000
山东少儿,http://192.168.23.1:4000/udp/239.253.224.25:8000
山东教育,http://192.168.23.1:4000/udp/239.253.224.59:8000
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


🌏【CCTV】,#genre#
CCTV-1 综合,http://150.138.8.143/00/SNM/CHANNEL00000311/index.m3u8
CCTV-2 财经,http://150.138.8.143/00/SNM/CHANNEL00000317/index.m3u8
CCTV-3 综艺,http://150.138.8.143/00/SNM/CHANNEL00000359/index.m3u8
CCTV-4 亚洲,http://150.138.8.143/00/SNM/CHANNEL00000320/index.m3u8
CCTV-4 欧洲,http://150.138.8.143/00/SNM/CHANNEL00000350/index.m3u8
CCTV-4 美洲,http://150.138.8.143/00/SNM/CHANNEL00000351/index.m3u8
CCTV-5 体育,http://150.138.8.143/00/SNM/CHANNEL00000360/index.m3u8
CCTV-5+体育赛事,http://150.138.8.143/00/SNM/CHANNEL00000316/index.m3u8
CCTV-6 电影,http://150.138.8.143/00/SNM/CHANNEL00000361/index.m3u8
CHC家庭影院,http://150.138.8.143/00/SNM/CHANNEL00002028/index.m3u8
CHC动作电影,http://150.138.8.143/00/SNM/CHANNEL00002030/index.m3u8
CHC高清电影,http://150.138.8.143/00/SNM/CHANNEL00002029/index.m3u8
CCTV-7 军事,http://150.138.8.143/00/SNM/CHANNEL00000318/index.m3u8
CCTV-8 电视剧,http://150.138.8.143/00/SNM/CHANNEL00000362/index.m3u8
CCTV-9 纪录,http://150.138.8.143/00/SNM/CHANNEL00000319/index.m3u8
CCTV-10 科教,http://150.138.8.143/00/SNM/CHANNEL00000321/index.m3u8
CCTV-11 戏曲,http://150.138.8.143/00/SNM/CHANNEL00000344/index.m3u8
CCTV-12 社会与法,http://150.138.8.143/00/SNM/CHANNEL00000322/index.m3u8
CCTV-13 新闻,http://150.138.8.143/00/SNM/CHANNEL00000345/index.m3u8
CCTV-14 少儿,http://150.138.8.143/00/SNM/CHANNEL00000323/index.m3u8
CCTV-15 音乐,http://150.138.8.143/00/SNM/CHANNEL00000346/index.m3u8
CCTV-17 农业农村,http://150.138.8.143/00/SNM/CHANNEL00000303/index.m3u8
CETV-1,http://150.138.8.143/00/SNM/CHANNEL00000076/index.m3u8
CETV-2,http://150.138.8.143/00/SNM/CHANNEL00000077/index.m3u8
CETV-4,http://150.138.8.143/00/SNM/CHANNEL00000666/index.m3u8
CGTN,http://150.138.8.143/00/SNM/CHANNEL00000352/index.m3u8

🌏 【卫视】,#genre#
山东卫视,http://150.138.8.143/00/SNM/CHANNEL10000301/index.m3u8
江苏卫视,http://150.138.8.143/00/SNM/CHANNEL00000304/index.m3u8
浙江卫视,http://150.138.8.143/00/SNM/CHANNEL00000305/index.m3u8
北京卫视,http://150.138.8.143/00/SNM/CHANNEL00000302/index.m3u8
东方卫视,http://150.138.8.143/00/SNM/CHANNEL00000309/index.m3u8
广东卫视,http://150.138.8.143/00/SNM/CHANNEL00000307/index.m3u8
广西卫视,http://150.138.8.143/00/SNM/CHANNEL00000368/index.m3u8
贵州卫视,http://150.138.8.143/00/SNM/CHANNEL00000329/index.m3u8
海南卫视,http://150.138.8.143/00/SNM/CHANNEL00000347/index.m3u8
安徽卫视,http://150.138.8.143/00/SNM/CHANNEL00000328/index.m3u8
河北卫视,http://150.138.8.143/00/SNM/CHANNEL00000330/index.m3u8
河南卫视,http://150.138.8.143/00/SNM/CHANNEL00000358/index.m3u8
黑龙江卫视,http://150.138.8.143/00/SNM/CHANNEL00000306/index.m3u8
湖北卫视,http://150.138.8.143/00/SNM/CHANNEL00000325/index.m3u8
湖南卫视,http://150.138.8.143/00/SNM/CHANNEL00000324/index.m3u8
吉林卫视,http://150.138.8.143/00/SNM/CHANNEL00000363/index.m3u8
山西卫视,http://150.138.8.143/00/SNM/CHANNEL00000032/index.m3u8
陕西卫视,http://150.138.8.143/00/SNM/CHANNEL00000029/index.m3u8
江西卫视,http://150.138.8.143/00/SNM/CHANNEL00000335/index.m3u8
辽宁卫视,http://150.138.8.143/00/SNM/CHANNEL00000326/index.m3u8
东南卫视,http://150.138.8.143/00/SNM/CHANNEL00000310/index.m3u8
甘肃卫视,http://150.138.8.143/00/SNM/CHANNEL00000349/index.m3u8
厦门卫视,http://150.138.8.143/00/SNM/CHANNEL00000075/index.m3u8
四川卫视,http://150.138.8.143/00/SNM/CHANNEL00000348/index.m3u8
深圳卫视,http://150.138.8.143/00/SNM/CHANNEL00000308/index.m3u8
天津卫视,http://150.138.8.143/00/SNM/CHANNEL00000327/index.m3u8
西藏卫视,http://150.138.8.143/00/SNM/CHANNEL00000045/index.m3u8
新疆卫视,http://150.138.8.143/00/SNM/CHANNEL00000044/index.m3u8
云南卫视,http://150.138.8.143/00/SNM/CHANNEL00000367/index.m3u8
内蒙古卫视,http://150.138.8.143/00/SNM/CHANNEL00000040/index.m3u8
青海卫视,http://150.138.8.143/00/SNM/CHANNEL00000366/index.m3u8
延边卫视,http://150.138.8.143/00/SNM/CHANNEL00000668/index.m3u8
重庆卫视,http://150.138.8.143/00/SNM/CHANNEL00000341/index.m3u8
兵团卫视,http://150.138.8.143/00/SNM/CHANNEL00000071/index.m3u8
大湾区卫视,http://150.138.8.143/00/SNM/CHANNEL00000670/index.m3u8
三沙卫视,http://150.138.8.143/00/SNM/CHANNEL00000078/index.m3u8
都市剧场,http://150.138.8.143/00/SNM/CHANNEL00000630/index.m3u8
金鹰纪实,http://150.138.8.143/00/SNM/CHANNEL00000334/index.m3u8
纪实人文,http://150.138.8.143/00/SNM/CHANNEL00000333/index.m3u8
武术世界,http://150.138.8.143/00/SNM/CHANNEL00000657/index.m3u8
梨园频道,http://150.138.8.143/00/SNM/CHANNEL00000656/index.m3u8
文物宝库,http://150.138.8.143/00/SNM/CHANNEL00000658/index.m3u8
快乐垂钓,http://150.138.8.143/00/SNM/CHANNEL00000648/index.m3u8
茶频道,http://150.138.8.143/00/SNM/CHANNEL00000649/index.m3u8
四海钓鱼,http://150.138.8.143/00/SNM/CHANNEL00000640/index.m3u8
新动漫,http://150.138.8.143/00/SNM/CHANNEL00000659/index.m3u8
卡酷少儿,http://150.138.8.143/00/SNM/CHANNEL00000661/index.m3u8
嘉佳卡通,http://150.138.8.143/00/SNM/CHANNEL00000074/index.m3u8
哈哈炫动,http://150.138.8.143/00/SNM/CHANNEL00000050/index.m3u8
优漫卡通,http://150.138.8.143/00/SNM/CHANNEL00000049/index.m3u8
金鹰卡通,http://150.138.8.143/00/SNM/CHANNEL00002027/index.m3u8
游戏风云,http://150.138.8.143/00/SNM/CHANNEL00002024/index.m3u8

🌏 【山东】,#genre#
山东齐鲁,http://150.138.8.143/00/SNM/CHANNEL10000313/index.m3u8
山东生活,http://150.138.8.143/00/SNM/CHANNEL00000336/index.m3u8
山东体育,http://150.138.8.143/00/SNM/CHANNEL00000315/index.m3u8
山东农科,http://150.138.8.143/00/SNM/CHANNEL00000339/index.m3u8
山东综艺,http://150.138.8.143/00/SNM/CHANNEL00000338/index.m3u8
山东少儿,http://150.138.8.143/00/SNM/CHANNEL00000340/index.m3u8
山东文旅,http://150.138.8.143/00/SNM/CHANNEL00000337/index.m3u8
山东新闻,http://150.138.8.143/00/SNM/CHANNEL00000314/index.m3u8
山东教育,http://150.138.8.143/00/SNM/CHANNEL00000331/index.m3u8

🌏 【青岛】,#genre#
青岛QTV-1,http://150.138.8.143/00/SNM/CHANNEL00000500/index.m3u8
青岛QTV-2,http://150.138.8.143/00/SNM/CHANNEL00000501/index.m3u8
青岛QTV-3,http://150.138.8.143/00/SNM/CHANNEL00000502/index.m3u8
青岛QTV-4,http://150.138.8.143/00/SNM/CHANNEL00000503/index.m3u8
青岛QTV-5,http://150.138.8.143/00/SNM/CHANNEL00000504/index.m3u8
青岛QTV-6,http://150.138.8.143/00/SNM/CHANNEL00000505/index.m3u8
崂山综合,http://150.138.8.143/00/SNM/CHANNEL00001022/index.m3u8
黄岛新闻,http://150.138.8.143/00/SNM/CHANNEL00001086/index.m3u8
黄岛生活,http://150.138.8.143/00/SNM/CHANNEL00001087/index.m3u8
胶州新闻,http://150.138.8.143/00/SNM/CHANNEL00001074/index.m3u8
莱西综合,http://150.138.8.143/00/SNM/CHANNEL00001067/index.m3u8
平度电视台,http://150.138.8.143/00/SNM/CHANNEL00001054/index.m3u8

🌏 【日照等】,#genre#
日照综合,http://150.138.8.143/00/SNM/CHANNEL00000262/index.m3u8
日照科教,http://150.138.8.143/00/SNM/CHANNEL00000263/index.m3u8
日照公共,http://150.138.8.143/00/SNM/CHANNEL00001100/index.m3u8
岚山电视台,http://150.138.8.143/00/SNM/CHANNEL00001044/index.m3u8
五莲新闻综合,http://150.138.8.143/00/SNM/CHANNEL00001068/index.m3u8
莒县综合,http://150.138.8.143/00/SNM/CHANNEL00001014/index.m3u8

烟台新闻综合,http://150.138.8.143/00/SNM/CHANNEL00000280/index.m3u8
烟台公共,http://150.138.8.143/00/SNM/CHANNEL00000281/index.m3u8
烟台经济科技,http://150.138.8.143/00/SNM/CHANNEL00000282/index.m3u8
烟台影视,http://150.138.8.143/00/SNM/CHANNEL00000283/index.m3u8
烟台招远,http://150.138.8.143/00/SNM/CHANNEL00001113/index.m3u8
烟台龙口,http://150.138.8.143/00/SNM/CHANNEL00001005/index.m3u8
烟台蓬莱,http://150.138.8.143/00/SNM/CHANNEL00001088/index.m3u8
烟台长岛,http://150.138.8.143/00/SNM/CHANNEL00001090/index.m3u8
烟台栖霞,http://150.138.8.143/00/SNM/CHANNEL00001055/index.m3u8
烟台牟平,http://150.138.8.143/00/SNM/CHANNEL00001076/index.m3u8
烟台牟平生活,http://150.138.8.143/00/SNM/CHANNEL00001077/index.m3u8

济南新闻综合,http://150.138.8.143/00/SNM/CHANNEL00000312/index.m3u8
济南新闻综合,http://150.138.8.143/00/SNM/CHANNEL00000061/index.m3u8
济南都市,http://150.138.8.143/00/SNM/CHANNEL00000062/index.m3u8
济南生活,http://150.138.8.143/00/SNM/CHANNEL00000063/index.m3u8
济南文旅体育,http://150.138.8.143/00/SNM/CHANNEL00000064/index.m3u8
济南娱乐,http://150.138.8.143/00/SNM/CHANNEL00000065/index.m3u8
济南少儿,http://150.138.8.143/00/SNM/CHANNEL00000067/index.m3u8
济南教育,http://150.138.8.143/00/SNM/CHANNEL00000069/index.m3u8
济南鲁中,http://150.138.8.143/00/SNM/CHANNEL00000244/index.m3u8
济南长清,http://150.138.8.143/00/SNM/CHANNEL00001018/index.m3u8
济南商河,http://150.138.8.143/00/SNM/CHANNEL00001008/index.m3u8
济南济阳,http://150.138.8.143/00/SNM/CHANNEL00001030/index.m3u8
济南平阴,http://150.138.8.143/00/SNM/CHANNEL00001050/index.m3u8
济南历城,http://150.138.8.143/00/SNM/CHANNEL00001105/index.m3u8

济宁综合,http://150.138.8.143/00/SNM/CHANNEL00000240/index.m3u8
济宁综合,http://150.138.8.143/00/SNM/CHANNEL00000238/index.m3u8
济宁教育,http://150.138.8.143/00/SNM/CHANNEL00000239/index.m3u8
济宁公共,http://150.138.8.143/00/SNM/CHANNEL00000241/index.m3u8
沂水综合,http://150.138.8.143/00/SNM/CHANNEL00001098/index.m3u8
沂水生活,http://150.138.8.143/00/SNM/CHANNEL00001099/index.m3u8
济宁高新,http://150.138.8.143/00/SNM/CHANNEL00001101/index.m3u8
济宁曲阜,http://150.138.8.143/00/SNM/CHANNEL00001052/index.m3u8
济宁兖州,http://150.138.8.143/00/SNM/CHANNEL00001051/index.m3u8
济宁鱼台综合,ttp://150.138.8.143/00/SNM/CHANNEL00001107/index.m3u8
济宁鱼台生活,http://150.138.8.143/00/SNM/CHANNEL00001108/index.m3u8
济宁任城-1,http://150.138.8.143/00/SNM/CHANNEL00001111/index.m3u8
济宁任城-2,http://150.138.8.143/00/SNM/CHANNEL00001112/index.m3u8
济宁嘉祥,http://150.138.8.143/00/SNM/CHANNEL00001016/index.m3u8
济宁邹城,http://150.138.8.143/00/SNM/CHANNEL00001038/index.m3u8
济宁梁山,http://150.138.8.143/00/SNM/CHANNEL00001075/index.m3u8

潍坊1,http://150.138.8.143/00/SNM/CHANNEL00000215/index.m3u8
潍坊2,http://150.138.8.143/00/SNM/CHANNEL00000216/index.m3u8
潍坊3,http://150.138.8.143/00/SNM/CHANNEL00000217/index.m3u8
潍坊4,http://150.138.8.143/00/SNM/CHANNEL00000218/index.m3u8
潍坊高新区,http://150.138.8.143/00/SNM/CHANNEL00001106/index.m3u8
潍坊高密,http://150.138.8.143/00/SNM/CHANNEL00001089/index.m3u8
潍坊寿光,http://150.138.8.143/00/SNM/CHANNEL00001000/index.m3u8
寿光蔬菜,http://150.138.8.143/00/SNM/CHANNEL00001045/index.m3u8
潍坊诸城,http://150.138.8.143/00/SNM/CHANNEL00001004/index.m3u8
潍坊安丘,http://150.138.8.143/00/SNM/CHANNEL00001015/index.m3u8
潍坊昌乐,,http://150.138.8.143/00/SNM/CHANNEL00001033/index.m3u8
潍坊青州,http://150.138.8.143/00/SNM/CHANNEL00001042/index.m3u8
潍坊青州文化旅游,http://150.138.8.143/00/SNM/CHANNEL00001057/index.m3u8
潍坊昌邑,http://150.138.8.143/00/SNM/CHANNEL00001083/index.m3u8
潍坊临朐,http://150.138.8.143/00/SNM/CHANNEL00001085/index.m3u8

淄博综合,http://150.138.8.143/00/SNM/CHANNEL00000292/index.m3u8
淄博影视,http://150.138.8.143/00/SNM/CHANNEL00001037/index.m3u8
淄博文旅,http://150.138.8.143/00/SNM/CHANNEL00000293/index.m3u8
淄博民生,http://150.138.8.143/00/SNM/CHANNEL00000294/index.m3u8
淄博沂源,http://150.138.8.143/00/SNM/CHANNEL00001002/index.m3u8
淄博淄川,http://150.138.8.143/00/SNM/CHANNEL00001007/index.m3u8
淄博张店,http://150.138.8.143/00/SNM/CHANNEL00001012/index.m3u8
淄博桓台,http://150.138.8.143/00/SNM/CHANNEL00001020/index.m3u8
淄博高青,http://150.138.8.143/00/SNM/CHANNEL00001023/index.m3u8

德州综合,http://150.138.8.143/00/SNM/CHANNEL00000206/index.m3u8
德州经济生活,http://150.138.8.143/00/SNM/CHANNEL00000207/index.m3u8
德州宁津,http://150.138.8.143/00/SNM/CHANNEL00001003/index.m3u8
德州齐河,http://150.138.8.143/00/SNM/CHANNEL00001056/index.m3u8
德州武城,http://150.138.8.143/00/SNM/CHANNEL00001059/index.m3u8
德州武城综艺影视,http://150.138.8.143/00/SNM/CHANNEL00001060/index.m3u8
德州禹城,http://150.138.8.143/00/SNM/CHANNEL00001061/index.m3u8
德州禹城综艺,http://150.138.8.143/00/SNM/CHANNEL00001062/index.m3u8
德州平原,http://150.138.8.143/00/SNM/CHANNEL00001064/index.m3u8
德州夏津,http://150.138.8.143/00/SNM/CHANNEL00001069/index.m3u8
德州夏津公共,http://150.138.8.143/00/SNM/CHANNEL00001070/index.m3u8
德州陵城,http://150.138.8.143/00/SNM/CHANNEL00001082/index.m3u8
德州临邑,http://150.138.8.143/00/SNM/CHANNEL00001104/index.m3u8

滨州新闻综合,http://150.138.8.143/00/SNM/CHANNEL00000220/index.m3u8
滨州公共,http://150.138.8.143/00/SNM/CHANNEL00000221/index.m3u8
滨州惠民,http://150.138.8.143/00/SNM/CHANNEL00001009/index.m3u8
滨州无棣,http://150.138.8.143/00/SNM/CHANNEL00001024/index.m3u8
滨州沾化,http://150.138.8.143/00/SNM/CHANNEL00001035/index.m3u8
滨州阳信,http://150.138.8.143/00/SNM/CHANNEL00001036/index.m3u8
滨州邹平,http://150.138.8.143/00/SNM/CHANNEL00001058/index.m3u8

菏泽综合,http://150.138.8.143/00/SNM/CHANNEL00000232/index.m3u8
菏泽公共,http://150.138.8.143/00/SNM/CHANNEL00000234/index.m3u8
菏泽郓城,http://150.138.8.143/00/SNM/CHANNEL00001041/index.m3u8
菏泽巨野,http://150.138.8.143/00/SNM/CHANNEL00001046/index.m3u8
菏泽定陶,http://150.138.8.143/00/SNM/CHANNEL00001063/index.m3u8
菏泽东明,http://150.138.8.143/00/SNM/CHANNEL00001065/index.m3u8
菏泽单县,http://150.138.8.143/00/SNM/CHANNEL00001079/index.m3u8
菏泽鄄城,http://150.138.8.143/00/SNM/CHANNEL00001084/index.m3u8

聊城综合,http://150.138.8.143/00/SNM/CHANNEL00000250/index.m3u8
聊城民生,http://150.138.8.143/00/SNM/CHANNEL00000251/index.m3u8
聊城冠县,http://150.138.8.143/00/SNM/CHANNEL00001040/index.m3u8
聊城莘县,http://150.138.8.143/00/SNM/CHANNEL00001047/index.m3u8
聊城茌平,http://150.138.8.143/00/SNM/CHANNEL00001048/index.m3u8
聊城临清,http://150.138.8.143/00/SNM/CHANNEL00001103/index.m3u8

东营综合,http://150.138.8.143/00/SNM/CHANNEL00000226/index.m3u8
东营公共,http://150.138.8.143/00/SNM/CHANNEL00000227/index.m3u8
东营广饶,http://150.138.8.143/00/SNM/CHANNEL00001043/index.m3u8


威海公共,http://150.138.8.143/00/SNM/CHANNEL00000275/index.m3u8
威海乳山,http://150.138.8.143/00/SNM/CHANNEL00001049/index.m3u8
威海荣成,http://150.138.8.143/00/SNM/CHANNEL00001053/index.m3u8
威海海阳,http://150.138.8.143/00/SNM/CHANNEL00001091/index.m3u8
威海海阳综艺,http://150.138.8.143/00/SNM/CHANNEL00001092/index.m3u8
威海？？？,http://150.138.8.143/00/SNM/CHANNEL00001093/index.m3u8


临沂河东ttp://150.138.8.143/00/SNM/CHANNEL00001109/index.m3u8
临沂莒南,http://150.138.8.143/00/SNM/CHANNEL00001011/index.m3u8
临沂蒙阴,http://150.138.8.143/00/SNM/CHANNEL00001031/index.m3u8
临沂兰陵,http://150.138.8.143/00/SNM/CHANNEL00001032/index.m3u8
临沂兰陵公共,http://150.138.8.143/00/SNM/CHANNEL00001095/index.m3u8


泰安泰山,http://150.138.8.143/00/SNM/CHANNEL00001114/index.m3u8
泰安东平,http://150.138.8.143/00/SNM/CHANNEL00001001/index.m3u8
泰安岱岳,http://150.138.8.143/00/SNM/CHANNEL00001013/index.m3u8
泰安新泰,http://150.138.8.143/00/SNM/CHANNEL00001029/index.m3u8
泰安新泰乡村,http://150.138.8.143/00/SNM/CHANNEL00001066/index.m3u8
泰安宁阳,http://150.138.8.143/00/SNM/CHANNEL00001071/index.m3u8
泰安宁阳公共,http://150.138.8.143/00/SNM/CHANNEL00001072/index.m3u8




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

