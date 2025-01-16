# Online Food Order

**Online Food Order** is a dynamic website created using Django. This project allows users to browse menus, place orders, and manage their food delivery experience online. It also includes features for restaurant owners to manage their menus, track orders, and improve customer satisfaction.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- **User Authentication**: Sign up, log in, and manage accounts.
- **Menu Browsing**: View and search for food items by category.
- **Order Management**: Add items to the cart, place orders, and view order history.
- **Admin Panel**: Manage food items, categories, and view all orders.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/subarnasaikia/OnlineFoodOrder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd OnlineFoodOrder
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/MacOS
   env\Scripts\activate  # For Windows
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply the migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Open your web browser and go to `http://localhost:8000/` to explore the website.
- For the admin panel, visit `http://localhost:8000/admin/` and log in with superuser credentials.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

