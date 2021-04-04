def menu():
    print("1.绘制散点图")
    print("2.数据排序")
    print("3.算法实现")
    print("4.结束")
    job = input("请选择操作：")

    if job == '1':
        user_dict = creating_dictionary()
    elif job == '2':
        updating_dictionary(user_dict)
    elif job == '3':
        sorting_dictionary(user_dict)
    else job == '4':
        break