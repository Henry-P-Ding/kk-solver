import unittest

from kk_solver import Agent


class ModernPSET(unittest.TestCase):
    def test_problem_1(self):
        print("-------Problem 1--------")
        statements = [
            lambda A, B: A.says(A.xor(B)),
            lambda A, B: B.says(A.xor(B))
        ]

        for A in Agent.generate_possible_agents():
            for B in Agent.generate_possible_agents():
                correct_identities = all(map(lambda statement: statement(A, B), statements))
                print(f"A: {A}, B: {B} is {correct_identities}" + ("  !" if correct_identities else ""))

    def test_problem_2(self):
        print("-------Problem 2--------")
        statements = [
            lambda A, B: A.says(A.or_(B)),
        ]

        for A in Agent.generate_possible_agents():
            for B in Agent.generate_possible_agents():
                correct_identities = all(map(lambda statement: statement(A, B), statements))
                print(f"A: {A}, B: {B} is {correct_identities}" + ("  !" if correct_identities else ""))

    def test_problem_3(self):
        print("-------Problem 3--------")
        statements = [
            lambda A, B: A.says(A.or_(B)),
        ]

        for A in Agent.generate_possible_agents():
            for B in Agent.generate_possible_agents():
                correct_identities = all(map(lambda statement: statement(A, B), statements))
                print(f"A: {A}, B: {B} is {correct_identities}" + ("  !" if correct_identities else ""))

if __name__ == '__main__':
    unittest.main()
