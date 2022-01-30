from linked_list import LinkedList

def main():
    ll = LinkedList()
    while True:
        print("=========================================")
        user_response = input("Give me data or type 'q' to quit -> ")
        if user_response == "q" or user_response=="Q":
            break
        ll.push(user_response)

        ll.printList()
        if input("Edit an element? ('y' for yes, any other key for no) ") == 'y':
            e = input("Enter data you want to edit: ")
            r = input(f"Enter data you wish to replace {e} with: ")
            ll.edit(e, r)
            

if __name__ == '__main__':
    main()