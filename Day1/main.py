### data parsing ###
data = ""
values = []
with open("data", "r") as f:
    data += f.read()
for line in data.split():
    values += [int(line)]


### /data parsing ###

def get_elements_gt_last(lst):
    result = 0
    lenlst = len(lst)
    if lenlst in [0, 1]:
        return 0
    last_element = lst[0]
    for i in range(1, lenlst):
        this_element = lst[i]
        if this_element > last_element:
            result += 1
        last_element = this_element

    return result


def get_n_elements_sum_gt_last(n, lst):
    result = 0
    lenlst = len(lst)
    if lenlst in range(n):
        return 0
    last_sum = sum_n_elements(n, lst, n)
    for i in range(n, lenlst+1):
        this_sum = sum_n_elements(n, lst, i)
        if this_sum > last_sum:
            result += 1
        last_sum = this_sum

    return result


def sum_n_elements(n, lst, start=0):
    result = 0
    for i in range(start-n, start):
        result += lst[i]
    return result

print(get_elements_gt_last(values))
print(get_n_elements_sum_gt_last(3, values))
