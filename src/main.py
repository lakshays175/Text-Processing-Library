import re
from InterfaceWordFrequencyAnalyzer import WordFrequencyAnalyzer
from InterfacewordFrequency import InterfaceWordfrequency
from typing import Optional

texts = """
The sun shines over oab the lake
"""


class WordProcessing(WordFrequencyAnalyzer):
   
    t=Optional[str]
    w=Optional[str]
    ns=Optional[int]

    def __init__(self,text=t,word=w,n=ns):
        self.text = text
        self.word = word
        self.n=n

    @property
    def word(self):
        return self.word
    
    @word.setter
    def word(self,value):
        self._word = value
    
    @property
    def frequency(self):
        return self.n

    def calculate_count_of_words(self,text):
        try:
            all_words = re.findall(
                r'[a-zA-Z]+', text, re.MULTILINE | re.IGNORECASE)
            all_words = [x.lower() for x in all_words]
            all_words = {
                i: all_words.count(i) for i in all_words
            }
            return all_words
        except TypeError:
            print("Invalid Type, Enter text in the parameter")

    # It returns the list with words removing seperators
    def calculate_highest_frequency(self,text):
        try:
            dict_words = self.calculate_count_of_words(text)
            return max(dict_words.values())
        except TypeError:
            print("Invalid Type, Enter text in the parameter")

    def calculate_most_frequent_n_words(self,text,n) -> list[InterfaceWordfrequency]:
        try:
            all_words = self.calculate_count_of_words(text)
            output_list = sorted(
                all_words.items(), key=lambda x: (-x[1], x[0]))[:n]
            return output_list
        except TypeError:
            print("Invalid Type, Enter text in the parameter")

    def calculate_frequency_for_word(self,text,word):
        try:
            all_words = self.calculate_count_of_words(text)
            return all_words.get(word.lower())
        except TypeError:
            print("Invalid Type, Enter text in the parameter")


if __name__ == '__main__':

    obj = WordProcessing()
    r= obj.calculate_count_of_words("Sun")
    #r= obj.calculate_frequency_for_word("Sun Shines",'Sun')
    #r= obj.calculate_highest_frequency("Sun Shines Shines")
    #r= obj.calculate_most_frequent_n_words("Sun Shines lake",2)

    print(r)
    print(type(r))

