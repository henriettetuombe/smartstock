# SmartStock – Scalable Inventory Management Web App

SmartStock is a modern, multilingual, mobile-responsive inventory management system built to help individuals and small businesses track their stock in real time. The platform supports full CRUD operations, low stock alerts, user personalization, and dynamic language switching (English, French, Kinyarwanda). It is built with Django on the backend and plain HTML, CSS, and JavaScript on the frontend.

## Live Deployment

- Frontend: https://merry-dango-a5ec2a.netlify.app/html/landing.html
- Backend: https://smartstock-1-1wm7.onrender.com

Make sure the backend is running for frontend interactions (like item creation, language loading, or authentication).

## GitHub Repository

https://github.com/henriettetuombe/smartstock

## Project Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/henriettetuombe/smartstock.git
cd smartstock
```

### 2. Backend Setup (Django)

```bash
cd backend
python -m venv env
# Activate the virtual environment:
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# (Optional) Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

### 3. Frontend Setup

No compilation or build steps needed.

- Open `frontend/html/landing.html` or `dashboard.html` in a browser.
- Make sure the backend is running and accessible for API features.

## Project Structure

```
smartstock/
├── backend/
│   ├── inventory/
│   ├── smartstock/
│   ├── static/
│   └── db.sqlite3
│
├── frontend/
│   ├── html/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── lang/
├── Screenshots/
├── demo_video/
├── requirements.txt
└── README.md
```

## Features

- Add / Update / Delete inventory items
- Low stock and out-of-stock notifications
- Multilingual support: English, French, Kinyarwanda
- User login/register with JWT auth
- Dynamic language switching
- Mobile and tablet responsive design
- LocalStorage support for user preferences
- Admin panel for backend management
- Pre-seeded product categories

## Authentication

Authentication is handled using JWT (via djangorestframework-simplejwt).

### Available Endpoints:

```
GET    /api/user/
POST   /api/token/
POST   /api/token/refresh/
POST   /api/register/
GET    /admin/
```

## Inventory API

```
GET    /api/items/
POST   /api/items/
PUT    /api/items/<id>/
DELETE /api/items/<id>/
GET    /api/categories/
GET    /api/seed-categories/
```

## Multilingual Support

Language files are stored in `frontend/lang/` and include:

- en.json
- fr.json
- rw.json

Using `data-i18n` attributes and JavaScript, the language can be switched dynamically.

## Testing & Quality Assurance

| Test Area                    | Status         |
|-----------------------------|----------------|
| CRUD operations             | Functional     |
| Category auto-loading       | Working        |
| Multilingual switching      | Dynamic        |
| Responsive UI               | Mobile/tablet verified |
| LocalStorage (preferences)  | Functional     |
| API Auth (JWT)              | Verified       |
| Admin functionality         | Working        |

## Screenshots

Screenshots are stored in `/Screenshots/` and show:

- Landing page
- Dashboard and item status
- Add/Update/Delete pages
- Mobile version UI
- Language switcher in action
- Admin panel categories

## Demo Video

Location: `/demo_video/demo.mp4`

Covers:

- Register/login flow
- Adding and editing stock items
- Category loading
- Real-time notifications
- Language toggle across interface
- Responsive layout demonstration

## Deployment Plan

### Backend (Render)

- Platform: Render.com
- Database: SQLite
- Endpoint: https://smartstock-1-1wm7.onrender.com
- Admin Creation: Temporary endpoint `/api/create-admin/` added for first-time setup

### Frontend (Netlify)

- Platform: Netlify
- Build: Static HTML/CSS/JS
- URL: https://merry-dango-a5ec2a.netlify.app/html/landing.html

## Tech Stack

| Layer         | Tools/Technologies         |
|---------------|----------------------------|
| Frontend      | HTML, CSS, JavaScript      |
| Backend       | Django, Django REST Framework |
| Authentication| JWT (SimpleJWT)            |
| Database      | SQLite3                    |
| Deployment    | Render (backend), Netlify (frontend) |
| i18n          | JSON with JavaScript       |

## Author

Henriette Tuombe  
Bachelor of Software Engineering  
African Leadership University – Rwanda

## License

MIT License