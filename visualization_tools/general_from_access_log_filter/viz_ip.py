import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi variabel untuk menghitung jumlah alamat IP
ipv4_count = {}
ipv6_count = {}

# menghitung jumlah alamat IP
for log in logs:
    ipv4 = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)
    if ipv4:
        ipv4 = ipv4.group(0)
        if ipv4 in ipv4_count:
            ipv4_count[ipv4] += 1
        else:
            ipv4_count[ipv4] = 1
    else:
        ipv6 = re.search(
            r'[a-fA-F0-9:]+:[a-fA-F0-9:]+:[a-fA-F0-9:]+:[a-fA-F0-9:]+:[a-fA-F0-9:]+:[a-fA-F0-9:]+:[a-fA-F0-9:]+:[a-fA-F0-9:]+', log)
        if ipv6:
            ipv6 = ipv6.group(0)
            if ipv6 in ipv6_count:
                ipv6_count[ipv6] += 1
            else:
                ipv6_count[ipv6] = 1

# mencari alamat IP yang paling sering muncul
most_common_ipv4 = max(ipv4_count, key=ipv4_count.get)
most_common_ipv6 = max(ipv6_count, key=ipv6_count.get)

# membuat grafik untuk alamat IP
fig, ax = plt.subplots(figsize=(15, 10))

labels = list(ipv4_count.keys()) + list(ipv6_count.keys())
values = list(ipv4_count.values()) + list(ipv6_count.values())

ax.barh(labels, values, color='blue')

# memberi label sumbu x dan y
ax.set_xlabel("Jumlah")
ax.set_ylabel("Alamat IP")

# memberi judul grafik
ax.set_title("Jumlah Alamat IP")

# menambahkan label jumlah di atas bar chart
for i, v in enumerate(values):
    ax.text(v, i, str(v), color='blue', fontweight="bold",
            ha="left", va="center")

# menentukan rentang sumbu X pada grafik
ax.set_xlim([0, max(values) + 100])

# memutar label sumbu y sebesar 45 derajat


# menyimpan grafik
plt.savefig("ip_viz.jpg")

# menampilkan grafik
plt.show()
