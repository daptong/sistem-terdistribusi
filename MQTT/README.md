# MQTT: Message Queuing Telemetry Transport

## Steps
<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjRlOTZycGttbHZnY2p4azdzaW1ibHVsam0zYjNjZjhtcGVldnI1OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IugLOTjmYCtDtgSZ5B/giphy.gif"><br>
Build docker container dengan memasukkan perintah diatas

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDVheWFyYWF1NHJ1YXgyZzZ5a2l1cTR2dWhqb2tsdG5sOXoxZDgzeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ecL0JUrEA0ryDXBqW2/giphy.gif"><br>
Jalankan perintah diatas untuk memulai model publisher pada MQTT

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2tsM3VsaGdmZHlqdWN0YjBib3J1aDk4c2Ezb2UzYjZpMXV1NTdpeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/x6Of5tmP4lRz1EJ1Ft/giphy.gif"><br>
Jalankan juga perintah diatas untuk memulai model subsriber pada MQTT

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTl1Z2h6OG1oMTBmNHdpcnk4NXJ0aGNhZnY3cmprd2lrYWU2OHB4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ILMVOeRny9LTHUv5gs/giphy.gif"><br>
Dapat dilihat ketika kedua model tersebut sudah dijalankan, maka publisher akan mengirimkan data dan subscriber akan menerimanya secara langsung

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2IwMDBnYWxpNTcxOGZtZ3RjMTZkN3NoZmYybm0wbWVybjhuaDRmMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wimoOMN0yA9owrp2Zs/giphy.gif"><br>
Cari interface bridge yang digunakan docker container menggunakan ip a

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmdmbHhmZDk4N3oybnZlMGp1cDdoaHA1dHk5MHNwY29kdmFtYTdnYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dRq7nKA8k4hEZVpgfa/giphy.gif"><br>
Gunakan tcpdump untuk menangkap packet yang berkomunikasi di interface tersebut dan mengumpulkannya pada file mqtt.pcap

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNieTloZDg0a2dqcDBrY2hlZ3lrbDl0YTc5cnU1cms0aWJkYmdzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/T3D6Iol1umHxLj1CKE/giphy.gif"><br>
Setelah mematikan tcpdump, buka file mqtt.pcap untuk menampilkan hasil packet capture-nya

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXQ0M2g0ZHFrcGdyYjUwOWtjYWY0ajQ5cGxndGZnNnB0OHZ3ZDZ4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mlAznb0Ae7pzlWIYLe/giphy.gif"><br>
Untuk memberhentikan docker containernya, jalankan perintah diatas

##
Dalam demonstrasi penggunaan protokol jaringan MQTT, terdapat dua model, yaitu pub (publisher) dan sub (subscriber). Publisher berfungsi sebagai server yang mengirimkan pesan ke broker MQTT, sedangkan subscriber berfungsi sebagai client yang menerima pesan yang dikirimkan oleh publisher. Subscriber harus men-subscribe 'topic' sebagai syarat untuk menerima pesan.

Pada pengujian ini, subscriber telah men-subscribe topic 'sister/temp' yang disediakan oleh publisher. Publisher akan mengirimkan pesan seperti:

```bash
Published: Suhu: 28°C
```

Pesan ini dikirimkan secara terus-menerus hingga subscriber menghentikannya sendiri. 

<img src="https://i.imgur.com/07FVBDv.png"><br>

Pada tampilan Packet Capture diatas, dapat dilihat terdapat dua jenis protokol yang berulang kali digunakan mengirim pesan, yaitu MQTT dan TCP. Publisher menggunakan protokol MQTT untuk mengirim pesan ke subscibernya sedangkan subscriber menggunakan protokol TCP untuk mengirimkan pesan ACK atau Acknowledgement, yang berarti pesan MQTT dari publisher sudah sampai ke subscriber dan subscriber mengonfirmasinya.

Selain itu, dapat dilihat juga dari port yang digunakannya, port 1883 merupakan unsecured port yang sering digunakan untuk protokol MQTT. Ini juga dapat divalidasi dengan melihat potongan kode dari sub.py.

```bash
broker = "mqtt-broker"
port = 1883
topic = "sister/temp"
```

##

<image src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGw2eXJ5eXpiNXNraGs1Y2R2eGlvOWcweXd6M3FmcnU5YnZhMzF6cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4w3vFYboLKB1n3X22V/giphy.gif"><br>
Berikut adalah percobaan untuk fibonacci sequence. Publisher akan mengirimkan nilai fibonacci dengan nilai awal 0 (sudah di-define di sisi publisher), lalu publisher akan terus menerus mengirimkan nilai sesuai dengan aturan fibonacci. Nilai fibonacci terus dikirimkan ke subscriber hingga publisher menghentikan programnya sendiri, atau ketika subscriber memberhentikan programnya untuk menerima pesan dari publisher
```bash
if n <= 0:
    return 0
elif n == 1:
    return 1:
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```