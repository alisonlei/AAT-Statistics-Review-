## HOW TO RUN OUR PROJECT ON WINDOWS ##
1. If you're viewing this from Git: Click the 'README.md' header above, then click the '</>' button (otherwise the below text won't show properly)
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
5. When you need to close the venv...
        Press CTRL+C
        Run 'deactivate'



## HOW TO ADD YOUR CODE ##
I (Anya) did this wrong at one point and basically deleted all of our stuff :/ 
I've now written a guide on how to do this properly, so that we all know how to integrate the code safely. 
The guide is in >GUIDES>Git guide.md



## HOW TO USE OUR DATABASE ##
### HOW TO CREATE TABLES ###
1. CreateTables.sql holds the code that creates our tables
2. Check if the tables have been added:
        Open command line
        cd into the folder that 'ourdb' is in
        Run...
            .open ourdb.db
            .tables
            .pragma table_info(name_of_table);
### HOW TO ADD DATA TO TABLES ###
1. PopTables.sql holds the code that populates our tables
2. Check if the tables have been populated:
        Open command line
        cd into the folder that 'ourdb' is in
        Run...
            .open ourdb.db
            SELECT * from name_of_table;