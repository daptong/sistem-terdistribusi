# REST: Representational State Transfer

## Steps

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2NodWVqYnJwNmtwdWltem03NTB5YmIzNzB6Y2NyZXhhcHdlaXk5aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7e35Qc4FIK3qj58oUv/giphy.gif"><br>
Build dan jalankan docker container untuk pengujian REST

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnRmdTdyYmVla256eHl5MjFyNzA0MGx4ZWx0ZmRvMWFkNnlhanp0aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hg5lbkI9K2oIjIUgXV/giphy.gif"><br>
Jalankan rest-server terlebih dahulu

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmxoZG85YnJzOXd5bDZkYnEycWtocTNyanY3NHplNjB0c3FpdTY1YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wuJ32NDA9o0Uj49Ib8/giphy.gif"><br>
Setelah itu, gunakan ip a untuk mencari interface bridge docker container yang digunakan

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzgyMm5sZ2FzejlrcWxwdHJpNjdsaTkzeDlqc2VtMTF1aW1iZXpkayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dP6tYqDje8cEktGEUL/giphy.gif"><br>
Lalu capture packet yang berkomunikasi antara client dan server pada interface bridge yang sudah di-copy dan membentuk hasilnya menjadi file rest.pcap

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzRia285M2xydXhmaWY5ZXhxOWl3cGFyZ3F4dmw0MG1tdXUzOXQ5ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LUxTH8tENSkhNdEjqF/giphy.gif"><br>
Jalankan rest-client dengan tambahan parameter:
```bash
--op both -a 2 -b 3
```

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHg5aDdpYmE0YWR3NTJ0MGM5dzJ6M29laW9hbjhhdGwwdm1lYTFzMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tC91pVlfiMxqBirKZQ/giphy.gif"><br>
Untuk melihat apakah tcpdump sudah meng-capture packet dengan baik, jalankan lagi rest-clientnya. Jika sudah benar, maka setiap client mengirimkan packet ke server, tcpdump akan meng-capture packet tersebut dan menyimpannya

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3E5MG5zOWs3Z2VpdWJ6djV0Z21qdHhmdXZubXJzdzlvejJmbXd3dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CJDtSqjmwN7Bw8Kzfl/giphy.gif"><br>
Jika pengujian rest-client sudah selesai, berhentikan program tcpdump menggunakan Ctrl+C/Command+C lalu buka file rest.pcap untuk melihat hasil packet capturenya

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGMwbmx6ejBnanhvc3J2ZzFyZWlxaTNob215aGlyM3RuZWQ3anFubyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/t7rPcNxWMtzZm9KSMJ/giphy.gif"><br>
Untuk memberhentikan docker containernya, gunakan perintah seperti di atas

##
REST merupakan arsitektur/konsep yang digunakan untuk membangun API yang biasa digunakan untuk web service. REST berjalan di atas protokol HTTP, sehingga komunikasi antara client dan server mengikuti aturan HTTP

Pada pengujian ini, terdapat juga dua node yaitu client dan server, dimana akan mengirimkan HTTP request ke server melalui kode berikut

```bash
r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
```

BASE dan endpoint yang dapat digunakan sudah di-define pada sisi server, yaitu GET, /add dan /mul. Untuk parameter lainnya - seperti a dan b - user dapat mengirimkan angka dengan tipe data integer. 

Protokol TCP juga digunakan pada client dan server untuk mengirimkan pesan HTTP. Ini dapat dilihat pada fungsi requests, dimana fungsi ini sekaligus membuat TCP connection antara client dan server dan melakukan 3-way handshake (SYN, SYN-ACK, dan ACK). Ini juga dapat dibuktikan melalui tampilan packet capture di bawah.

<img src="https://i.imgur.com/GmgLBRy.png"><br>

- Baris 1-3: <br>
Client akan membuka koneksi TCP ke server serta melakukan tahap awal dari 3-way handshake, yaitu SYN.
<br>Ketika server menerima packet SYN tersebut, server mebalasnya dengan SYN, ACK
<br>Setelah itu, client mengonfirmasinya dengan membalas ACK ke server. Disini tahap 3-way handshake sudah selesai dan TCP connection antara client dan server siap digunakan
- Baris 4:<br>
Disini client mengirimkan HTTP request ke server berisikan:

```bash
   GET /add?a=2&b=3 HTTP/1.1
```

- Baris 8:<br>
Server merespons HTTP request tersebut dengan:

```bash
   HTTP/1.1 200 OK
   Content-Type: application/json
   {"result":5}
```

- Baris 10-12:<br>
Disini terdapat TCP flags yaitu FIN dan ACK, client mengirimkan sinyal untuk menutup TCP connection ke server lalu pada baris 12 server merespons tersebut dengan menutup koneksinya