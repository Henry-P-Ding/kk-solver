import unittest

from kkn_solver import Knave, Knight, Normal


class KKNProblems(unittest.TestCase):
    def test_problem_5(self):
        one_of_each = [
            [Knight(), Knave(),  Normal()],
            [Knight(), Normal(), Knave()],
            [Knave(),  Knight(), Normal()],
            [Knave(),  Normal(), Knight()],
            [Normal(), Knight(), Knave()],
            [Normal(), Knave(),  Knight()],
        ]

        statements = [
            lambda A, B, C: A.says(A.is_normal()),
            lambda A, B, C: B.says(A.is_normal()),
            lambda A, B, C: C.says(not C.is_normal()),
        ]

        for A, B, C in one_of_each:
            correct_identities = all(map(lambda statement: statement(A, B, C), statements))
            print(f"A: {A}, B: {B}, C: {C} is {correct_identities}")

    def verify_all_cases(self, agent):
        base_statements = [
            lambda s1, s2 : agent.is_knight(),
            lambda s1, s2 : agent.is_knave(),
            lambda s1, s2 : agent.is_normal(),
            lambda s1, s2 : agent.says(s1),
        ]
        for tt_result in [True, False]:
            for tf_result in [True, False]:
                for ft_result in [True, False]:
                    for ff_result in [False, False]:
                        result_dict = {
                            (True, True):   tt_result,
                            (True, False):  tf_result,
                            (False, True):  ft_result,
                            (False, False): ff_result,
                        }
                        base_statements.append(lambda s1, s2: result_dict[(s1, s2)])

    def test_problem_7(self):
        knight, knave, normal = Knight(), Knave(), Normal()






if __name__ == '__main__':
    unittest.main()
