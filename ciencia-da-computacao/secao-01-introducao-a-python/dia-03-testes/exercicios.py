
import re

# ======================================================
# FUNCAO FIZZBUZZ

def fizzBuzz(num):
    array = []
    fizzBuzz_number = ''
    for i in range(num):
      array.append(i + 1)

    if num % 3 == 0 and num % 5 == 0:
       fizzBuzz_number = 'FizzBuzz'
  
    elif num % 3 == 0:
       fizzBuzz_number = 'Fizz'

    elif num % 5 == 0:
       fizzBuzz_number = 'Buzz'
      
    else:
       fizzBuzz_number = num
    
    array[-1] = fizzBuzz_number
    return array

# fizzBuzz()

# ======================================================
# FUNCAO REPLACE LETTERS

def replace_letters(text):
    ABC = re.sub(r'A|B|C', '2', text.upper())
    DEF = re.sub(r'D|E|F', '3', ABC)
    GHI = re.sub(r'G|H|I', '4', DEF)
    JKL = re.sub(r'J|K|L', '5', GHI)
    MNO = re.sub(r'M|N|O', '6', JKL)
    PQRS = re.sub(r'P|Q|R|S', '7', MNO)
    TUV = re.sub(r'T|U|V', '8', PQRS)
    return(re.sub(r'W|X|Y|Z', '9', TUV))

# replace_letters()