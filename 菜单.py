def menu():
    print("1.����ɢ��ͼ")
    print("2.��������")
    print("3.�㷨ʵ��")
    print("4.����")
    job = input("��ѡ�������")

    if job == '1':
        user_dict = creating_dictionary()
    elif job == '2':
        updating_dictionary(user_dict)
    elif job == '3':
        sorting_dictionary(user_dict)
    else job == '4':
        break