# 📝 Daily Journal

A full-stack journaling web app to log your mood and thoughts, view past entries, and get inspired by daily quotes. Built with Flask (backend), SQLite (database), and HTML/CSS/JavaScript (frontend).

## 🌟 Features

- 🌈 Add daily journal entries (date, mood, thoughts)
- 📅 View all past entries
- 🔍 Filter entries by specific date
- 💬 Get an inspirational quote (from quotable.io)
- 🖼️ Clean and responsive user interface

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask, Flask-CORS
- **Database:** SQLite
- **Testing:** Postman
- **Version Control:** Git + GitHub

## 🗂 Project Structure
```
daily-journal/
├── backend/
│ ├── app.py
│ ├── database.py
│ ├── models.py
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│ └── assets/
├── README.md
└── .gitignore
```

## 🔌 API Endpoints

- `GET /api/quote` – Get daily inspirational quote
- `POST /api/journal` – Add a new journal entry
- `GET /api/journal` – Get all journal entries
- `GET /api/journal/<date>` – Get entries for a specific date
- `DELETE /api/journal/<id>` – Delete a journal entry

## ▶️ Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/daily-journal.git
cd daily-journal
```
### 2. Setup Backend
```
cd backend
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
python app.py
```





### 3. Setup Frontend
Open frontend/index.html in a browser. You can use the Live Server extension in VSCode for automatic reloading.

## Author
- Anosh Ardeni
- GitHub: AnoshArdeni

