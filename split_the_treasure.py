import itertools

treasure = [3,3,3,3,2,2,2,2,2,2,2,2]   #[3,3,3,3,2,2,2,2,2,2,2,2]  #[6,3,2,4,1] #[4,4,4]  #[27,7,20] --> (20,7)+(27)
total = sum(treasure)
print("\ntotal: ", total, "\n")

def solve():
    sum_of_sum = 0
    k_list=[]
    k_list2=[]
    print("")
    for j in range(len(treasure)):
        for k in itertools.combinations(treasure, j):
            k = list(k)

            if sum(k) == each:
                for i in k:
                    k_list.append(i)
                k_list2.append(k)
                
                if sorted(k_list) == sorted(treasure):
                    print(sum(k) ," each ",k_list2,"among ", no_of_crew, "persons")
                    
for no_of_crew in range(2, len(treasure)+1):
    each = total/no_of_crew
    if each %1 == 0:
        each = int(each)
        solve()
