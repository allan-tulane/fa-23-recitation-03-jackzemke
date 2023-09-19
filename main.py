"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    if type(x) != type(BinaryNumber(5)) or type(y) != type(BinaryNumber(5)):
        xvec = BinaryNumber(x).binary_vec
        yvec = BinaryNumber(y).binary_vec
    else:
        xvec = x.binary_vec
        yvec = y.binary_vec
        x = x.decimal_val
        y = y.decimal_val
    xvec, yvec = pad(xvec,yvec)
    n = len(xvec)
    # print(n)
    if x <= 1 and y <= 1:
        return BinaryNumber(x*y)
    else:
        x_left, x_right = split_number(xvec)
        y_left, y_right = split_number(yvec)
    # print(xvec)
    # print(yvec)
    # print(y_left.binary_vec,y_right.binary_vec)
    a = bit_shift(_quadratic_multiply(x_left.decimal_val,y_left.decimal_val),n)
    b1 = _quadratic_multiply(x_left.decimal_val,y_right.decimal_val)
    b2 = _quadratic_multiply(x_right.decimal_val,y_left.decimal_val)
    bs = BinaryNumber(b1.decimal_val+b2.decimal_val)
    b = bit_shift(bs,n//2)
    c = _quadratic_multiply(x_right.decimal_val,y_right.decimal_val)
    # print(a)
    return(BinaryNumber(a.decimal_val+b.decimal_val+c.decimal_val))
    # return bit_shift(quadratic_multiply(x_left,x_right), n) + bit_shift((quadratic_multiply(x_left,y_right)) + (quadratic_multiply(x_right*y_left)), n/2) + (quadratic_multiply(x_right, y_right))
    # pass
    ###

print(quadratic_multiply(120,60))
print(quadratic_multiply(10,10))
print(quadratic_multiply(BinaryNumber(10),BinaryNumber(20)))
print(quadratic_multiply(640,234))
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    f(x,y)
    return (time.time() - start)*1000

    

