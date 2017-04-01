import unittest
from bidict import BiDict


class TestBiDictOne(unittest.TestCase):

    def test_basics(self):
        my_bidict = BiDict()
        my_bidict['one'] = 1

        self.assertTrue('one' in my_bidict)
        self.assertEqual(my_bidict['one'], 1)
        self.assertEqual(my_bidict.get_key(1), 'one')
        self.assertEqual(len(my_bidict), 1)

        del my_bidict['one']

        self.assertEqual(len(my_bidict), 0)

        real_dict = {}
        for i in range(10):
            key = 'key' + str(i)
            my_bidict[key] = i
            real_dict[key] = i

        for key in my_bidict:
            my_bidict_value = my_bidict[key]
            self.assertEqual(my_bidict_value, real_dict[key])
            self.assertEqual(my_bidict.get_key(my_bidict_value), key)

    def test_duplicate_value(self):
        my_bidict = BiDict()
        my_bidict['key1'] = 1

        my_bidict['key1'] = 2
        self.assertEqual(my_bidict['key1'], 2)

        my_bidict['key1'] = 'key1'
        self.assertEqual(my_bidict['key1'], my_bidict.get_key('key1'))

        my_bidict['key1'] = 1
        with self.assertRaises(BiDict.DuplicateValueError):
            my_bidict['key2'] = 1

if __name__ == '__main__':
    unittest.main()
