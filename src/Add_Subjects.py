import sqlite3
from sys_env import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

data = [
    ('GH141', 'English I', '', '', '', 3, 'Engineering', 'General', ''),
    ('GH142', 'English II', 'GH141', '', '', 3, 'Engineering', 'General', ''),
    ('GH150', 'Arabic I', '', '', '', 1, 'Engineering', 'General', ''),
    ('GH151', 'Arabic II', 'GH150', '', '', 1, 'Engineering', 'General', ''),
    ('GH152', 'Technical Writing in Arabic', 'GH151', '', '', 1, 'Engineering', 'General', ''),
    ('GS101', 'Mathematics I', '', '', '', 3, 'Engineering', 'General', ''),
    ('GS102', 'Mathematics II', 'GS101', '', '', 3, 'Engineering', 'General', ''),
    ('GS111', 'Physics I', '', '', '', 3, 'Engineering', 'General', ''),
    ('GS112', 'Physics II', 'GS111', '', '', 3, 'Engineering', 'General', ''),
    ('GS112L', 'Physics Lab', 'GS111', '', '', 1, 'Engineering', 'General', ''),
    ('GS115', 'Chemistry', '', '', '', 3, 'Engineering', 'General', ''),
    ('GS115L', 'Chemistry Lab', '', '', '', 1, 'Engineering', 'General', ''),
    ('GS200', 'Computer Programming', '', '', '', 3, 'Engineering', 'General', ''),
    ('GS203', 'Mathematics III', 'GS102', '', '', 3, 'Engineering', 'General', ''),
    ('GS204', 'Mathematics IV', '', '', '', 3, 'Engineering', 'General', ''),
    ('GS206', 'Probability & Statistics', '', '', '', 3, 'Engineering', 'General', ''),
    ('GE121', 'Engineering Mechanics I', '', '', '', 3, 'Engineering', 'General', ''),
    ('GE125', 'Engineering Graphics', '', '', '', 3, 'Engineering', 'General', ''),
    ('GE127', 'Engineering Drawing', '', '', '', 3, 'Engineering', 'General', ''),
    ('GE129', 'Workshop Technology', '', '', '', 1, 'Engineering', 'General', ''),
    ('GE129L', 'Workshop Technology Lab', '', '', '', 1, 'Engineering', 'General', ''),
    ('GE133', 'Properties of Materials', 'GS101 GS111 GS115', '', '', 3, 'Engineering', 'General', ''),
    ('GE222', 'Engineering Mechanics II', 'GE121', '', '', 3, 'Engineering', 'General', ''),
    ('EE280', 'Electrical Eng Fundamentals', 'GS101 GS112', '', '', 3, 'Engineering', 'General', '')
]

# Insert data into the table
cursor.executemany('''
    INSERT INTO subjects (code, title, preq, coreq, description, cr, faculty, dept, branch)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', data)

courses = [
    ('GS200', 'Computer Programming (C & Mat Lab)', 'GS102', 'GS203', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE200', 'Fundamental of Electrical Engineering', 'GS102 GS112', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE201', 'Electrical Laboratory', 'EE200', 'EE202', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE202', 'Electric Networks', 'GS112 EE200', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE219', 'Basic Electronic Circuits', 'EE200', 'EE202', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE234', 'Introduction to Digital Systems', 'GS102', 'GS200', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE280', 'Fundamental of Electrical Engineering', 'GS102 GS112', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE302', 'Signals and Systems', 'GS204 EE202', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE303', 'Numerical Methods with Mat Lab Applications', 'GS200 GS203 GS204', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE304', 'Measurements & Instrumentation', 'EE200 EE219 EE234', 'EE319', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE311', 'Electronics Laboratory', 'EE201 EE219 EE319', '', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE313', 'Electromagnetic I', 'GS203 GS204 EE200', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE316', 'Communication Engineering I', 'GS204 EE302', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE319', 'Analog Electronic Circuits', 'EE202 EE219', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE331N', 'Digital Laboratory', 'EE201 EE234', 'EE334', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE334', 'Introduction to Microprocessor', 'EE234 GS200', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE342', 'Electrical Power Engineering I', 'EE202', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE352', 'Electrical Machines I', 'EE202', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE362', 'Control Systems', 'EE302', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE413', 'Electromagnetic II', 'EE313', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE416', 'Communication Engineering II', 'GS206 EE316', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE419', 'Digital Electronic Circuits', 'EE319', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE421', 'Communication & Electronics Lab. I', 'EE304 EE311 EE331N EE316', 'EE413 EE419', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE423', 'Active Networks', 'EE302 EE319', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE429', 'Semiconductor Electronics', 'EE319', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE432', 'Data Structures', 'EE334', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE433', 'Operating Systems', 'EE334', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE434', 'Computer Architecture', 'EE334', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE442', 'Electrical Power Engineering II', 'EE342', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE443', 'Power Plants', 'EE342 EE352 ME210', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE445', 'Power Distribution Systems', 'EE342', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE446', 'High Voltage Engineering I', 'EE342 EE352', 'EE452', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE448', 'Power Electronics I', 'EE219 EE342', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE449', 'Power Systems Analysis', 'EE352', 'EE442', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE451', 'Electrical Power Lab. I', 'EE304 EE311 EE331N', 'EE448 EE452', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE452', 'Electrical Machines II', 'EE352', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE461', 'Control & Computer Lab. I', 'EE304 EE311 EE331N EE362', 'EE434', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE462', 'Digital Control Systems', 'EE362', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE463', 'Data Acquisition & Conversion Systems', 'EE334 EE362', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE491', 'Computer Applications & Design Lab.', 'EE421 or EE451 or EE461', '', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE513', 'Electromagnetic III', 'EE413', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE516', 'Communication Systems I', 'EE416', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE519', 'Semiconductor Devices', 'EE429', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE521', 'Communication & Electronics Lab. II', 'EE421 EE416 EE419', 'EE513', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE524', 'Data Communication & Networking', 'EE416', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE526', 'Communication Systems II', 'EE416', 'EE516', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE532', 'Computer Networks', 'EE303 EE434', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE535', 'Micro Controllers', 'EE434 EE462', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE542', 'Electrical Power Engineering III', 'EE442', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE548', 'Power Electronics II', 'EE448', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE551', 'Electrical Power Lab. II', 'EE451 EE448 EE449', 'EE552', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE552', 'Electrical Machines III', 'EE452', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE561', 'Control & Computer Lab. II', 'EE461 EE462 EE463', 'EE535 EE563', '', 2, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE562', 'Modeling & Simulation', 'EE303 EE462', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE563', 'Control Systems Design', 'EE303 EE462', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', ''),
    ('EE599', 'B. Sc. Project', 'EE491 Minimum_128_credits', '', '', 3, 'Engineering', 'Electric and Electronics Engineering', '')
]

cursor.executemany('''
    INSERT INTO subjects (code, title, preq, coreq, description, cr, faculty, dept, branch)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', courses)



conn.commit()
conn.close()
