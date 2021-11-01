import sqlite3
# use panadas to import excel data into python
import pandas as pd

#  1. make a new database named "nolaps.db"
conn = sqlite3.connect('nolaps.db')
print("Opened database successfully");


c = conn.cursor()
df = pd.read_excel('AD of Data Engineering Task1-2.xlsx')
# print(df)

# 2. create a new table in the nolaps.db named "NewTable" and use the colum headers in excel (row 1) as your column names
c.execute("""CREATE TABLE IF NOT EXISTS NewTable (
              one_app_id INT PRIMARY KEY      NOT NULL,
               active INT     NOT NULL,
               current_grade TEXT,
               school TEXT,
               future_school_grade  TEXT,
               future_school TEXT,
              new_match INT    NOT NULL
            )""")
print("Table created successfully")

# 3. Using Python and sqlite3 library INSERT the data from Data Set 1 tab
# transfers the data into the appropriate table in the database.
df.to_sql('NewTable', conn, if_exists='replace', index = False)

# 4. Write a SELECT where all of the data in the NewTable is selected but it is ordered by the column named one_app_id
def get_schools_by_one_app_id() :
    c.execute("SELECT * FROM NewTable ORDER BY one_app_id")
    return c.fetchall()
conn.commit()

# read the data with read_sql query
p = pd.read_sql("SELECT * FROM NewTable ORDER BY one_app_id", conn)
print(p)
# get_schools_by_one_app_id()
# print(get_schools_by_one_app_id())




# General Questions
# 1. How many students are assigned to each school for next year?
def students_assigned_new_school(arg) :
    c.execute("SELECT * FROM NewTable WhERE future_school = ?", (arg,))
    return len(c.fetchall())
    # data = c.fetchall()

# 2. How many students are in each grade currently?
def get_student_grade(arg) :
    c.execute("SELECT * FROM NewTable WHERE current_grade = ?", (arg,))
    return len(c.fetchall())
    # data = c.fetchall()

# 3. How many students are going to a new school next year?
def student_new_school_count(arg) :
    c.execute("SELECT * FROM NewTable WHERE new_match = ?", (arg,))
    data = len(c.fetchall())
    return data

# 4. What school is getting the most new students?
def most_new_students() :
   c.execute("SELECT new_match, future_school AS MOST_FREQUENT FROM NewTable GROUP BY new_match ORDER BY COUNT(future_school) DESC")
   return c.fetchall()


# print(student_new_school_count())

# print(get_student_grade("NULL"))
# print(get_student_grade(1))
# print(get_student_grade(8))
# print(get_student_grade("INF"))
# print(get_student_grade("K"))
# print(get_student_grade("PK3"))
# print(get_student_grade("PK4"))


# print(most_new_students())
# print(student_new_school_count(1))



