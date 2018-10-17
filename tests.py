from code import readCsv


def test_readCsv():
    r1 = 'tests.csv'
    assert readCsv(r1) == ['h1', 'h2', 'h3', '1', '2', '3', 'a', 'b', 'c', 'i', 'ii', 'iii']


test_readCsv()
