# TUTORIAL
* 1. Download python 3.10.4

link download `https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe`
lalu install dan check python sudah terinstall atau belum pada cmd
ketika sudah terinstall maka muncul gambar seperti berikut
![image](https://user-images.githubusercontent.com/101288815/206202342-544b2019-387c-427e-94f9-67f54d592d00.png)

* 2. Upgrade Pip

check versi pip pada cmd dengan mengetik `pip --version`
![image](https://user-images.githubusercontent.com/101288815/206202802-ad12b2a8-f0d3-4b93-81d5-de299d5c2a15.png)
jika dibawah 22.3.1 maka upgrade pip dengan `mengetik python -m pip install --upgrade pip`
lalu check kembali versi pip

* 3. Download file pada github ini

![image](https://user-images.githubusercontent.com/101288815/206203247-62df3b68-b6ca-4098-b9be-b0b3819e14a7.png)
tekan download zip lalu unzip file zip yang sudah didownload tadi
![image](https://user-images.githubusercontent.com/101288815/206203364-7323c2d9-c31c-49ca-bf3b-291366893fb5.png)
maka akan menjadi seperti ini

* 4. Install Pytorch

buka cmd lalu ketik `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117`
tunggu sampai selesai, tanda jika sudah selesai muncul baris terbawah seperti berikut


![image](https://user-images.githubusercontent.com/101288815/206203996-4e423939-4af6-48af-9dcb-4e5be2774905.png)

* 5. Install Requirement

install requirement yang dibutuhkan dengan cara 
    * buka lokasi folder yang diunzip
      ![image](https://user-images.githubusercontent.com/101288815/206204638-617d62d4-ce69-4f47-aa87-ed64119e6423.png)
  
  tekan sebelah huruf a maka akan terlihat lokasi penyimpanan
  
  ![image](https://user-images.githubusercontent.com/101288815/206204895-2414cff8-3273-4b6b-b0bf-9ad4b5658ca5.png)
  
  * buka cmd 
  
    ![image](https://user-images.githubusercontent.com/101288815/206205351-2825c48d-77a0-48ad-95a8-e78158762148.png)
    
    lalu pindahkan `C:\Users\ASUS>` ke lokasi folder yolov5
    dengan cara menekan cd [folder] 
    contohnya berikut
    ![image](https://user-images.githubusercontent.com/101288815/206205807-d22bd0b5-4706-4645-ad18-05087a2e7923.png)
    
    lalu ketik `pip install -r requirements.txt` dan tunggu hingga selesai
    lalu ketik lagi `pip install opencv-python --upgrade`

* 6. Menjalankan program

lalu pindahkan `C:\Users\ASUS>` ke lokasi folder sebelum yolov5

![image](https://user-images.githubusercontent.com/101288815/206206388-06466ef9-0d2f-43d8-862d-25754d48d049.png)

lalu ketik `python kamera.py`

lalu akan muncul pop up kamera seperti berikut 

![image](https://user-images.githubusercontent.com/101288815/206206991-3c4ded94-6b2c-4686-8c04-84ed7a348251.png)

lalu tekan huruf **Q** pada keyboard untuk mengcapture gambar dan memulai deteksi, akan muncul seperti ini

![image](https://user-images.githubusercontent.com/101288815/206207236-30e587c3-00d5-4d80-803f-1ef31fe12ab1.png)

titik merah menandakan titik bola 

jika ingin mengulang ketik `python kamera.py` lagi pada cmd

![image](https://user-images.githubusercontent.com/101288815/206207584-f7f05d5e-7d88-4e93-8d1c-23d65c40d67c.png)

### TERIMA KASIH
code by Antonio Taifan Montana

