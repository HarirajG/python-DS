class Node:
    def __init__(self,char):
        self.char = char
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return "No Data"
        print("_"*15,"Data printing","_"*15)
        temp = self.head
        stt = ""
        while(temp != None):
            stt += '\n'+str(temp.char)
            temp = temp.next
        return stt
    
    def insertNode(self):
        if self.head == None:
            self.head = Node(input("Enter the Head data:"))
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(input("Enter the data:"))

    def deleteNode(self):
        if self.head == None:
            print("Stack is Empty")
        else:
            temp = self.head
            self.head = self.head.next
            print(temp.char,"is deleted")
            del temp
            
#implemention of Stack using linked list
if __name__ == '__main__':

    #execution loop
    list1 = LinkedList()
    while True:
        option = int(input("*"*30+"\nPress 1 for insert\nPress 2 for del \nPress 3 for print\nPress any key for Exit\nEnter your option:"))
        print("*"*30)
        if option == 1:
            list1.insertNode()
        elif option == 2:
            list1.deleteNode()
        elif option == 3:
            print(list1)
        else:
            break

print("Thankyou")
