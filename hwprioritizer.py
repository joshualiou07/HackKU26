class Prioritizer:
    def __init__(self):
        self.assignments = []

 #Ranked by point system based on difficulty and due date
    def add(self, days, difficulty):
        hw = Assignments(days, difficulty)
        self.assignments.append(hw)

    def sort(self):

    def remove(self, index):
        if index >= 0 and index < len(self.assignments):
            self.assignments.pop