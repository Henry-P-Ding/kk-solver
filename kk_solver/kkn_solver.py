from enum import Enum


class AgentTypes(Enum):
    KNIGHT = 1
    KNAVE = 2
    NORMAL = 3


class Agent:
    def __init__(self, agent_type):
        self.type = agent_type

    def says(self, statement: bool) -> bool:
        if self.type is AgentTypes.KNIGHT:
            return statement is True
        elif self.type is AgentTypes.KNAVE:
            return statement is False
        elif self.type is AgentTypes.NORMAL:
            return True

        raise ValueError('statement is not a knight, knave, or normal')

    def is_knight(self) -> bool:
        return self.type is AgentTypes.KNIGHT

    def is_knave(self) -> bool:
        return self.type is AgentTypes.KNAVE

    def is_normal(self) -> bool:
        return self.type is AgentTypes.NORMAL

    @staticmethod
    def gen_all_agents():
        return [Knight(), Knave(), Normal()]


class Knight(Agent):
    def __repr__(self):
        return "Knight"

    def __init__(self):
        super().__init__(AgentTypes.KNIGHT)


class Knave(Agent):
    def __repr__(self):
        return "Knave_"

    def __init__(self):
        super().__init__(AgentTypes.KNAVE)


class Normal(Agent):
    def __repr__(self):
        return "Normal"

    def __init__(self):
        super().__init__(AgentTypes.NORMAL)
