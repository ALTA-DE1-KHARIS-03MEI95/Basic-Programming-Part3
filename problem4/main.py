def palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def main():
    string = input("Masukkan string: ")
    result  = palindrome(string)
    if result:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()


