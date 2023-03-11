import re
from InterfaceWordFrequency import WordFrequencyAnalyzer


texts = """
The sun shines over oab the lake
"""

class WordFrequency(WordFrequencyAnalyzer):
    def __init__(self):
        pass

    def calculate_count_of_words(self,text):
        try:
            all_words= re.findall(r'[a-zA-Z]+', text, re.MULTILINE|re.IGNORECASE)
            all_words= [x.lower() for x in all_words]
            all_words= {
                i:all_words.count(i) for i in all_words
            }
            return all_words
        except Exception:
            print("Entered Incorrectly, pls enter text in the parameter")



    # It returns the list with words removing seperators 
    def calculate_highest_frequency(self,text):
        try:
            dict_words = self.calculate_count_of_words(text)
            return max(dict_words.values())
        except Exception:
            print("Entered Incorrectly, enter text in the parameter")

    

    def calculate_most_frequent_n_words(self,text,n):
        try:
            all_words= self.calculate_count_of_words(text)
            output_list = sorted(all_words.items(),key= lambda x:(-x[1], x[0]))[:n]
            return output_list
        except Exception:
            print("Entered Incorrectly, enter text in first parameter and integer in the second parameter")

    
    def calculate_frequency_for_word(self,text, word):
        try:
            all_words= self.calculate_count_of_words(text)
            return all_words.get(word.lower())
        except Exception:
            print("Entered Incorrectly, enter text in first parameter and single word in the second parameter")

    
    
if __name__ == '__main__':

    obj= WordFrequency()
    obj.calculate_most_frequent_n_words(texts,2)
    obj.calculate_highest_frequency(texts)
    obj.calculate_frequency_for_word(texts,'the')

    obj.calculate_most_frequent_n_words(texts,'r')
    obj.calculate_highest_frequency('')
    obj.calculate_frequency_for_word(texts,3)
       