# print(students_assigned_new_school("Akili Academy of New Orleans"))
# print(students_assigned_new_school("Andrew H. Wilson Charter School"))
# print(students_assigned_new_school("Audubon Charter School French"))
# print(students_assigned_new_school("Audubon Gentilly"))
# print(students_assigned_new_school("Audubon Gentilly Tuition"))
# print(students_assigned_new_school("Benjamin Franklin Elementary Mathematics and Science School"))
# print(students_assigned_new_school("Booker T. Washington High School (KIPP)"))
# print(students_assigned_new_school("Bricolage Academy"))
# print(students_assigned_new_school("CA: G.W. Carver High School"))
# print(students_assigned_new_school("CA: Livingston Collegiate Academy"))
# print(students_assigned_new_school("CA: Rosenwald Collegiate Academy"))
# print(students_assigned_new_school("Carrollton-Dunbar Head Start (Head Start)"))
# print(students_assigned_new_school("Delores Taylor Arthur School for Young Men"))
# print(students_assigned_new_school("Dr. Martin Luther King Jr. Charter School"))
# print(students_assigned_new_school("Dr. Peter Dangerfield Head Start (Head Start)"))
# print(students_assigned_new_school("Dwight D. Eisenhower Academy of Global Studies"))
# print(students_assigned_new_school("Edna Karr High School"))
# print(students_assigned_new_school("Educare (Head Start)"))
# print(students_assigned_new_school("Edward Hynes Charter School - Lakeview Campus"))
# print(students_assigned_new_school("Einstein Charter Middle School at Sarah Towles Reed"))
# print(students_assigned_new_school("Eleanor McMain Secondary School"))
# print(students_assigned_new_school("Encore Academy"))
# print(students_assigned_new_school("Esperanza Charter School"))
# print(students_assigned_new_school("FirstLine Schools: Arthur Ashe Charter School"))
# print(students_assigned_new_school("FirstLine Schools: Langston Hughes Academy"))
# print(students_assigned_new_school("FirstLine Schools: Live Oak Charter School"))
# print(students_assigned_new_school("FirstLine Schools: Phillis Wheatley Community School"))
# print(students_assigned_new_school("Foundation Preparatory Charter"))
# print(students_assigned_new_school("Frederick A. Douglass High School (KIPP Renaissance)"))
# print(students_assigned_new_school("Good Shepherd Nativity Mission School"))
# print(students_assigned_new_school("Harriet Tubman Charter School"))
# print(students_assigned_new_school("Homer A. Plessy Community School"))
# print(students_assigned_new_school("IDEA Oscar Dunn"))
# print(students_assigned_new_school("International High School of New Orleans"))
# print(students_assigned_new_school("International School of Louisiana: Dixon Campus (French)"))
# print(students_assigned_new_school("International School of Louisiana: Dixon Campus (Spanish)"))
# print(students_assigned_new_school("James M. Singleton Charter School"))
# print(students_assigned_new_school("John F. Kennedy High School (KIPP)"))
# print(students_assigned_new_school("KIPP Believe"))
# print(students_assigned_new_school("KIPP Central City"))
# print(students_assigned_new_school("KIPP East"))
# print(students_assigned_new_school("KIPP Leadership"))
# print(students_assigned_new_school("KIPP Morial"))
# print(students_assigned_new_school("Kingsley House Incorporated (Preschool and School Age Daycare) (Head Start)"))
# print(students_assigned_new_school("L. B. Landry - O. Perry Walker College and Career Preparatory High School"))
# print(students_assigned_new_school("Lafayette Academy Charter School"))
# print(students_assigned_new_school("Lawrence D. Crocker College Prep: A School for the Arts and Technology"))
# print(students_assigned_new_school("Living School"))
# print(students_assigned_new_school("Lycee Francais de la Nouvelle-Orleans (LFNO)"))
# print(students_assigned_new_school("Lycee Francais de la Nouvelle-Orleans (LFNO) Tuition"))
# print(students_assigned_new_school("Martin Behrman Charter School Academy of Creative Arts and Sciences"))
# print(students_assigned_new_school("Mary McLeod Bethune Elementary Charter School"))
# print(students_assigned_new_school("McDonogh #35 Senior High School"))
# print(students_assigned_new_school("McDonogh #42 Elementary Charter School"))
# print(students_assigned_new_school("Morris Jeff Community School"))
# print(students_assigned_new_school("New Harmony High"))
# print(students_assigned_new_school("New Orleans Charter Science and Math High School (Sci High)"))
# print(students_assigned_new_school("New Orleans Military and Maritime Academy"))
# print(students_assigned_new_school("Paul Habans Charter School"))
# print(students_assigned_new_school("Pearlie H. Elloie Head Start Center (TCA Head Start)"))
# print(students_assigned_new_school("Pierre A. Capdau @ Avery Alexander Charter School"))
# print(students_assigned_new_school("ReNEW Dolores T. Aaron Academy"))
# print(students_assigned_new_school("Resurrection of Our Lord School"))
# print(students_assigned_new_school("Robert Russa Moton Charter School"))
# print(students_assigned_new_school("Sophie B. Wright High School"))
# print(students_assigned_new_school("St. Joan of Arc School"))
# print(students_assigned_new_school("St. Leo the Great"))
# print(students_assigned_new_school("St. Paul the Apostle (Head Start)"))
# print(students_assigned_new_school("St. Rita School"))
# print(students_assigned_new_school("Success at Thurgood Marshall"))
# print(students_assigned_new_school("TCA Head Start at Mahalia Jackson (Head Start)"))
# print(students_assigned_new_school("Élan Academy"))

