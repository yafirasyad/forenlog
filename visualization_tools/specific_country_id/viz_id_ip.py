import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi dictionary untuk menyimpan jumlah tanda [ID] per IP
id_ips = {}

# menghitung jumlah tanda [ID] per IP
for log in logs:
    if "[ID]" in log:
        # regular expression untuk mencari alamat IP, baik IPv4 maupun IPv6
        ip = re.search(
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+:[0-9a-fA-F:]+", log).group()
        if ip in id_ips:
            id_ips[ip] += 1
        else:
            id_ips[ip] = 1

# mencari IP dengan jumlah tanda [ID] terbanyak
most_id_ip = max(id_ips, key=id_ips.get)
most_id_count = id_ips[most_id_ip]

# membuat grafik untuk jumlah tanda [ID] per IP
fig, ax = plt.subplots(figsize=(12, 8))

labels = list(id_ips.keys())
values = list(id_ips.values())

# menambahkan text di sebelah kanan bar
for i in range(len(labels)):
    ax.text(values[i]+1, i, str(values[i]), ha='left', va='center')

ax.barh(labels, values, color='blue')

# memberi label sumbu x dan y
ax.set_xlabel("Jumlah Kemunculan")
ax.set_ylabel("IP")

# memberi judul grafik
ax.set_title("Jumlah Kemunculan per IP asal ID dari Log yang terfilter")

# menyesuaikan jarak antar ticks pada sumbu y
plt.yticks(range(len(labels)), labels, fontsize=8)

# menyesuaikan rentang nilai (range) pada sumbu x menjadi 0-25
plt.xlim(0, 1000)

# menyimpan grafik
plt.savefig("viz_id_ip.jpg")

# menampilkan grafik
plt.show()
