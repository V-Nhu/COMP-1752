
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

# Problem 2
    @staticmethod
    def get_count():
        return PartTimeStudent.count  

s1 = PartTimeStudent("Alice", "Computer Science", "PT001", 10, 20)
s2 = PartTimeStudent("Bob", "Math", "PT002", 5, 15)

print(f"Total Part-Time Students: {PartTimeStudent.get_count()}")


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

# Problem 3
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
project1 = Project("AI Research", 5000, lecturer1, [])

school.add_lecturer(lecturer1)
school.add_project(project1)

student1 = FullTimeStudent("Alice", "Computer Science", "F001", project1.name, "AI Enthusiast")
student2 = PartTimeStudent("Bob", "Math", "P001", 5, 15)

school.add_student(student1)
school.add_student(student2)

school.display_students()
school.display_lecturers()
school.display_projects()








