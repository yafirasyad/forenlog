import re
import matplotlib.pyplot as plt

# membaca file log
with open("/var/log/nginx/fix/filter_tools/hasil_filter_from_access_log/attack_attempt_filtered.log", "r") as f:
    logs = f.readlines()

# inisialisasi variabel untuk menghitung jumlah kode negara
country_count = {}

# menghitung jumlah kode negara
for log in logs:
    country_code = re.search(r'\[([A-Z]{2})\]', log)
    if country_code:
        country_code = country_code.group(1)
        if country_code in country_count:
            country_count[country_code] += 1
        else:
            country_count[country_code] = 1

# membuat grafik untuk jumlah kode negara
labels = list(country_count.keys())
values = list(country_count.values())

plt.bar(labels, values, color='blue', width=0.5)

# memberi label sumbu x dan y
plt.xlabel("Kode Negara")
plt.ylabel("Jumlah")

# memberi judul grafik
plt.title("Jumlah Kemunculan per Kode Negara")

# menambahkan label jumlah di atas bar chart
for i, v in enumerate(values):
    plt.text(i, v, str(v), color='blue', fontweight="bold", ha="center", va="bottom")

# menentukan rentang sumbu Y pada grafik
plt.ylim([0, 2000])

# menyimpan grafik
plt.savefig("country_viz.jpg")

# menampilkan grafik
plt.show()
