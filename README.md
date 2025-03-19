If you're viewing this from Git: 
        Click the 'README.md' header above, 
        then click the '</>' button 
        (otherwise the below text won't show properly)



## HOW TO RUN OUR PROJECT ON WINDOWS ##
1. Open our project on the GitLab website > 
        Use the drop down to move to the master branch > 
        Click 'Code' on the right > 
        Click 'Download source code: zip' 
        [You could use cloning instead but downloading the zip is simpler]
2. Open Command Prompt
3. Navigate into the 'AAT' folder
4. Copy and paste the below into Command Prompt. You only need to do the first line one time, to create the venv.
        py -3 -m venv .venv
        .venv\Scripts\activate
        pip install Flask
        pip install -U Flask-SQLAlchemy
        pip install flask flask_sqlalchemy
        pip install flask_restful
        flask --app __init__ run --debug
5. When you need to close the venv...
        Press CTRL+C
        Run 'deactivate'



## HOW TO ADD YOUR CODE ##
I (Anya) did this wrong at one point and basically deleted all of our stuff :/ 
I've now written a guide on how to do this properly, so that we all know how to integrate the code safely. 
The guide is in >GUIDES>Git guide.md



## HOW TO USE OUR DATABASE ##
### CREATING TABLES ###
- CreateTables.sql holds the code that creates our tables
- To check what tables are in a .db file...
        Open Command Line
        Navigate into the folder that the file is in
        Run...
            .open fileName.db [This has to be exact or it'll create a new file]
            .tables
            .pragma table_info(name_of_table);
### POPULATING TABLES ###
- PopTables.sql holds the code that populates our tables
- To check what data is in a table...
        Open Command Line
        Navigate into the folder that your .db file is in
        Run...
            .open fileName.db [This has to be exact or it'll create a new file]
            SELECT * from name_of_table;