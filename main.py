import commonTimings

print("---------------------------------")
print("---------------------------------")
print("")


people = int(input("Enter the number of the people who will be in the meeting: "))
participants = {}
for i in range(people):
    freeSlots = list(map(int,input(f"Enter Slots with a space for participant - {i+1} : ").split(" ")))
    participants[i]=freeSlots
    freeSlots = []
print(participants)

common = commonTimings.getTimings(participants)
commonSorted = []
for i in common.keys():
    commonSorted.append([i,common[i]])
print("---------------------------------")


for j in range(len(commonSorted)-1):
    for i in range(len(commonSorted)-j-1):
        if commonSorted[i][1] < commonSorted[i+1][1]:
            commonSorted[i][1],commonSorted[i+1][1] = commonSorted[i+1][1],commonSorted[i][1]

print("---------------------------------")
print("Timings - Participants")
for i in commonSorted:
    print(i[0],"---------->",i[1])