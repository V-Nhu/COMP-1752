
class Student:
    def __init__(self, name: str, major: str, student_id: str):
        self.name = name
        self.major = major
        self.student_id = student_id


class FullTimeStudent(Student):
    def __init__(self, name: str, major: str, student_id: str, joined_project: str, research_profile: str):
        super().__init__(name, major, student_id)
        self.joined_project = joined_project
        self.research_profile = research_profile


class PartTimeStudent(Student):
    count = 0  

    def __init__(self, name: str, major: str, student_id: str, min_hour: int, max_hour: int):
        super().__init__(name, major, student_id)
        self.min_hour = min_hour
        self.max_hour = max_hour
        PartTimeStudent.count += 1  

    @staticmethod
    def get_count():
        return PartTimeStudent.count  



class Lecturer:
    def __init__(self, lecturer_id: str, name: str, rank: str, project_led: str, research_profile: str):
        self.lecturer_id = lecturer_id
        self.name = name
        self.rank = rank
        self.project_led = project_led
        self.research_profile = research_profile


class Project:
    def __init__(self, name: str, budget: float, leader: Lecturer, members: list):
        self.name = name
        self.budget = budget
        self.leader = leader
        self.members = members


class SchoolSystem:
    def __init__(self):
        self.students = []  
        self.lecturers = []  
        self.projects = []  

    def add_student(self, student: Student):
        if len(self.students) < 10:
            self.students.append(student)
            return True
        return False  

    def add_lecturer(self, lecturer: Lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
            return True
        return False  

    def add_project(self, project: Project):
        if len(self.projects) < 10:
            self.projects.append(project)
            return True
        return False  

    def display_students(self):
        print("Students List:")
        for student in self.students:
            print(student.name)

    def display_lecturers(self):
        print("Lecturers List:")
        for lecturer in self.lecturers:
            print(lecturer.name)

    def display_projects(self):
        print("Projects List:")
        for project in self.projects:
            print(project.name)

school = SchoolSystem()


lecturer1 = Lecturer("L001", "Dr. John", "Professor", "AI Research", "Machine Learning")
lecturer2 = Lecturer("L002", "Dr. Smith", "Associate Professor", "Data Science", "Deep Learning")
lecturer3 = Lecturer("L003", "Dr. Williams", "Assistant Professor", "Cybersecurity", "Network Security")
lecturer4 = Lecturer("L004", "Dr. Brown", "Professor", "Robotics", "AI in Robotics")
lecturer5 = Lecturer("L005", "Dr. Taylor", "Professor", "Blockchain", "Cryptography")
project1 = Project("AI Research", 5000, lecturer1, [])
project2 = Project("Deep Learning", 7000, lecturer2, [])
project3 = Project("Cybersecurity", 6000, lecturer3, [])
project4 = Project("Robotics AI", 8000, lecturer4, [])
project5 = Project("Blockchain Security", 6500, lecturer5, [])


school.add_lecturer(lecturer1)
school.add_lecturer(lecturer2)
school.add_lecturer(lecturer3)
school.add_lecturer(lecturer4)
school.add_lecturer(lecturer5)
school.add_project(project1)
school.add_project(project2)
school.add_project(project3)
school.add_project(project4)
school.add_project(project5)


student1 = FullTimeStudent("Alice", "Computer Science", "F001", project1.name, "AI Enthusiast")
student2 = PartTimeStudent("Bob", "Math", "P001", 5, 15)
student3 = FullTimeStudent("Charlie", "Physics", "F002", project2.name, "Quantum Mechanics")
student4 = PartTimeStudent("David", "Engineering", "P002", 10, 20)
student5 = FullTimeStudent("Eve", "Cybersecurity", "F003", project3.name, "Ethical Hacking")
student6 = PartTimeStudent("Frank", "Robotics", "P003", 8, 18)
student7 = FullTimeStudent("Grace", "Data Science", "F004", project2.name, "Big Data Analysis")
student8 = PartTimeStudent("Hank", "Physics", "P004", 12, 22)
student9 = FullTimeStudent("Ivy", "Computer Science", "F005", project4.name, "AI in Robotics")
student10 = PartTimeStudent("Jack", "Mathematics", "P005", 6, 14)
student11 = FullTimeStudent("Kevin", "Blockchain", "F006", project5.name, "Decentralized Systems")
student12 = PartTimeStudent("Linda", "Cryptography", "P006", 7, 16)


school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.add_student(student4)
school.add_student(student5)
school.add_student(student6)
school.add_student(student7)
school.add_student(student8)
school.add_student(student9)
school.add_student(student10)
school.add_student(student11)
school.add_student(student12)


#Problem 3
school.display_students()
school.display_lecturers()
school.display_projects()


#Problem 2
print(f"Total Part-Time Students: {PartTimeStudent.get_count()}")







