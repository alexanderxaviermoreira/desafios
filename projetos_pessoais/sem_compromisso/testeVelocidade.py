import speedtest
import csv

servers = [15014]
threads = 16

s = speedtest.Speedtest()
try:
    s.get_servers(servers)
except:
    s.get_closest_servers()
    s.get_best_server()

s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()
print(results_dict)

arquivo_relatorio = 'speedtest.csv'

try:
    file = open(arquivo_relatorio, 'x')
    file.close()

    with open(arquivo_relatorio, 'w', newline='', encoding='UTF8') as f:
        w = csv.DictWriter(f, results_dict.keys())
        w.writeheader()
        w.writerow(results_dict)
except IOError:
    with open(arquivo_relatorio, 'a', newline='', encoding='UTF8') as f:
        w = csv.DictWriter(f, results_dict.keys())
        w.writer(results_dict)
        