## Getting Started

### Installation Steps

1. **Clone this repository**:

   ```bash
   git clone https://github.com/Miroslav‑Miro/ICT‑Strypes‑Projects.git
   cd ICT‑Strypes‑Projects/django_projects
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a project** (example: `test_project`):
   ```bash
   cd test_project
   python manage.py migrate
   python manage.py createsuperuser  # optional, for admin access
   python manage.py runserver
   ```
   Now head to `http://127.0.0.1:8000/` to see it live!

---

## Features & Technologies

| Feature             | Description                                  |
| ------------------- | -------------------------------------------- |
| Django Admin        | Auto-generated interface for database models |
| Models & Migrations | Database structure via Django ORM            |
| Views & Templates   | Handling requests, rendering HTML            |
| Form Handling       | Using Django's built-in `forms` module       |
| User Authentication | Registration, login/logout mechanisms        |
| Static & Media      | Serving CSS, and uploaded files              |

---

## Usage Tips

- **Switch between projects**:  
  Navigate into each project folder and use `python manage.py runserver`.

- **Add new apps**:

  ```bash
  python manage.py startapp app_name
  ```

  Then update `settings.py` to include your new app.

- **Admin access**:  
  Use `createsuperuser` to generate an admin user, then visit `/admin/`.

---

## License

This project is licensed under the **MIT License**

---

## Contact

If you have questions or suggestions, feel free to open an issue or submit a PR.

---
