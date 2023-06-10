import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi variabel untuk menghitung jumlah tanda [Abuser] dan [non-Abuser]
abuser_count = 0
non_abuser_count = 0

# menghitung jumlah tanda [Abuser] dan [non-Abuser]
for log in logs:
    if "[Abuser]" in log:
        abuser_count += 1
    elif "[non-Abuser]" in log:
        non_abuser_count += 1

# membuat grafik untuk jumlah tanda [Abuser] dan [non-Abuser]
fig, ax = plt.subplots(figsize=(10, 6))

labels = ["Abuser", "Non-Abuser"]
values = [abuser_count, non_abuser_count]

colors = ["red", "blue"]  # menentukan warna untuk masing-masing bar chart

ax.bar(labels, values, color=colors)

# memberi label sumbu x dan y
ax.set_xlabel("Tanda")
ax.set_ylabel("Jumlah")

# memberi judul grafik
ax.set_title("Perbandingan Jumlah IP [Abuser] dan [non-Abuser]")

# menambahkan label jumlah di atas bar chart
for i, v in enumerate(values):
    ax.text(i, v, str(v), color=colors[i], fontweight="bold",
            ha="center", va="bottom")

# menyimpan grafik
plt.savefig("viz_abuser.jpg")

# menampilkan grafik
plt.show()
