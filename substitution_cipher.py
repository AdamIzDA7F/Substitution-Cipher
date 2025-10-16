
key = "bendjuicxlytzopvwfqkgrahmso" #Key to use from the Alphabet


def substitutionEncrypt(plainText, key):
    import string #Import string module to return chrs to a string
    alphabet = string.ascii_lowercase + " " #Returns lowecase characters
    plainText = plainText.lower()
    
    cipherText = " " #Encrypted text chosen by user.
    for ch in plainText: #Starts a for loop to check for a character in the plainText idx
        idx = alphabet.find(ch) #Assigns idx value with a character in the chosen word
        cipherText = cipherText + key[idx] #Assign cipherText to character Lookup based on key idx ex.values[1]

    return cipherText #Returns the encrypted Text 


def substitutionDecrypt(cipherText, key):
    import string
    alphabet = string.ascii_lowercase + " "
    cipherText = cipherText.lower()
    plainText = ""

    for ch in cipherText: #Starts a for loop to look for characters in cipherText
        
        idx = key.find(ch) #Assigns an idx value to a character in the keys that will be used to translate the encryptedText
        
        if idx != -1: #Checks if the idx value does not equal to -1
            plainText = plainText + alphabet[idx]  #Adds the character found at the idx to the list in plainText
            
    return plainText #Returns the decrypted Text


choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()

if choice == 'e':
    # Encrypt Logic
    userText = input("Enter the text to encrypt: ") #Asks user for word to be encrypted
    resultText = substitutionEncrypt(userText, key) #Encrypts the users word and associates it with a key.
    
    print("Original Text: {}".format(userText)) #Prints the original word the user enters.

    print("Encrypted Text: {}".format(resultText)) #Prints the original word as an encrypted word the user enters.

elif choice == 'd': 
    # Decrypt Logic
    userText = input("Enter the text to decrypt: ")
    resultText = substitutionDecrypt(userText, key)
    
    print("Encrypted Text: {}".format(userText)) #Prints out the encrypted word from the user

    print("Decrypted Text: {}".format(resultText)) #Prints out the decrypted word using the Decrypt Logic.

else:
    # Error Handling
    print("Invalid choice. Please enter 'E' for Encrypt or 'D' for Decrypt.") #Testing output.

input()
