# 🇮🇩 Cloud Computing Tugas 3 - Backend

Simple Flask REST API backend dengan data dummy.


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