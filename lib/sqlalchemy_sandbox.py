#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__  = (
        PrimaryKeyConstraint(
            "id",
            name = "id_pk"),
        UniqueConstraint(
            "email", 
            name ="unique_email"),
        CheckConstraint(
            "grade between 1 and 12",
            name = "grade_between_1_and_12")
    )
    Index("index_name", "name")

    id = Column(Integer())
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default= datetime.now())


    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name},  " \
            + f"Grade {self.grade}"


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)


    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)

    # use 'Session' class to create 'session' object
    session = Session()

    albert_einstein = Student(
        name = "Albert Einstein",
        email = "albert.einstein@zurich.edu",
        grade = 6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )

    medrine = Student(
        name = "Medrine Mulindi",
        email = "medrine.mulindi@zurich.edu",
        grade = 10,
        birthday=datetime(
            year=1988,
            month=5,
            day=1
        ),
    )
    session.bulk_save_objects([albert_einstein, medrine])
    session.commit()

    #Deleting Data
    # query = session.query(Student).filter(Student.name=="Albert Einstein")
    # albert_einstein = query.first()
    # session.delete(albert_einstein)
    # session.commit()

    #  # try to retrieve deleted record
    # albert_einstein = query.first()

    # print(albert_einstein)

# => None

#OR

    # query = session.query(
    #     Student).filter(
    #         Student.name == "Albert Einstein")

    # query.delete()

    # albert_einstein = query.first()

    # print(albert_einstein)

# => None

    #Updating Data
    # for student in session.query(Student):
    #     student.grade +=1

    # session.commit()

    # print([(student.name, student.grade) for student in session.query(Student)])

    #Using the update method
    # session.query(Student).update({
    #     Student.grade: Student.grade + 1
    # })

    # print([(
    #     student.name,
    #     student.grade
    # ) for student in session.query(Student)])

    #Filtering
    # query = session.query(Student).filter(Student.name.like("%med%"), Student.grade ==10)
    # for record in query:
    #     print(record.name)

        #func
    # student_count = session.query(func.count(Student.id)).first()
    # for number in student_count:
    #     print(number)


       #limit
    # oldest_student = [student for student in session.query(Student.name, Student.birthday).order_by(desc(Student.birthday)).first()]
    # print(oldest_student)

    #desc
    # students_by_grades_desc = [student for student in session.query(Student.name, Student.grade).order_by(desc(Student.grade))]
    # print(students_by_grades_desc)

    # students_by_name = [ student for student in session.query(Student.name).order_by(Student.name)]
    # print(students_by_name)

    # names = [name for name in session.query(Student.name)]
    # print(names)

    # students = session.query(Student).all()
    # print(students)

    # students = session.query(Student)
    # print([student for student in students])

    # print(f"New student id is {albert_einstein.id}")
    # print(f"New student id is {medrine.id}")

   