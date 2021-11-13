import main
import unittest


class TestMain(unittest.TestCase):

    def test_jimmy_false(self):

        self.assertEqual(main.is_unique(string_input="jimmy"), False)

    def test_abc_true(self):

        self.assertEqual(main.is_unique(string_input="abc"), True)

    def test_abc_true(self):

        self.assertEqual(main.is_unique(string_input="abc"), True)


    def test_Ff_true(self):

        self.assertEqual(main.is_unique(string_input="Ff"),True)

    def test_ff_false(self):

        self.assertEqual(main.is_unique(string_input="ff"),False)
