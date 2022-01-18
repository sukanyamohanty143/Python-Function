def encrypt():
    message = input("Enter the message you want to encrypt")
    ascii_message = [ord(i)+3 for i in message]
    encrypt_message = [ chr(i) for i in ascii_message]  
    print (''.join(encrypt_message))
def decrypt():
    message = input("Enter the message you want to decrypt")
    ascii_message = [ord(i)-3 for i in message]
    decrypt_message = [ chr(i) for i in ascii_message]  
    print (''.join(decrypt_message))
flag = True
while flag == True:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()    
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break