from unittest import TestCase

from .string_functions import *

class StringTests(TestCase):
    def test_greeting_jeremy(self):
        """Test for greet_by_name"""
        # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

        # Step 2: Decide what the expected outcome is for the scenario
        expected = 'Hello, Jeremy!'

        # Step 3: Call the function being tested to get its actual output
        actual = greet_by_name('Jeremy')

        # Step 4: Compare expected & actual outcomes. If they match, the test 
        # passes
        self.assertEqual(actual, expected)

    def test_greeting_dani(self):
        """Test for greet_by_name"""
        expected = 'Hello, Dani!'
        actual = greet_by_name('Dani')
        self.assertEqual(actual, expected)

    def test_reverse_long(self):
        """Test reversing a long string."""
        expected = 'Testing'
        actual = find_longest_word('I am Testing')
        self.assertEqual(actual, expected)

    def test_reverse_short(self):
        """Test reversing a short string."""
        expected = 'gnitset'
        actual = reverse('testing')
        self.assertEqual(actual, expected)

    def test_reverse_words_long(self):
        """Test reversing words in a long string."""
        expected = 'ten puppies'
        actual = reverse_words('net seippup')
        self.assertEqual(actual, expected)

    def test_reverse_words_short(self):
        """Test reversing words in a short string."""
        expected = 'owt'
        actual = reverse('two')
        self.assertEqual(actual, expected)

    def test_sarcastic_long(self):
        """Test sarcastic-ifying a long string."""
        expected = 'ThE cUp WaS bIg'
        actual = sarcastic('The Cup Was Big')
        self.assertEqual(actual, expected)

    def test_sarcastic_short(self):
        """Test sarcastic-ifying a short string."""
        expected = 'TwO'
        actual = sarcastic('Two')
        self.assertEqual(actual, expected)


    def test_find_longest_word_empty(self):
        expected = ''
        actual = find_longest_word('')
        self.assertEqual(actual, expected)
