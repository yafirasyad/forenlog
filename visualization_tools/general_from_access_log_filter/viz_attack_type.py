import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi variabel untuk menghitung jumlah serangan
xss_count = 0
ddos_count = 0

# menghitung jumlah serangan
for log in logs:
    if "[XSS Attack Attempt]" in log:
        xss_count += 1
    elif "[DDoS Attack Attempt]" in log:
        ddos_count += 1

# membuat grafik untuk jumlah serangan berdasarkan jenis serangan
labels = ["XSS Attack Attempt", "DDoS Attack Attempt"]
values = [xss_count, ddos_count]
colors = ["green", "red"]
plt.bar(labels, values, color=colors)

# memberi label sumbu x dan y
plt.xlabel("Jenis serangan")
plt.ylabel("Jumlah serangan")

# memberi judul grafik
plt.title("Perbandingan XSS dan DDoS Attack Attempt")

# menambahkan label jumlah di atas bar chart
for i, v in enumerate(values):
    plt.text(i, v + 0.5, str(v),
             color=colors[i], fontweight="bold", ha="center")

# mengatur range sumbu y
plt.ylim(0, 4000)

# menyimpan grafik
plt.savefig("attack_type.jpg")

# menampilkan grafik
plt.show()
