class Garden:
    STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    PLANT = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.split()
        self.students = sorted(students)
    def plants(self, student):
        index = self.students.index(student) * 2
        index_plants = self.diagram[0][index:index+2] + self.diagram[1][index:index+2]
        return [self.PLANT[i] for i in index_plants]