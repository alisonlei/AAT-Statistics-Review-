### HOW TO RUN ON WINDOWS ###
1. If viewing this from Git: Click the </> button above to view this properly, as the IDE is changing some of the symbols
2. Download the entire Zip file
3. Open Command Prompt
4. Navigate into 'AAT' folder
5. Copy and paste the below into Command Prompt. You only need to do the first line one time, to create the venv.
    py -3 -m venv .venv
    .venv\Scripts\activate
    pip install Flask
    pip install -U Flask-SQLAlchemy
    pip install flask flask_sqlalchemy
    flask --app __init__ run --debug