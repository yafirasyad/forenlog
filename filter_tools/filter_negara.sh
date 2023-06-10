#!/bin/bash

# Fungsi untuk filter XSS
filter_xss() {
    echo " ====== Filter XSS Attack Attempt + VPN/non-VPN + Kode Negara ======"
    echo " !! Kode negara dapat dilihat pada file kode_negara.txt !!"
    read -p " Masukkan Kode Negara dua digit, misal ID/US/RU (tekan enter jika tidak berdasarkan negara *sehingga output hanya attack dan vpn/non-vpn): " kode_negara 
    echo "Sedang melakukan filter XSS, harap tunggu"
    echo "..."
    echo "..."
    if [[ -n "$kode_negara" ]]; then
        mkdir -p attack_type_filtered_bycountry/xss_country
        grep "\[XSS Attack Attempt\].*\[${kode_negara}\].*\[VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_bycountry/xss_country/xss_${kode_negara}_vpn.log
        grep "\[XSS Attack Attempt\].*\[${kode_negara}\].*\[non-VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_bycountry/xss_country/xss_${kode_negara}_nonvpn.log
    else
        mkdir -p attack_type_filtered_nocountry/xss_nocountry
        grep "\[XSS Attack Attempt\].*\[VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_nocountry/xss_nocountry/xss_vpn_nocountry.log
        grep "\[XSS Attack Attempt\].*\[non-VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_nocountry/xss_nocountry/xss_nonvpn_nocountry.log
    fi
    echo "Filtering log XSS sudah selesai. File tersimpan pada folder attack_type_filtered"
}

# Fungsi untuk filter DDoS
filter_ddos() {
    echo " ====== Filter DDoS Attack Attempt + VPN/non-VPN + Kode Negara ======"
    echo " !! Kode negara dapat dilihat pada file kode_negara.txt !!"
    read -p " Masukkan Kode Negara dua digit, misal ID/US/RU (tekan enter jika tidak berdasarkan negara *sehingga output hanya attack dan vpn/non-vpn): " kode_negara 
    echo "Sedang melakukan filter XSS, harap tunggu"
    echo "..."
    echo "..."
    if [[ -n "$kode_negara" ]]; then
        
        mkdir -p attack_type_filtered_bycountry/ddos_country
        grep "\[DDoS Attack Attempt\].*\[${kode_negara}\].*\[VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_bycountry/ddos_country/ddos_${kode_negara}_vpn.log
        grep "\[DDoS Attack Attempt\].*\[${kode_negara}\].*\[non-VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_bycountry/ddos_country/ddos_${kode_negara}_nonvpn.log
    else
        mkdir -p attack_type_filtered_nocountry/ddos_nocountry
        grep "\[DDoS Attack Attempt\].*\[VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_nocountry/ddos_nocountry/ddos_vpn_nocountry.log
        grep "\[DDoS Attack Attempt\].*\[non-VPN\]" hasil_filter_from_access_log/attack_attempt_filtered.log > attack_type_filtered_nocountry/ddos_nocountry/ddos_nonvpn_nocountry.log
    fi
    echo "Filtering log DDoS sudah selesai. File tersimpan pada folder attack_type_filtered"
}

# # Hapus folder hasil filter sebelumnya jika ada
# if [ -d "attack_type_filtered" ]; then
#     rm -rf attack_type_filtered
# fi

# if [ -d "attack_type_filtered_nocountry" ]; then
#     rm -rf attack_type_filtered_nocountry
# fi

# Tampilkan menu
echo "Pilih filter yang ingin dilakukan:"
echo "1. Filter XSS Attack Attempt + VPN/non-VPN + Kode Negara"
echo "2. Filter DDoS Attack Attempt + VPN/non-VPN + Kode Negara"
read -p "Masukkan angka menu: " pilihan

# Jalankan fungsi sesuai dengan pilihan
case $pilihan in
    1)
        filter_xss
        ;;
    2)
        filter_ddos
        ;;
    *)
        echo "Pilihan tidak valid"
        ;;
esac


# echo "==================  HARAP DIBACA  ======================!"
# echo "Setelah selesai melakukan filter harap hasil filter disimpan pada folder tersendiri karena file hasil output pada program ini akan otomatis terhapus jika memulai program lagi untuk menghindari duplikasi hasil filter"
