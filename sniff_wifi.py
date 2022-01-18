import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[1]
iface.scan()
time.sleep(0.5)
results = iface.scan_results()

print(results)
for i in results:
     bssid = i.bssid
     ssid  = i.ssid
     print(f"{bssid}: {ssid}")
