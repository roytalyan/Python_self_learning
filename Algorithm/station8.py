# coding:utf-8

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
states_needed = set()
for i in stations.values():
    for j in i:
        if j not in states_needed:
            states_needed.add(j)


final_station = set()


while states_needed:
    best_station = None
    states_covered = set()

    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

        states_needed -= states_covered
        # final_station.add(best_station) if best_station is not None else final_station
        if best_station is not None:
            final_station.add(best_station)

print final_station
