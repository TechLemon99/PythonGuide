-- SQLite
SELECT Enrolment.StudentID, Student.FirstName, Student.Surname, Student.Grade, Enrolment.SubjectID, Subject.SubjectName
FROM Enrolment
JOIN Student ON Enrolment.StudentID = Student.StudentID
JOIN Subject ON Enrolment.SubjectID = Subject.SubjectID