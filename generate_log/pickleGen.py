import pickle

# Import the class declarations here only to be able to code with them.
# The declarations will be hidden later by the exec statement.
from logdef import *


if __name__ == '__main__':
    filename = '../AI_pickle_object.dat'

    # The file content will be read as string
    with open('logdef.py', 'r') as f:
        defs = f.read()

    # and then executed / applied - now the class objects created from them refer
    # to the declaration in this scope
    exec(defs, globals())

    # write (pickle) some data to a pickle file
    with open(filename, 'wb') as f:
        # at first write the class declarations
        pickle.dump(defs, f)

        # then write objects based on these definitions
        for n in range(5):
            if (n % 1) == 1:
                data = MyClass()
            else:
                data = MyClass2()
            pickle.dump(data, f)

        data = MyClass3()
        pickle.dump(data, f)
