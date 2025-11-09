# Kelas karyawan
class DataKaryawan:
    def __init__(self):
        # Konsep enkapsulasi, method hanya dapat di akses internal
        self._data_karyawan = [
            {"id": 1, "nama": "Andi Pratama", "jabatan": "Manager", "alamat": "Jl. Merpati No. 12, Jakarta",
                "email": "andi.pratama@staphsec.com", "no_hp": "0812-3456-7890", "gambar": "https://randomuser.me/api/portraits/men/1.jpg"},
            {"id": 2, "nama": "Budi Santoso", "jabatan": "Supervisor", "alamat": "Jl. Anggrek No. 8, Bandung",
                "email": "budi.santoso@staphsec.com", "no_hp": "0813-2233-4455", "gambar": "https://randomuser.me/api/portraits/men/2.jpg"},
            {"id": 3, "nama": "Citra Lestari", "jabatan": "Staff HRD", "alamat": "Jl. Melati No. 45, Surabaya",
                "email": "citra.lestari@staphsec.com", "no_hp": "0821-5544-6677", "gambar": "https://randomuser.me/api/portraits/women/3.jpg"},
            {"id": 4, "nama": "Dewi Anggraini", "jabatan": "Staff Keuangan", "alamat": "Jl. Dahlia No. 10, Yogyakarta",
                "email": "dewi.anggraini@staphsec.com", "no_hp": "0812-9988-7766", "gambar": "https://randomuser.me/api/portraits/women/4.jpg"},
            {"id": 5, "nama": "Eko Nugroho", "jabatan": "Staff IT", "alamat": "Jl. Kenanga No. 5, Semarang",
                "email": "eko.nugroho@staphsec.com", "no_hp": "0851-3322-1100", "gambar": "https://randomuser.me/api/portraits/men/5.jpg"},
            {"id": 6, "nama": "Farah Nabila", "jabatan": "Marketing", "alamat": "Jl. Mawar No. 7, Medan",
                "email": "farah.nabila@staphsec.com", "no_hp": "0822-4444-5555", "gambar": "https://randomuser.me/api/portraits/women/6.jpg"},
            {"id": 7, "nama": "Galih Saputra", "jabatan": "Sales", "alamat": "Jl. Flamboyan No. 3, Malang",
                "email": "galih.saputra@staphsec.com", "no_hp": "0838-1234-9876", "gambar": "https://randomuser.me/api/portraits/men/7.jpg"},
            {"id": 8, "nama": "Hana Wulandari", "jabatan": "Admin", "alamat": "Jl. Cempaka No. 9, Bekasi",
                "email": "hana.wulandari@staphsec.com", "no_hp": "0819-5555-2222", "gambar": "https://randomuser.me/api/portraits/women/8.jpg"},
            {"id": 9, "nama": "Irfan Maulana", "jabatan": "Teknisi", "alamat": "Jl. Kamboja No. 2, Depok",
                "email": "irfan.maulana@staphsec.com", "no_hp": "0813-6000-8899", "gambar": "https://randomuser.me/api/portraits/men/9.jpg"},
            {"id": 10, "nama": "Joko Setiawan", "jabatan": "Driver", "alamat": "Jl. Teratai No. 20, Tangerang",
                "email": "joko.setiawan@staphsec.com", "no_hp": "0823-1111-9999", "gambar": "https://randomuser.me/api/portraits/men/10.jpg"},
            {"id": 11, "nama": "Kiki Ramadhani", "jabatan": "Customer Service", "alamat": "Jl. Pandan No. 6, Jakarta",
                "email": "kiki.ramadhani@staphsec.com", "no_hp": "0812-4455-6677", "gambar": "https://randomuser.me/api/portraits/women/11.jpg"},
            {"id": 12, "nama": "Lutfi Hidayat", "jabatan": "Analis Data", "alamat": "Jl. Melur No. 15, Bandung",
                "email": "lutfi.hidayat@staphsec.com", "no_hp": "0821-1122-3344", "gambar": "https://randomuser.me/api/portraits/men/12.jpg"},
            {"id": 13, "nama": "Maya Sari", "jabatan": "Desainer Grafis", "alamat": "Jl. Cendana No. 4, Surabaya",
                "email": "maya.sari@staphsec.com", "no_hp": "0831-7777-8888", "gambar": "https://randomuser.me/api/portraits/women/13.jpg"},
            {"id": 14, "nama": "Niko Ardian", "jabatan": "Web Developer", "alamat": "Jl. Jati No. 9, Semarang",
                "email": "niko.ardian@staphsec.com", "no_hp": "0852-1234-5678", "gambar": "https://randomuser.me/api/portraits/men/14.jpg"},
            {"id": 15, "nama": "Olivia Putri", "jabatan": "Sekretaris", "alamat": "Jl. Mahoni No. 17, Medan",
                "email": "olivia.putri@staphsec.com", "no_hp": "0819-8765-4321", "gambar": "https://randomuser.me/api/portraits/women/15.jpg"},
            {"id": 16, "nama": "Pandu Wicaksono", "jabatan": "Staff Gudang", "alamat": "Jl. Pinus No. 8, Yogyakarta",
                "email": "pandu.wicaksono@staphsec.com", "no_hp": "0812-9999-0000", "gambar": "https://randomuser.me/api/portraits/men/16.jpg"},
            {"id": 17, "nama": "Qory Amanda", "jabatan": "Finance Supervisor", "alamat": "Jl. Sakura No. 13, Jakarta",
                "email": "qory.amanda@staphsec.com", "no_hp": "0853-1111-2222", "gambar": "https://randomuser.me/api/portraits/women/17.jpg"},
            {"id": 18, "nama": "Rizky Fahreza", "jabatan": "Software Engineer", "alamat": "Jl. Cemara No. 19, Bandung",
                "email": "rizky.fahreza@staphsec.com", "no_hp": "0822-3333-4444", "gambar": "https://randomuser.me/api/portraits/men/18.jpg"},
            {"id": 19, "nama": "Sinta Marlina", "jabatan": "Quality Assurance", "alamat": "Jl. Kenari No. 11, Surabaya",
                "email": "sinta.marlina@staphsec.com", "no_hp": "0812-5678-9999", "gambar": "https://randomuser.me/api/portraits/women/19.jpg"},
            {"id": 20, "nama": "Teguh Prakoso", "jabatan": "Project Manager", "alamat": "Jl. Angsana No. 2, Depok",
                "email": "teguh.prakoso@staphsec.com", "no_hp": "0813-9090-1010", "gambar": "https://randomuser.me/api/portraits/men/20.jpg"},
            {"id": 21, "nama": "Utami Rahma", "jabatan": "Staff Legal", "alamat": "Jl. Nangka No. 18, Tangerang",
                "email": "utami.rahma@staphsec.com", "no_hp": "0819-3030-4040", "gambar": "https://randomuser.me/api/portraits/women/21.jpg"},
            {"id": 22, "nama": "Vino Saputra", "jabatan": "Network Engineer", "alamat": "Jl. Wijaya Kusuma No. 16, Bekasi",
                "email": "vino.saputra@staphsec.com", "no_hp": "0851-5050-6060", "gambar": "https://randomuser.me/api/portraits/men/22.jpg"},
            {"id": 23, "nama": "Wulan Ayu", "jabatan": "HR Manager", "alamat": "Jl. Anggrek No. 22, Jakarta",
                "email": "wulan.ayu@staphsec.com", "no_hp": "0812-8080-9090", "gambar": "https://randomuser.me/api/portraits/women/23.jpg"},
            {"id": 24, "nama": "Yoga Pradana", "jabatan": "Data Scientist", "alamat": "Jl. Melati No. 7, Bandung",
                "email": "yoga.pradana@staphsec.com", "no_hp": "0813-7070-8080", "gambar": "https://randomuser.me/api/portraits/men/24.jpg"},
            {"id": 25, "nama": "Zahra Nuraini", "jabatan": "Content Writer", "alamat": "Jl. Cempaka No. 14, Yogyakarta",
                "email": "zahra.nuraini@staphsec.com", "no_hp": "0812-6060-7070", "gambar": "https://randomuser.me/api/portraits/women/25.jpg"}
        ]

        self._next_id = 26

    # Konsep enkapsulasi, method hanya dapat di akses internal
    def _get_new_id(self):
        id_baru = self._next_id
        self._next_id += 1
        return id_baru

    # Method/fungsi untuk mengambil semua data karyawan, jika method tidak dimasukkan parameter id yang sama dengan None (nilai default) maka akan mengembalikan semua data karyawan, tapi jika memasukkan parameter id tertentu maka hanya akan mengembalikan data pada id tersebut
    def get(self, id=None):
        if id is None:
            # Kembalikan semua data karyawan
            return self._data_karyawan
        else:
            # Kembalikan data karyawan dengan id itu sendiri
            for item in self._data_karyawan:
                if item['id'] == id:
                    return item
            return None

    # Method/fungsi untuk menambahkan dan mengupdate/mengubah data karyawan, yang menerima 2 parameter yaitu data dan id. Id di set default sebagai None, sehingga ketika id sama dengan None maka fungsi ini hanya akan menambahkan data baru, tetapi ketika id diberikan dengan nilai tertentu maka fungsi ini akan mengupdate/mengubah data pada id tersebut.
    def set_data(self, data, id=None):
        if id is None:
            data['id'] = self._get_new_id()
            self._data_karyawan.append(data)
            return True
        else:
            for i, item in enumerate(self._data_karyawan):
                if item['id'] == id:
                    self._data_karyawan[i].update(data)
                    self._data_karyawan[i]['id'] = id
                    return True
            return False

    def delete_data(self, data, id=None):
        for i, item in enumerate(self._data_karyawan):
            if item['id'] == id:
                self._data_karyawan.pop(i)
                break

    # Method/fungsi untuk implementasi fitur pencarian
    def search(self, query):
        search = query.lower().strip()

        results = []

        for item in self.get():
            nama = search in item['nama'].lower()
            jabatan = search in item['jabatan'].lower()

            if nama or jabatan:
                results.append(item)

        return results

class Users:
    def __init__(self):
        self._users = [
        ]
        
        self._id = 1

    def _get_id(self):
        id_baru = self._id
        self._id += 1
        return id_baru

    def get_user(self):
        return self._users

    def add_user(self, data):
        data['id'] = self._get_id()
        self._users.append(data)
        return True
