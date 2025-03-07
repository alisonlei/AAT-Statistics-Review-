### HOW TO ADD YOUR WORK TO THIS ###
I (Anya) did this wrong at one point and basically deleted all of our stuff :/ Luckily I'd made a backup but :/
I've now written up the steps on how to do this properly, so that we all know how to integrate the code safely.
Those steps are written in >GUIDES>Git guide.md


### HOW TO RUN OUR PROJECT ON WINDOWS ###
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