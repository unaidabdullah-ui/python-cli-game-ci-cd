idef test_random_number():
    import random
    num = random.randint(1, 10)
    assert 1 <= num <= 10

