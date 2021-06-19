class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self,key,value):
        self[key] = value

    def delete(self,key):
        self.pop(key)

def Menu():

    dict_obj = my_dictionary()
    counter = False
    print("Menu:")
    print("[a]:Add Data \n[b]:Delete Data \n[c]:End")

    while counter == False:
        
        choice = input("Enter your choice: ")
        case_choice = choice.casefold()

        if case_choice == 'a':

            dict_obj.key = input("Enter Key: ")
            dict_obj.value = input("Value:")
            dict_obj.add(dict_obj.key,dict_obj.value)
            print(dict_obj)
            try_choice = input("Try Again? yes/no: ")
            t_choice = try_choice.casefold()
            if t_choice == 'yes':
                counter = False
            elif t_choice == 'no':
                counter = True
            else:
                print("Invalid Choice!")
            print("\n")

        elif case_choice == 'b':

            counter = False
            dict_obj.key = input("Enter Key: ")
            dict_obj.delete(dict_obj.key)
            print(dict_obj)
            try_choice = input("Try Again? yes/no: ")
            t_choice = try_choice.casefold()
            if t_choice == 'yes':
                counter = False
            elif t_choice == 'no':
                counter = True
            else:
                print("Invalid Choice!")
            print("\n")
            
        elif case_choice == 'c':
            print("THANK YOU")
            counter = True
        else:
            print("Invalid Choice")
            

Menu()