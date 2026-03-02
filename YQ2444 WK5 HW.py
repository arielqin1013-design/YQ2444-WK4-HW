def mysum(a,b):
    c = a+b
    return(c)

mysum(7,8)

a = 5

import numpy as np
np.arange(1, 8)
np.full(10,2)

def square_all(x, y):
    return x**3,y**3

square_all(2,3)


def WhoAmI():
    return('yq2444')


WhoAmI()

import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    t = np.arange(1, n + 1)
    coupon = face * couponRate / ppy
    cf = np.full(n, coupon) #cash flow
    cf[-1] += face
    df = (1 + r) ** (-t) #discount factor
    price = float(np.sum(cf * df))
    return(price)


getBondPrice(0.03, 2000000, 0.04, 10)

getBondPrice(0.03, 2000000, 0.04, 10, 1)

getBondPrice(0.03, 2000000, 0.04, 10, 2)

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    t = np.arange(1, n + 1)
    coupon = face * couponRate / ppy
    cf = np.full(n, coupon) #cash flow
    cf[-1] += face
    df = (1 + r) ** (-t) #discount factor
    pv = cf * df
    price = np.sum(pv)
    duration_periods = np.sum(t * pv) / price
    duration_years = float(duration_periods  / ppy)
    return(duration_years)


getBondDuration(0.03, 200000, 0.04, 10)

getBondDuration(0.03, 200000, 0.04, 10, 1)

getBondDuration(0.03, 200000, 0.04, 10, 2)

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    conditions = [
        (numvec % 15 == 0),
        (numvec % 3 == 0),
        (numvec % 5 == 0)
    ]
    choices = ["fizzbuzz", "fizz", "buzz"]
    result = np.select(conditions, choices, default = numvec.astype(str))
    result = result.tolist()
    return(result)


print(FizzBuzz(46, 60))

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype = object)
    objvec = np.array([
        'fizzbuzz' if (x % 3 == 0 and x % 5 == 0) else
        'fizz' if x % 3 == 0 else
        'buzz' if x % 5 == 0 else
        str(x)
        for x in objvec
    ], dtype = object)
    return(objvec)

print(FizzBuzz(46, 60))

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype = object)
    fizz_mask = (objvec % 3 == 0)
    buzz_mask = (objvec % 5 == 0)
    fizzbuzz_mask = fizz_mask & buzz_mask

    objvec = np.where(fizzbuzz_mask, 'fizzbuzz', objvec)
    objvec = np.where(~fizzbuzz_mask & fizz_mask, 'fizz', objvec)
    objvec = np.where(~fizzbuzz_mask & buzz_mask, 'buzz', objvec)
    objvec = np.where(~(fizz_mask | buzz_mask), objvec.astype(str), objvec)
    objvec = objvec.tolist()
    return(objvec)

FizzBuzz(46, 60)



