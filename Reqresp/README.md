# reqresp: Request and Response / TCP

## Steps
<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemFuZDBjaWxtbWJzNDcyd2oxaG81Y3liOWdzaGdrdXpqaW53b3dpciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jrWIrESZttoB9wN0uX/giphy.gif"><br>
Build docker container untuk pengujian reqresp menggunakna perintah diatas

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGg4M2I4YjFnZnk1MWlmNWdxeDN1ZDhheTZ3OGl6a3ZzNWV1b3hrbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HgJ6k8Ebj1aAZbdNZ5/giphy.gif"><br>
Lalu, jalankan perintah diatas untuk memulai TCP server pada container

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2Z5MTBkZXNlcm9qajlsbmp4NTg0a2EwMnQ5NG9xdmNuaDR2MDU1MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pwazxEOGPn0vbGTppI/giphy.gif"><br>
Jalankan juga perintah diatas untuk memulai TCP client pada container

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTdmNGdjMjN1cXVmMGd2d204Ym83NnNuMW90cDJlZGw1emcza2w0dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/e74PXxYg94MbgjG3AX/giphy.gif"><br>
Sebelum melakukan pengujian, gunakan perintah ip a untuk mencari bridge interface yang digunakan container untuk melakukan packet capturing

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3Rod28zY3l1azI3M2o1cDJjN3J5bnhkOTlheTk3ZmdtYnZrM2JzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cW1ytY3hbq7sGOyDDx/giphy.gif"><br>
Gunakan perintah tcpdump untuk melakukan packet capturing pada bridge interface container yang sudah didapat dan membuatnya menjadi file tcp.pcap 

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnRyc2RudHc5ODUyOXEyOWl6NjExYXAxZnNycHdiM2E0N25meXliYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uetEfIXEj1OnznlZnn/giphy.gif"><br>
Coba mengirimkan pesan dari client, jika sudah maka akan terlihat bahwa server menerima pesan yang dikirim client dan client menerima pesan juga dari server

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmxqMW16NW1na2ppNnJua3QyNXBmOXY2Z2lyMGdzMTU4bHFkZnV5NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NlM46QWr4o5KmjhJVh/giphy.gif"><br>
Jika sudah, matikan semua node (client, server, tcpdump) menggunakan Ctrl+C / Command+C

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG5lNXN4dzB2ZWY4b2kzeWFhcWJzejlsaXdpc3N6Y2wzcDh3MWwwNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6oK0xztPNRYdNcxIGO/giphy.gif"><br>
Buka hasil packet capturing untuk melihat visualisasi dari komunikasi antar client dan server pada protokol jaringan TCP

##
Pada pengujian reqresp, protokol jaringan yang digunakan adalah protokol TCP (Transmission Control Protocol). Terdapat juga dua model seperti yang lainnya, yaitu client dan server. Client akan mengirimkan pesan custom (user defined) lalu server akan menerima pesan tersebut dan mengirimkannya kembali ke client.

Terdapat kode yang merupakan karakteristik dari penggunaan protokol TCP, yaitu

```bash
server_socket.listen(1)
server_socket.accept()
```

Fungsi .listen() digunakan pada tahap SYN (synchronize) saat pertama kali dilakukannya handshake antara client dan server, dan fungsi .accept() digunakan pada tahap ACK (acknowledge) ketika client dan server sudah melakukan handshake

<img src="https://i.imgur.com/YzloGHf.png"><br>

Pada tampilan packat capture diatas, terdapat dua node dengan port 42476 (client) dan 2222 (server) yang terus berulang kali mengirimkan data satu sama lain menggunakan protokol TCP.

Pada tab info di baris 1-3, terdapat tiga TCP flags yang muncul, yaitu:
- Baris 1: PSH, ACK: <br>
Disini client mengirimkan (PUSH) pesan ke server dan client mengonfirmasi (ACK) pesan yang dterima dari server
- Baris 3: ACK: <br>
Setelah server mengirimkan kembali pesan tersebut (baris dua) ke client, client mengonfirmasi (ACK) pesan tersebut

##