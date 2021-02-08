import itertools

treasure = [27,7,20]   #[3,3,3,3,2,2,2,2,2,2,2,2]  #[6,3,2,4,1] #[4,4,4]  #[27,7,20] --> (20,7)+(27)
total = sum(treasure)
print("total: ", total)

def solve(each):
    for j in range(len(treasure)):
        for k in itertools.combinations(treasure, j):
            k = list(k)
            if sum(k) == each:
                print(sum(k) ," each ", k, " among ", i, "persons")

for i in range(2, len(treasure)+1):
    each = total/i
    if each %1 == 0:
        each = int(each)
        solve(each)
