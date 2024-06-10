from building import *
import numpy as np

x = np.random.randint(0, 100)
y = np.random.randint(0, 100)

print(f'x = {x}, y = {y}')

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(10,5) == 2

print ('All tests pass!')

print ('Testing done')
