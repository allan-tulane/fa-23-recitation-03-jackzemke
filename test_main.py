from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(80), BinaryNumber(3)) == 80*3
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(13)) == 13*1
    assert quadratic_multiply(BinaryNumber(16), BinaryNumber(12)) == 16*12

