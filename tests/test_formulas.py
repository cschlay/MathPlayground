from unittest import TestCase

from logic.formulas import Formula


class FormulaTest(TestCase):
    def test_and(self):
        f1 = Formula("p", True)
        f2 = Formula("q", True)

    def test_equivalence(self):
        pass

    def test_implies(self):
        pass

    def test_not(self):
        f1 = Formula("p", False).apply_not()
        self.assertTrue(f1.value)
        f2 = f1.apply_not()
        self.assertFalse(f2.value)

    def test_apply_or(self):
        f1 = Formula("p", True)
        f2 = Formula("q", False)
