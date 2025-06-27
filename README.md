# SmartStock – Scalable Inventory Management Web App

SmartStock is a multilingual, mobile-friendly inventory management system built to help individuals and small businesses easily track stock levels in real time. The app supports full CRUD operations, real-time low-stock alerts, and multiple language options (English, Kinyarwanda, French). It’s designed for both mobile and desktop users, providing a clean, responsive interface.

## GitHub Repository

https://github.com/henriettetuombe/smartstock

## How to Set Up the Project

### 1. Clone the Repository

```bash
git clone https://github.com/henriettetuombe/smartstock.git
cd smartstock
```

### 2. Backend Setup (Django)

```bash
cd backend
python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Frontend Setup

If using plain HTML/JS:
- Open `frontend/html/index.html` or `dashboard.html` in your browser.
- Ensure the Django server is running for API-based features to function.

## Project Structure

```
smartstock/
├── backend/              # Django backend logic & API
│   ├── inventory/        # Inventory app
│   ├── smartstock/       # Django project config
│   ├── static/           # Static files (JS, CSS, etc.)
│   ├── db.sqlite3        # Development DB
│   └── manage.py
│
├── frontend/             # HTML/CSS/JS frontend
│   ├── html/             # Pages (dashboard, settings, etc.)
│   ├── css/              # Stylesheets
│   ├── js/               # Script logic
│   ├── images/           # UI graphics/icons
│   └── lang/             # JSON translation files
│
├── demo_video/           # Final project demo video
├── Screenshots/          # Screenshots showing functionality
├── .gitignore
└── README.md
```

## Key Features

- Inventory management (CRUD)
- Low stock and out-of-stock notifications
- Multilingual interface (EN, FR, RW)
- Mobile-responsive layout
- User preferences stored in local storage
- Simple and clean user interface

## Backend Highlights

- Built with Django
- Uses SQLite3 for local development
- API-ready structure with support for CRUD
- Static file support and authentication ready

## Multilingual Support

Languages supported:
- English
- French
- Kinyarwanda

Language files are found in `frontend/lang/` and use JavaScript with `data-i18n` attributes to update content dynamically.

## Demo Video

Location: `/demo_video/demo.mp4`  
Duration: 5 minutes

Covers:
- Dashboard overview
- Add, update, delete item demo
- Notifications and stock level indicators
- Language switch and responsiveness

## Screenshots

All screenshots are stored in `/Screenshots/`, showing:
- Dashboard
- Notifications
- Forms (add/update/delete)
- Mobile responsiveness
- Language toggle in action

## Testing Strategies and Results

- CRUD functionality tested with valid/invalid inputs
- Mobile responsiveness tested on various screen sizes
- Checked on Chrome, Edge, Firefox browsers
- Storage of user preferences validated with LocalStorage
- Stock threshold alerts confirmed working

## Performance

| Feature                    | Result         |
|---------------------------|----------------|
| CRUD                      | Working         |
| Notifications             | Triggered correctly |
| Language Switching        | Dynamic          |
| Mobile Responsiveness     | Confirmed        |
| Settings Storage          | Functional       |

## Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Django               |
| Database    | SQLite3              |

## Author

Henriette Tuombe  
Bachelor of Software Engineering  
African Leadership University – Rwanda

## License

MIT License