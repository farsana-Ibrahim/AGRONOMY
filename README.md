# AGRONOMY
An e-commerce platform that connects farmers directly with buyers and agricultural suppliers.

# Agricultural Information and Commerce Platform - README

A comprehensive Django-based agricultural e-commerce platform connecting farmers, agricultural service centers, and consumers for seamless trade of agricultural products and essentials.

## 🌟 Overview

KrishiSetu is a full-stack agricultural platform built with Django that bridges the gap between farmers and consumers. It enables farmers to sell their organic produce directly to buyers while providing easy access to agricultural essentials through Krishi Bhavans and Agroservice Centers.

## 🎯 Key Features

### 🛒 E-Commerce Marketplace
- **Farmers Marketplace**: Direct selling platform for organic produce
- **Agricultural Essentials**: Seeds, seedlings, fertilizers, and tools
- **Dual Payment Options**: Online payments & cash-on-delivery
- **Inventory Management**: Stock tracking for service centers

### 👨‍🌾 Farmer Empowerment
- **Direct Selling**: Farmers can list and sell products directly
- **Fair Pricing**: Ensures better profit margins for farmers
- **Product Management**: Easy inventory and sales tracking
- **Farmer Verification**: Authenticated farmer profiles

### 🏪 Service Center Integration
- **Krishi Bhavan Integration**: Official agricultural department stores
- **Agroservice Centers**: Local agricultural service providers
- **Order Management**: Streamlined order processing
- **Delivery Coordination**: Logistics management

### 💳 Payment & Transactions
- **Secure Online Payments**: Integration with payment gateways
- **Cash on Delivery**: Flexible payment option
- **Transaction History**: Complete purchase records
- **Order Tracking**: Real-time order status updates

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Django 4.x** - Web framework
- **Django REST Framework** - API development
- **MySQL** - Database management
- **Celery** - Asynchronous task processing

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript** - Frontend interactivity
- **Bootstrap 5** - Responsive design framework
- **jQuery** - DOM manipulation

### Additional Components
- **Pillow** - Image processing
- **Stripe/Razorpay** - Payment gateway integration
- **Redis** - Caching and Celery broker
- **Gunicorn** - WSGI HTTP server
- **Nginx** - Web server and reverse proxy

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL 5.7 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/krishisetu-platform.git
cd krishisetu-platform
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration
```bash
# MySQL setup
mysql -u root -p
CREATE DATABASE krishisetu;
CREATE USER 'krishiuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON krishisetu.* TO 'krishiuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5. Environment Configuration
```bash
cp .env.example .env
```
Edit `.env` file:
```ini
DEBUG=True
SECRET_KEY=your-django-secret-key
DATABASE_URL=mysql://krishiuser:password@localhost:3306/krishisetu
STRIPE_SECRET_KEY=your-stripe-secret-key
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 6. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Load Sample Data (Optional)
```bash
python manage.py loaddata categories.json
python manage.py loaddata products.json
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 🗄️ Database Models

### Core Models
- **User** - Extended Django user model with user types
- **Farmer** - Farmer profile with verification status
- **Product** - Agricultural products with categories
- **Order** - Customer orders with status tracking
- **OrderItem** - Individual items in orders
- **Payment** - Payment transaction records
- **Category** - Product categorization

## 🔐 User Roles

1. **Admin** - Platform administrator
2. **Krishi Bhavan Staff** - Service center operators
3. **Farmer** - Verified farmers selling products
4. **Customer** - End consumers buying products

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout

### Products
- `GET /api/products/` - List all products
- `POST /api/products/` - Create product (farmer/admin)
- `GET /api/products/{id}/` - Product details
- `PUT /api/products/{id}/` - Update product

### Orders
- `GET /api/orders/` - User orders
- `POST /api/orders/` - Create order
- `GET /api/orders/{id}/` - Order details

### Payments
- `POST /api/payments/create/` - Initiate payment
- `POST /api/payments/verify/` - Verify payment

## 🎨 Frontend Features

### Pages
- **Homepage** - Featured products and categories
- **Product Listing** - Filterable product catalog
- **Product Detail** - Product information and purchase
- **Shopping Cart** - Cart management
- **Checkout** - Order placement and payment
- **Farmer Dashboard** - Product and order management
- **Admin Panel** - Platform administration

## 🔧 Configuration

### Django Settings
Key configurations in `krishisetu/settings.py`:
```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'krishisetu',
        'USER': 'krishiuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## 🚀 Deployment

### Production Setup
1. Set `DEBUG=False`
2. Configure production database
3. Set up static files with WhiteNoise
4. Configure Gunicorn and Nginx
5. Set up SSL certificate
6. Configure domain and DNS

### Sample Nginx Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location /static/ {
        alias /path/to/staticfiles/;
    }
    
    location /media/ {
        alias /path/to/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

**Empowering Farmers, Connecting Communities** 🌱
