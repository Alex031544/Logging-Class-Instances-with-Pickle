# Logging Class Instances with Pickle

Storing data in Python using dataclasses is a very comfortable way then handling different datasets.

Pickle is an easy tool to store data. But in case of class objects it is required to ship the class declarations
with the data. This can be done on several ways:

1. as code within the writing and reading code
2. separately in a py file holding the definitions

Both methods require to have the writing and reading code aligned. In case of changing class declarations
the risc of loosing alignment between data and code arises. The problem on using pickle is, that it stores
the binaries, but not the class declaration. Due to that, while unpacking the data it can happen, that the
object can not be restored because of not fitting or lost declarations.

Therefore, it seems to be reasonable to store the class declaration into the pickle file as well. But it
seems, that the class objects also store the relative path of the class definition it based on.

## How To

### Data Writer

1. Write Class Declarations to a separate py file (here *generate_log/logdef.py*).
2. Read the file and execute its content to have the declarations within the local scope.
3. Dump the file content as first into the log file.
4. Dump class objects into the log file.

### Data Reader

1. Read the log file and execute the first string to have the declarations within the local scope.
2. Extract all following class objects until the end of log file.
3. Ship object and declarations together

## References

- https://docs.python.org/3/library/pickle.html
- https://stackoverflow.com/questions/45535284/exec-and-variable-scope
- https://stackoverflow.com/questions/6726183/pickle-class-instance-plus-definition
- https://pythonexamples.org/python-pickle-class-object/#2
