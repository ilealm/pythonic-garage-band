import pytest
from  pythonic_garage_band.pythonic_garage_band import Guitarist, Bassist, Drummer, Band 


def test_guitarrist_one(dummy_guitarist):    
    actual = dummy_guitarist.name
    expected = "Carlos Santanna"
    assert actual == expected

def test_guitarrist_two(dummy_guitarist):
    actual = dummy_guitarist.play_solo()
    expected = "Carlos Santanna is playing an amazing Guitar solo!!!"
    assert actual == expected
  
def test_guitarrist_three(dummy_guitarist):
    actual = dummy_guitarist.get_instrument()
    expected = "Guitar"
    assert actual == expected


def test_bassist_one(dummy_bassist):    
    actual = dummy_bassist.name
    expected = "Sabo Romo"
    assert actual == expected

def test_bassist_two(dummy_bassist):
    actual = dummy_bassist.play_solo()
    expected = "Sabo Romo is playing an amazing Bassis solo!!!"
    assert actual == expected
  
def test_bassist_three(dummy_bassist):
    actual = dummy_bassist.get_instrument()
    expected = "Bassis"
    assert actual == expected



def test_drummer_one(dummy_drummer):    
    actual = dummy_drummer.name
    expected = "Alfonso Andre"
    assert actual == expected

def test_drummer_two(dummy_drummer):
    actual = dummy_drummer.play_solo()
    expected = "Alfonso Andre is playing an amazing Drumms solo!!!"
    assert actual == expected
  
def test_drummer_three(dummy_drummer):
    actual = dummy_drummer.get_instrument()
    expected = "Drumms"
    assert actual == expected
    
def test_band_one(dummy_band):
    actual = len(dummy_band.members)
    expected = 3
    assert actual ==  expected

def test_band_two(dummy_band):
    actual = dummy_band.to_list()
    expected = ""
    assert actual !=  expected

@pytest.fixture
def dummy_guitarist():
    return Guitarist("Carlos Santanna")

@pytest.fixture
def dummy_bassist():
    return Bassist("Sabo Romo")

@pytest.fixture
def dummy_drummer():
    return Drummer("Alfonso Andre")

@pytest.fixture
def dummy_band():
    my_band = Band("Caifanes")
    my_band.add_member(Guitarist("Carlos Santanna"))
    my_band.add_member(Bassist("Sabo Romo"))
    my_band.add_member(Drummer("Alfonso Andre"))
    return my_band