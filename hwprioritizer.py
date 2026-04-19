class Prioritizer:
    def __init__(self):
        self.assignments = []

 #Ranked by point system based on difficulty and due date
    def add(self, days, difficulty):
        hw = Assignments(days, difficulty)
        self.assignments.append(hw)

    def sort(self):
        sorted_list = []
        copy = self.assignments[:]

        while len(copy) > 0:
            top_index = 0
            highest_score = copy[0].score()

            for i in range(1, len(copy)):
                if copy[i].score() > highest_score:
                    highest_score = copy[i].score()
                    top_index = i

            sorted_list.append(copy[top_index])
            copy.pop(top_index)
        
        self.assignments = sorted_list

    def remove(self, index):
        if index >= 0 and index < len(self.assignments):
            self.assignments.pop