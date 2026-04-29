# 🎡 Theme Park Table Booking System

A full-stack web application built with Django that allows guests to book tables at themed restaurants across a theme park. The system intelligently manages table availability, prevents overbooking, and matches parties to the most suitable table sizes.

🌐 **Live Demo:** [https://web-production-89e3.up.railway.app/](https://web-production-89e3.up.railway.app/)

---

## 🌟 Features

- 📋 **Table Booking Form** — guests can book tables by selecting a restaurant, date, time, and party size
- 🔒 **Overbooking Prevention** — system checks real-time availability before confirming any booking
- 🪑 **Smart Table Matching** — assigns the smallest suitable table to avoid wasting large tables on small parties
- ✅ **Form Validation** — validates all inputs including past dates, empty fields, and invalid party sizes
- 💬 **Success & Error Messages** — clear feedback shown after every booking attempt
- 🍽️ **5 Themed Restaurants** — data loaded from CSV covering multiple park zones
- 🗄️ **Database Backed** — all bookings and restaurant data stored persistently

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10, Django 5.2 |
| Database | SQLite |
| Frontend | HTML5, CSS3 (vanilla) |
| Data Loading | Python CSV parser + Django management command |
| Version Control | Git + GitHub |
| Deployment | Railway |

---

## 🗂️ Project Structure

django-table-booking/
├── manage.py
├── restaurants.csv               # Source data for restaurants & tables
├── requirements.txt
├── Procfile                      # Railway deployment config
├── runtime.txt                   # Python version for deployment
├── README.md
├── app/
│   ├── models.py                 # Restaurant, Table, Booking models
│   ├── views.py                  # Booking logic & overbooking prevention
│   ├── urls.py                   # App URL routing
│   ├── admin.py                  # Django admin registration
│   ├── templates/
│   │   └── booking_template.html # Booking form UI
│   └── management/
│       └── commands/
│           └── load_restaurants.py  # CSV data loader
└── main/
├── settings.py               # Django configuration
├── urls.py                   # Project URL routing
└── wsgi.py
---

## 🗄️ Database Design

### Restaurant
| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| name | CharField | Restaurant name |
| location | CharField | Park zone location |

### Table
| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| restaurant | ForeignKey | Links to Restaurant |
| size | IntegerField | Number of seats |
| total_count | IntegerField | How many tables of this size |

### Booking
| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| guest_name | CharField | Guest full name |
| email | EmailField | Guest email |
| visit_date | DateField | Date of visit |
| visit_time | TimeField | Time of visit |
| party_size | IntegerField | Number of guests |
| restaurant | ForeignKey | Links to Restaurant |
| table | ForeignKey | Links to assigned Table |
| created_at | DateTimeField | Booking timestamp |

---

## 🍽️ Restaurants & Zones

| Restaurant | Zone | Table Sizes |
|-----------|------|-------------|
| Pirate's Galley | Adventure Zone | 2, 4, 6 |
| Dino Bites Grill | Jurassic Land | 2, 4, 8 |
| Rocket Diner | Space Port | 2, 4, 6 |
| Jungle Feast | Wild Trails | 2, 4, 6 |
| Kingdom Café | Fantasy Kingdom | 2, 4, 6 |

---

## ⚙️ How the Booking Logic Works

1. Guest fills in the booking form and submits
2. System validates all fields (empty check, past date check, party size check)
3. System finds the selected restaurant in the database
4. System filters tables that can fit the party size, ordered smallest first
5. For each candidate table, system counts existing bookings at that date/time
6. First table with availability is assigned to the booking
7. If no tables are available, an error message is shown
8. If successful, booking is saved and a confirmation message is displayed

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.10+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Arkam11/django-table-booking.git
cd django-table-booking

# Create virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations app
python manage.py migrate

# Load restaurant data from CSV
python manage.py load_restaurants

# Start the development server
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000** 🎉

---

## 🚂 Deployment (Railway)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Sign in with GitHub
4. Click **New Project → Deploy from GitHub repo**
5. Select `django-table-booking`
6. Railway auto-detects Django and deploys!
7. Go to **Settings → Generate Domain** to get your public URL

---

## 🧪 Testing Scenarios

| Scenario | Expected Result |
|----------|----------------|
| Valid booking | ✅ Success message, booking saved |
| Past date | ❌ Error: date cannot be in the past |
| Empty fields | ❌ Error: all fields required |
| Party too large | ❌ Error: no suitable table available |
| Fully booked slot | ❌ Error: restaurant fully booked |

---

## 👨‍💻 Author

**Mohammed Arkam**
- GitHub: [@Arkam11](https://github.com/Arkam11)
- Email: mohammedarkam3856@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
