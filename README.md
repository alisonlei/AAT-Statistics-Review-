### HOW TO RUN ON WINDOWS ###
1. Download the entire Zip file
2. Open Command Prompt
3. Navigate into 'AAT' folder
4. Copy and paste the below into Command Prompt [You only need to do the first line one time, to create the venv - but remember not to push the '.venv' or '_pycache_' to Git. Also note this IDE is removing the two underscores on either side of 'init' below]
py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask
pip install -U Flask-SQLAlchemy
pip install flask flask_sqlalchemy
flask --app __init__ run --debug