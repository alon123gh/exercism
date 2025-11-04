class School:
    def __init__(self):
        self.student_list = dict()
        self.add_tracker = []
    def add_student(self, name, grade):
        added = False
        if name not in self.student_list:
            self.student_list[name] = grade
            added = True
        self.add_tracker.append(added)



    def roster(self):
        return  [name for name,_  in sorted(self.student_list.items(), key = lambda  item : (item[1], item[0]))]

    def grade(self, grade_number):
        return sorted([student for student, grade in self.student_list.items() if grade == grade_number])

    def added(self):
        return self.add_tracker
