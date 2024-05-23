# Let's encode secret messages with ROT13!

import codecs

def programIntro():
    print("\n[&] Encryption and Decryption using ROT13 [&]")
    print("$-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+$\n")

def applyROT13(inputFile):
    # File extension splitting
    if '.' in inputFile:
        fileParts = inputFile.rsplit('.', 1)
        outputFile = f"{fileParts[0]}_rot13.{fileParts[1]}"
    else:
        outputFile = f"{inputFile}_rot13"

    # File reading and rot13 application
    try:
        with open(inputFile, 'r', encoding='utf-8') as file:
            text = file.read()
            rot13Text = codecs.encode(text, 'rot_13')
        # Writing results to a new file
        with open(outputFile, 'w', encoding='utf-8') as file:
            file.write(rot13Text)
            file.flush()  # Ensuring all data is written to disk
        print(f"rot13 encrypted file created: {outputFile}")
    except FileNotFoundError:
        print(f"Error: The file {inputFile} does not exist. Please check the filename and try again.\n")
        return False
    except Exception as e:
        print(f"An error occurred: {e}\n")
        return False
    return True

def programOutro():
    print("\n[&] Good Bye! [&]")
    print("$-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+$\n")

def main():
    programIntro()
    userChoice = input("Choose an option:\n"
                       "\t1. Encrypt/Decrypt an existing file\n"
                       "\t2. Write a new message to encrypt\n"
                       "\t3. Exit\n"
                       "\nEnter your choice (1 or 2 or 3): ")
    if userChoice == '1':
        while True:
            inputFilename = input("Please enter the filename including its extension: ")
            if applyROT13(inputFilename):
                break
    elif userChoice == '2':
        print("\nPlease write your message (end with ':wq' to save and exit): ")
        lines = []
        while True:
            line = input()
            if line == ":wq":
                break
            lines.append(line)
        message = '\n'.join(lines)
        outputFilename = input("Enter the output filename (including extension): ")
        try:
            with open(outputFilename, 'w', encoding='utf-8') as file:
                file.write(codecs.encode(message, 'rot_13'))
            print(f"rot13 encrypted message saved to: {outputFilename}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
    elif userChoice == '3':
        programOutro()
        exit()
    else:
        print("Invalid input. Please enter 1 or 2.")
    programOutro()

if __name__ == "__main__":
    main()
