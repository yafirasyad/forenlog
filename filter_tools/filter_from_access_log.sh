#!/bin/bash

# Mengatur API key ipdata
API_KEY=""

# Membuat regex untuk XSS Attack Pattern dengan encoding
XSS_REGEX='(<\s*(script|iframe|img|body|input|style|textarea|base|object|embed|form)[^<>]>|(%3C|<)[\s\/.?](s|S)(c|C)(r|R)(i|I)(p|P)(t|T|f|F|r|R|b|B|i|I|m|M|o|O|e|E)[\s\/.?](:|>|%3E)|javascript:|data:text\/html|vbscript:|on[a-z]+\s?=\s?["'"'"']?[^"'"'"'>]+|expression\s?\(\))'

# Membuat regex untuk DoS Attack Pattern
DOS_REGEX='HTTP\/1\.[01]\" [45][0-9][0-9]'

# Membuat array untuk menyimpan IP yang terdeteksi melakukan serangan
declare -A attack_ips

echo "Sedang melakukan filter, harap tunggu"
echo "..."
echo "Menandai Attack Attempt (V)"
echo "Mencari Kode Negara dari IP (V)"
echo "Menandai Jika Termasuk Abuser/non-Abuser (V)"
echo "Menandai Jika Termasuk VPN/non-VPN (V)"
echo "Finisihing..."


