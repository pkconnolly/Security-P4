import hashlib, itertools

# Wordlists
# - rockyou.txt
# - found2015.txt
# - english.txt
# - realuniq.txt
# - phpbb.txt

basic_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', '\'', '!', '@', '#', '$', '%', '^', '&', '*', '?']


#For automatic cracking using a wordlist
def crack_wordlist(filename, wordlist):
    file = open(filename, "r", encoding="utf8")
    wordlist = open(wordlist, "r", errors="replace")
    for password in wordlist:
        password_hash = hashlib.md5(password[:-1].encode('utf8')).hexdigest()
        file.seek(0)
        for line in file:
            if line[4:-1] == password_hash:
                print(line[:-1] + ": " + "'" + password[:-1] + "'")


#For brute force, permutations of 'characters' between lengths 'char_min' and 'char_max'
def brute_force(filename1, characters, char_min, char_max):
    file = open(filename1, "r", encoding="utf8")
    for i in range(char_min, char_max+1):
        wordlist = itertools.product(characters, repeat=i) #Generate permutations of characters for length i
        for item in wordlist:
            password = ''.join(item) #Wordlist is full of tuples, join tuple into 1 string
            password_hash = hashlib.md5(password.encode('utf8')).hexdigest()
            file.seek(0)  # Go to beginning of list
            for line in file: #Check each hash in file
                if line[4:-1] == password_hash:
                    print("In " + filename1 + ": " + line[:-1] + ": " + "'" + password + "'")


#For manually testing passwords
def crack_manual(filename1, filename2):
    file = open(filename1, "r", encoding="utf8")
    file2 = open(filename2, "r", encoding="utf8")
    while True:
        password = input("Password: ")
        password_hash = hashlib.md5(password.encode('utf8')).hexdigest()
        file.seek(0)
        file2.seek(0)
        for line in file:
            if line[4:-1] == password_hash:
                print(line[:-1] + ": " + "'" + password + "'")
        for line in file2:
            if line[4:-1] == password_hash:
                print(line[:-1] + ": " + "'" + password + "'")


#Examples:
crack_wordlist("weak.txt", "rockyou.txt")
#brute_force("strong2.txt", special_chars, 0, 4)
#crack_manual("moderate2.txt", "strong2.txt")
