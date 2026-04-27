🛒 Apni Dukaan (Django E-commerce Website)

Apni Dukaan is a fully functional e-commerce web application built using Django. It allows users to browse products, manage their cart, place orders, and handle user authentication.

🚀 Features
🛍️ Browse products
🔍 View product details
🛒 Add to cart & manage cart
📦 Place and manage orders
👤 User authentication (Login/Register)
🧑‍💼 Admin panel for product & order management
🖼️ Product image handling (media support)

🛠️ Tech Stack
Backend: Python, Django
Frontend: HTML, CSS, JavaScript
Database: SQLite
Media Handling: Django Media Files

📂 Project Structure
apni-dukaan/
│── cart/                 # Cart management app
│── ecommerce_project/    # Main project settings
│── media/products/       # Product images
│── orders/               # Order management app
│── products/             # Product listing app
│── users/                # User authentication app
│── db.sqlite3            # Database
│── manage.py


⚙️ Installation & Setup
Clone the repository
git clone https://github.com/your-username/apni-dukaan.git
Navigate to the project
cd apni-dukaan
Create virtual environment
python -m venv venv
Activate environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Apply migrations
python manage.py migrate
Run server
python manage.py runserver
Open in browser
http://127.0.0.1:8000/

🔐 Admin Panel

Access admin panel at:

http://127.0.0.1:8000/admin/

Create admin user:

python manage.py createsuperuser


🎯 Future Improvements
💳 Payment gateway integration
📦 Order tracking system
⭐ Product reviews & ratings
📱 Fully responsive UI
🚀 Deployment (Render / AWS)
🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

📄 License

This project is open-source under the MIT License.

👨‍💻 Author

Rajat Kumar Gupta
