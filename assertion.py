def plus_positive_number(a, b):
    assert a > 0, 'Number A must be possitive'
    assert b > 0, 'Number B must be positive'
    return a + b

print(plus_positive_number(5, -8))