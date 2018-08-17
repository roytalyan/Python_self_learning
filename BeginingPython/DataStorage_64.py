def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def lookup(data, label, name):
    return data[label].get(name)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


myname = {}
init(myname)
print store(myname, 'roy yan')
print lookup(myname, 'first', 'roy')