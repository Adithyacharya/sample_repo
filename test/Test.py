def sum_of_list(list1,l2):
    for ele in list1:
        if isinstance(ele,int):
            l2.append(ele)
        elif isinstance(ele,list):
            sum_of_list(ele,l2)
#            for ele1 in ele:
#                print("inside list", ele1)
#                l2.append(ele1)
    print(l2)
    print(list1)



def sum_tranning(l):

    sum = 0

    for i in range(0, len(l)):
        if isinstance(l[i], list):
            for j in range(0, len(l[i])):
                print((l[i][j]))
                sum += l[i][j]
#                print("true")

    print(sum)

if __name__ == '__main__':
    l = [1, 2, 3, [4, 5, 6], 7, [8, 9, 10]]
    list1 = [1, 2, 4, [2, 3, 4,[1,2,3,4],2, 1, 3, 4, 3], [2, 3, 4], 6]
    l2=[]
   # sum_tranning(l)
    sum_of_list(list1,l2)
