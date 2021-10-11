# Welcome to Hacktoberfest 2021
Hacktoberfest adalah acara tahunan yang bertujuan untuk mendorong berkontribusi pada project open source. Acara ini bebas untuk siapa saja, baik untuk pemula hingga professional sekalipun. Target dari acara ini adalah peserta dapat melakukan minimal 4 pull request di antara tanggal 1 hingga 31 oktober 2021.
## Cara berkontribusi
#### 1. Fork
Untuk melakukan fork repository, klik pada pojok kanan atas halaman, tersedia tombol fork disana.
#### 2. Clone
Clone forknya di local computer masing - masing.
```sh
git clone https://github.com/username-github/hacktoberfest-2021.git
```
#### 3. Buat branch
```sh
git checkout -b <branch-name>
```
#### 4. Tambahkan file command
Tambahkan file python pada folder Commands menggunakan username github.
```sh
/Commands/<username-github>.py
```
#### 5. Definisikan file
Definisikan file yang sudah dibuat didalam folder Global.py
```sh
'<nama-file>' : <nama-file>,
```
#### 6. Tambahkan list API dan Free Course
Tambahkan list pesan yang akan di tampilkan bot.
```sh
data = {
  'photo' : '<link-image>',
  'message-1' : 'Hello',
  'message-2' : 'World',
  'message-3' : ':)',
  'course' : 'Free Course = free-course.com',
  'api' : 'Free API = api.com',
}
```
#### 7 Commit dan push
```sh
git add <files-name>
git commit -m <message>
git push origin <branch-name>
```
####  8. Pull request
Buka github, klik tombol compare & pull request, lalu akan diredirect ke halaman open a pull request. Pull request dari head repository branch kelian sendiri ke base repository branch master. 
