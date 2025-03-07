### HOW TO RUN ON WINDOWS ###
Copy and paste the below into Command Prompt... [ANYA: I CAN'T REMEMBER IF ALL OF THESE ARE NEEDED]
py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask
pip install -U Flask-SQLAlchemy
pip install flask flask_sqlalchemy
flask --app __init__ run --debug