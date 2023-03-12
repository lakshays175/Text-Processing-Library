import re
from InterfaceWordFrequencyAnalyzer import WordFrequencyAnalyzer
from InterfacewordFrequency import InterfaceWordfrequency
from typing import Optional


class WordProcessing(WordFrequencyAnalyzer):
    """Text Processing module

    Method
    calculate_count_of_words(text): Accepts Parameter as a string and Returns the dictionary with Key as Word and the Value contains the Count
    
    calculate_highest_frequency(text): Accepts Parameter as a string and returns the highest frequency in the text

    calculate_most_frequent_n_words(text,n): Accepts Two Parameters, one string and one integer and returns a list of the most frequent 'n' words in the input text
    
    calculate_frequency_for_word(text,word): Accepts Two Parameters, both strings and returns the frequency of the specified word
    """
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
        """Returns the dictionary with Key as Word and the Value contains the total Count of the word even if there are duplicates

        Args:
            text (str):  String or multi line string

        Returns:
            dictionary : Key as Word and the Value contains the total Count of the word even if there are duplicates
        """
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
        """ highest frequency in the text

        Args:
            text (str): String or Multi-line String

        Returns:
            int : Highest Frequency number in the text
        """
        try:
            dict_words = self.calculate_count_of_words(text)
            return max(dict_words.values())
        except TypeError:
            print("Invalid Type, Enter text in the parameter")

    def calculate_most_frequent_n_words(self,text,n) -> list[InterfaceWordfrequency]:
        """Returns list of the most frequent 'n' words in the input text

        Args:
            text (str)  : String or Multi-line String
            n (int)     : number up to 

        Returns:
            list[InterfaceWordfrequency]: Returns list of the most frequent 'n' words in the input text
        """
        try:
            all_words = self.calculate_count_of_words(text)
            output_list = sorted(
                all_words.items(), key=lambda x: (-x[1], x[0]))[:n]
            return output_list
        except TypeError:
            print("Invalid Type, Enter text in the parameter")

    def calculate_frequency_for_word(self,text,word):
        """Returns the frequency of the specified word

        Args:
            text (str): string of Multi-line String
            word (str): Single word 

        Returns:
            int: returns the frequency of the specified word
        """
        try:
            all_words = self.calculate_count_of_words(text)
            return all_words.get(word.lower())
        except TypeError:
            print("Invalid Type, Enter text in the parameter")


if __name__ == '__main__':

    obj = WordProcessing()
    #r= obj.calculate_count_of_words("Sun")
    #r= obj.calculate_frequency_for_word("Sun Shines",'Sun')
    #r= obj.calculate_highest_frequency("Sun Shines Shines")
    #r= obj.calculate_most_frequent_n_words("Sun Shines lake",2)

    #print(r)
    #print(type(r))

