from sys import exit
class Node:
    def __init__(self,char):
        self.char = char
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head == None:
            return "No Data"
        print("_"*15,"Data printing","_"*15)
        temp = self.head
        stt = ""
        while(temp != None):
            stt += str(temp.char)+'\n'
            temp = temp.next
        return stt[::-1]
    
    def enqueue(self):
        if self.head == None:
            self.head = Node(input("Enter the Head data:"))
            self.tail = self.head
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(input("Enter the data:"))
            self.tail = temp.next

    def dequeue(self):
        if self.head == None:
            print("Queue is empty")
        elif self.head.next == None:
            print(self.head.char,"is deleted")
            self.head = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            print(temp.next.char,"is deleted")
            temp.next = None
            
#implemention of Queue using linked list
if __name__ == '__main__':

    #execution loop
    list1 = LinkedList()
    while True:
        option = int(input("*"*30+"\nPress 1 for insert\nPress 2 for del \nPress 3 for print\nPress any key for Exit\nEnter your option:"))
        print("*"*30)
        if option == 1:
            list1.enqueue()
        elif option == 2:
            list1.dequeue()
        elif option == 3:
            print(list1)
        else:
            break

print("Thankyou")
exit()
