import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi dictionary untuk menyimpan jumlah tanda [Abuser] per IP
abuser_ips = {}

# menghitung jumlah tanda [Abuser] per IP
for log in logs:
    if "[Abuser]" in log:
        # regular expression untuk mencari alamat IP, baik IPv4 maupun IPv6
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+", log).group()
        if ip in abuser_ips:
            abuser_ips[ip] += 1
        else:
            abuser_ips[ip] = 1

# mencari IP dengan jumlah tanda [Abuser] terbanyak
most_abuser_ip = max(abuser_ips, key=abuser_ips.get)
most_abuser_count = abuser_ips[most_abuser_ip]


# membuat grafik untuk jumlah tanda [Abuser] per IP
fig, ax = plt.subplots(figsize=(10, 6))

labels = list(abuser_ips.keys())
values = list(abuser_ips.values())

# menambahkan text di sebelah kanan bar
for i in range(len(labels)):
    plt.text(values[i], i, str(values[i]), ha='left', va='center')

ax.barh(labels, values, color='blue')

# memberi label sumbu x dan y
ax.set_xlabel("Jumlah [Abuser]")
ax.set_ylabel("IP")

# memberi judul grafik
ax.set_title("Jumlah [Abuser] Per IP yang Terdeteksi")

# menyimpan grafik
plt.savefig("viz_ip_abuser.jpg")

# menampilkan grafik
plt.show()