# Membaca file access log nginx dan memfilter setiap baris log
while read line; do
  # Mengecek apakah baris log mengandung XSS Attack Pattern
  if [[ "$line" =~ $XSS_REGEX ]]; then
   
    # Mengambil IP dari baris log menggunakan regex
    ip_regex='([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}|:)|(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?::(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?|([0-9]{1,3}\.){3}[0-9]{1,3}'
    if [[ $line =~ $ip_regex ]]; then
      ip=${BASH_REMATCH[0]}
      # Menambahkan IP ke array attack_ips dengan key "xss"
      attack_ips[xss]+="$ip "

      # Memanggil API ipdata.co untuk mendapatkan informasi lokasi IP dan informasi tambahan
      response=$(curl -s "https://api.ipdata.co/${ip}?api-key=${API_KEY}")
      country=$(echo $response | jq -r '.country_code')
      is_known_attacker=$(echo $response | jq -r '.threat.is_known_attacker')
      is_known_abuser=$(echo $response | jq -r '.threat.is_known_abuser')
      is_threat=$(echo $response | jq -r '.threat.is_threat')
      is_tor=$(echo $response | jq -r '.threat.is_tor')
      is_vpn=$(echo $response | jq -r '.threat.is_vpn')
      is_proxy=$(echo $response | jq -r '.threat.is_proxy')
      is_anonymous=$(echo $response | jq -r '.threat.is_anonymous')

  # Check apakah IP merupakan penyerang
    if [ "$is_known_attacker" == "true" ] || [ "$is_known_abuser" == "true" ] || [ "$is_threat" == "true" ]; then
      ip_status="Abuser"
    else
      ip_status="non-Abuser"
    fi

  # Check if it's a proxy, VPN or anonymous
    if [[ "$is_tor" == "true" || "$is_vpn" == "true" || "$is_proxy" == "true" || "$is_anonymous" == "true" ]]; then
        # Jika terdeteksi menggunakan proxy atau anonymous, tulis "VPN"
        vpn_status="VPN"
    else
        # Jika tidak terdeteksi menggunakan proxy atau anonymous, tulis "non-vpn"
        vpn_status="non-VPN"
    fi
  # Mengambil tanggal dan waktu dari baris log menggunakan regex
     datetime_regex='([0-9]{1,2}\/[a-zA-Z]{3}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}) [\+\-][0-9]{4}'
      if [[ $line =~ $datetime_regex ]]; then
        datetime=${BASH_REMATCH[1]}

        # Mencari request payload pada baris log menggunakan regex
         payload_regex='\"([A-Z]{3,7}) ([^ ]+) HTTP(s?)\/[0-9]\.[0-9]\"'

          if [[ $line =~ $payload_regex ]]; then
            payload=${BASH_REMATCH[0]}
          else
            payload="-"
          fi
              
      # Menambahkan informasi lokasi beserta tanggal dan waktu ke dalam file attack_ips.log
      echo "[XSS Attack Attempt] [$country] [$ip] [$datetime] [$ip_status] [$vpn_status] [$payload]" >> hasil_filter_from_access_log/attack_attempt_filtered.log
        fi
      fi
      continue
      fi




  # Mengecek apakah baris log mengandung DoS Attack Pattern
  if [[ "$line" =~ $DOS_REGEX ]]; then
    
     # Mengambil IP dari baris log menggunakan regex
      ip_regex='([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}|:)|(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?::(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?|([0-9]{1,3}\.){3}[0-9]{1,3}'
      if [[ $line =~ $ip_regex ]]; then
        ip=${BASH_REMATCH[0]}
      # Menambahkan IP ke array attack_ips dengan key "ddos"
      attack_ips[ddos]+="$ip "
   
      # Memanggil API ipdata.co untuk mendapatkan informasi lokasi IP dan informasi tambahan
        response=$(curl -s "https://api.ipdata.co/${ip}?api-key=${API_KEY}")
        country=$(echo $response | jq -r '.country_code')
        is_known_attacker=$(echo $response | jq -r '.threat.is_known_attacker')
        is_known_abuser=$(echo $response | jq -r '.threat.is_known_abuser')
        is_threat=$(echo $response | jq -r '.threat.is_threat')
        is_tor=$(echo $response | jq -r '.threat.is_tor')
        is_vpn=$(echo $response | jq -r '.threat.is_vpn')
        is_proxy=$(echo $response | jq -r '.threat.is_proxy')
        is_anonymous=$(echo $response | jq -r '.threat.is_anonymous')

     # Check apakah IP merupakan penyerang
    if [ "$is_known_attacker" == "true" ] || [ "$is_known_abuser" == "true" ] || [ "$is_threat" == "true" ]; then
      ip_status="Abuser"
    else
      ip_status="non-Abuser"
    fi

  # Check if it's a proxy, VPN or anonymous
    if [[ "$is_tor" == "true" || "$is_vpn" == "true" || "$is_proxy" == "true" || "$is_anonymous" == "true" ]]; then
        # Jika terdeteksi menggunakan proxy atau anonymous, tulis "VPN"
        vpn_status="VPN"
    else
        # Jika tidak terdeteksi menggunakan proxy atau anonymous, tulis "non-vpn"
        vpn_status="non-VPN"
    fi
  # Mengambil tanggal dan waktu dari baris log menggunakan regex
     datetime_regex='([0-9]{1,2}\/[a-zA-Z]{3}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}) [\+\-][0-9]{4}'
      if [[ $line =~ $datetime_regex ]]; then
        datetime=${BASH_REMATCH[1]}
    
       # Mencari request payload pada baris log menggunakan regex
          payload_regex='\"([A-Z]{3,7}) ([^ ]+) HTTP(s?)\/[0-9]\.[0-9]\"'

          if [[ $line =~ $payload_regex ]]; then
            payload=${BASH_REMATCH[0]}
          else
            payload="-"
          fi
      # Menambahkan informasi lokasi beserta tanggal dan waktu ke dalam file attack_ips.log
      echo "[DDoS Attack Attempt] [$country] [$ip] [$datetime] [$ip_status] [$vpn_status] [$payload]" >> hasil_filter_from_access_log/attack_attempt_filtered.log
      fi
      fi
      continue
      fi

  
  done < /var/log/nginx/fix/barang_bukti/barangbukti_1011042023.log


echo "Filtering log sudah selesai. File tersimpan pada folder yang sama"
