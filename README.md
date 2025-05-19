# ecommerce-product-catalog-frontend
# ecommerce-product-catalog-frontend

A Django-based ecommerce product catalog application.

## Features

- Product listing and detail views
- Admin interface for managing products
- Responsive frontend design
- Image upload support

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- SQLite (default) or another supported database

### Installation

1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd ecommerce-product-catalog-frontend
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

7. Access the app at (https://ecommerce-product-catalog-frontend.onrender.com/)) 

## Deployment

- Configure environment variables for production (e.g., `DEBUG=False`, `ALLOWED_HOSTS`, database settings).
- Use a production-ready server (e.g., Gunicorn, uWSGI) and a web server (e.g., Nginx).
- Collect static files:
  ```sh
  python manage.py collectstatic
  ```



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For questions or support, please open an issue on the repository.
