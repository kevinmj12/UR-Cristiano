list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 함수 파라미터의 타입을 정의하면 더 좋을 것 같아요

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
