#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value='') -> None:
    self.value = value

  @property
  def value(self):
    """the value property"""
    return self._value
  
  @value.setter
  def value(self,value):
    """checks if value is a string"""
    if isinstance(value, str):
      self._value = value
      
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    #split the sentence to a list of sentences
    split_sentence = re.split(r'[.!?]', self.value)
    print(split_sentence)
    count = 0  #initialize sentence count

    for sentence in split_sentence:
      #check for empty strings and trailing white spaces
      if sentence.strip():
        count += 1  #increment count by 1

    return count
  
  


sentence = MyString("I am a software engineer. It is fun to code! would you like to try?")
# result = sentence.is_sentence()
# print(result)
result2 = sentence.count_sentences()
print(result2)

