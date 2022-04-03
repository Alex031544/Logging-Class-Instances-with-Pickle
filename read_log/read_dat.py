import pickle


def read_dat(filename):
    pkl_objects = list()

    with open(filename, 'rb') as f:

        # first grab the class declarations for later execution
        defs = pickle.load(f)
        exec(defs, globals())

        # load the class object until the end of file
        counter = 0
        while True:
            try:
                data = pickle.load(f)
                if data:
                    pkl_objects.append(data)
                    counter += 1
                    print('%d - %s' % (counter, data.__str__()))
            except pickle.PickleError:
                print('PickleError')
                break
            except EOFError:
                print('EOF')
                break

    # return object and declarations together
    return pkl_objects, defs


if __name__ == '__main__':
    objects, defs = read_dat('AI_pickle_object.dat')
    exec(defs, globals())
    for obj in objects:
        print(obj)
