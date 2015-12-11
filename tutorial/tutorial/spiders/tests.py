import unittest
from myhome import MyHomeSpider


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        mhs = MyHomeSpider()

        f = open("/Users/cnicholson/PycharmProjects/Scrapper/scrapper/tutorial/test", "r")
        stuff = f.read()

        result = mhs.parse_brochure(stuff)

        print result



if __name__ == '__main__':
    unittest.main()