# SmartStock Deployment Instructions

## Backend Deployment (Django API) – Railway

### Prerequisites:
- GitHub repo connected
- Railway account (free): https://railway.app/

### Steps:
1. Go to [https://railway.app/](https://railway.app/) and sign in
2. Click **“New Project” > “Deploy from GitHub Repo”**
3. Select `smartstock` repo
4. Set environment variables:
   - `SECRET_KEY`: your Django secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: `*` or your Railway domain
5. Railway will install dependencies and deploy
6. Add a **PostgreSQL plugin** → It will auto-connect the DB
7. Run:
   - `python manage.py migrate`
   - `python manage.py createsuperuser`

### Live API URL:
Check your Railway app domain (e.g., `https://smartstock-production.up.railway.app/`)

---

## Frontend Deployment – Netlify (HTML/CSS/JS)

### Steps:
1. Go to [https://www.netlify.com/](https://www.netlify.com/)
2. Create new site from GitHub
3. Select the `smartstock/frontend` folder
4. Netlify auto-deploys your static site
5. In your JS files, update API calls:
   ```js
   const API_BASE_URL = 'https://smartstock-production.up.railway.app/api/';
