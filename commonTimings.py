def getTimings(participants):
    timings = {}
    for i in range(0,24):
        timings[i]=0
    for i in range(24):
        for slots in participants.values():
            if i in slots:
                timings[i]+=1

    commonTimings = {}
    for i in range(24):
        if timings[i] != 0:
            commonTimings[i]=timings[i]
    return commonTimings
