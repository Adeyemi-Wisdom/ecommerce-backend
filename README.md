Ecommerce Backend API

A Django REST Framework backend for a fully functional ecommerce platform**, designed to showcase real-world backend development skills, including authentication, product management, cart and order handling, and payment integration readiness.

This project demonstrates expertise in building secure, scalable, and maintainable APIs, suitable for production-level applications.

Features

Authentication & User Management
* Register, login, and logout using token-based authentication
* Role-based permissions:
  * Admin: full access to products and categories
  * Users: read-only access to products, cart management, and order creation

Product & Category Management
* Admin can create, update, delete, and list products and categories
* Products include: name, description, price, stock, availability, and timestamps
* Users can view product and category details
* Search products by name or category

Cart System

* Authenticated users can:

  * Add products to cart
  * Update cart item quantity
  * Remove items from cart
  * View current cart

Orders

* Users can checkout their cart to create orders
* Orders snapshot the cart at purchase:

  * Includes product details, quantity, price at purchase
  * Maintains historical data even if product info changes
* Users can view their orders; admins can view all orders

Payment Gateway Integration (Ready)

* Designed for **Stripe/Paystack integration** to process payments
* Orders can be updated to `PAID` status via payment webhook
* Stock deduction occurs post-payment to ensure accurate inventory

Security & Permissions

* Only admin can modify products or categories
* Users can only interact with their own carts and orders
* Public access limited to viewing products and categories


Tech Stack

* Backend: Python, Django, Django REST Framework
* Authentication: Token-based (DRF Token)
* Database: SQLite
* API Testing: Postman
* Version Control: Git, GitHub


Getting Started

Clone Repository

git clone <your-repo-url>
cd ecommerce-backend

Install Dependencies

pip install -r requirements.txt

Apply Migrations


python manage.py makemigrations
python manage.py migrate


Create Superuser (Admin)

python manage.py createsuperuser

Run Server

python manage.py runserver

API Documentation

Authentication

| Endpoint     | Method | Description                    |
| ------------ | ------ | ------------------------------ |
| `/login/`    | POST   | User login, returns auth token |
| `/register/` | POST   | User registration              |
| `/logout/`   | POST   | Logout user (invalidate token) |

Products

| Endpoint             | Method    | Description                           |
| -------------------- | --------- | ------------------------------------- |
| `/product/`          | GET       | List all products                     |
| `/product/`          | POST      | Create a new product (admin only) |
| `/product/<int:pk>/` | GET       | Retrieve product details by ID        |
| `/product/<int:pk>/` | PUT/PATCH | Update product (**admin only**)       |
| `/product/<int:pk>/` | DELETE    | Delete product (**admin only**)       |

Categories

| Endpoint              | Method    | Description                            |
| --------------------- | --------- | -------------------------------------- |
| `/category/`          | GET       | List all categories                    |
| `/category/`          | POST      | Create a new category (**admin only**) |
| `/category/<int:pk>/` | GET       | Retrieve category details by ID        |
| `/category/<int:pk>/` | PUT/PATCH | Update category (**admin only**)       |
| `/category/<int:pk>/` | DELETE    | Delete category (**admin only**)       |

Cart

| Endpoint           | Method | Description                              |
| ------------------ | ------ | ---------------------------------------- |
| `/create-cart/`    | POST   | Add a product to the cart                |
| `/remove-product/` | POST   | Remove a product from the cart           |
| `/reduce-cart/`    | POST   | Reduce quantity of a product in the cart |

Future Improvements

* Full payment gateway integration (Paystack)
* Order status tracking
* Advanced product search & filtering
* Email notifications for orders and registration
* Multi-vendor support

Why This Project Stands Out

* Demonstrates production-ready backend architecture
* Implements role-based permissions and secure authentication
* Prepares for real-world ecommerce features like payment processing
* Can be extended into a full-stack ecommerce platform


Skills Highlighted

* Python, Django, Django REST Framework
* Token-based authentication & permissions
* CRUD operations & data validation
* Relational data modeling (Product, Category, Cart, Order)
* API design & documentation
* Payment integration concepts

