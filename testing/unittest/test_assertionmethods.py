'''
different assertionmethods in testing
'''
import unittest


class ShowAssert(unittest.TestCase):

    def test_assertion(self):
        a = 2
        b = a
        c = 1. + 1.
        self.assertEqual([1, 2, 3], [1, 2, 3])  # fails if a != b
        self.assertNotEqual("hello", "bye")  # Fails if a == b
        self.assertTrue("hello" == "hello")  # Fails if bool(x) == False
        self.assertFalse("hello" == "bye")  # Fails if bool(x) == False
        self.assertIsNot(a, c)  # fails if a == b
        self.assertIsNone(None)  # fails if x is not None
        self.assertIsNotNone(2)  # fails if x is None
        self.assertIn(2, [2, 3, 4])  # fails if a is not in b
        self.assertNotIn(1, [2, 3, 4])  # fails if a is in b

        # fails is isinstance(a, b) is False
        self.assertIsInstance("hello", str)
        # fails is isinstance(a, b) is True
        self.assertNotIsInstance("1", int)

if __name__ == "__main__":
    unittest.main()
