no_elements=int(input('enter number of elements: '))
dic={}
for elements in range(no_elements):
    key=input('enter key: ')
    dic[key]=list(map(int,input('enter value for key: ').split()))

def reform_dictionary(dic):
    ans={}
    for key in dic:
        for element in dic[key]:
            if element in ans.keys():
                ans[element].append(key)
            else:
                ans[element]=[key]

    return ans

print(reform_dictionary(dic))