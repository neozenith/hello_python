"""Hello Greeting Unit test"""
import unittest
from . import hello

class TestGreeting(unittest.TestCase):
    def test_greeting_failure(self):
        self.assertNotEqual(hello.greeting("Diana Prince"), "Hello Batman")

    def test_greeting_success(self):
        self.assertEqual(hello.greeting("Diana Prince"), "Hello Diana Prince")

if __name__ == '__main__':
    unittest.main()
