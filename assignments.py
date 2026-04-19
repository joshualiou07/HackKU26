class Assignments:
    def __init__(self, name, due, difficulty):
        self.name = name
        self.due = due
        self.difficulty = difficulty

    def score(self):
        if self.due == 0:
            due_date = 2
        else:
            due_date = 1 / (self.due + 1)
        diff = self.difficulty / 5
        return due_date + diff