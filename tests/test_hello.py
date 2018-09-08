"""
    author: Josh Peak
    description: Hello Greeting Unit test
"""
from greeting import hello

# TODO: Investigate this further https://hypothesis.readthedocs.io/en/latest/
# It uses property based testing which could be useful


class TestGreeting():

    def test_greeting_failure(self):
        assert hello.greeting("Diana Prince") != "Hello Batman"

    def test_greeting_success(self):
        assert hello.greeting("Diana Prince") == "Hello Diana Prince"
