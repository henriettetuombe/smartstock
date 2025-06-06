#  SmartStock – Scalable Inventory Management Web App

SmartStock is a multilingual, user-friendly inventory management system designed for small businesses and individuals. It enables users to track their stock in real time, perform CRUD operations, and access the system in multiple languages (English, Kinyarwanda, Swahili, and French). The system is optimized for both desktop and mobile users.

---

## 🔗 GitHub Repository

[https://github.com/henriettetuombe/smartstock](https://github.com/henriettetuombe/smartstock)

---

##  How to Set Up the Project

### 1. Clone the Repository

```bash
git clone https://github.com/henriettetuombe/smartstock.git
cd smartstock
```

---

### 2. Backend Setup (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

### 3. Frontend Setup

If using HTML/CSS:

- Open `index.html` in any browser.

If using React:

```bash
cd frontend
npm install
npm start
```

---

##  Project Structure

```
smartstock/
├── backend/           # Django REST API
├── frontend/          # HTML/JS/React frontend
├── database/          # ER diagram and DB schema
├── designs/           # UI designs (desktop & mobile)
├── deployment/        # Deployment steps & screenshots
├── demo_video/        # Demo video (mp4)
├── README.md          # This documentation file
```

---

##  User Interface Designs

Design mockups available in the `/designs` folder:

- `login-desktop`, `login-mobile`
- `signup-desktop`, `signup-mobile`
- `SmartStock_Desktop_Add item`, `Update item`, `Delete item`
- `SmartStock_Mobile_Add`, `Update`, `Delete`, and `Dashboard`
-  Fully responsive design
-  Multilingual layout considerations
-  Light/dark contrast options

 **Style Guide** included: `style-guide.pdf` (colors, font, layout spacing)

---

##  Backend Features

- Built with Django REST Framework
- API endpoints to Create, Read, Update, Delete inventory items
- JWT/Session-based authentication
- User-specific inventory access
- PostgreSQL database (can work with SQLite for dev)

Sample API routes:
```http
POST /api/items/
GET /api/items/
PUT /api/items/{id}/
DELETE /api/items/{id}/
```

---

##  Database Schema

ER Diagram available in `/database/erd.png`

Key Tables:
- `User`
- `Item`
- `Category` *(optional)*
- `Transaction` *(for future stock movement logging)*

---

##  Multilingual Support

Languages supported:
- 🇬🇧 English
- 🇫🇷 French
- 🇰🇪 Swahili
- 🇷🇼 Kinyarwanda

Each UI label and message is dynamically translated based on user preference.

---

##  Deployment Plan

This app is prepared for deployment with the following tools:

| Component     | Platform     |
|---------------|--------------|
| Frontend      | Vercel / Netlify |
| Backend       | Railway / Heroku |
| Database      | Supabase PostgreSQL |
| Domain        | [Insert deployment URL here] |

To deploy:

1. Push frontend to Vercel (auto-deploy from GitHub).
2. Push backend to Railway.
3. Connect Railway backend to PostgreSQL (Supabase).
4. Set environment variables for both frontend & backend.

---

##  Demo Video

 Located in `/demo_video/demo.mp4`

⏱ Duration: ~7 minutes  
 Covers: UI walkthrough, backend features, multilingual demo, and deployment explanation.

---

##  Key Features Recap

 User authentication (Register / Login / Logout)  
 Inventory CRUD operations  
 Language selector  
 Responsive UI for mobile/desktop  
 Clean database architecture  
 Ready for deployment  

---

##  Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Frontend    | HTML/CSS/JS or React.js |
| Backend     | Django + Django REST Framework |
| Database    | PostgreSQL (or SQLite) |
| Deployment  | Railway, Vercel, Supabase |

---

##  Author

**Henriette Tuombe**  
Bachelor of Software Engineering – ALU Rwanda 

---

##  License

This project is open source and available under the [MIT License](LICENSE).
