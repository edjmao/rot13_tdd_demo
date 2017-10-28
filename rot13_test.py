from rot13 import ROT13
import unittest

class ROT13Test(unittest.TestCase):

    def test_defaultconstructor(self):
        rot13obj = ROT13()
        print(rot13obj)

    def test_basicencrypt(self):
        rot13obj = ROT13("AAAA")
        self.assertEqual(
            "NNNN",
            str(rot13obj),
            "Should translate AAAA as NNNN")

    def test_encryptlatterhalfofalphabet(self):
        rot13obj = ROT13("NUNS")
        self.assertEqual(
            "AHAF",
            str(rot13obj),
            "NUNS should translate as AHAF")

    def test_encryptmixedcase(self):
        rot13obj = ROT13("TAcos")
        self.assertEqual(
            "GNpbf",
            str(rot13obj),
            "Lowercase letters should work, too.")

    def test_nonalpha(self):
        rot13obj = ROT13("I love tacos 2!")
        self.assertEqual(
            "V ybir gnpbf 2!",
            str(rot13obj),
            "Non-alpha characters should just pass through.")
        
if __name__=="__main__":
    unittest.main()
