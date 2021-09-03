list1=input().split()
list2=list(map(int,input().split()))

def return_combination(list1,list2):
    ans=[]
    for lst2_elmnts in range(0,-len(list2),-1):
        test_lst=[]
        for lst1_elmnts in range(len(list1)):
            test_lst.append((list1[lst1_elmnts],list2[lst1_elmnts+lst2_elmnts]))
        ans.append(test_lst)

    return ans

print(return_combination(list1,list2))