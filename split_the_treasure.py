
#given
crew = 3

treasure = [27,7,20]  #[4,4,4]  #[27,7,20] --> (20,7)+(27)


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


t = 0
for i in treasure:
    t += i
print("tplm: ",t)
each = t/2
if each%1==0:
    each = int(each)
    print("each: ",each)
    subset_sum(treasure, each)   # topla=16, 2,3,4 ve 5 e böl -->8,x,4

