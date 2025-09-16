# SOAP: Simple Object Access Protocol

## Steps

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTBla3k0cmJkOHJidmNyNXF4ZnFvc2RrMG8yeThwejZreHV0OWg2YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/usO1YBFuNt0SeW5lb7/giphy.gif"><br>
Build docker container untuk pengujian SOAP

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXRsZ3JzbGtzMXgxejYyOW05MHZqZzE2dDlkaGNnY3k4djljbHFoZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NvbYtQTzgS6HdGRHOv/giphy.gif"><br>
Jalankan terlebih dahulu soap-servernya

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHkxb2MzNHUxdHVuYzJ3Znh6dTZrbmhhODJ3NTRmc3VmbWU1YW1tdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FwNRk6GCNR2nYwe0V0/giphy.gif"><br>
Cari bridge interface yang digunakan oleh docker container SOAP

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjMyM3N3bjF2NDN3Y3d6anA3MWw4MzdpY2RuZjI5NWpoZnRiZDNxYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ss3tl1tzetLtsaRqba/giphy.gif"><br>
Mulai packet capturingnya menggunakan bridge interface yang sudah didapat dan mengumpulkan hasil capturinnya dalam bentuk file soap.pcap

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmhlY3Z0ZHBzNTVtNDFvZ2RieXExYWN3bjRwbGw2ZnNkcG5mOXljaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ze0wiCVWrjgmvNLWv5/giphy.gif"><br>
Coba jalankan client-soapnya, jika berhasil, maka dari sisi server akan menampilkan output seperti ini:
```bash
"GET /?wsdl HTTP/1.1" 200
"POST / HTTP/1.1" 200
```

Dan dari sisi client akan menampilkan output seperti:
```bash
Hasil penjumlahan dari server SOAP: 15
```

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWY1ZmkyNXVkcHdzaHJxZmQwMzc5NGRodHd0MmlxNWh1Y3F4ZTY3aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IdzHvDQ1MwFeHsCgk2/giphy.gif"><br>
Pastikan jalankan client-soapnya setelah menjalankan tcpdump, karena setiap menjalankan client, maka tcpdump akan otomatis meng-capture packetnya 

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2o1bW1qNXRoc2JyZHRtNHdrd2U2OGxmaWVhZjBoMHc2MDdkY3NhNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ysdpMcMYzz4QOjtcD5/giphy.gif"><br>
Jika sudah menjalankan client-soapnya, matikan tcpdump-nya dan buka file soap.pcap untuk melihat hasil packet capturingnya.

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmZ1Z2c2bnF1enRhZWV0OW95OHZrcjQ3MGN4cGt5Ym92dm0xY3VlMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Hvhbs8hvatmg7XKTXU/giphy.gif"><br>
Setelah semuanya selesai, berhentikan docker containernya

##
SOAP atau Simple Object Access Protocol merupakan protokol berbasil XML yang digunakan untuk komunikasi antara client dan server di suatu jaringan. Pada pengujian ini terdapat library yang masing-masing digunakan oleh client dan server, yaitu Zeep dan Spyne.

Zeep merupakan library yang digunakan client untuk menggunakan SOAP web services yang disediakan oleh server. Zeep ini akan membaca wsdl (Web Services Description Language) dari server dan otomatis membentuk SOAP request dalam bentuk XML, lalu mengirimkannya melalui protokol HTTP. Ini ditunjukkan pada potongan kode berikut:

```bash
wsdl = 'http://soap-server:8000/?wsdl'
client = Client(wsdl=wsdl)
result = client.service.add(10, 5)
```

Pada sisi server, digunakan library/framework Spyne untuk membangun SOAP web services. Spyne akan membuat endpoint HTTP serta meng-handle request SOAP yang dikirimkan oleh client. Disini sudah ter-define fungsi method yang disediakan oleh server untuk dipanggil oleh client

```bash
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b
```
<br>
<img src="https://i.imgur.com/qoJNPFZ.png"><br>

- Baris 1-3:<br>
Disini dijalankan 3-way handshake oleh protokol TCP untuk membuka koneksi HTTP (SOAP) sebelum digunakan
- Baris 4:<br>
Client meminta file WSDL dari server SOAP. WSDL ini berisi berbagai services seperti fungsi dan parameter. pada sisi client akan mengirimkan output ke terminal berupa:
```bash
Hasil penjumlahan dari server SOAP: 15
```
- Baris 14:<br>
Server merespons kembali ke client dengan file WSDL dan mengirimkan output pada terminal seperti:
```bash
"GET /?wsdl HTTP/1.1" 200
"POST / HTTP/1.1" 200
```
Ini menunjukkan server menerima request GET dari client dan server mengirimkan hasil requestnya menggunakan method POST
- Baris 15-17:<br>
Koneksi TCP ditutup, ini ditunjukkan dengan flags FIN, ACK