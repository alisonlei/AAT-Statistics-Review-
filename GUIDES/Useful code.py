


# HOW TO RENDER A PAGE THAT PULLS FROM ALL ROWS OF A TABLE (A TABLE THAT HAS A RELATIONSHIP WITH ANOTHER TABLE)
# EG: A PAGE ABOUT ALL ASSIGNMENTS [ALL ROWS] WITHIN THE 'Assignment' TABLE OF A 'db' DATABASE, WHICH HAS A PRIMARY KEY 'a_id'. THIS TABLE IS LINKED TO TABLE 'Exercise' WHICH HAS PRIMARY KEY 'e_id'. 
    # 1. CREATE THE HTML FOR THAT PAGE (e.g., assignment_list.html)
    
    # 2. IN __init__.py ...
            # SET UP 'db' AND 'app'
                # ???

    # 3. IN models.py: LINK THE TABLES THROUGH 'OBJECT RELATIONSHIP MAPPING'(ORM)
            # TABLE 1
            class AssignmentORM(Base):    
                # STATE THE NAME OF THIS TABLE
                __tablename__ = "Assignment"
                # STORE EACH COLUMN'S VALUE. MAKE SURE TO (A) LABEL THE PRIMARY KEY (B) INTICATE THE DATA TYPE
                a_id = Column(Integer, primary_key=True)
                assignment_name = Column(String)
                q1_id = Column(Integer)
                # LINK IT TO TABLE 2'S ORM
                assignments: Mapped[List["ExerciseORM"]] = relationship(secondary='relationshipName')

            # TABLE 2
            class ExerciseORM(Base):    
                # STATE THE NAME OF THIS TABLE
                __tablename__ = "Exercise"
                # STORE EACH COLUMN'S VALUE. MAKE SURE TO (A) LABEL THE PRIMARY KEY (B) INTICATE THE DATA TYPE
                e_id = Column(Integer, primary_key=True)
                question = Column(String)
                correct_answer = Column(String)
                # LINK IT TO TABLE 1
                exercises: Mapped[List["AssignmentORM"]] = relationship(secondary='relationshipName')

            # DEFINE THE RELATIONSHIP
                relationshipName = Table(
                    'relationshipName',
                    Base.metadata,
                    # STATE THE KEYS OF BOTH TABLES [Anya: I can't remember how this part works tbh]
                    Column("e_id", ForeignKey("Exercise.e_id"), primary_key=True),
                    Column("a_id", ForeignKey("Assignment.a_id"), primary_key=True),
                )

    # 4. IN models.py: WRITE THE 'DATA ACCESS OBJECTS' (DAO) SO WE CAN ACCESS THE DATA FROM THESE TABLES
            # TABLE 1
            class AssignmentDAO():
                # METHOD TO ACCESS AN INDIVIDUAL ROW, WHEN GIVEN THE PRIMARY KEY VALUE FOR THAT ROW
                def AssignmentById(a_id, db):
                    stm = select(AssignmentORM).where(AssignmentORM.a_id == a_id)
                    assignment = db.session.scalar(stm)
                    return assignment
                # METHOD TO ACCESS ALL ROWS
                def allAssignments(db):
                    stm = select(AssignmentORM)
                    assignments = db.session.scalars(stm).all()
                    return assignments

            # TABLE 2
            class ExerciseDAO():
                # METHOD TO ACCESS AN INDIVIDUAL ROW, WHEN GIVEN THE PRIMARY KEY VALUE FOR THAT ROW
                def ExerciseById(a_id, db):
                    stm = select(ExerciseDAO).where(ExerciseDAO.e_id == e_id)
                    exercise = db.session.scalar(stm)
                    return exercise
                # METHOD TO ACCESS ALL ROWS
                def allExercises(db):
                    stm = select(ExerciseDAO)
                    exercises = db.session.scalars(stm).all()
                    return exercises

    # 5. IN routes.py ...
            from flask import render_template
            @app.route("/assignments")    # State the page's URL
                def list_assignments():  # Name a function that will be used to render the page
                    # GET ALL THE ROWS IN THE 'Assignment' TABLE, AND STORE THEM IN A VARIABLE 'found_assignments'
                    found_assignments = AssignmentDAO.allAssignments(db)
                    
                    # RENDER THE PAGE 'assignment_list.html', AND PASS IN THE RESULTS OF THE ABOVE THROUGH A VARIABLE 'assignments'
                    return render_template('assignment_list.html',assignments=found_assignments)








# HOW TO RENDER A PAGE THAT PULLS FROM A SPECIFIC ROW OF A TABLE (A TABLE THAT HAS A RELATIONSHIP WITH ANOTHER TABLE)
# EG: A PAGE ABOUT AN ASSIGNMENT [ROW] WITHIN THE 'Assignment' TABLE OF A 'db' DATABASE, WHICH WAS FOUND USING PRIMARY KEY 'a_id'. THIS TABLE IS LINKED TO TABLE 'Exercise' WHICH HAS PRIMARY KEY 'e_id'.
    # 1. CREATE THE HTML FOR THAT PAGE (e.g., assignment.html)
       
    # 2. IN __init__.py ...
            # STORE THE DATABASE WITHIN A VARIABLE 'db'
                # ???

    # 3. IN models.py: LINK THE TABLES THROUGH 'OBJECT RELATIONSHIP MAPPING'(ORM)
            # See above

    # 4. IN models.py: WRITE THE 'DATA ACCESS OBJECTS' (DAO) SO WE CAN ACCESS THE DATA FROM THESE TABLES
            # See above

    # 5. IN routes.py ...
            from flask import render_template
            @app.route("/assignments/<a_id>")    # State the page's URL (you can use <x> when x may vary depending on the assignment you're looking at)
                def assignment_load(a_id):  # Name a function that will be used to render the page
                    # GET THIS ROW FROM THE 'Assignment' TABLE, AND STORE IT IN A VARIABLE 'assignment_found'
                    assignment_found=AssignmentDAO.AssignmentById(a_id,db)
                    # RENDER THE PAGE 'assignment.html', AND PASS IN THE RESULTS OF THE ABOVE THROUGH A VARIABLE 'assignment'
                    return render_template('assignment.html',assignment=assignment_found)








# ACCESS A ROW'S DATA WITHIN A HTML FILE
# EG: Within the aforementioned 'assignment.html' I want to write the assignment's name, which was saved under 'assignment_name' during Step 3
        <li> {{assignment.assignment_name}} </a> </li>








# WRITE A LINK TO A SPECIFIC VERSION OF A PAGE
# EG:
# Imagine in step 5 we had rendered a page for "/exercises/<e_id>".
# We have table 'Assignment', which has 11 columns - a_id, q1_id, q2_id, q3_id, etc...
#   > These columns hold the IDs of exercises that were added to that assignment. A maximum of 10 exercises can be added.
#   > These IDs are foreign keys to the 'e_id' column in the 'Exercise' table, which holds information on each exercise (e.g., the question, the correct answer)
# Let's say we want to write a link that takes the user to a page specifically about that exercise...
        # 1. Define the object 'assignment' through an ORM (see above), storing the columns within 'q1_id', 'q2_id', etc.
        # 2. At the start of ? routes.py ? say...
            from flask import url_for
        # 3. Write the link in your HTML...
            <li> <a href="{{url_for('exercise_load',e_id=assignment.q1_id)}}">  {{assignment.q1_id}} </a> </li>