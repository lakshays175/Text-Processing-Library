from abc import ABC,abstractmethod

class WordFrequencyAnalyzer(ABC):
    def __init__(self) -> None:
        pass
            
    @abstractmethod
    def calculate_highest_frequency(self,text):
        raise NotImplementedError
    
    @abstractmethod
    def calculate_most_frequent_n_words(self,text,n):
        raise NotImplementedError
    
    @abstractmethod
    def calculate_frequency_for_word(self,text,word):
        raise NotImplementedError