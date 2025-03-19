INSERT INTO Teacher
VALUES (1)
;

INSERT INTO Assessment
VALUES (1,1,1,'KS2 Mathematics: Term 1',1,2,6,7,9,15,16,17,18,20),
        (2,1,0,'KS3 Mathematics: Term 1',3,4,5,6,10,11,12,13,14,19)
;

INSERT INTO Exercise
VALUES
    (
        1,
        1,
        1,
        'Shapes',
        'What shape has 4 sides of equal length?',
        'Square',
        'A square has a total of 4 sides, and all 4 are the same length.',
        'Rectangle',
        'Circle',
        'Triangle'
    ),
    (
        2,
        1,
        1,
        'Shapes',
        'What is the name for a 3D circle?',
        'Sphere',
        'A sphere is the 3D version of a circle - it looks like a ball!',
        'Rounder',
        'Circle',
        'Cylinder'
    ),
    (
        3,
        1,
        1,
        'Geometry',
        'What is the name of the theorem that tells us the length of a right-angle triangle’s hypotenuse?',
        'Pythagoras',
        'Pythagoras theorum tells us that c2 = a2 + b2',
        'Gauss',
        'Newton',
        'Einstein'
    ),
    (
        4,
        1,
        1,
        'Shapes',
        'What is the name of a triangle with sides of equal length?',
        'Equilateral',
        'An equilaterial triangle has a total of 3 sides, and all 3 are the same length.',
        'Scalene',
        'Isosceles',
        'Right-Angle'
    ),
    (
        5,
        1,
        1,
        'Geometry',
        'Which greek letter helps us calculate the circumference of a circle?',
        'Pi',
        'We multiply a circle`s diameter by pi (3.14 ...) to get its circumference.',
        'Alpha',
        'Beta',
        'Sigma'
    ),
    (
        6,
        1,
        1,
        'Shapes',
        'Which of these is not a 3D shape?',
        'Octagon',
        'An octagon is a 2D shape of 8 sides',
        'Cube',
        'Triangular prism',
        'Cylinder'
    ),
    (
        7,
        1,
        1,
        'Shapes',
        'What is the difference between a square and a cube?',
        'One is 3D',
        'A cube is the 3D version of a square - all of it`s sides are of equal size.',
        'One is blue',
        'One is round',
        'One is longer than the other'
    ),
    (
        8,
        1,
        1,
        'Shapes',
        'Which of these shapes doesn`t have identical sides?',
        'Cone',
        'A cone has 1 flat side in the shape of a circle, and 1 side that curves the whole way around the shape.',
        'Square',
        'Sphere',
        'Cube'
    ),
    (
        9,
        1,
        1,
        'Shapes',
        'Which shape has a total of 5 sides?',
        'Pentagon',
        'A pentagon has 5 sides. The term `penta` comes from the Greek word `Pente`, which means 5.',
        'Hexagon',
        'Octagon',
        'Decagon'
    ),
    (
        10,
        1,
        1,
        'Geometry',
        'If an angle is 2 degrees below 180 degrees, what type of angle is it?',
        'Obtuse',
        'This would be 178 degrees. An angle above 90 degrees but less than 180 is known as an `obtuse` angle.',
        'Acute',
        'Right',
        'Reflect'
    )
;

INSERT INTO Exercise(Exercise_ID,Teacher_ID,Set0forFTB_1forMCQ,Topic,Question,Correct_answer,How_corr_answ_was_reached)
VALUES
    (
        11,
        1,
        0,
        'Shapes',
        'There are _ types of triangle',
        '6',
        'There are 6 types of angles -  Acute, Obtuse, Right, Straight, reflex and full rotation.'			
    ),
    (
        12,
        1,
        0,
        'Geometry',
        'There are _ degrees in a right angle',
        '90',
        'There are 90 degrees in a ride angle - remember that it is a quarter of a full rotation (360)!'
    ),
    (
        13,
        1,
        0,
        'Geometry',
        'The interior angles in an acute triangle add up to _ degrees.',
        '90',
        'Regardless of the specific shape, an acute triangle`s interior angles will always add up to 90 degrees.'			
    ),
    (
        14,
        1,
        0,
        'Geometry',
        'The angles in a quadrilateral add up to _ degrees',
        '360',
        'Regardless of the specific shape, a quadrilateral`s angles will always add up to 360 degrees.'			
    ),
    (
        15,
        1,
        0,
        'Addition',
        'Jerry has 2 blue pens. Sally has 1 red pen. They have _ pens in total.',
        '3',
        'Regardless of the colours, they have 3 pens. 2 + 1 = 3'		
    ),
    (
        16,
        1,
        0,
        'Multiplication',
        '3, 6, 9, 12 is the beginning of the _ times tables.',
        '3',
        'This is the 3 times table - 3, 6, 9, 12, 15, 18, 21, etc.'			
    ),
    (
        17,
        1,
        0,
        'Addition',
        '8 plus 2 equals _',
        '10',
        'If we add 1 to 8 we get 9. If we add another 1 we get 10!'		
    ),
    (
        18,
        1,
        0,
        'Time',
        'There are _ minutes in an hour.',
        '60',
        'There are 60 minutes in an hour, just as there are 60 seconds in a minute.'			
    ),
    (
        19,
        1,
        0,
        'Algebra',
        'We square a number by writing a little number _ next to it',
        '2',
        'Writing a small 2 next to a number says that we need to times it by itself - think of it as there are two of that number in the sum.'			
    ),
    (
        20,
        1,
        0,
        'Time',
        '16:00 represents _ PM',
        '4',
        'Remember to count up from 12. We count 13 (1PM)... 14 (2PM)... 15 (3PM)... 16 (4PM)!'
    )
;