# GUI-Based Shopping System with Database Integration Using PyQt5

---

## Project Overview

This project features a user-friendly shopping system with a **PyQt5-based GUI** integrated with a relational database backend (PostgreSQL or MySQL). It supports distinct user roles, allowing **admins** to manage products, customers, and suppliers, while **customers** can browse products, manage their shopping carts, and view invoices. The modular design facilitates scalability and easy feature expansion.

---

## Features

- **Role-Based Access:**
  - **Admin:** Full control over customers, products, and suppliers management.
  - **Customer:** Product browsing, cart management, and invoice viewing.

- **Database Support:**
  - Compatible with PostgreSQL and MySQL for reliable, scalable data storage.

- **Intuitive Interface:**
  - Interactive, role-specific panels tailored for admins and customers.

- **Modular & Scalable:**
  - Clean codebase with modular structure to support future feature additions.

---

## Project Structure

```
.
├── main.py                # Main program to run the application
├── login.py               # User login and registration logic
├── admin_panel.py         # Admin panel navigation
├── admin_customer.py      # Admin functionalities to manage customers
├── admin_product.py       # Admin functionalities to manage products
├── admin_supplier.py      # Admin functionalities to manage suppliers
├── customer.py            # Customer functionalities (products, cart, invoices)
├── ui_forms/              # UI files for all windows
├── sample_database.sql    # SQL file to set up the database
├── erd_diagram.png        # Database Entity Relationship Diagram
```

---

## Prerequisites

- Python 3.8 or higher  
- PostgreSQL or MySQL server installed  
- Required Python packages:  
  ```bash
  pip install PyQt5 mysql-connector-python psycopg2
  ```

---

## Setting Up the Database

### Step 1: Install Database
- Install [PostgreSQL](https://www.postgresql.org/download/) or [MySQL](https://www.mysql.com/downloads/).

### Step 2: Create the Database
1. Create a new database:
   ```sql
   CREATE DATABASE inventory_management;
   ```

2. Import the provided SQL schema:
   ```bash
   psql -U <username> -d inventory_management -f sample_database.sql
   ```

---

## Configuration

Update the database credentials in the `config.py` file:

```python
DatabaseConfig = {
    'user': 'your_username',#root
    'password': 'your_password',#admin
    'host': 'localhost',
    'database': 'sample_database'
}
```

---

## Running the Application

1. Ensure all prerequisites are installed and the database is set up.
2. Run the application:
   ```bash
   python main.py
   ```
3. Log in or register as:
   - **Admin**: Access administrative features like product, customer, and supplier management.
   - **Customer**: Browse products, manage the cart, and view invoices.

---

## Application Overview

### 1. Login and Registration
- Log in or register as a customer or admin.
- Redirected to role-specific panels.

### 2. Admin Panel
- **Customer Management**: Add, edit, delete, and search customer data.
- **Product Management**: Manage inventory and pricing.
- **Supplier Management**: Maintain supplier details.

### 3. Customer Panel
- **Browse Products**: View available products.
- **Cart Management**: Add/remove products and calculate totals.
- **Invoice History**: View past purchases and invoices.

---

## Database Diagram

Refer to the Entity Relationship Diagram (ERD) for an overview of the database structure:

<img width="1007" height="1393" alt="diagram" src="https://github.com/user-attachments/assets/7389e49d-0642-44a9-b247-d3c9a0b7dc1e" />

---

## Extending the Application

- **Adding Features**:
  Add UI files under ui_forms/, implement corresponding logic modules, and register new features in main.py.

- **Modifying Database**:
  Update sample_database.sql schema and adjust queries across relevant modules accordingly.

---

## Future Enhancements

- Sales and customer analytics dashboard.
- Integration with payment gateways and supplier APIs.
- Additional user roles (e.g., delivery personnel).

---
