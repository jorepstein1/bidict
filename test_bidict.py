import unittest
from bidict import BiDict


class TestBiDictOne(unittest.TestCase):

    def test_basics(self):
        my_bidict = BiDict()
        my_bidict['one'] = 1

        self.assertTrue('one' in my_bidict)
        self.assertEqual(my_bidict['one'], 1)
        self.assertTrue('one' in my_bidict.get_key(1))
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
            self.assertTrue(key in my_bidict.get_key(my_bidict_value))

    def test_duplicate_value(self):
        my_bidict = BiDict()

        my_bidict['key'] = 1
        my_bidict['key'] = 2
        self.assertEqual(my_bidict['key'], 2)

        my_bidict['key'] = 'key'
        self.assertTrue(my_bidict['key'] in my_bidict.get_key('key'))

        for i in range(10):
            key = 'key' + str(i)
            my_bidict[key] = 1

        keys = my_bidict.get_key(1)
        for i in range(10):
            key = 'key' + str(i)
            self.assertTrue(key in keys)

        key = 'key1'
        del my_bidict[key]
        keys = my_bidict.get_key(1)
        self.assertFalse(key in keys)

    def test_initialize_with_values(self):
        real_dict = {'one': 1, 'two': 2}
        my_bidict = BiDict(real_dict)

        self.assertEquals(my_bidict['one'], 1)
        self.assertTrue('two' in my_bidict.get_key(2))

        my_bidict = BiDict(one=1)
        self.assertEquals(my_bidict['one'], 1)

    def test_equals(self):
        real_dict = {'one': 1, 'two': 2}
        my_bidict = BiDict()
        my_bidict['one'] = 1
        my_bidict['two'] = 2

        self.assertEquals(my_bidict, real_dict)

        my_bidict = BiDict(real_dict)
        self.assertEquals(my_bidict, real_dict)

        my_bidict = BiDict()
        my_bidict.update(real_dict)
        self.assertEquals(my_bidict, real_dict)

if __name__ == '__main__':
    unittest.main()
