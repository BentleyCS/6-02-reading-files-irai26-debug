import CSP_6_02_reading_files as HW
def test_to_string():
    assert not(HW.toString("ExampleText.txt")=="Here is the text\ni am another line")
def test_longest_line():
    assert HW.longestLine("ExampleText.txt") == "Name\n"
def test_to_Binary():
    assert True