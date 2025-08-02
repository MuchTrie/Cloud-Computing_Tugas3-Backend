# 🇮🇩 Cloud Computing Tugas 3 - Backend

Simple Flask REST API backend dengan data pengguna Indonesia.

## 🌟 Features

- ✅ **REST API Endpoints** - Get all users, get user by ID, API info
- ✅ **Indonesian User Data** - 8 sample users dengan data lengkap
- ✅ **JSON Data Separation** - Data terpisah dari kode untuk mudah maintenance
- ✅ **CORS Enabled** - Bisa diakses dari frontend di domain berbeda
- ✅ **Error Handling** - Response yang informatif untuk setiap kondisi
- ✅ **Clean Code** - Struktur kode yang rapi dan mudah dipahami

## 📡 API Endpoints

### GET `/`
**API Information**
```json
{
    "message": "🇮🇩 Backend Flask API - Data Pengguna Indonesia",
    "status": "active",
    "data_info": {...},
    "endpoints": {...},
    "usage_examples": {...}
}
```

### GET `/api/users`
**Get All Users**
```json
{
    "status": "success",
    "message": "Data berhasil diambil",
    "data": [...],
    "total": 8,
    "meta": {...}
}
```

### GET `/api/users/<id>`
**Get User by ID (1-8)**
```json
{
    "status": "success",
    "message": "Data {name} berhasil ditemukan",
    "data": {
        "id": 1,
        "name": "Budi Santoso",
        "email": "budi.santoso@email.com",
        "age": 25,
        "city": "Jakarta",
        "pekerjaan": "Software Engineer",
        "hobi": "Bermain musik"
    }
}
```

## 🚀 Quick Start

### Local Development

1. **Clone repository**
   ```bash
   git clone https://github.com/MuchTrie/Cloud-Computing_Tugas3-Backend.git
   cd Cloud-Computing_Tugas3-Backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run application**
   ```bash
   python app.py
   ```

4. **Test API**
   ```bash
   curl http://localhost:5000/
   curl http://localhost:5000/api/users
   curl http://localhost:5000/api/users/1
   ```

Backend akan berjalan di: **http://localhost:5000**

## 📁 File Structure

```
Backend/
├── app.py              # Flask application main file
├── data.json           # Data pengguna Indonesia (8 users)
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore patterns
└── README.md          # Documentation (this file)
```

## 📊 Sample Data

Backend menyediakan data 8 pengguna Indonesia:

- **Budi Santoso** (Jakarta) - Software Engineer
- **Siti Nurhaliza** (Bandung) - Designer Grafis  
- **Ahmad Fauzi** (Surabaya) - Data Analyst
- **Dewi Sartika** (Yogyakarta) - Marketing Manager
- **Rizki Pratama** (Medan) - Frontend Developer
- **Maya Sari** (Makassar) - Product Manager
- **Andi Wijaya** (Semarang) - Backend Developer
- **Rina Mulyani** (Palembang) - HR Manager

Setiap user memiliki: ID, nama, email, umur, kota, pekerjaan, dan hobi.

## 🚀 Deploy to AWS EC2

### Prerequisites
- EC2 instance (Amazon Linux 2 atau Ubuntu)
- Python 3 dan pip
- Security Group dengan port 5000 terbuka

### Steps
1. **Upload files ke server**
   ```bash
   scp -i your-key.pem -r * ec2-user@your-ec2-ip:/home/ec2-user/backend/
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run application**
   ```bash
   python3 app.py
   ```

### Production Setup (Optional)
- Use supervisor untuk auto-restart
- Setup nginx sebagai reverse proxy
- Configure SSL dengan Let's Encrypt

## 🛠️ Technologies Used

- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **JSON** - Data storage format
- **Python 3** - Programming language

## 🔧 Development

### Adding New Users
Edit `data.json` file dan restart server:

```json
{
  "id": 9,
  "name": "Nama Baru",
  "email": "email@example.com",
  "age": 25,
  "city": "Kota",
  "pekerjaan": "Pekerjaan",
  "hobi": "Hobi"
}
```

### Adding New Endpoints
Edit `app.py` dan tambahkan route baru:

```python
@app.route('/api/new-endpoint')
def new_endpoint():
    return jsonify({"message": "New endpoint"})
```

## 📝 API Usage Examples

```bash
# Get API info
curl http://your-server:5000/

# Get all users
curl http://your-server:5000/api/users

# Get specific user
curl http://your-server:5000/api/users/1

# With headers
curl -H "Content-Type: application/json" http://your-server:5000/api/users
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

This project is for educational purposes (Cloud Computing Assignment).

## 👨‍💻 Author

**MuchTrie** - Cloud Computing Student

---

⭐ **Star this repository if you find it helpful!**
