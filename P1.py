import copy
 
# def sub_decorator(func):
#     def sub():
#         x = func()
#         return x - 5
#     return sub
 

# @sub_decorator
# def sub_num():
#     return 10

# print(sub_num())


#copy()
# original_list = [10, 20]
# list = original_list.copy()
# list.remove(10)
# original_list.append(901)
# print("Shallow Copy \n original_list: " ,original_list,"\n list: " , list)



#shallow Copy
# original_list_shallow = [100, 200]
# list_shallow = original_list_shallow
# list_shallow.remove(100)
# original_list_shallow.append(900)
# print("Shallow Copy \n original-list-shallow: " ,original_list_shallow,"\n List-shallow: " , list_shallow)

# import threading
# import time

# def sq():
#     for i in range(1, 10):
#         print(i)
#         time.sleep(0.1)

# def sq_2():
#     for i in range(1, 10):
#         print(i*i, " second func")
#         time.sleep(0.1)

# th1 = threading.Thread(target=sq)
# th2 = threading.Thread(target=sq_2)

# th1.start()
# th2.start()
# th1.join()
# th2.join()


employee = [{"name": "hjbdsd", "name1": "meet"}, {"name": "ajsbd"}, {"name": "ajsbd"}]

for i in employee:
    if "name1" in i:
        print(i["name1"])
    else:
        print(i["name"])