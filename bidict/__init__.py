from collections import UserDict


class BiDict(UserDict):
    """BiDict is a bi-directional dictionary class.
        It extends collections.UserDict - a wrapper class 
    designed to make subclassing the built-in dict class easier.
        BiDict works with same functionality as dict.
    """

    def __init__(self, *args, **kwargs):
        """Initialization based on UserDict initialization.
        Supports initializing an empty BiDict or initializing with given key:value pairs"""
        self.data_fw = {}  # dictionary containing dict["key"] = value
        self.data_rv = {}  # dictionary containing dict["value"] = key

        if len(args) > 1:
            raise TypeError('expected at most 1 argument, got {0}'.format(len(args)))
        if args:
            initial_dict = args[0]
            self.update(initial_dict)
        if len(kwargs):
            self.update(kwargs)

    def __len__(self):
        return len(self.data_fw)

    def __setitem__(self, key, value):
        if key in self.data_fw:
            del self[key]

        self.data_fw[key] = value

        if value in self.data_rv:
            self.data_rv[value].append(key)
        else:
            self.data_rv[value] = [key]

    def __getitem__(self, key):
        if key in self.data_fw:
            return self.data_fw[key]
        raise KeyError(key)

    def get_key(self, value):
        """Returns a list of keys with value. Raises ValueKeyError if value is not in instance"""
        if value in self.data_rv:
            return self.data_rv[value]
        raise self.ValueKeyError(value)

    def __delitem__(self, key):
        """Deletes entry from instance."""
        value = self.data_fw[key]
        keys_with_value = self.data_rv[value]
        keys_with_value.remove(key)
        if len(keys_with_value) == 0:
            del self.data_rv[value]

        del self.data_fw[key]

    def __iter__(self):
        return iter(self.data_fw)

    def iter_values(self):
        return iter(self.data_rv)

    def __contains__(self, key):
        return key in self.data_fw

    def contains_value(self, value):
        return value in self.data_rv

    def __repr__(self):
        return "{0}:\n{1}".format(repr(type(self)), repr(self.data_fw))

    class ValueKeyError(KeyError):
        """Raise when a value cannot be found during an attempt
            to retrieve key from value """
