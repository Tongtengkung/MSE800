import unittest

class TestStringMethods(unittest.TestCase):                                 # test string input 
    def test_upper(self):                                                   # test 'upper all letter'
        self.assertEqual('foo'.upper(), 'FOO')                              # try on 'foo' to 'FOO'

    def test_isupper(self):                                                 # test is upper is correct?
        self.assertTrue('FOO'.isupper())                                    # test 'FOO' and must be correct
        self.assertFalse('foo'.isupper())                                   # test 'Foo' and must be incorrect because 'oo'

    def test_split(self):                                                   # test split word by normal string
        s = 'hello world'                                                   # set s = string 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])                     # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):                                  
            s.split(2)                                                                                  

    def test_isdigit(self):                                                 # test is digit?
        self.assertTrue('123'.isdigit())                                    # test '123' is digit and must be correct   

if __name__ == '__main__':                                                  # running
    unittest.main()
