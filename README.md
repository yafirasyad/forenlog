_Bismillah_
# Forenlog :mag: - Tools untuk filtering log serangan pada situs web 
Program untuk filtering log setelah serangan yang terjadi pada situs web yang tersimpan pada acccess.log web server Nginx. Program dapat memfilter serangan *currently XSS dan DDoS menggunakan Regular Expression dan API dari ipdata.co untuk mendapatkan informasi IP.

```catatan:```<br>
Sebelum menggunakan dapat dipahami bahwa file di atas masih terdapat hasil filter dan gambar hasil visualisasi, anda dapat menghapusnya karena file hasil filter tersebut hanyalah contoh. 
Seperti pada folder ```filter_tools``` terdapat folder:
- hasil_filter_from_access_log
- attack_type_filtered_bycountry
- attack_type_filtered_nocountry

dan folder ```visualization_tools``` di dalamnya terdapat folder dan di dalam folder tersbut ada file dengan format ```.jpg``` anda dapat menghapusnya.

## Technologies :computer:
### Programming Languages 
- Bash/Shell
- Python
### 3rd Party
- ipdata.co API

<br>

## Features :man_technologist:
- Filtering log serangan XSS dan DDoS (pemberian tanda [XSS Attack Attempt] atau [DDoS Attack Attempt])
- Pemberian informasi penggunaan VPN, status abusive IP dan kode negara
- Filtering sesuai kode negara yang akan dicari 
- Mengelompokkan sesuai penggunaan VPN dan negara

#### Next Development: 
- Menggunakan python untuk visualisasi perbandingan data pada log 
- Menambahkan filter serangan lain mengacu pada OWASP TOP 10, 
- lebih mudah digunakan dan hemat API request (karena saat ini terbatas hanya 1.500 request/day dari ipdata.co)

<br>

## How to use :hammer_and_wrench:	
### Syarat:
- Dijalankan pada sistem operasi berbasis unix/linux
- Terinstall Bash
- Terinstall Python3 (opsional)
- Mendapatkan API key ipdata.co (untuk mendapat detail informasi vpn, abusive dan kode negara pada IP)
### Simple Step
1. Clone repository
```bash
$ https://github.com/yafirasyad/forenlog.git
```
2. Isi API Key pada file yang terletak pada folder ```filter_tools/filter_from_access_log.sh``` baris awal
3. Sesuaikan path folder penyimpanan (baris ke 77 dan 136) maupun input file (baris ke 143) pada folder ```filter_tools/filter_from_access_log.sh```
4. Simpan dan jalankan
 
*Untuk lebih jelasnya dapat lihat pada ```Contoh Penggunaan``` di bawah 
<br>

## Contoh Penggunaan (detail step)
Pada awalnya terdapat 3 folder utama
1. ```barang_bukti``` berisi file barang bukti yang nantinya akan difilter
2. ```filter_tools``` berisi program yang akan digunakan untuk filtering log serangan
3. ```visualization_tools``` berisi file program python untuk membantu memvisualisasikan data serangan (comingsoon)

Pada contoh penggunaan kali ini hanya digunakan 2 folder utama yaitu ```barang_bukti``` dan ```filter_tools``` saja. Berikut contoh penggunaan 
1. Filter langsung dari access.log dan penambahan detail informasi kode negara, vpn, dan abusive ip
2. Filter untuk mencari penyerang berdasarkan kode negara

```Opsional``` pada folder ```visualization_tools``` Pada folder tersebut terdapat file dengan ekstensi ```.py``` yang nantinya bisa diatur path input file dan penyimpanan dan dijalankan menggunakan python3.

### 1. Filter langsung dari access.log dan penambahan detail informasi kode negara, vpn, dan abusive ip
1. Jika sudah clone kamu dapat mengisi dan mengubah terlebih dahulu api key maupun path folder input file log dan penyimpanan log sesuai kebutuhan. 
- Dapatkan API Key dari https://ipdata.co dan atur nilai API Key pada baris: <img width="1047" alt="Screenshot 2023-06-10 at 23 01 55" src="https://github.com/yafirasyad/forenlog/assets/46275481/67ec6e35-a436-4ba8-ac39-b34cfb1260b1">
- Berikut contoh penyimpanan hasil filter XSS: <img width="1191" alt="Screenshot 2023-06-10 at 22 45 25" src="https://github.com/yafirasyad/forenlog/assets/46275481/02a78328-d126-4e06-9eb9-d2b08f1f7066">
- Dan untuk DDoS: <img width="1223" alt="Screenshot 2023-06-10 at 22 49 20" src="https://github.com/yafirasyad/forenlog/assets/46275481/424d0678-debc-46a0-b22b-f5295c6b6a42">
- file log untuk diinput: <img width="1060" alt="Screenshot 2023-06-10 at 23 02 38" src="https://github.com/yafirasyad/forenlog/assets/46275481/6a93d0c9-7db4-45f7-8eaf-4f15a2e76490">

2. Jika sudah maka file filter_from_access_log.sh dapat dijalankan.
Berikut contoh pada gambar di bawah terlihat file dapat dijalankan menggunakan perintah ```./filter_from_access_log.sh``` 
<br> <img width="359" alt="image" src="https://github.com/yafirasyad/forenlog/assets/46275481/d9cf1a1a-3400-4e05-aa10-faa0bed512cf">

3. Jika sudah, maka file hasil filter akan tersimpan pada folder ```filter_tools/hasil_filter_from_access_log```
    <img width="301" alt="image" src="https://github.com/yafirasyad/forenlog/assets/46275481/1b2e45ed-0f2e-4c9d-a8a9-d47624b1a76e">

 ### 2. Filter untuk mencari penyerang berdasarkan kode negara
 1. Atur path untuk menyimpan hasil filter dan input file (cara hampir sama seperti pada poin 1)
 2. Eksekusi file dengan memilih apakah ingin memfilter serangan XSS atau DDoS
<br> <img width="378" alt="image" src="https://github.com/yafirasyad/forenlog/assets/46275481/caf95d18-9160-41a1-98ac-3175152f96ea">
 3. Mengisi negara yang ingin difilter. Contoh: ID (Indonesia)
 <br><img width="377" alt="image" src="https://github.com/yafirasyad/forenlog/assets/46275481/4b91c0ee-fc25-46e8-aa51-427a6935fcd9">
 4. Jika tidak memilih salah satu dari 2 serangan maka program akan berhenti, tetapi jika tidak mengisi kode negara maka akan tersimpan pada folder ```attack_type_filtered_nocountry``` jika tersimpan sesuai negara yang dicari maka tersimpan pada folder ```attack_type_filtered_bycountry```. Berikut contoh folder hasil filter:<br> <img width="157" alt="image" src="https://github.com/yafirasyad/forenlog/assets/46275481/43c669e0-ce76-47c9-9358-5152d6ac0fb2">
<br>
PS: not finished yet, but you can use it with guidance.
<br> <br>
Built With :heart: by Grinaldy Yafi' Rasyad | Yogyakarta, Indonesia
