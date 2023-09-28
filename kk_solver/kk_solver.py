class Agent:
    def says(self, statement):
        return self.bi(statement)

    def or_(self, other):
        return self or other

    def and_(self, other):
        return self and other

    def neg(self):
        return not self

    def implies(self, other):
        return not (self and not other)

    def bi(self, other):
        return self.implies(other) and other.implies(self)

    def xor(self, other):
        return not (self and other) and (self or other)

    @staticmethod
    def generate_possible_agents():
        return [Knight(), Knave()]

class Knight(Agent):
    def __str__(self):
        return "Knight"

    def __bool__(self):
        return True


class Knave(Agent):
    def __str__(self):
        return "Knave_"

    def __bool__(self):
        return False

# Problem 1