"Akili Academy of New Orleans"	# 1
"Andrew H. Wilson Charter School"	# 2
"Audubon Charter School French"	# 3
"Audubon Gentilly"	# 1
"Audubon Gentilly Tuition"	# 1
"Benjamin Franklin Elementary Mathematics and Science School"	# 3
"Booker T. Washington High School KIPP)"	# 2
"Bricolage Academy"	# 7
"CA: G.W. Carver High School"	# 2
"CA: Livingston Collegiate Academy"	# 3
"CA: Rosenwald Collegiate Academy"	# 1
"Carrollton-Dunbar Head Start Head Start)"	# 1
"Delores Taylor Arthur School for Young Men"	# 1
"Dr. Martin Luther King Jr. Charter School"	# 7
"Dr. Peter Dangerfield Head Start Head Start)"	# 2
"Dwight D. Eisenhower Academy of Global Studies"	# 3
"Edna Karr High School"	# 4
"Educare Head Start)"	# 1
"Edward Hynes Charter School - Lakeview Campus"	# 1
"Einstein Charter Middle School at Sarah Towles Reed"	# 0
"Eleanor McMain Secondary School"	# 1
"Encore Academy"	# 1
"Esperanza Charter School"	# 3
"FirstLine Schools: Arthur Ashe Charter School"	# 3
"FirstLine Schools: Langston Hughes Academy"	# 1
"FirstLine Schools: Live Oak Charter School"	# 2
"FirstLine Schools: Phillis Wheatley Community School"	# 5
"Foundation Preparatory Charter"	# 1
"Frederick A. Douglass High School KIPP Renaissance)"	# 1
"Good Shepherd Nativity Mission School"	# 2
"Harriet Tubman Charter School"	# 5
"Homer A. Plessy Community School"	# 2
"IDEA Oscar Dunn"	# 1
"International High School of New Orleans"	# 1
"International School of Louisiana: Dixon Campus French)"	# 4
"International School of Louisiana: Dixon Campus Spanish)"	# 2
"James M. Singleton Charter School"	# 4
"John F. Kennedy High School KIPP)"	# 1
"KIPP Believe"	# 1
"KIPP Central City"	# 2
"KIPP East"	# 4
"KIPP Leadership"	# 7
"KIPP Morial"	# 1
"Kingsley House Incorporated Preschool and School Age Daycare) Head Start)"	# 2
"L. B. Landry - O. Perry Walker College and Career Preparatory High School"	# 1
"Lafayette Academy Charter School"	# 2
"Lawrence D. Crocker College Prep: A School for the Arts and Technology"	# 1
"Living School"	# 1
"Lycee Francais de la Nouvelle-Orleans LFNO)"	# 9
"Lycee Francais de la Nouvelle-Orleans LFNO) Tuition"	# 1
"Martin Behrman Charter School Academy of Creative Arts and Sciences"	# 6
"Mary McLeod Bethune Elementary Charter School"	# 2
"McDonogh #35 Senior High School"	# 2
"McDonogh #42 Elementary Charter School"	# 2
"Morris Jeff Community School"	# 11
"New Harmony High"	# 1
"New Orleans Charter Science and Math High School Sci High)"	# 3
"New Orleans Military and Maritime Academy"	# 5
"Paul Habans Charter School"	# 5
"Pearlie H. Elloie Head Start Center TCA Head Start)"	# 1
"Pierre A. Capdau @ Avery Alexander Charter School"	# 1
"ReNEW Dolores T. Aaron Academy"	# 2
"Resurrection of Our Lord School"	# 2
"Robert Russa Moton Charter School"	# 1
"Sophie B. Wright High School"	# 1
"St. Joan of Arc School"	# 1
"St. Leo the Great"	# 1
"St. Paul the Apostle Head Start)"	# 1
"St. Rita School"	# 2
"Success at Thurgood Marshall"	# 2
"TCA Head Start at Mahalia Jackson Head Start)"	# 1
"Élan Academy"	# 4


conn.close()




