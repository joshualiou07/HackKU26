class Assignments:
    def __init__(self, name, due, difficulty):
        self.name = name
        self.name = due
        self.name = difficulty

    def points(self):
        due_date = 1/(self.due + 1)
        diff = self.difficulty/5
        return due_date + diff