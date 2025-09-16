# ZMQ: ZeroMQ

## Steps

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTloM28xdm1xeWRjczhlYXVvOXJucWZ2Nnk3bjdrMXc0YzRnbG1xdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nUk0ZWsqujV9uJQUQ9/giphy.gif"><br>
Build docker containernya untuk pengujian ZMQ

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3VjcTJ6bzY3cWsyd3pibHdhbDh5dnoyNXloeWR0emxia2xxeTQzYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fQr62AaRht5HrWzg6Z/giphy.gif"><br>
Cari bridge interface yang digunakan oleh container ZMQnya

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTR6MGsxY3Nzd3NxZDJ3czhnNGx6dnNwYXA2czdrZzJ3eXdqNTZrNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CjjqutOxOwJHB8MrFW/giphy.gif"><br>
Jalankan tcpdump untuk meng-capture komunikasi yang terjadi di bridge interface container ZMQ dan mengumpulkan hasilnya ke dalam file zmq.pcap

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDJsMmJ1czBrZ3pmZ3F3dmcyMmE0am12ZGkxOHpvdmplNWpkYmQ2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SzxzSBUyGMyYktr2UU/giphy.gif"><br>
Jalankan client untuk mekanisme client-server. Jika berhasil maka akan ditampilkan output berikut pada terminal:
```bash
Sending request 0 ...
Received reply 0: b'World'
```

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2hlczQ5bGt5cnYwam10ZDB0ZGNqam0zbXBmOGltMThzNTRtY2VpYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lPGuZB9NTvaMxvTl0P/giphy.gif"><br>
Jalankan worker untuk mekanisme push-pull. Jika berhasil maka akan ditampilan output seperti:
```bash
Worker 1 received work: 62
```

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmw3YTFlaGRnZXB6MHFzOWtidWNsbDZlZ3phcDkxZTkzcmF4b2ZleCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/47ogVaG7qGsUvBqMOg/giphy.gif"><br>
Jalankan subscriber untuk mekanisme pub-sub. Jika berhasil maka akan mendapatkan tampilan output seperti:
```bash
Received: WAKTU Mon Sep 15 12:32:19 2025
```

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjlhejd5YTRiYjFyeDdjcmo2YnJjOW50NDNrczEyczEwZTRseXU5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NwdlGe0AmLNzXjgVAR/giphy.gif"><br>
Jika semua mekanisme sudah dijalankan, berhentikan tcpdump dan buka file zmq.pcap untuk menampilkan hasil packet capturingnya

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGFueG00b29pOGthemt1aWp0NDJlZTdhbnRzZm92dW1pNGZ4b3o2NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9INiY7quDQTakBgwRS/giphy.gif"><br>
Jika sudah selesai, maka berhentikan docker containernya

##
ZeroMQ merupakan library yang dapat memungkinkan digunakannya berbagai pola komunikasi, seperti Publish-Subscribe, Push-Pull (Pipeline), dan Client-Server

## Publish-Subscribe
Sama halnya dengan MQTT, publisher akan terus menerus mengirimkan pesan hingga subscriber menberhentikannya sendiri. Pesan yang dikirimkan publisher berupa pesan waktu seperti:
```bash
WAKTU Mon Sep 15 12:32:19 2025
```

Serta pada sisi subscriber, diharuskan untuk men-'subscribe' topik yang ingin di-'subscribe'. Pada pengujian ini, subscriber hanya akan menerima pesan yang diawali dengan string "WAKTU"
```bash
socket.setsockopt_string(zmq.SUBSCRIBE, "WAKTU")
```

Mekanisme pub-sub ini bekerja menggunakan protokol TCP di port 12345, ini ditunjukkan pada potongan kode dari pubzmq.py
```bash
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:12345")
```
<img src="https://i.imgur.com/Sh08Tzp.png"><br>

1. Baris 50-52:<br>
Seperti biasanya, dilakukan 3-way handshake antara subssciber (172.19.0.7) untuk membuka koneks ke publisher (172.19.0.3) di port 12345.
2. Baris 53-dst:<br>
Setelah koneksi berhasil dibuat, maka publiser akan terus menerus mengirimkan paket ke subscriber. Ini ditandai dengan flags PSH, yaitu publisher mem-push data ke subscriber dan subscriber mengirimkan packet ACK untuk mengonfirmasi penerimaan data ke publisher

## Push-Pull
Konsep push-pull ini bekerja seperti client-server, push berfungsi untuk mengirimkan pesan ke satu atau lebih penerima dan pull berfungsi untuk menerima pesan dari push.

Pada file pushzmq.py, terdapat producer yang akan menghasilkan workload acak. Ini ditandai dengan potongan kode:
```bash
workload = random.randint(1, 100)
```

Lalu pesan tersebut dikirim ke worker dengan:
```bash
socket.send(pickle.dumps(workload))
```

Pada sisi pull, worker akan selalu menunggu pekerjaan yang dikirimkan oleh worker
```bash
work = pickle.loads(socket.recv())
```
Jika sudah mendapat pekerjaan dari producer, maka worker akan menampilkan output seperti:
```bash
Worker 1 received work: 40
```

Disini juga digunakan protokol TCP yang secara explisit di-define pada potongan kode:
```bash
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:9999")
```
<img src="https://i.imgur.com/Ue2tSC3.png"><br>

- Baris 23-25:<br>
Disini terjadi 3-way handshake antara worker (172.19.0.5) dan producer (172.19.0.2) pada port 9999. 
- Baris 26-36:<br>
Disini terjadi pengiriman data dari producer ke worker yang ditandai dengan flags PSH (Push) dan ACK (Acknowledge). Data ini berisi angka random yang di-produce oleh producer.
- Baris 43-45:<br>
Disini worker meminta menutup koneksi antara worker dan producer yang ditandai dengan flags FIN (Finish)

## Client-Server
Mekanisme client-server ini mirip dengan mekanisme request-response, dimana req digunakan oleh client untuk mengirim request dan response digunakan server untuk menerima request dan membalasnya.

Client akan mengirimkan request ke server yang ditandai dengan potongan kode:
```bash
socket.send(b"Hello")
message = socket.recv()
```

Lalu server mengolah request tersebut dan mengirimkan balasan pesan yang dilakukan oleh potongan kode:
```bash
message = socket.recv()
socket.send(b"World")
```

Contoh tampilan pada sisi client ketika mengirim request ke server adalah sebagai berikut:
```bash
Sending request 0 ...
Received reply 0: b'World'
```

Sama seperti mekanisme pub-sub dan push-pull, client-server ini menggunakan protokol TCP untuk berkomunikasi. Ini ditujukan pada potongan kode pada file serverzmq.py maupun clientzmq.py
```bash
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

socket = context.socket(zmq.REQ)
socket.connect("tcp://zmq-rep:5555")
```

<img src="https://i.imgur.com/zYXWYqt.png"><br>

- Baris 3-5:<br>
Terjadi 3-way handshake antara client (172.19.0.6) dan server (172.19.0.4) untuk membuka koneksi satu sama lain
- Baris 6-15:<br>
Client mengirimkan request ke server, ini ditandai dengan flag PSH (Push) dan server membalas request tersebut dengan mengirimkan pesan dan ditandai dengan flag ACK (Acknowledge). Ini berlangsung terus menerus hingga client me-request untuk memutus koneksinya
- Baris 16-17:<br>
Disini client me-request server untuk memutus koneksinya yang ditandai dengan flag FIN (Finish)

