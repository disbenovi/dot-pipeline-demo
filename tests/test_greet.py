import unittest

import greet


class GreetTests(unittest.TestCase):
    def test_greet_uses_the_name(self):
        self.assertEqual(greet.greet("Ada"), "Hello, Ada!")

    def test_greet_falls_back_to_world(self):
        self.assertEqual(greet.greet(), "Hello, world!")
        self.assertEqual(greet.greet("   "), "Hello, world!")

    def test_farewell_uses_the_name(self):
        self.assertEqual(greet.farewell("Ada"), "Goodbye, Ada.")


if __name__ == "__main__":
    unittest.main()
