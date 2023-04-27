from exercicios import fizzBuzz, replace_letters


# ======================================================
# FUNCAO FIZZBUZZ
def test_fizz():
    assert fizzBuzz(3) == [1, 2, 'Fizz']

def test_buzz():
    assert fizzBuzz(5) == [1, 2, 3, 4, 'Buzz']
  

def test_fizz_buzz():
    assert fizzBuzz(15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'FizzBuzz']

def test_fizz_buzz_none():
    assert fizzBuzz(7) == [1, 2, 3, 4, 5, 6, 7]

# ======================================================
# FUNCAO REPLACE LETTERS

def test_abc():
    assert replace_letters('abc') == '222'

def test_def():
    assert replace_letters('def') == '333'

def test_ghi():
    assert replace_letters('ghi') == '444'

def test_jkl():
    assert replace_letters('jkl') == '555'

def test_mno():
    assert replace_letters('mno') == '666'

def test_pqrs():
    assert replace_letters('pqrs') == '7777'

def test_tuv():
    assert replace_letters('tuv') == '888'

def test_wxyz():
    assert replace_letters('wxyz') == '9999'

def test_letters():
    assert replace_letters('pamonha gamming') == '7266642 4266464'