def ele_list(list, idx):
    if(idx==len(list)):
        return
    print(list[idx])
    ele_list(list, idx+1)

ele_list([2,3,4,5],0)