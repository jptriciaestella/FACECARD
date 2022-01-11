**Perkembangan Prototype:**

1. **Prototype Figma**

Kami menyediakan prototype program berupa UI Design dalam website Figma yang dapat diakses dalam link ini:

[https://www.figma.com/proto/jcb0Va0Ef6gTKnrDrZJKfX/FACE-CARD?node-id=1%3A9&amp;scaling=contain&amp;page-id=0%3A1&amp;starting-point-node-id=1%3A9](https://www.figma.com/proto/jcb0Va0Ef6gTKnrDrZJKfX/FACE-CARD?node-id=1%3A9&amp;scaling=contain&amp;page-id=0%3A1&amp;starting-point-node-id=1%3A9)

Prototype Figma dibuat untuk mempermudah pembuatan program, dan membuat user atau pengguna awam mengerti _flow_ aplikasi dari FACECARD, yaitu: login, menambahkan siswa, menambahkan kelas, menambahkan siswa ke dalam kelas yang dipilih, menambahkan sesi baru di kelas yang dipilih, memilih sesi yang sudah ditambahkan untuk melihat absensi yang sudah selesai atau memulai scanning untuk absensi siswa.

1. **Hal-hal yang perlu disiapkan untuk mengakses program prototype**

Ada beberapa hal yang harus disiapkan terlebih dahulu untuk menjalankan program FACECARD yang sudah tim kami buat. Berikut merupakan langkah-langkah dan program apa saja yang harus dipasang dalam perangkat komputer, yang kami sarankan menggunakan OS Windows 10 dan memori yang cukup untuk menjalankan program secara maksimal. Kami sarankan untuk menggunakan perangkat dengan memori minimal 4 GB dengan ruang penyimpanan minimal 12 GB untuk menginstall semua perangkat dari awal. User juga akan membutuhkan perangkat webcam untuk melakukan absensi menggunakan face recognition yang sudah kami buat.

  1. **Python**

Python adalah bahasa pemrograman yang digunakan untuk membuat prototype kami. Oleh karena itu, untuk mengcompile prototype yang sudah kami buat maka user harus menginstall python terlebih dahulu, dengan minimal versi 3.9.6. Perlu diperhatikan bahwa versi ini tidak dapat digunakan di perangkat dengan Windows 7 kebawah.

Pertama, download installer python di link berikut:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

![](RackMultipart20220111-4-1am1yaf_html_a186cba58ca830ab.png)

Klik tombol &quot;Download Python 3.x.x&quot; untuk mengunduh versi terbaru dari python. Jika anda hanya ingin menginstall python sesuai dengan versi yang kami gunakan, maka dapat diunduh di link berikut:
[https://www.python.org/downloads/release/python-396/](https://www.python.org/downloads/release/python-396/)

![](RackMultipart20220111-4-1am1yaf_html_62cd87feb213f105.png)

Scroll kebagian files dan download sesuai dengan device anda (Windows Installer 32/64 bit).

Jalankan executable yang sudah didownload untuk memulai instalasi python.

![](RackMultipart20220111-4-1am1yaf_html_ec079a4466c751dc.png)

Pilih opsi &quot;Install Now&quot;, dan jangan lupa untuk mencentang &quot;Add Python 3.x to PATH&quot;. Instalasi akan dimulai dan akan diberi notifikasi instalasi berhasil ketika python sudah terpasang di perangkat anda.

![](RackMultipart20220111-4-1am1yaf_html_43ada0d810cc98c5.png)

Jangan lupa untuk mengecek kembali PATH anda, yaitu dengan mengakses &quot;Edit the system environment variables&quot; pada windows anda.

![](RackMultipart20220111-4-1am1yaf_html_70a64e2252214955.png)

Tekan tombol &quot;environment variables&quot;

![](RackMultipart20220111-4-1am1yaf_html_2fe27378bbdfd843.png)

Pilih Path pada System Variables

![](RackMultipart20220111-4-1am1yaf_html_5afc0bb0c197e213.png)

![](RackMultipart20220111-4-1am1yaf_html_aa3ba4c432d35a15.png)

Pastikan Python versi anda sudah ada di dalam PATH, jika belum, klik tombol &quot;New&quot; dan arahkan ke folder dimana Python anda di-install (folder Scripts). Untuk mengecek versi python yang anda miliki di perangkat anda, jalankan perintah **python –version** di command prompt anda.

![](RackMultipart20220111-4-1am1yaf_html_18e3ce4e2e8ebaa1.png)

  1. **PIP for Python**

PIP merupakan tools terbaik untuk menginstall packages dalam python. Untuk menggunakannya, user haru mendownload pip terlebih dahulu di link berikut:
[https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)

Anda dapat mengklik kanan website tersebut, dan tekan tombol &quot;Save as..&quot; untuk mendownload file get-pip.py. Setelah itu, buka command prompt atau windows PowerShell di direktori di mana get-pip.py diunduh. Lalu, jalankan command berikut:

python get-pip.py

![](RackMultipart20220111-4-1am1yaf_html_535d4f5786df1ae.png)

Instalasi PIP akan dimulai. Setelah mendapatkan line yang mengatakan instalasi sukses dan sudah selesai, anda dapat menjalankan command pip -V untuk mengecek versi PIP anda.

![](RackMultipart20220111-4-1am1yaf_html_53b1f4032ace75bc.png)

Jika terminal anda menampilkan versi PIP seperti gambar diatas, maka PIP sudah dapat digunakan.

  1. **Cmake**

Karena program kami menggunakan dlib yang dikembangkan melalui bahasa C, maka Cmake dibutuhkan untuk menjalankan dlib tersebut. Download cmake di link berikut:
[https://cmake.org/download/](https://cmake.org/download/)

![](RackMultipart20220111-4-1am1yaf_html_238ed55789447bcb.png)

Pilih windows installer sesuai dengan perangkat anda. File yang akan terunduh akan berbentuk .msi, run program tersebut dan ikuti langkah-langkahnya. Jangan lupa untuk mencentang &quot;Add CMake to the system PATH for all users&quot;.

![](RackMultipart20220111-4-1am1yaf_html_1abdf79d23cb50bf.png)

Setelah itu, kita perlu memeriksa atau menambahkan PATH cmake kedalam perangkat kita, di menu environment variables. Kali ini, kita mengubah PATH dalam user variable.

![](RackMultipart20220111-4-1am1yaf_html_96d833eac5b21ed7.png)

Pastikan CMake sudah terdapat dalam PATH, seperti pada gambar berikut:

![](RackMultipart20220111-4-1am1yaf_html_321ad884950c29c.png)

Jika belum, anda dapat menekan tombol &quot;New&quot; dan arahkan ke folder bin dimana CMake anda install.

  1. **Visual Studio**

Karena dlib menggunakan bahasa C, selain harus mengunduh Cmake, kita juga harus menginstall compiler berupa Visual Studio yang dapat diunduh di link berikut:
[https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Ikuti langkah-langkah yang diberikan Visual Studio untuk menginstall Build Tools Visual Studio. Jangan lupa untuk menginstall package untuk C dan C++, yaitu Packages CMake tools for Windows.

![](RackMultipart20220111-4-1am1yaf_html_9f93fab56ea641eb.png)

C++ CMake tools for Windows tidak boleh dilewatkan disini. Setelah instalasi selesai, anda dapat memeriksanya kembali di Modify \&gt; Individual Components \&gt; Compilers, build tools, and runtimes \&gt; C++ CMake tools for Windows.

![](RackMultipart20220111-4-1am1yaf_html_fb30d6256bbd2da8.png)

![](RackMultipart20220111-4-1am1yaf_html_554db11102097644.png)

Klik tombol install jika belum didapati C++ CMake tools for Windows.

  1. **Download source code FACECARD**

Source code untuk menjalankan program ini dapat diakses dari link berikut:

[https://github.com/jptriciaestella/FACECARD.git](https://github.com/jptriciaestella/FACECARD.git)

![](RackMultipart20220111-4-1am1yaf_html_91c46fee64485eff.png)

Untuk mendownload code dalam github, maka anda dapat menekan tombol code hijau dan pilih opsi &quot;Download ZIP&quot;. Pilih direktori yang anda inginkan untuk menyimpan program ini.

Ketika FACECARD-main.zip sudah terdownload, maka anda dapat extract file tersebut agar bisa mengakses folder dan file yang dibutuhkan dalam program FACECARD kami.

  1. **Install requirements.txt**

Untuk menjalankan program, kita harus menginstall beberapa library lain di dalam python yang sudah kami tuliskan dalam requirements.txt. Library tambahan yang akan digunakan antara lain tkcalendar untuk membuat calendar, cmake yang sudah di_download_ sebelumnya, dlib dan opencv sebagai deep learning, face-recognition untuk algoritma face recognition yang digunakan, dan library lainnya untuk membuat UI sesuai dengan prototype yang digambarkan.

Oleh karena itu, user dapat membuka command prompt ataupun windows PowerShell di direktori face\_card anda. Hal ini dapat dilakukan dengan perintah **cd \&lt;alamat face\_card\&gt;** ataupun menekan tombol shift+klik kanan di direktori face card.

![](RackMultipart20220111-4-1am1yaf_html_201398362a56fbbe.png)

dan jalankan perintah berikut:
**pip install -r requirements.txt**

![](RackMultipart20220111-4-1am1yaf_html_ca2fe30bf00ed618.png)

Tunggu sampai semua library dan packages terinstall dengan benar, pastikan komputer anda terhubung dengan koneksi internet yang baik.

1. **Program Prototype**

Untuk menjalankan program, jalankan powershell di direktori facecard, dan jalankan perintah berikut:

**cd ui**

**python main.py**

![](RackMultipart20220111-4-1am1yaf_html_c95d5e0a6122a176.png)

Jika semua instalasi sudah dilakukan dengan benar, maka akan muncul pop-up window aplikasi FACECARD yang siap digunakan.

![](RackMultipart20220111-4-1am1yaf_html_ffd4473052c133bc.png)

Note: Prototype ini belum mengaplikasikan design yang responsif, sehingga window belum bisa di-_resize_ ataupun memasuki mode _full-screen_.

**Langkah penggunaan program ini adalah sebagai berikut:**

  1. **Login**

User perlu memasukkan username dan password dari admin yang mengatur absensi mahasiswa. Kami menyediakan beberapa kombinasi username dengan password sebagai berikut:

| Username | Password |
| --- | --- |
| Admin | Admin |
| teacher | Password |
| a | a |

Jika user tidak mengisi form atau memasukan kombinasi yang salah, maka program akan mengeluarkan pesan error dan mengulangi permintaannya lagi.

![](RackMultipart20220111-4-1am1yaf_html_26dfca4371f974a7.png)

Jika kombinasi benar, maka user akan diarahkan ke laman utama aplikasi, berjudul MANAGE DATA dengan tampilan sebagai berikut:

![](RackMultipart20220111-4-1am1yaf_html_422a3d2cce139f72.png)

User dapat menekan tombol logout untuk keluar dari akun dan menutup halaman ini.

  1. **Add Student**

Data siswa adalah data pertama yang perlu ditambahkan ke dalam database program ini. Dengan menekan tombol &quot;Add Student Data&quot; di halaman utama, maka user akan ditampilkan halaman untuk mengisi data siswa sebagai berikut:

![](RackMultipart20220111-4-1am1yaf_html_e121a0aaab94aa0b.png)

Halaman ini diisi dengan foto siswa, nama, nomor mahasiswa, tanggal lahir, dan nomor telepon. Halaman ini dapat disesuaikan dengan kebutuhan data lainnya yang dibutuhkan oleh lembaga administrasi universitas yang berlangganan. Pastikan foto yang diunggah jelas wajahnya, tidak tertutup atribut apapun dan menghadap ke kamera.

![](RackMultipart20220111-4-1am1yaf_html_2c575eba6f337aec.png)

Setelah mengisi data dengan benar, tekan tombol &quot;Save Data&quot; untuk menyimpan data tersebut. Aplikasi akan menampilkan pemberitahuan &quot;Student Added!&quot; jika berhasil menambahkan data dengan benar.

Ulangi langkah ini untuk setiap siswa yang akan terlibat di perkuliahan.

  1. **Class Schedule**

Setiap menambahkan siswa, program akan mengembalikan user ke halaman utama. Untuk melihat setiap kelas yang ada, user dapat memilih tombol kedua yaitu &quot;Class Schedule&quot;. Tampilan pertama halaman ini adalah sebagai berikut:

![](RackMultipart20220111-4-1am1yaf_html_16b41468fd318955.png)

Tabel class yang ada akan kosong karena secara default database perkuliahan kosong. Oleh karena itu, user dapat menambahkan kelas-kelas yang dibutuhkan dalam perkuliahan dengan menekan tombol &quot;Add New&quot;. Program akan menampilkan form pengisian kelas baru seperti gambar berikut:

![](RackMultipart20220111-4-1am1yaf_html_ea5935252d7d81fe.png)

Setelah mengisi form dengan benar, maka program akan memunculkan pemberitahuan &quot;Class Added!&quot; yang menandakan kelas berhasil ditambahkan. Program akan kembali ke halaman sebelumnya, dan menampilkan kelas yang baru ditambahkan. Ulangi proses ini untuk setiap kelas yang dibutuhkan.

![](RackMultipart20220111-4-1am1yaf_html_7afdbd980ee1691c.png)

![](RackMultipart20220111-4-1am1yaf_html_e9e4615835987701.png)

Perlu diingat bahwa kode kelas merupakan _key_ yang akan digunakan oleh program, dan tidak dapat menambahkan kelas baru dengan kode yang sama. Jika dilakukan, akan muncul pemberitahuan seperti ini:

![](RackMultipart20220111-4-1am1yaf_html_a3038e60ad779c25.png)

  1. **Add Student to the Selected Class**

Ketika user telah menambahkan kelas-kelas yang dibutuhkan, saatnya mendaftarkan atau meng-_enroll_ siswa yang sudah ada ke dalam kelas tersebut. Caranya, di halaman manage class schedule, user dapat memilih kelas yang diinginkan dan lakukan double klik untuk masuk ke detail kelas tersebut.

![](RackMultipart20220111-4-1am1yaf_html_88e4dbb8fb57a231.png)

Halaman detail class adalah sebagai berikut:

![](RackMultipart20220111-4-1am1yaf_html_95c61d3b4ad54760.png)

Kelas yang baru dibuat tidak akan memiliki siswa yang terdaftar di dalamnya. Oleh karena itu, user dapat menekan tombol &quot;Add Student&quot;.

![](RackMultipart20220111-4-1am1yaf_html_1421538e5331ce02.png)

Program akan menampilkan seluruh siswa yang ada di database, yang belum terdaftar di kelas terpilih. Untuk menambahkannya, cukup pilih siswa yang diinginkan dan tekan tombol &quot;Add&quot;. Sama seperti menu lainnya, bar &quot;Search…&quot; dapat memudahkan user dalam mencari data yang diinginkan.

![](RackMultipart20220111-4-1am1yaf_html_528ea9718be42e3a.png)

Siswa yang dipilih akan masuk ke database kelas tersebut, dan program akan me-_refresh_ halaman ini, dan menampilkan seluruh siswa yang ada dikurangi dengan siswa yang sudah ada di kelas. Tambahkan sampai jumlah siswa di kelas tersebut sesuai.

![](RackMultipart20220111-4-1am1yaf_html_f9e1c173a0d9b5d4.png)

Jika user menekan tombol back, maka halaman detail kelas yang dipilih akan terupdate nama siswanya. Dalam contoh diatas, kelas LA01 hanya memiliki murid sejumlah 2 orang. User dapat kembali menambahkan siswa pada kelas ini jika diperlukan.

  1. **Add Session to the Selected Class**

Untuk melihat semua sesi yang ada di sebuah kelas, user harus terlebih dulu masuk ke halaman detail kelas tersebut. Selanjutnya, user dapat menekan tombol &quot;View Sessions&quot; untuk melihat sesi yang ada.

![](RackMultipart20220111-4-1am1yaf_html_3cc36af9467656fc.png)

Pada awal kelas ditambahkan maka kelas tersebut tidak akan memiliki sesi. Oleh karena itu, user dapat menambahkan sesi-sesi terlebih dahulu sesuai dengan jadwal yang ada dengan menekan tombol &quot;Add Session&quot;. Berikut tampilah halaman setelah menekan tombol tersebut:

![](RackMultipart20220111-4-1am1yaf_html_4873bb3e38f74401.png)

Aplikasi akan menampilkan kalender, dan user akan memilih tanggal yang sesuai dengan jadwal kelas tersebut. Setelah itu, tekan tombol &quot;Confirm&quot; untuk mengkonfirmasi, dan akan keluar pop up dan notifikasi sukses menambahkan jadwal. Perlu dicatat bahwa kita tidak dapat menambahkan sesi dengan tanggal yang sudah terlewat dari tanggal kapan aplikasi ini dijalankan.

![](RackMultipart20220111-4-1am1yaf_html_4003cc143f82a37c.png)

Program akan kembali ke halaman sebelumnya, dan menampilkan sesi sesuai dengan apa yang sudah ditambahkan. Jika hari itu sama dengan tanggal sesi yang akan berjalan, maka statusnya akan berubah menjadi ONGOING. Jika tidak, maka statusnya akan menjadi UPCOMING.

  1. **Melakukan Absensi**

Absensi hanya dapat dilakukan di sesi yang sedang &quot;ONGOING&quot;. Kunjungi halaman sesi kelas yang dituju, lalu pilih sesi yang sedang berlangsung, dengan menggunakan _double-click._ Jumlah siswa yang hadir otomatis berada di angka 0 sebelum melakukan absensi, dan akan ter-_update_ setelah melakukan absensi.

![](RackMultipart20220111-4-1am1yaf_html_dae26c7cb445ddb1.png)

Untuk membuka kamera dan memulai absensi, maka user dapat menekan tombol &quot;Start Scanning&quot; di halaman sesi yang terpilih.

![](RackMultipart20220111-4-1am1yaf_html_cf84dd8c65b16084.png)

Aplikasi akan langsung memunculkan pop-up window yang menampilkan webcam anda, dan langsung mendeteksi wajah yang ada di dalam kamera tersebut.

![](RackMultipart20220111-4-1am1yaf_html_367b5bd9475075e.png)

Untuk menutup halaman ini, user dapat menekan tombol &#39;X&#39; pada keyboard, dan aplikasi akan memunculkan konfirmasi untuk menutup halaman absensi dan memberhentikan proses absensi. Dalam arti lain, sesi sudah berakhir.

![](RackMultipart20220111-4-1am1yaf_html_a99830d166e3806f.png)

Halaman absensi siswa sudah terupdate sesuai dengan siapa saja yang sudah melakukan absensi menggunakan face recognition ini, dengan status &quot;PRESENT&quot; untuk siswa yang hadir, dan &quot;ABSENT&quot; untuk siswa yang tidak hadir.

![](RackMultipart20220111-4-1am1yaf_html_370f617881dfa31b.png)

Sesi yang sudah selesai pada halaman &quot;VIEW SESSIONS&quot; juga akan terupdate menjadi &quot;COMPLETED&quot; ketika halaman absensi dimatikan.

![](RackMultipart20220111-4-1am1yaf_html_cd40ab5348008be4.png)

  1. **Melihat Absensi**

User hanya dapat melihat list absensi siswa yang hadir (PRESENT) atau tidak hadir (ABSENT) ketika sesi tersebut sudah selesai. Jadi, user harus membuat sesi dan melakukan absensi menggunakan face recognition terlebih dahulu. Program akan otomatis mengupdate status sesi menjadi COMPLETED beserta absensi siswa didalamnya, dengan memilih sesi yang sudah ada dengan double-click, dan program akan menampilkan seluruh datanya.

![](RackMultipart20220111-4-1am1yaf_html_a2fb1237fffb5203.png)

![](RackMultipart20220111-4-1am1yaf_html_370f617881dfa31b.png)

1. **Video praktik penggunaan program**

Untuk praktik penggunaan program secara _step-by-step,_ maka anda dapat mengakses video penggunaan prototype FACECARD dengan link sebagai berikut:

Kendala yang didapatkan dari prototype ini adalah kurangnya data facial yang digunakan mesin untuk dipelajari. Karena dalam penggunaan aplikasi ini user hanya mengupload satu foto untuk setiap murid dari sisi depan saja, maka aplikasi akan kurang maksimal dalam _tracking_ setiap sisi siswa ketika sedang diabsen. Jika siswa yang sedang melakukan absen tidak menatap langsung kamera, yang tidak sesuai dengan _training image_ yang ada, maka program akan kesulitan dalam mendeteksi wajahnya. Selain itu, algoritma yang kami gunakan untuk face recognition ini belum dilatih untuk membedakan wajah asli dengan gambar, sehingga ketika kamera dihadapkan dengan gambar seorang siswa, maka siswa itu akan terdeteksi hadir di database.

Prototype ini belum dirancang untuk diaplikasikan ke setiap kelas yang ada di institusi pembelajaran. Kami belum membuat sistem dimana setiap kelas akan terintegrasi oleh mesin dengan kamera dan database langsung terupdate sesuai dengan letak kelas dan jadwalnya ketika ada siswa yang melakukan absensi. Prototype ini baru merupakan gambaran aplikasi yang digunakan dan admin/pengajar harus memilih kelas dan memulai sesinya secara manual di setiap pertemuan.

Selain itu, prototype ini baru dibuat untuk menu class schedule saja, yaitu kelas pelajaran biasa. Kami belum membuat laman student activity, yang bisa mencakup aktivitas siswa yang lain, seperti seminar, ekstrakulikuler, organisasi, dan sebagainya. Selanjutnya, kami akan melengkapi hal ini juga mengintegrasikan aplikasi ini dengan aplikasi ketiga seperti aplikasi video conference yang ada. Integrasi tersebut akan memudahkan pengembangan fitur kami yang lain yaitu absensi dengan face recognition melalui meeting untuk mewujudkan _combined learning_ yang akan marak di masa mendatang.
