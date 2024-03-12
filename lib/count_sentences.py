#!/usr/bin/env python3

import re
class MyString:

    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return True if self._value.endswith(".") else False

    def is_question(self):
        return True if self._value.endswith("?") else False

    def is_exclamation(self):
        return True if self._value.endswith("!") else False

    def count_sentences(self):
      #Using the re.split() to remove the punctuation. re.split() will look for those 'patterns' in quotation and returns
      #remaining characters in the list.
        sentences = [sentence for sentence in re.split('[.!?]', self.value) if sentence]
        return len(sentences)
        
