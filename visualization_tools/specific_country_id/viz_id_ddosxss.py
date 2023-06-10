import re
import matplotlib.pyplot as plt

# Membuka file attack_attempt_filtered.log dan membaca isinya
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as file:
    content = file.read()

# Menghitung jumlah kata "[DDoS Attack Attempt] [ID]"
ddos_count = len(re.findall(r"\[DDoS Attack Attempt\] \[ID\]", content))

# Menghitung jumlah kata "[XSS Attack Attempt] [ID]"
xss_count = len(re.findall(r"\[XSS Attack Attempt\] \[ID\]", content))

# Membuat visualisasi
labels = ["DDoS Attack Attempt [ID]", "XSS Attack Attempt [ID]"]
values = [ddos_count, xss_count]
plt.bar(labels, values)

# Menambahkan label jumlah di atas barnya
for i, v in enumerate(values):
    plt.text(i, v+1, str(v), ha="center")

# Memberikan judul dan label pada grafik
plt.title("Jumlah  DDoS dan XSS Attack Attempt dari [ID]")
plt.xlabel("Jenis Serangan")
plt.ylabel("Jumlah Kemunculan")
plt.ylim([0, 1000])

# Menyimpan grafik dalam file viz_id_ddosxss.jpg
plt.savefig("viz_id_ddosxss.jpg")
