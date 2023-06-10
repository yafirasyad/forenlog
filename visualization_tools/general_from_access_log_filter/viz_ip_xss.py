import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi dictionary untuk menyimpan jumlah tanda [XSS Attack Attempt] per IP
xss_ips = {}

# menghitung jumlah tanda [XSS Attack Attempt] per IP
for log in logs:
    if "[XSS Attack Attempt]" in log:
        ip = re.search(r"\d+\.\d+\.\d+\.\d+|\w+:\w+:\w+:\w+:\w+:\w+:\w+:\w+", log).group()
        if ip in xss_ips:
            xss_ips[ip] += 1
        else:
            xss_ips[ip] = 1

# mencari IP dengan jumlah tanda [XSS Attack Attempt] terbanyak
most_xss_ip = max(xss_ips, key=xss_ips.get)
most_xss_count = xss_ips[most_xss_ip]


# membuat grafik untuk jumlah tanda [XSS Attack Attempt] per IP
fig, ax = plt.subplots(figsize=(12, 8))

labels = list(xss_ips.keys())
values = list(xss_ips.values())

# menambahkan text di sebelah kanan bar
for i in range(len(labels)):
    plt.text(values[i]+0.2, i, str(values[i]), ha='left', va='center')

ax.barh(labels, values, color='red')

# memberi label sumbu x dan y
ax.set_xlabel("Jumlah [XSS Attack Attempt]")
ax.set_ylabel("IP")

# memberi judul grafik
ax.set_title("Jumlah [XSS Attack Attempt] yang dilakukan per IP")

# menyimpan grafik
plt.savefig("viz_ip_xss.jpg")

# menampilkan grafik
plt.show()
