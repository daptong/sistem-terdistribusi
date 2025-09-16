# upcall

## Steps

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmxuNW5mNGJtb2I5a3Jkd3Rhd2Jrem9oN3UwdnJ4bTJqaDlrajByZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d2WEiIRm5ld7KW1Bo7/giphy.gif"><br>
Build docker containernya untuk pengujian upcall

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2ttMzc3dGN3MXVndjFuenp5MWo5emZzanB1d2FuODV1Y2IzYWU5ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NOcNMzHAEK2aLENC3Q/giphy.gif"><br>
Jalankan upcall-servernya terlebih dahulu

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExczlhMmppeGE3MWVodGMyOXJqN254MnBmdjA5OXJtd3JjbmJ5MXAxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fVT6zWQvYjTuNjE6Kp/giphy.gif"><br>
Cari bridge interface yang digunakan oleh docker container upcall

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJrOXdjazA2Y2FxMDVoNmVwZHMxMDN5ankxcHQ3Z3k4bTVwZXI1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4pc3uzntutVTXfzyDp/giphy.gif"><br>
Jalankan tcpdump untuk meng-capture komunikasi pada bridge interface container upcall dan mengumpulkan hasilnya menjadi file upcall.pcap

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjd0MGRkNWJrZmN1ems1Y3ZvcWhlYjZmZjViYm5mZzB3a3Z2MmpweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F7pjACxLKEbMCqXrvy/giphy.gif"><br>
Baru jalankan upcall-clientnya

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmNrd3ZrOHFmZHZpaTJpeGtmeTJqeXI5cmgwb3U1Ync0ZzB6dTBjbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lgk4t2jl63P3kBqGFc/giphy.gif"><br>
Untuk melihat apakah server berhasil mengirimkan callback ke server, maka coba kirimkan pesan dari client ke server, jika berhasil, maka server akan mengirimkan callback seperti:
```bash
Received from server: Upcall event: Processing 
```
<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHcxb2tiOGRtM2s0bDM3bmUycHA2bDhpbTJ1MnF1a2pramIzODd4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TINKmUutJURVw0kwKA/giphy.gif"><br>
Pastikan juga selama menjalankan upcall-client, tcpdump terus meng-capture packetnya

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExemsxNXdpbGJkOWdxNDV2bnd3eGhxN25tZGlpYW8xZGg3cDIzemRrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7noXiq6d1ZjAb83uw0/giphy.gif"><br>
Setelah selesai menjalankan upcall-client, matikan tcpdumpnya lalu buka file upcall.pcap untuk melihat hasil packet capture-nya

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHk5OHJ5a2ZlZHcxbG9ocGMzdnA4bHVlazI4bmJtMXU0dHY3bjc0OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7XEGaFsN3SKH047bNX/giphy.gif"><br>
Berhentikan docker containernya jika semua sudah selesai dijalankan

##
Upcall merupakan suatu pola komunikasi antar client dan server dimana server tidak hanyak merespons permintaan client secara pasif, tetapi juga mengirimkan callback kepada client. Pada pengujian ini, mekanisme upcall terjadi ketika server menerima pesan dari client, setelah itu server langsung mengirimkan balasan khusus berupa:
```bash
"Upcall event: Processing " + data
```
Ini merupakan callback yang dikirimkan dari server ke client

Contohnya, ketika user mengirimkan pesan '1' ke client, maka server akan menerima pesan tersebut dan mengemasnya menjadi:
```bash
Received from client: 1
```
Lalu server mengirimkan callback ke client dengan pesan:
```bash
Received upcall from server: Upcall event: Processing 1
```

Ini berlangsung terus menerus hingga salah satu dari mereka (client/server) memutus koneksinya

Pada pola komunikasi upcall, digunakan protokol TCP karena terdapat pada potongan kode dibawah ini yang menunjukkan bahwa secara default, Python akan membuat socket dengan tipe TCP
```bash
server_socket = socket.socket()
client_socket = socket.socket()
```

Pada kode servercall.py, terdapat juga potongan kode seperti dibawah ini yang menunjukkan karakteristik dari protokol TCP, yaitu .listen() dan .accept():
```bash
server_socket.listen(1)
conn, address = server_socket.accept()  
```

<img src="https://i.imgur.com/IUGD1XW.png"><br>

- Baris 1-3:<br>
Seperti TCP pada umumnya, dilakukan 3-way handshake untuk membuka jalur komunikasi antara client ke server, maupun sebaliknya
- Baris 4-9:<br>
Disini terjadi pertukaran data antara client dan server, dimana client awalnya mengirim pesan ke server, lalu pada baris selanjutnya server menerima pesan tersebut dan memprosesnya. Setelah itu server mengirimkan callback berupa pesan khusus ke client dan client menerima callback tersebut
- Baris 10-13:<br>
Terjadi tahapan 4-way termination, yaitu client me-request untuk menutup koneksi, dan pada baris 12, server menyetujui request tersebut
