import pandas as pd
import mysql.connector as c
import winsound

winsound.Beep(1000, 300)

db = c.connect(host='localhost', user='root', password='Chakkalayil7$23', database='school',auth_plugin='mysql_native_password')
if db.is_connected():
    print('successfully connected')


def menu():
    print("**************************************************************************************************")
    print("**************************************************************************************************")
    print('{:^100s}'.format("SCHOOL MANAGEMENT"))
    print("**************************************************************************************************")
    print("**************************************************************************************************\n")
    print('{:^100s}'.format("STUDENT MANAGEMENT"))
    print("**************************************************************************************************")
    print('{:^100s}'.format("MENU"))
    print('{:^100s}'.format("1.About"))
    print('{:^100s}'.format("2.Show All Tables From Database"))
    print('{:^100s}'.format("3.Create table student_detail"))
    print('{:^100s}'.format("4.Describe table student_detail"))
    print('{:^100s}'.format("5.Show all records from student_detail"))
    print('{:^100s}'.format("6.Show records from top"))
    print('{:^100s}'.format("7.Show records from bottom"))
    print('{:^100s}'.format("8.Show 5 records from top"))
    print('{:^100s}'.format("9.Show 5 records from bottom"))
    print('{:^100s}'.format("10.Add in table table student "))
    print('{:^100s}'.format("11.Delete from table student "))
    print('{:^100s}'.format("12.Update from table student "))
    print("**************************************************************************************************")
    print("**************************************************************************************************\n")
    print('{:^100s}'.format("EXAM MANAGEMENT"))
    print("**************************************************************************************************")
    print()
    print('{:^100s}'.format("13.Create table marks"))
    print('{:^100s}'.format("14.Show table marks"))
    print('{:^100s}'.format("15.Add in table marks"))
    print('{:^100s}'.format("16.delete from marks"))
    print('{:^100s}'.format("17.Update from marks"))
    print('{:^100s}'.format("18.Search by roll no"))
    print('{:^100s}'.format("19.Marks less than"))
    print('{:^100s}'.format("20.Highest marks in English"))
    print('{:^100s}'.format("21.Order by subject marks"))
    print('{:^100s}'.format("22.Total marks of every student"))
    print('{:^100s}'.format("23.Average marks of every student\n"))
    print("**************************************************************************************************")
    print("**************************************************************************************************")


menu()


def about():
    print('School Management Systems Plays an essential role in the current educational system.\n'
          'School authorities all over the world are engaged in a lot of day-to-day administrative\n'
          'Activities to manage and provide a better administrative experience to students effectively.\n'
          'However, maintaining and keeping track of school administrative activities is not an easy process\n'
          'In the fast-growing world. It requires hard work and often it is time-consuming.\n'
          'To better perform the school administrative activities of educational institutions,\n'
          'School Management systems are used nowadays. Such applications often offer many features that help\n'
          'To enhance the performance of schools with minimum efforts. School Management software does it by\n'
          'Avoiding the manual paper works and automation of many academic and administrative activities.\n')


def show_tables():
    print("Show names of tables in the current database")
    mc = db.cursor()
    mc.execute("Show Tables")
    for x in mc:
        print(x)


def create_student_detail():
    mc = db.cursor()
    mc.execute("create table student_detail"
               "(admno varchar(10) PRIMARY KEY,"
               "name varchar(30),"
               "fathers_name varchar(30),"
               "mobile int(12),"
               "address varchar(50));")
    print("Table Created")


def desc_student_detail():
    print("Show table structure")
    df = pd.read_sql("desc student_detail", db)
    print(df)


def show_recordsstudent_detail():
    print("All records of student_detail")
    df = pd.read_sql("select * from student_detail", db)
    print(df)


def anynofromtop():
    print("All records")
    df = pd.read_sql("select *from student_detail", db)
    print(df)
    df = pd.read_sql("select *from student_detail", db)
    r = int(input("Enter no of rows from top"))
    print(df.head(r))


def anynofrombottom():
    print("All records")
    df = pd.read_sql("select * from student_detail", db)
    print(df)
    df = pd.read_sql("select * from student_detail", db)
    r = int(input("Enter no of rows from bottom"))
    print(df.tail(r))


def fivefromtop():
    print("Top 5 records")
    df = pd.read_sql("select * from student_detail", db)
    print(df.head())


def fivefrombottom():
    print("Last 5 records")
    df = pd.read_sql("select * from student_detail", db)
    print(df.tail())


def add_student_detail():
    print("Before any changes in table")
    df = pd.read_sql("select * from student_detail", db)
    print(df)
    print("New Entries")
    mc = db.cursor()
    mc.execute("insert into student_detail values(10,'Sanjay Kumar','Rajendra Kumar',867987655,'M_67 Sanjay Nagar');")
    print("Done")
    db.commit()
    df = pd.read_sql("select * from student_detail", db)
    print(df)
    print("Record Inserted")


