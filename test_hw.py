import os
import tempfile
import shutil
import filecmp
import ex5

class Playground():
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.temp_dir = temp_dir.name
        shutil.copytree(self.path, self.temp_dir, dirs_exist_ok=True)
        return temp_dir

    def __exit__(self, *_):
        shutil.rmtree(self.temp_dir)


def test_vigenere_cipher():
    vigenere = ex5.VigenereCipher([3])
    assert vigenere.encrypt("l") == "o"
    vigenere = ex5.VigenereCipher([2, -4, -14, -16, -17, -17])
    assert vigenere.encrypt("we wish you the best of luck in all of your exams") == "ya isbq akg dqn daed xo nqou rw chx yo hqqd ogjoo"
    vigenere = ex5.VigenereCipher([1, 2, 3, 4, -5])
    assert vigenere.encrypt("Hello World!") == "Igopj Xqupy!"

def test_vigenere_from_str():
    vigenere = ex5.getVigenereFromStr("python rules, C drools")
    assert vigenere.encrypt("JK, C is awesome") == "YI, V pg nnydseg"
    assert vigenere.decrypt("YI, V pg nnydseg") == "JK, C is awesome"

def test_process_directory():
    for expected, output in zip(os.listdir("tests/expected"), os.listdir("tests/output")):
        with Playground(os.path.join("tests/output", output)) as pg:
           ex5.processDirectory(pg.name)
           expected = os.path.join("tests/expected", expected)
           files = set(os.listdir(expected) + os.listdir(pg.name))
           for file in files:
                expected_file = os.path.join(expected, file)
                assert os.path.isfile(expected_file), f"your code created an unexpected file: '{expected_file}'" 
                output = os.path.join(pg.name, file)
                assert os.path.isfile(output), f"your code did not create the following file: '{file}'" 
                assert filecmp.cmp(output, expected_file), f"'{expected_file}' and '{output}' do not match"

