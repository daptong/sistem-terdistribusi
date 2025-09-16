# RPC: Remote Procedure Call

## Steps

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmlxOXdsNHpjaXQ5dnJ5MXdwMjJiNTAzbHRlam9kODAweWlvZ3dheiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aeV0G5L6A1sB8WLdm8/giphy.gif"><br>
Build docker containernya menggunakan perintah diatas

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemkyMndvcmdwMm9vczZ5NnRieHlrZWx2aWxkaTY4dGdnMnQ3bTUwayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xe2dLfEppDQj4r0HCC/giphy.gif"><br>
Jalankan terlebih dahulu rpc-servernya

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2hobWVzbWlzYTFkM2c0bDJnMTdmM3AwaW40YzkwMXloOTEzYjV5OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lg8ot0zDfj7CCqJjrf/giphy.gif"><br>
Cari bridge interface yang digunakan container tersebut

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTZhMnE4OG1yYmVzaXh5aHlhbzNyZjh3NHM3dTZueTc2dG5zNnNzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pvKCKkJRQPNDq5O3YZ/giphy.gif"><br>
Memulai packet capturing menggunakan tcpdump pada bridge interface yang sudah ditentukan dan mengumpulkannya dalam bentuk file rpc.pcap

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNW9xZDd0dTFrbjNqbDAzMDE1azljMms0NmY3dnEwaDRsNTVzY2RpeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5DJY51hDYLhXKsEeuG/giphy.gif"><br>
Setelah tcpdump sudah berjalan, lalu jalankan rpc-clientnya dan jalankan beberapa kali hingga tcpdump benar-benar meng-capture komunikasi di interface tersebut

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExemh5bnp4aXh3MGl2bzVtaXF4OGdnMGlzNzNlcW9wajM3c2VyODBiYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fDHMWdrTy51zQ0YzS6/giphy.gif"><br>
Jika server sudah berjalan, maka ketika client mengirimkan HTTP POST ke server, dan jika server telah menerima pesan tersebut dengan benar, maka server akan membalasnya dengan:
```bash
["POST / HTTP/1.1" 200]
```

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2hyZmp1d204czcyMHNxam94d3MxeG1ibTFybXhxemMzZHFkYnJmayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VcnOppuEm0qRU4aUuo/giphy.gif"><br>
Setelah selesai meng-capture packet menggunakan tcpdump, buka hasil packet capture tersebut untuk melihat visualisasi komunikasi antara client dan server

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExenZkbGZvazNjcDQzbGx3NWlhbnh4dm9rcjhkeXQybzdoYmlka3NyNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OPpg833eG7hTUndzDk/giphy.gif"><br>
Setelah itu, berhentikan docker container-nya

##
RPC atau Remote Procedure Call adalah protokol yang dapat memungkinkan client untuk memanggil suatu fungsi dari server, seolah-olah fungsi itu ada di lokal (client).

Pada pengujian ini, client mengirimkan request ke server menggunakan format pesan yaitu JSON. Payload JSON yang digunakan sudah ter-define pada file rpcclient.py

```bash
payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1,
}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()
```

Dimana method yang digunakan ada POST (tertera pada fungsi requests.post) dan params juga ter-define, yaitu add: [10, 2] dan multiply: [10, 5].

```bash
result_add = call_rpc("add", [10, 2])

result_multiply = call_rpc("multiply", [10, 5])
```

Setelah client mengirimkan pesan request ke server, maka server akan menerima HTTP POST tersebut dan datanya akan diproses menggunakan JSONRPCResponseManager. Disini akan dilihat apa isi dari HTTP POST yang dikirimkan dari client. Lalu server akan menulis response yang akan dikirimkan ke client melalui potongan kode berikut

```bash
response = JSONRPCResponseManager.handle(post_data, dispatcher)
```

Disini dispatcher akan mencari fungsi yang sesuai dengan fungsi yang sudah di-define di server dengan fungsi yang direquest oleh client. Jika terdapat fungsi tersebut maka fungsi add() dan multiply() pada server akan dieksekusi.

```bash
def add(a, b):
    return a / b

def multiply(a, b):
    return a * b
```

Lalu hasil eksekusi fungsi tersebut akan diubah menjadi format JSON lalu dikirimkan ke client.

```bash
self.wfile.write(response.json.encode())
```
<br>
<img src="https://i.imgur.com/C1k9Ope.png">

- Baris 1-3:<br>
Seperti TCP pada umumnya, client dan server akan melakukan tahapan 3-way handshake, dimana client akan mengirimkan packet SYN ke server untuk membuka koneksi dari client ke server. Setelah itu server mengonfirmasi packet SYN tersebut dan membuka koneksi juga dari server ke client melalui packet SYN, ACK.<br>
- Baris 6:<br>
Client mengirimkan pesan ke server berupa HTTP POST dengan body requestnya berisi JSON-RPC seperti

```bash
{
    "method": "add",
    "params": [10, 2]
}
```
- Baris 7-11:<br>
Karena JSON memiliki data yang panjang, maka dikirim secara bertahap yang dibagi menjadi beberapa segmen
- Baris 12:<br>
Server membalas HTTP POST client dengan HTTP/1.0 200 OK serta JSON-nya (hasil RPC)
- Baris 13-14:<br>
Client mengirimkan packet FIN, ACK untuk menutup koneksi antara client dan server