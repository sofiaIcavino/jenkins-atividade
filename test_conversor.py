from conversor import fahrenheit_para_celsius, celsius_para_fahrenheit

def test_fahr_para_celsius_freezing():
    assert fahrenheit_para_celsius(32) == 0.0

def test_fahr_para_celsius_boiling():
    assert fahrenheit_para_celsius(212) == 100.0

def test_celsius_para_fahr_freezing():
    assert celsius_para_fahrenheit(0) == 32.0

def test_celsius_para_fahr_boiling():
    assert celsius_para_fahrenheit(100) == 212.0
