import os.system


def clear():
    """Clears a terminal (May not work on devices without certain permissions)"""
    system("cls || clear")


class StateDict(object):
    """Class to create dictionaries that can be stored on disk in the `{file}.statedict` format\n
    Data Type: `StateDict(f_name)` \n
        `f_name`: File name to write | `string` | default = "Data"

    See Wiki for more details.
    """

    def __init__(self, f_name="Data"):
        self.f_name = f"{f_name}.statedict"
        self.start()

    def start(self):
        """Do not run this function. \n
        It only serves to be called in the `StateDict.__init__()` function."""
        try:
            self.f = open(self.f_name, "r+")
            self.data = eval(self.f.read())
        except:
            self.f = open(self.f_name, "w")
            self.reset_file()
            self.start()

    def unpack(self, whole=True, start=0, end=0):
        """Function to return data from a `StateDict` as a `dictionary`
        `whole`: When `True`, returns the whole `StateDict`
        `start`: First number in a range of keypairs to return
        `end`: Last number in a range of keypairs to return"""
        self.read()
        if not whole:
            data_list = list(self.data)
            unpacked_dict = {}
            for x in range(start, end+1):
                unpacked_dict[data_list[x]] = self.data[data_list[x]]
            return unpacked_dict
        else:
            return self.data

    def exit(self):
        """Function to close a `StateDict` after using it."""
        self.f.close()

    def append_data(self, key, value, write=True):
        """Function to append new data to a `StateDict`
        `key`: Key to append to the `StateDict`
        `value`: Value to append to the `StateDict`
        `write`: When `False`, does not append data to the `StateDict`, but to a temporary dictionary"""
        self.data[key] = value
        self.reset_file(True, False)
        if write:
            self.f.write(str(self.data))
        self.refresh_file()

    def append_dict(self, dict, write=True, overwrite=False):
        """Function to append entire dictionaries to a `StateDict`
        `dict`: A dictionary to append to the `StateDict`
        `write`: When `True`, appends data to the `StateDict`,
                          When `False`, only appends data to temporary dictionary
        `overwrite`: When `True`, completely overwrites current data in the `StateDict`"""
        if overwrite:
            for key, value in dict.items():
                self.data[key] = value
        self.reset_file(True, False)
        if write:
            if overwrite:
                self.f.write(str(dict))
            else:
                self.f.write(str(self.data))
        self.refresh_file()

    def reset_file(self, erase=False, backup=True):
        """Function to completely reset a `StateDict`
        `erase`: When `True`, prevents the `StateDict` from being reset with `{}` as the data
        `backup`: When `True`, backs up the `StateDict` to a file in the `{file_name}.statedict.bak` format"""
        self.refresh_file()
        if self.f.read(1) and backup:
            with open(f"{self.f_name}.bak", "w") as bak:
                bak.write(self.f.read())
                bak.close()
        self.f.truncate(0)
        self.f.seek(0)
        if not erase:
            self.f.write("{}")

    def refresh_file(self):
        """Function to open and close a `StateDict`"""
        self.f.close()
        self.f = open(f"{self.f_name}", "r+")

    def read(self):
        """Function to read the `StateDict`"""
        self.refresh_file()
        self.data = eval(self.f.read())
        return self.f.read()
