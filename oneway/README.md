# oneway: UDP

## Steps
<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExemVwcnF0dHh2dTRqMGVjNm5lbjY3bDQweGJxZTUwbnBubHdlaWN0YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QSZ3ByaSIFU7ZJcyAW/giphy.gif"><br>
Build docker container dengan menjalankan perintah diatas

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExejVwMDhqdGJuZjNxZHdka3FoNGVqajZvNG1pdzY0Y3VuNXl2dTg5YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ffEuioc9ERoWasOaqt/giphy.gif"><br>
Jalankan server dengan menggunakan perintah diatas

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdG1ycW41ZnNhMGhyd25zbzhwdWdxd2M2YXhzZHR3enZxMHlxOTAwcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HL1JcD4G1JStsKBHq5/giphy.gif"><br>
Jalankan ip a untuk mencari interface bridge yang digunakan docker container tersebut

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWJsaXczamZuYWdnMWgzdXJ1MTFkeG01dno3ODYzendlcHYxNTczYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GBDmqDwWy3nWC8YHja/giphy.gif"><br>
Jalankan tcpdump terlebih dahulu sebelum menjalankan client karena client hanya mengirimkan satu pesan saja lalu menutup connection-nya dengan server

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExejJnMXRqNmRucWhla3Rka2FyamtxamI0d3plODhqbDh2ampkNHVuZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ss89BA0O1lMyxfcDG3/giphy.gif"><br>
Jalankan client menggunakan perintah di atas

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGNkeDJzcThpZ2wyaXFzbjkyNmZ0NXpoOWZmcHE3bmFlYzR3bW95dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oCysz6OYqtSKlD3ICY/giphy.gif"><br>
Setelah client sudah dijalankan, close/matikan tcpdump lalu buka file udp.pcap untuk melihat hasil packet capture-nya

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWtiaTZpbmtjejFiam40ZmlzNXFmNWppcDJocXU5YTA5aDh4ZGNsbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/z9tAvYlilyMMKk5CBK/giphy.gif"><br>
Gunakan perintah diatas untuk memberhentikan docker containernya

##
Berbeda dengan protokol jaringan TCP (Transmission Control Protocol), protokol jaringan UDP (User Datagram Protocol) merupakan protokol yang connectionless, ini membuat user dapat mengirimkan data secara langsung, tidak membutuhkan handshake seperti TCP. Ini dapat dibuktikan dengan potongan kode dari serverUDP.py seperti:

```bash
server_socket.recvfrom(1024)
server_socket.sendto(message.encode('utf-8'), client_address)
```

Fungsi .sendto() hanya secara eksplisit menyatakan tujuan kemana data akan dikirim, tidak memperdulikan apakan tujuan dapat mengonfirmasi dan menerima data, sedangkan pada TCP terdapat fungsi .listen() dan .accept() dimana kedua fungsi ini dibutuhkan untuk melakukan handshake. Fungsi .listen() digunakan pada tahap SYN (synchronize) antara client dan server sedangkan .accept() digunakan pada tahap ACK (acknowledge) yang berarti data sudah siap untuk dikirim. 

<img src="https://i.imgur.com/pTBLwU2.png"><br>

Pada packet capture diatas, dapat dilihat tedapat dua komunikasi antara port 57314 dengan 12345. Port 57314 merupakan port yang digunakan client untuk mengirim pesan kepada server dengan port 12345. Pesan yang dikirim berupa:

```bash
message = "Hello, UDP server2!"
```

Selain itu, protokol yang digunakan dan ditangkap oleh tcpdump merupakan protokol UDP.
