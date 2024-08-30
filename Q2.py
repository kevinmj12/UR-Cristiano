list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

def removeDup(l):
    l = set(l)
    l = list(l)
    print(l)

def addAndRemoveDup(l1, l2):
    l = l1 + l2
    l = set(l)
    l = list(l)
    print(l)

def sameElements(l1, l2):
    intersection = set(l1) & set(l2)
    print(list(intersection))

removeDup(list1)
addAndRemoveDup(list1, list2)
sameElements(list1, list2)