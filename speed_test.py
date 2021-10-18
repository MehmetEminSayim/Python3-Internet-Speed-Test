import speedtest
import math
st = speedtest.Speedtest()

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

print('1) Download Speed: ',end='')
print(convert_size(st.download()))
print('2) UpLoad Speed: ', end='')
print(convert_size(st.upload()))
print('3) Ping: ', end='')
servernames = []
st.get_servers(servernames)
print(convert_size(st.results.ping));