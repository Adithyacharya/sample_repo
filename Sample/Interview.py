class InterviewClass:
    def __init__(self):
        pass
    def reverse_string(self,stringz):
        return stringz[::-1]
    def enter_input(self):
        return(input("Enter the string"))



if __name__ == '__main__':
    obj=InterviewClass()
    str=obj.enter_input()
    print(obj.reverse_string(str))




