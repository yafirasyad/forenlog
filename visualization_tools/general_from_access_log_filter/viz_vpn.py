import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi variabel untuk menghitung jumlah VPN dan non-VPN
vpn_count = 0
non_vpn_count = 0

# menghitung jumlah VPN dan non-VPN
for log in logs:
    if "[VPN]" in log:
        vpn_count += 1
    else:
        non_vpn_count += 1

# membuat grafik untuk jumlah VPN dan non-VPN
labels = ["VPN", "Non-VPN"]
values = [vpn_count, non_vpn_count]
colors = ["purple", "orange"]
plt.bar(labels, values, color=colors, width=0.5)

# memberi label sumbu x dan y
plt.xlabel("Tipe koneksi")
plt.ylabel("Jumlah")

# memberi judul grafik
plt.title("Jumlah penggunaan VPN dan non-VPN")

# menambahkan label jumlah di atas bar chart
for i, v in enumerate(values):
    plt.text(i, v + 0.5, str(v),
             color=colors[i], fontweight="bold", ha="center", va="bottom")

# membatasi range sumbu y
plt.ylim(0, 3000)

# menyimpan grafik
plt.savefig("vpn_viz.jpg")

# menampilkan grafik
plt.show()
