import sqlite3

#set up db connection
diaryDB = sqlite3.connect("./diary.db")
diaryC = diaryDB.cursor()

diaryC.execute ('DROP TABLE IF EXISTS users')
#Create main table
diaryC.execute('''CREATE TABLE users (
                  username VARCHAR(20) PRIMARY KEY,
                  password VARCHAR(20),
                  name VARCHAR(30),
                  sq1 NUMERIC(1),
                  sq1a VARCHAR(20),
                  sq2 NUMERIC(1),
                  sq2a VARCHAR(20));''')

#Insert test data
diaryC.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('user123', 'P@ssw0rd', 'User Name', 1, 'ans1', 4, 'ans2'))
diaryC.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('user246', 'P@ssw0rd', 'User 2', 1, 'Ans1', 2, 'Ans2'))
diaryC.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('ser123', 'P@sw0rd', 'Uer Name', 3, 'as1', 4, 'an2'))

#Close database to save data.
diaryDB.commit()

