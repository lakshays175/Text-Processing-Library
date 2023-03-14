
# Text Processing Library

Process of Automating the creation or manipulation of elctronic text. 


## Installation

### development

I Used Python as a primary tools for development. 
See [requirements.txt](requirement.txt) for dependency packages. 
Basically to reproduce environment you need to run `pip install -r requirements.txt`



## Implementation

In src folder,we provide the [main.py](../Word-Processing-Library/src/main.py) script, which is a class implments interfaces. 

### interfaces

#### WordFrequency

Contains the definition of two methods, word and frequency. 

```py
    def word(self):
        pass

    def frequency(self):
        pass
```

#### WordFrequencyAnalyzer

Contains the definition of three methods. 
 ```py
    def calculate_highest_frequency(self,text):
        pass
    
    def calculate_most_frequent_n_words(self,text,n):
        pass
    
    def calculate_frequency_for_word(self,text,word):
        pass
```
More information can be found in [Documentaton](./Docs/_build/html/index.html)

### class

It is used to implments interfaces with the methods inside it. 

To Test various methods, object should be created for the following class and then methods can be called providing required parameters. 

For example, Calling method calculate_highest_frequency
```py
    if __name__ == '__main__':

    obj = WordProcessing()
    r= obj.calculate_highest_frequency("Sun Shines Shines")

    print(r)
    print(type(r))

```

More information can be found in the [Documentaton](./Docs/_build/html/index.html)


## Running Tests

To run tests, run the below command. 

```py
   pytest .\test\test_wordfrequency.py 
```
pytest is used for testing, which need to be installed.

### Testcases

Testcases are added in the [testwordfrequency.py](../Word-Processing-Library/test/test_wordfrequency.py) script.

## Documentation

Documentation is contained in [Documentaton](./Docs/_build/html/index.html)