def del_student_detail():
    print("Before any changes in table")
    df = pd.read_sql("select * from student_detail", db)
    print(df)
    print()
    print()
    mc = db.cursor()
    mc.execute("delete from student_detail where admno='10'")
    print("Record Deleted")
    db.commit()


def update_student_detail():
    print("Before any changes in table")
    df = pd.read_sql("select * from student_detail", db)
    print(df)
    print()
    print()
    mc = db.cursor()
    mc.execute("update student_detail set mobile= 843524567 where name='Anika Kaur'")
    print("Record Updated")
    db.commit()
    df = pd.read_sql("select * from student_detail", db)
    print(df)


def create_marks():
    mc = db.cursor()
    mc.execute("create table marks"
               "(admno varchar(10),"
               "roll int(5) PRIMARY KEY,"
               "name varchar(30),"
               "english int(5),"
               "ip int(5),"
               "chemistry int(5),"
               "physics int(5),"
               "biology int(5));")
    print("Table Created")


def desc_marks():
    print("Show table structure")
    df = pd.read_sql("desc marks", db)
    print(df)


def show_recordsmarks():
    print("All records of marks")
    df = pd.read_sql("select * from marks", db)
    print(df)


def add_marks():
    print("Before any changes")
    df = pd.read_sql("select * from marks", db)
    print(df)
    print("New Entries")
    mc = db.cursor()
    mc.execute("insert into marks values(11,11,'Sanjay Kumar',70,80,90,100,90);")
    print("Done")
    db.commit()
    df = pd.read_sql("select * from marks", db)
    print(df)
    print("Record Inserted")


def show_marks():
    print("Show marks of all students")
    df = pd.read_sql("select * from marks", db)
    print(df)


def delete_record():
    print("Before any changes in table")
    df = pd.read_sql("select * from marks", db)
    print(df)
    print()
    print()
    mc = db.cursor()
    mc.execute("Delete from marks where admno='1'")
    print("Record deleted")
    df = pd.read_sql("select * from marks", db)
    print(df)
    db.commit()


def update_marks():
    print("Before any changes in table")
    df = pd.read_sql("select * from marks", db)
    print(df)
    print()
    print()
    mc = db.cursor()
    mc.execute("update marks set ip=100 where roll=6")
    print("Record Updated")
    db.commit()
    df = pd.read_sql("select * from marks", db)
    print(df)


def search_byrollno():
    print("Search student record by entering roll no")
    a = float(input("Enter roll no:"))
    qry = "select * from marks where roll=%s;" % (a,)
    df = pd.read_sql(qry, db)
    print(df)


def marks_less_than():
    print("Show details of student with less marks")
    m1 = float(input("Enter marks in english:"))
    qry = "select * from marks where roll<%s;" % (m1,)
    df = pd.read_sql(qry, db)
    print(df)


def subject_max():
    df = pd.read_sql("select admno,roll,name,english,ip,chemistry,physics,biology from marks", db)
    print(df)
    print("To find highest marks in subject")
    qry = "select max(english) from marks"
    df = pd.read_sql(qry, db)
    print(df)


def orderby_subject():
    df = pd.read_sql("select roll,name,english,ip,chemistry,physics,biology from marks", db)
    print(df)
    print("Ascending order marks of english")
    mc = db.cursor()
    mc.execute("select english from marks order by english")
    print("Done")
    for x in mc:
        print(x)


def totalmarks():
    print("Total marks of each student")
    df = pd.read_sql("select roll,name,english,ip,chemistry,physics,biology from marks", db)
    print(df)
    print()
    df['total'] = df['english'] + df['ip'] + df['physics'] + df['chemistry'] + df['biology']
    print(df)


def avgmarks():
    print("Average marks of each student")
    df = pd.read_sql("select roll,name,english,ip,chemistry,physics,biology from marks", db)
    print()
    print()
    df['total'] = df['english'] + df['physics'] + df['chemistry'] + df['biology'] + df['ip']
    df['avg'] = df['total'] / 6
    print(df)


opt = ""
opt = int(input("Enter your choice:"))
if opt == 1:
    about()
if opt == 2:
    show_tables()
elif opt == 3:
    create_student_detail()
elif opt == 4:
    desc_student_detail()
elif opt == 5:
    show_recordsstudent_detail()
elif opt == 6:
    anynofromtop()
elif opt == 7:
    anynofrombottom()
elif opt == 8:
    fivefromtop()
elif opt == 9:
    fivefrombottom()
elif opt == 10:
    add_student_detail()
elif opt == 11:
    del_student_detail()
elif opt == 12:
    update_student_detail()
elif opt == 13:
    create_marks()
elif opt == 14:
    show_recordsmarks()
elif opt == 15:
    add_marks()
elif opt == 16:
    delete_record()
elif opt == 17:
    update_marks()
elif opt == 18:
    search_byrollno()
elif opt == 19:
    marks_less_than()
elif opt == 20:
    subject_max()
elif opt == 21:
    orderby_subject()
elif opt == 22:
    totalmarks()
elif opt == 23:
    avgmarks()
else:
    print("invalid option")

winsound.PlaySound("SystemExit", winsound.SND_ALIAS 
