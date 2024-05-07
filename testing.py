from base import Student, Group, Teacher, Subject, Grade, session
from sqlalchemy import select



if __name__ == '__main__':
    student = select(Student)
    result = session.execute(student)
    print(result.all())