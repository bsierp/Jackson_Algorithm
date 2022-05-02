

class Task:
    def __init__(self, i, r, p):
        self.i = i  # nr zadania
        self.r = r  # czas dostarczenia zadania
        self.p = p  # czas trwania zadania

    def __eq__(self, other):
        return self.r == other.r

    def __lt__(self, other):
        if self == other:
            return self.p > other.p
        else:
            return self.r < other.r
