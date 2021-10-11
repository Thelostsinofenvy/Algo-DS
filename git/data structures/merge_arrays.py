arr = [0, 3, 4, 31]
arr2 = [4, 6, 30]
myarr = []


def mergesortedarrays(arr, arr2):
    # combine both arrays
    for i in range(len(arr)):
        myarr.append(arr[i])

    for j in range(len(arr2)):
        myarr.append(arr2[j])

    # sort the combined arrays
    # myarr.sort()
    # return myarr

    # sorting without sort()
    for num in range(len(myarr)-1):
        if myarr[num] >= myarr[num+1]:
            myarr[num], myarr[num+1] = myarr[num+1], myarr[num]

    return myarr


print(mergesortedarrays(arr, arr2))
