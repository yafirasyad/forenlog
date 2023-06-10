import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi dictionary untuk menyimpan jumlah tanda [DDoS Attack Attempt] per IP
ddos_ips = {}

# menghitung jumlah tanda [DDoS Attack Attempt] per IP
for log in logs:
    if "[DDoS Attack Attempt]" in log:
        ip = re.search(r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\d+\.\d+\.\d+\.\d+", log).group()
        if ip in ddos_ips:
            ddos_ips[ip] += 1
        else:
            ddos_ips[ip] = 1

# mencari IP dengan jumlah tanda [DDoS Attack Attempt] terbanyak
most_ddos_ip = max(ddos_ips, key=ddos_ips.get)
most_ddos_count = ddos_ips[most_ddos_ip]

# membuat grafik untuk jumlah tanda [DDoS Attack Attempt] per IP
fig, ax = plt.subplots(figsize=(15, 10))

labels = list(ddos_ips.keys())
values = list(ddos_ips.values())

# menambahkan text di sebelah kanan bar
for i in range(len(labels)):
    plt.text(values[i], i, str(values[i]), ha='left', va='center')

ax.barh(labels, values, color='red')

# memberi label sumbu x dan y
ax.set_xlabel("Jumlah [DDoS Attack Attempt]")
ax.set_ylabel("IP")

# memberi judul grafik
ax.set_title("Jumlah [DDoS Attack Attempt] yang dilakukan per IP")

# menyimpan grafik
plt.savefig("viz_ip_ddos.jpg")

# menampilkan grafik
plt.show()
