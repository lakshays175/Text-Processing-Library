import pytest
from src.main import WordProcessing

class WF(WordProcessing):
    """
    We used class member which is a object, 
    if not created, create a new object else return the obj which already existing
    """
    
    wf = None
    def __init__(self) -> None:
        if WF.wf is None:
            """
            We added this to call the super class first
            """
            WF.wf = super().__init__()
            
        return WF.wf

@pytest.fixture(scope="module")
def wf():
    """
    We added thi fixture to be used in the test cases to initilize a new object
    """
    return WF()

 #positive test case   
@pytest.mark.parametrize(
        "input, output",
        [
            ["Sun",1],
            ["Sun shines shines daily",2],
           # ["Sun shines shines shines daily",3]
        ]
)
def test_calculate_highest_frequency(input,output,wf):
    assert wf.calculate_highest_frequency(input) == output

 #negative test case   
@pytest.mark.parametrize(
        "input, output",
        [
            ["Sun shines daily",0],
            ["Sun shines shines daily",'this'],
            ["Sun shines shines shines daily",2.4]
        ]
)
def test_calculate_highest_frequency(input,output,wf):
    try:
        assert wf.calculate_highest_frequency(input) != output
    except TypeError:
        pass

#positive test case
@pytest.mark.parametrize(
        "input_text,input_n, output_list",
        [
            ["Sun shines shines over the lake",1,[('shines',2)]],
            ["""Sun shines shines over the lake over lake""",3,[('lake',2),('over',2),('shines',2)]],
            ["""Sun shines shines over the lake over lake""",4,[('lake',2),('over',2),('shines',2),('sun',1)]],
        ]
)
def test_calculate_most_frequent_n_words(input_text,input_n, output_list,wf):
        assert wf.calculate_most_frequent_n_words(input_text,input_n) == output_list

#negative test case
@pytest.mark.parametrize(
        "input_text,input_n, output_list",
        [
            ["Sun shines shines over the lake",1,[('shines',3)]],
            ["""Sun shines shines over the lake over lake""",3,[('lake',3),('over',2),('shines',2)]],
            ["""Sun shines shines over the lake over lake""",4,[('over',2),('shines',2),('sun',1)]],
        ]
)
def test_calculate_most_frequent_n_words(input_text,input_n, output_list,wf):
    try:
        assert wf.calculate_most_frequent_n_words(input_text,input_n) != output_list
    except TypeError:
        pass


#positive test case
@pytest.mark.parametrize(
        "input_text,input_word, output",
        [
            ["Sun shines shines over the lake",'shines',2],
            ["Sun shines shines over the lake",'over',1],
            ["Sun shines shines over the lake",'lake',1],
        ]
)
def test_calculate_frequency_for_word(input_text,input_word, output,wf):
        assert wf.calculate_frequency_for_word(input_text,input_word) == output


#negative test case
@pytest.mark.parametrize(
        "input_text,input_word, output",
        [
            ["Sun shines shines over the lake",'shines',1],
            ["Sun shines shines over the lake",'over','r'],
            ["Sun shines shines over the lake",'lake',5],
        ]
)
def test_calculate_frequency_for_word(input_text,input_word, output,wf):
    try:
        assert wf.calculate_frequency_for_word(input_text,input_word) != output
    except TypeError:
        pass


#negative test case
@pytest.mark.parametrize(
        "input_text, output",
        [
            ["sun",{"sun" : 1}]

        ]
)
def test_calculate_count_of_words(input_text,output,wf):
        assert wf.calculate_count_of_words(input_text) == output
 