from abc import ABC,abstractmethod

class WordFrequencyAnalyzer(ABC):
    """
    Defines three methods using Formal Interface

    Method
    calculate_highest_frequency(text) 
    calculate_most_frequent_n_words(text,n)
    calculate_frequency_for_word(text,word)

    """
    def __init__(self) -> None:
        pass
            
    @abstractmethod
    def calculate_highest_frequency(self,text):
        pass
    
    @abstractmethod
    def calculate_most_frequent_n_words(self,text,n):
        pass
    
    @abstractmethod
    def calculate_frequency_for_word(self,text,word):
        pass