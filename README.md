A full-stack Expense Tracker application that allows users to manage daily expenses efficiently. Built using FastAPI (backend) and HTML/CSS/JavaScript (frontend) with PostgreSQL as the database and deployed using Docker and Render.


✨ Features
Add, update, and delete expenses
View all expenses in a structured table
Filter expenses by category
Sort expenses by date (Newest / Oldest)
Real-time total expense calculation
Clean and responsive UI
RESTful API integration


🖥️ Application Preview
Amount	Category	Description	Date	Actions
₹ 6,000	Rent	House Rent	2026-05-08	Edit / Delete

Total Amount: ₹ 6,000

🏗️ Tech Stack
Backend
FastAPI
SQLAlchemy ORM
PostgreSQL
Uvicorn
Frontend
HTML
CSS
JavaScript (Fetch API)
DevOps & Deployment
Docker
Docker Compose
Render (Cloud Deployment)


⚙️ Local Setup (Docker)
1️⃣ Clone Repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
2️⃣ Run Application
docker compose up --build
3️⃣ Access
Backend → http://localhost:8000
Frontend → Open frontend/index.html

🔗 API Endpoints
Method	Endpoint	Description
POST	/expenses	Create expense
GET	/expenses	Get all expenses
PUT	/expenses/{id}	Update expense
DELETE	/expenses/{id}	Delete expense


🔧 Environment Variables

Create a .env file (if using locally):

DATABASE_URL=postgresql://postgres:password@db:5432/expense_db
🐳 Docker Overview
Backend runs in a Python container
Database runs in PostgreSQL container
Managed using Docker Compose
🌍 Deployment
Backend
Hosted on Render (Web Service)
Frontend
Hosted on Render (Static Site)
Database
PostgreSQL (Render / Docker)