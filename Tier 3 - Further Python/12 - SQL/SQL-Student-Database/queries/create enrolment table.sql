PRAGMA foreign_keys = ON;

CREATE TABLE Enrolment (
    StudentID INTEGER,
    SubjectID varchar(6),
    PRIMARY KEY (StudentID, SubjectID),
    CONSTRAINT FKStudent
        FOREIGN KEY (StudentID) 
        REFERENCES Student(StudentID),
    CONSTRAINT FKSubject
        FOREIGN KEY (SubjectID)
        REFERENCES Subject(SubjectID)
);