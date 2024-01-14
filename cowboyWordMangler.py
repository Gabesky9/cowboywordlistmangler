import itertools
import sys 
import time 
def generate_wordlist(chars, min_length, max_length, max_size_bytes=5*1024*1024):  # 5MB default
    wordlist = set()
    current_size = 0
    print("Let's mangle those words, cowboy!! AARGH!!!", end="")
    sys.stdout.flush()

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            word = ''.join(combination)
            word_size = len(word.encode('utf-8'))

            if current_size + word_size > max_size_bytes:
                print("\nWOA THERE, WE JUST REACHED THE MAXIMUM SIZE! 5MB..")
                return wordlist

            wordlist.add(word)
            current_size += word_size
            print(".", end="")
            sys.stdout.flush()
            time.sleep(0.01)  # If i dont do this the dots go way too fast and the dots really got nothin to do with the speed the list is created

    print("\nConsider those words mangled, cowboy....")
    return wordlist
    wordlist.add(word)
    current_size += word_size 
    print(".", end="")
    sys.stdout.flush()

def main():
    blue = '\033[96m'
    green = '\033[92m'
    ENDC = '\033[0m'

    print(blue + """
     .~~~~`\~~
     ;       ~~
     |           ;
 ,--------,______|---.
/          \-----`    \    
`.__________`-_______-'                   
                                                       
    """ + ENDC)

    print(green + """
   ,___ ___  __    __ __   ___  __   _   __    ____  _ __   ___  _ _ _    _,  _ __   ,___ __   ______ _ __ 
  /   //  ()( /   /( /  ) /  ()( /  /   ( /   //  ()( /  ) ( / \( / ) )  / | ( /  ) /   /( /  (  /   ( /  )
 /    /   /  / / /  /--< /   /  (__/     / / //   /  /--<   /  / / / /  /--|  /  / /  __  /     /--   /--< 
(___/(___/  (_/_/  /___/(___/    _/_    (_/_/(___/  /   \_(/\_/ / / (__/   |_/  (_(___/ (/___/(/____//   \_
                                //                                                                         
                               (/           

    """ + ENDC)

    print(blue + "AUTHOR: Gabesky9" + ENDC)
    print(green + "I DO NOT ENCOURAGE YOU TO DO BAD THINGS EVEN THO THIS IS A POORLY WRITTEN SCRIPT, UR ILLEGAL ACTIVITY IS NOT MY FAULT!" + ENDC)
    print(blue + "Anyhow, it's been a real grand time making this, and I hope people want to add onto my lil project here. Keep it sleazy, space cowboys!" + ENDC)

    words = input("Howdy partner! Enter words separated by space: ").split()
    numbers = input("Enter numbers, think birthdays, lucky numbers, all the like (012346789) duh: ")
    special_chars = input(str('is there any special characters needed for this here list? (! @ # $ % ^ & *tes)'))
    numbers_list = list(numbers.replace(" ", " "))
    special_chars_list = list(special_chars.replace(" ", " "))
    chars = words + special_chars_list  + numbers_list

    min_length = int(input("What's the minimum length of the password for that target there, cowboy? : "))
    max_length = int(input("What's the maximum password length for the target, partner? : "))

    
    if max_length < min_length:
        print("Whoa there, partner! Maximum length must be greater than or equal to minimum length.")
        return


    wordlist = generate_wordlist(chars, min_length, max_length)

    with open("cowboywordmangler.txt", "w") as file:
        for word in wordlist:
            file.write(word + "\n")

    print("""'cowboywordmangler.txt' is the name of that there list,an remeber this thing here done gone an saved into your current directory! partner. Now be careful, even though she may be dumb, if you crack into something you ain't supposed to, 
          I never said that was okay to do, and I am not liable! Elsewise, load that pistol up and shoot!""")

if __name__ == "__main__":
    main()
wordlist = generate_wordlist(chars, min_length, max_length)
