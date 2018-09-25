
def datacorrection(datalist, toltime=1e-8):

    newlist = list()

    for example in datalist:
        states = example[0]
        times = example[1]

        # skip this example
        if len(states) < 2:
            continue

        # delete durations < toltime
        tmp = [row for row in zip(states, times) if row[1] >= toltime]

        # skip this example
        if len(tmp) < 2:
            continue

        # merge consecutive states that are the same
        tmp2 = list()
        s = tmp[0][0]
        t = tmp[0][1]
        for i in range(1, len(tmp)):
            if s is tmp[i][0]:
                t += tmp[i][1]
            else:
                tmp2.append([s, t])
                s = tmp[i][0]
                t = tmp[i][1]

        # add the last
        tmp2.append([s, t])

        # skip this example
        if len(tmp2) < 2:
            continue

        # add to new list
        newlist.append([l for l in zip(*tmp2)])

    # done
    return newlist
