# Auto Commit & Push ke GitHub

Project otomatisasi commit dan push ke GitHub (3 - 10 commit per hari).

Terdapat 2 metode yang bisa kamu gunakan:
1. **GitHub Actions (Cloud / Otomatis 24 Jam)**: Berjalan di server GitHub secara gratis tanpa perlu menyalakan PC/laptop kamu.
2. **Local Python (PC Sendiri)**: Berjalan di komputer lokal menggunakan Python.

---

## 🚀 Langkah 1: Push Project ini ke Repository GitHub Kamu

1. Buat repository baru di GitHub (misalnya bernama `pushcommit`).
2. Buka terminal di folder ini (`D:\python\pushcommit`) lalu jalankan:

```bash
git init
git add .
git commit -m "feat: initial commit auto push setup"
git branch -M main
git remote add origin https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git
git push -u origin main
```
*(Ganti `USERNAME_KAMU` dan `NAMA_REPO_KAMU` sesuai dengan akun GitHub kamu)*

---

## ⚙️ Langkah 2: Aktifkan Izin GitHub Actions (PENTING untuk Metode Cloud)

Agar GitHub Actions memiliki izin untuk melakukan push otomatis ke repositori kamu:
1. Buka repositori kamu di GitHub di browser.
2. Klik tab **Settings** -> pilih **Actions** -> pilih **General**.
3. Scroll ke bawah sampai bagian **Workflow permissions**.
4. Pilih **Read and write permissions**.
5. Centang **Allow GitHub Actions to create and approve pull requests**.
6. Klik **Save**.

Sekarang, GitHub Actions akan otomatis berjalan setiap beberapa jam (6-8 kali sehari) dan meng-update `activity.txt` serta mem-push commit secara otomatis!

Kamu juga bisa memicu jalannya workflow kapan saja secara manual melalui tab **Actions** -> **Automated Daily Commit & Push** -> **Run workflow**.

---

## 💻 Alternatif: Menjalankan Secara Lokal di Komputer

Jika kamu ingin menjalankannya di laptop/PC kamu sendiri:

### 1. Mode Batch (Langsung membuat 3 - 10 commit sekaligus):
```bash
python auto_commit.py --mode batch --min 3 --max 10
```

### 2. Mode Single (1 kali commit & push):
```bash
python auto_commit.py --mode single
```

### 3. Mode Daemon (Berjalan terus di background sepanjang hari):
```bash
python auto_commit.py --mode daemon --min 3 --max 10
```

---

## 📁 Struktur File
- [auto_commit.py](file:///D:/python/pushcommit/auto_commit.py): Skrip Python untuk menambahkan log dan mengeksekusi git commit & push.
- [.github/workflows/auto-commit.yml](file:///D:/python/pushcommit/.github/workflows/auto-commit.yml): Workflow GitHub Actions cron job.
- [activity.txt](file:///D:/python/pushcommit/activity.txt): File log yang diperbarui pada setiap commit otomatis.
- [.gitignore](file:///D:/python/pushcommit/.gitignore): File git ignore untuk Python.
