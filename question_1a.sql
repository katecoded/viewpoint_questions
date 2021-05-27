-- Author: Katelyn Lindsey
-- Date: 5/26/2021
-- Question 1.a.

SELECT name_table.Name as Name, name_table.StudentID as StudentID FROM name_table
INNER JOIN mark_table ON name_table.StudentID = mark_table.StudentID
WHERE mark_table.Total_marks > (SELECT mark_table.Total_marks FROM mark_table
WHERE mark_table.StudentID = 'V002');