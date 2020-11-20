import psutil
import time

       
print("\n----------Monitoring----------")

print(f"CPU : {psutil.cpu_percent(interval=1)}%")
print(f"Memori : {psutil.virtual_memory().percent}%")

tx = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_sent
rx = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_recv
print(f"Tx/Rx : {tx}kbps / {rx}kbps")

'''
jaringan = psutil.net_io_counters(pernic=False)
tx = jaringan[2] / 1000
rx = jaringan[3] / 1000

time.sleep(2)
'''
    

    

    
