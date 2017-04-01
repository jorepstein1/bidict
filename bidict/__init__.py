from collections import UserDict


class BiDict(UserDict):

    class DuplicateValueError(Exception):
        """Raised when an entry is added with a value that has previously been added"""

    def __init__(self):
        self.data_fw = {}  # dictionary containing dict["key"] = value
        self.data_rv = {}  # dictionary containing dict["value"] = key

    def __len__(self):
        return len(self.data_fw)

    def __getitem__(self, key):
        if key in self.data_fw:
            return self.data_fw[key]
        raise KeyError(key)

    def get_key(self, value):
        if value in self.data_rv:
            return self.data_rv[value]
        raise KeyError(value)

    def __setitem__(self, key, value):
        if value in self.data_rv:
            raise self.DuplicateValueError("Entry has already been added with this value")

        if key in self.data_fw:
            current_value = self.data_fw[key]
            del self.data_rv[current_value]

        self.data_fw[key] = value
        self.data_rv[value] = key

    def __delitem__(self, key):
        value = self.data_fw[key]
        del self.data_rv[value]
        del self.data_fw[key]

    def __iter__(self):
        return iter(self.data_fw)

    def __contains__(self, key):
        return key in self.data_fw

    def __repr__(self):
        return "{0}\n{1}".format(repr(self.data_fw), repr(self.data_rv))
