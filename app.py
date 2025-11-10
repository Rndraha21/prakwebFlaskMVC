from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
from models import DataKaryawan, Users
import re

# Lebih fleksibel jadi saya define sendiri nama template foldernya dan static foldernya:)
app = Flask(__name__, template_folder="templates",
            static_folder="static", static_url_path="/")

app.secret_key = 'staphsecpembantaihama'

# Variabel untuk menampung kelas karyawan (Kelas Abangkuh🔥)
model = DataKaryawan()
user = Users()


# Route index/halaman pertama
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    elif request.method == "POST":
        data_user = user.get_user()

        username = request.form["username"]
        password = request.form["password"]

        for i, item in enumerate(data_user):
            if item["username"] == username and item["password"] == password:
                session['username'] = item["username"]

                flash("Login berhasil!", "success")
                return redirect(url_for("index"))

        pesan = "Username atau password salah."
        print("Gagal untuk login")
        return render_template('auth/login.html', message=pesan)


@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    data_user = user.get_user()
    msg = []

    if request.method == "GET":
        return render_template("auth/signup.html", methods=["POST", "GET"])

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Validasi username
        if len(username) < 4:
            msg.append("Username terlalu pendek.")

        # Cek username sudah digunakan
        username_exists = any(item["username"] ==
                              username for item in data_user)
        if username_exists:
            msg.append("Username telah digunakan.")

        # Validasi password
        if len(password) < 8:
            msg.append("Password terlalu pendek, minimal 8 karakter.")
        if not re.search(r'\d', password):
            msg.append("Password harus mengandung minimal satu angka.")

        # Jika tidak ada error, buat user baru
        if not msg:
            data_baru = {
                "username": username,
                "password": password
            }
            user.add_user(data_baru)
            return redirect(url_for("login"))

    return render_template("auth/signup.html", msg=msg)


@app.route("/logout")
def logout():
    if "username" not in session:
        return render_template("error.html"), 404

    session.pop("username")
    flash("Anda berhasil logout.", "success")
    return redirect(url_for("index"))


# Route untuk read.html (menampilkan semua data karyawan)
@app.route("/read")
def read():
    if "username" not in session:
        flash("Silahkan login atau sign up terlebih dahulu.", "warning")
        return redirect(url_for('index'))

    query = request.args.get("q")

    if query:
        data = model.search(query)
    else:
        data = model.get()
    return render_template("read.html", data=data, query=query)


# Fungsi untuk menerima post di service section
@app.route("/proses-data", methods=["POST"])
def proses_data():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    new_data = {
        "name": name,
        "email": email,
        "message": message
    }

    print(new_data)

    if name and email:
        msg = f"Halo, {name} terima kasih telah berkunjung ke web kami. Pesan Anda telah kami terima. "
        return jsonify({"msg": msg})

    return jsonify({"error": "Missing Data"})


# Route untuk details.html (untuk menampilkan detail karyawan)
@app.route("/details/<int:id>")
def details(id):
    data = model.get(id=id)

    return render_template("details.html", data=data)


# Route untuk update.html (untuk mengupdate/mengubah data karyawan) dengan 2 method yaitu POST dan GET, get untuk mendapatkan filenya (intinya mah request file update.html ke server mweheheheh😅) kemudian POST untuk mengirimkan data baru ke kelas Karyawan dengan method yang sudah kita bikin tadi yaitu (method set_data), dan disini sedikit detail ux yaitu flash message.
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    data = model.get(id=id)

    if data is None:
        abort(404)

    if request.method == "GET":
        return render_template("update.html", data=data)
    elif request.method == "POST":
        data_update = {
            "nama": request.form["nama"],
            "jabatan": request.form["jabatan"],
            "alamat": request.form["alamat"],
            "email": request.form["email"],
            "no_hp": request.form["no_hp"]
        }

        updated = False
        for key in data_update.keys():
            if str(data.get(key)) != str(data_update.get(key)):
                updated = True
                break

        if updated:
            model.set_data(data_update, id=id)
            flash("Data berhasil diperbarui.", "success")
        else:
            flash("Tidak ada data yang diubah.", "info")
        return redirect(url_for("details", id=id))


# Route untuk create.html (untuk menambahkan data karyawan) yang menerima dua method yaitu POST dan GET, penjelasan POST dan GET bisa dilihat di atas
@app.route("/add_data", methods=["POST", "GET"])
def add_data():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        data_baru = {
            "nama": request.form["nama"],
            "jabatan": request.form["jabatan"],
            "alamat": request.form["alamat"],
            "email": request.form["email"],
            "no_hp": request.form["no_hp"],
            "gambar": request.form["gambar"]
        }

        model.set_data(data_baru)

        flash(
            f"Data karyawan {data_baru["nama"]} berhasil di tambahkan!", "success")
        return redirect(url_for("read"))


@app.route("/delete/<int:id>")
def delete(id):
    data = model.get(id=id)
    if data is None:
        abort(404)

    model.delete_data(data, id=id)
    flash(f"Data {data["nama"]} berhasil di hapus.", "success")
    return redirect(url_for("read"))


# Route untuk orang-orang yang sesat
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
