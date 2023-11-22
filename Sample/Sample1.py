import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
print("testing brach")
print("testing brach1")
print("testing brach3")




print("testing brach4")
print("testing brach5")
print("testing brach6")