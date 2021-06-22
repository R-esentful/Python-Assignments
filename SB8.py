class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self,key,value):
        self[key] = value

    def delete(self,key):
        self.pop(key)

def Menu():

    dict_obj = my_dictionary()
    print("Menu:")
    print("[a]:Add Data \n[b]:Delete Data \n[c]:End")
    isActive = True
    
    while isActive == True:
        user_input = input("Enter your choice:")
        if user_input == 'a'or user_input == 'A':
            dict_obj.key = input("Enter Key:")
            dict_obj.value = input("Value:")
            dict_obj.add(dict_obj.key,dict_obj.value)
            print(dict_obj)
            
        elif user_input == 'b' or user_input == 'B':
            dict_obj.key = input("Enter Key:")
            dict_obj.delete(dict_obj.key)
            print(dict_obj)
        
        elif user_input == 'c' or user_input =='C':
            print("THANK YOU!")
        
        else:
            print("Invalid Input")
        
        choice = input("Try again? yes/no:")
        x = choice.casefold()
        if x == 'yes':
            isActive = True
        elif x == 'no':
            isActive = False
        else:
            print("Invalid input!")

    print(dict_obj)

Menu()
