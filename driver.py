import binascii
import AES

key = "5468617473206D79204B756E67204675"
plainText = "54776F204F6E65204E696E652054776F"
encryptedText = "29C3505F571420F6402299B31A02D73A"

# /*
#    *
#    * The getFileContents function grabs text from a file so it can later be encrypted or
#    * decrypted.
#    *
#    * Parameters:
#    * file_path: Location of file
#    *
#    * return contents: text from file
# */
def getFileContents(file_path):
    contents = []
    with open(file_path, 'r') as reader:
        for line in reader:
            # strip removes line breaks
            # contents.append(line.strip())
            contents.append(line)
    return contents

def convertStringToHex(str):
    encode = str.encode('utf-8')
    return encode.hex()

def convertHexToString(hexStr):
    string = ''.join(chr(int(hexStr[i:i+2], 16)) for i in range(0, len(hexStr), 2))
    return string

def splitString(string):
    num_groups = len(string) // 32 + 1
    result = ['0'] * num_groups
    count = 0
    i = 0
    while (i < len(string)):
        part = string[i:min(len(string), i+32)]
        result[count] = part
        count += 1
        i += 32
    return result


# /*
#    *
#    * The encryptFile function grabs takes the text from the encrypted file, breaks it up, and then
#    * sends it off to AES.encrypt(). It then stores that encrypted text in a new file with the
#    * original name
#    *
#    * Parameters:
#    * file_path: Location of file
#    * file_name: name of file
#    *
# */
def encryptFile(file_path, file_name):
    file_text = getFileContents(file_path)
    encrypted_text = []

    for line in file_text:
        if len(line) == 0:
            break
        else:
            encrypted_line = ""
            content = convertStringToHex(line).upper()
            split_strings = splitString(content)
            for i in split_strings:
                if (i != "0"):
                    encrypted_line = encrypted_line + AES.encrypt(i, key)
            encrypted_text.append(encrypted_line)

    file_location = "files/{}".format(file_name)
    with open(file_location, 'w') as writer:
        for line in encrypted_text:
            writer.write(line + "\n")


# /*
#    *
#    * The decryptFile function grabs takes the text from the encrypted file, breaks it up, and then
#    * sends it off to AES.decrypt(). It then stores that decrypted text in a new file with the
#    * original name
#    *
#    * Parameters:
#    * file_path: Location of file
#    * file_name: name of file
#    *
# */
def decryptFile(file_path, file_name):
    file_text = getFileContents(file_path)
    decrypted_text = []

    for line in file_text:
        if len(line) == 0:
            break
        else:
            decrypted_line = ""
            split_strings = splitString(line.strip())
            
            for i in split_strings:
                if (i != "0"):
                    decrypted_line = decrypted_line + AES.decrypt(i, key)
            content = convertHexToString(decrypted_line).strip()
            decrypted_text.append(content)

    file_location = "files/{}".format(file_name)
    with open(file_location, 'w') as writer:
        for line in decrypted_text:
            writer.write(line + "\n")
