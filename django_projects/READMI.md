# Django Blog Project

This is a Django-based blog application developed as part of the **ICT Strypes Internship Program**.  
It demonstrates core Django concepts such as views, templates, models, forms, static/media file handling, and modular app structure.

---

## Getting Started

Follow the steps below to set up and run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/Miroslav-Miro/ICT-Strypes-Projects.git
cd ICT-Strypes-Projects/django_projects/my_site

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
