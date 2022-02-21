import unittest

import api


class TestAPI(unittest.TestCase):
    def test_gc_content(self):
        self.assertEqual(api.gc_content("CC"), 1)
        self.assertEqual(api.gc_content("CG"), 1)
        self.assertEqual(api.gc_content("GC"), 1)
        self.assertEqual(api.gc_content("GG"), 1)
        self.assertEqual(api.gc_content("GAG"), 2 / 3)
        self.assertEqual(api.gc_content("GAAG"), 2 / 4)
        self.assertEqual(api.gc_content("GATTG"), 2 / 5)
        self.assertEqual(api.gc_content("AGTCTCATTCG"), 5 / 11)

    def test_melting_temperature(self):
        self.assertEqual(api.melting_temperature(""), 0)
        self.assertEqual(api.melting_temperature("A"), 2)
        self.assertEqual(api.melting_temperature("T"), 2)
        self.assertEqual(api.melting_temperature("C"), 4)
        self.assertEqual(api.melting_temperature("G"), 4)
        self.assertEqual(api.melting_temperature("AT"), 4)
        self.assertEqual(api.melting_temperature("CG"), 8)
        self.assertEqual(api.melting_temperature("AC"), 6)
        self.assertEqual(api.melting_temperature("TG"), 6)
        self.assertEqual(api.melting_temperature("ATCG"), 12)
        self.assertEqual(api.melting_temperature("AATTCCGG"), 24)

    def test_valid_primer(self):
        self.assertEqual(api.valid_primer("AAAAAAAAAAAAAAAAAAAA"), False)
        self.assertEqual(api.valid_primer("TTTTTTTTTTTTTTTTTTTT"), False)
        self.assertEqual(api.valid_primer("CCCCCCCCCCCCCCCCCCCC"), False)
        self.assertEqual(api.valid_primer("GGGGGGGGGGGGGGGGGGGG"), False)
        self.assertEqual(api.valid_primer("CGTGGTACGATTAGAGACAC"), True)
        self.assertEqual(api.valid_primer("CAGCCTCCCTTATAGTAGTG"), True)

    def valid_primers_pair(self):
        self.assertEqual(api.valid_primers_pair("A", "T"), True)
        self.assertEqual(api.valid_primers_pair("C", "G"), True)
        self.assertEqual(api.valid_primers_pair("A", "C"), True)
        self.assertEqual(api.valid_primers_pair("AAA", "TTT"), True)
        self.assertEqual(api.valid_primers_pair("CCC", "GGG"), True)
        self.assertEqual(api.valid_primers_pair("AAA", "CCC"), False)
        self.assertEqual(api.valid_primers_pair("TTTT", "GGGG"), False)
        self.assertEqual(api.valid_primers_pair("ATATAATATATA", "CGCGCGCG"), False)


if __name__ == '__main__':
    unittest.main()
