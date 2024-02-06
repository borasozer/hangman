import random
win_no = 0
lose_no = 0
new = "2"
stage = 0
ex_themes = []

cities = ["london", "birmingham", "glasgow", "liverpool", "leeds", "sheffield", "edinburgh", "bristol", "manchester",
    "leicester", "islington", "coventry", "hull", "cardiff", "bradford", "belfast", "stoke-on-trent", "wolverhampton",
    "plymouth", "nottingham", "southampton", "reading", "derby", "dudley", "northampton", "portsmouth", "luton",
    "newcastle upon tyne", "preston", "sutton", "milton keynes", "aberdeen", "sunderland", "norwich", "walsall",
    "swansea", "bournemouth", "southend-on-sea", "swindon", "oxford", "dundee", "poole", "huddersfield", "york",
    "ipswich", "blackpool", "middlesbrough", "bolton", "peterborough", "stockport", "brighton", "telford",
    "west bromwich", "slough", "gloucester", "cambridge", "watford", "rotherham", "newport", "exeter", "eastbourne",
    "bassetlaw district", "mendip", "colchester", "dagenham", "crawley", "sutton coldfield", "blackburn", "oldham",
    "woking", "cheltenham", "chelmsford", "saint helens", "basildon", "gillingham", "worcester", "becontree",
    "worthing", "rochdale", "basingstoke", "solihull", "harlow", "bath", "southport", "maidstone", "lincoln",
    "hastings", "darlington", "londonderry county borough", "harrogate", "hartlepool", "bedford", "hemel hempstead",
    "stevenage", "saint albans", "south shields", "derry", "weston-super-mare", "halifax", "birkenhead"]

turkey_cities = ["adana", "adıyaman", "afyonkarahisar", "ağrı", "amasya", "ankara", "antalya","artvin",
    "aydın", "balıkesir", "bilecik", "bingöl", "bitlis", "bolu", "burdur", "bursa", "çanakkale", "çankırı",
    "çorum", "denizli", "diyarbakır", "edirne", "elazığ", "erzincan", "erzurum", "eskişehir", "gaziantep", "giresun",
    "gümüşhane", "hakkari", "hatay", "isparta", "mersin", "istanbul", "izmir", "kars", "kastamonu", "kayseri", "kırklareli",
    "kırşehir", "kocaeli", "konya", "kütahya", "malatya", "manisa", "kahramanmaraş", "mardin", "muğla", "muş", "nevşehir",
    "niğde", "ordu", "rize", "sakarya", "samsun", "siirt", "sinop", "sivas", "tekirdağ", "tokat", "trabzon", "tunceli",
    "şanlıurfa", "uşak", "van", "yozgat", "zonguldak", "aksaray", "bayburt", "karaman", "kırıkkale", "batman", "şırnak",
    "bartın", "ardahan", "ığdır", "yalova", "karabük", "kilis", "osmaniye", "düzce"]
fruits = ["apple", "banana", "peach", "watermelon", "cherry"]
instruments = ['piano', 'guitar', 'drums', 'violin', 'trumpet', 'saxophone', 'flute', 'clarinet', 'bass guitar', 'cello', 'harp', 'accordion', 'banjo', 'ukulele', 'mandolin', 'tambourine', 'xylophone', 'maracas', 'bagpipes', 'didgeridoo']
sports = ["football", "cricket", "hockey", "tennis", "volleyball", "table tennis", "basketball", "baseball", "rugby", "golf"]

theme_list = {1:"cities",2:"fruits",3:"instruments",4:"turkey_cities",5:"sports"}
theme_dict = {1:cities,2:fruits,3:instruments,4:turkey_cities,5:sports}
total_rem = sum(len(theme) for theme in theme_dict.values())

while True:
    total_rem = sum(len(theme) for theme in theme_dict.values())
    if total_rem == 0:
        new = 17
    if new == "1" or new == "2" or new == "3" or new == "17":
        print(r"                                                 ")
        print(r"  ---------------------------------------------  ")
        print(r" |                    ___                      | ")
        print(r" | |  |   /\   |\  | |     |\  /|   /\   |\  | | ")                 
        print(r" | |--|  /--\  | \ | |  _  | \/ |  /--\  | \ | | ")            
        print(r" | |  | /    \ |  \| |___| |    | /    \ |  \| | ")               
        print(r" |                                             | ")                             
        print(r"  ---------------------------------------------- ")
        if new == "17":
            print("\nYou finished all words!\nThank you for playing.")
            while True:
                x = input()
        if new == "3":
            print("\nThank you for playing. See you next time!")
            print(f"Win:{win_no} Lose:{lose_no}")
            break
    while new == "2" or new == "15" :
        print("\nNo  Themes   Remaining words ")
        print("\n".join(f"{kk} : {vv}   ({len(eval(vv))})" for kk, vv in theme_list.items()))
        print(f"\n       Total:({total_rem})") 
        no = input("\nChoose theme(type no):")
        while not (no == "1" or no == "2" or no == "3" or no == "4" or no == "5"):
            no = input("\nPlease enter valid number:")
    
        word_list = theme_dict[int(no)]
        new = "1"
        
        while no in ex_themes:
            print("\nNo question left on: " + theme_list[int(no)])
            print(total_rem)
            print("\nNo  Themes   Remaining words ")
            print("\n".join(f"{kk} : {vv}   ({len(eval(vv))})" for kk, vv in theme_list.items()))
            print(f"\n       Total:({total_rem})") 
            no = input("\nChoose another theme(type no):")
            while not (no == "1" or no == "2"):
                no = input("\nPlease enter valid number:")
        if no in ex_themes:
            new = "2"
    while new == "1":
        difficulty = input("\nChoose difficulty level easy(1)/normal(2)/hard(3)/very hard(4):")
        while not (difficulty == "easy" or difficulty == "1" or difficulty == "normal" or difficulty == "2" or difficulty == "hard" or difficulty == "3" or difficulty == "very hard" or difficulty == "4"):
            difficulty = input("\nWrite correct difficulty level easy(1)/normal(2)/hard(3)/very hard(4):")
        if difficulty == "easy" or difficulty == "1":
            dif_level = 0
            print("\nDifficulty Level: Easy")
        elif difficulty == "normal" or difficulty == "2":
            dif_level = 1
            print("\nDifficulty Level: Normal")
        elif difficulty == "hard" or difficulty == "3":
            dif_level = 2
            print("\nDifficulty Level: Hard")
        elif difficulty == "very hard" or difficulty == "4":
            dif_level = 3
            print("\nDifficulty Level: Very Hard")
        if 0 <= int(difficulty) <=4:
            new = ""
        print(f"\nTheme : {(theme_list[int(no)]).capitalize()}")

    while new == "":
        word = random.choice(word_list)
        word_list.remove(word)
        letters = []
        true_letters = []
        wrong_letters = []
        win = False
        if dif_level == 0:
            print(r"  _______________  ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |_______________| ")
            print(r"                   ")
        if dif_level == 1:
            print(r"  _______________  ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |               | ")
            print(r" |  __________   | ")
            print(r" |_______________| ")
            print(r"                   ")
        if dif_level == 2:
            print(r"  _______________  ")
            print(r" |               | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |  _|________   | ")
            print(r" |_______________| ")
            print(r"                   ")
        if dif_level == 3:
            print(r"  _______________  ")
            print(r" |   ______      | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |   |           | ")
            print(r" |  _|________   | ")
            print(r" |_______________| ")
            print(r"                   ")
        for i in word:
            if i == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print("\n")
        while win == False:
            temp = wrong_letters.copy()
            stage = len(wrong_letters) + dif_level
            if stage == 10:
                break
            if stage < 10:
                letter = input("Guess letter:")
                print(" ")
            if letter == word:
                break
            if letter in letters:
                print(f"You already type {letter}\n")
                continue
            else:
                letters.append(letter)
            win = True
            if letter not in word and letter not in wrong_letters:
                wrong_letters.append(letter)
            stage = len(wrong_letters) + dif_level       
            if stage == 1:
                print(r"  _______________  ")
                print(r" |               | ")
                print(r" |               | ")
                print(r" |               | ")
                print(r" |               | ")
                print(r" |               | ")
                print(r" |               | ")
                print(r" |  __________   | ")
                print(r" |_______________| ")
            elif stage == 2:
                print(r"  _______________  ")
                print(r" |               | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 3:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 4:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |    O      | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |   |           | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 5:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |    O      | ")
                print(r" |   |    |      | ")
                print(r" |   |    |      | ")
                print(r" |   |           | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 6:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |    O      | ")
                print(r" |   |   /|      | ")
                print(r" |   |    |      | ")
                print(r" |   |           | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 7:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |    O      | ")
                print(r" |   |   /|\     | ")
                print(r" |   |    |      | ")
                print(r" |   |           | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 8:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |    O      | ")
                print(r" |   |   /|\     | ")
                print(r" |   |    |      | ")
                print(r" |   |   /       | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            elif stage == 9:
                print(r"  _______________  ")
                print(r" |   ______      | ")
                print(r" |   |           | ")
                print(r" |   |    O      | ")
                print(r" |   |   /|\     | ")
                print(r" |   |    |      | ")
                print(r" |   |   / \     | ")
                print(r" |  _|________   | ")
                print(r" |_______________| ")
            print(" ")
            for i in word:
                if i in letters or i == " ":
                    print(i, end=' ')

                    if i not in true_letters:
                        true_letters.append(i)
                else:
                    print('_', end=' ')
                    win = False
                        
            print("\n")
            if not wrong_letters == temp:
                print("Wrong...\n")
                        
            print("Non-existent letters: ", end=' ')
            print(*wrong_letters, "\n")
        if stage < 10:
            win_no += 1
            print(f"Congratulations. You won!")
        else:
            lose_no += 1
            print(r"  _______________  ")
            print(r" |   ______      | ")
            print(r" |   |    |      | ")
            print(r" |   |   \O/     | ")
            print(r" |   |    |      | ")
            print(r" |   |    |      | ")
            print(r" |   |   / \     | ")
            print(r" |  _|________   | ")
            print(r" |_______________| ")
            print(" ")
            print(f"Word was {word}\nAfter {len(wrong_letters)} wrong and {len(true_letters)} correct guesses,\nYou are DEAD!!!")
        new ="31"
        while not (new == "" or new == "1" or new == "2" or new == "3"):
            if len(word_list) == 0:
                print("\nYou finished all the words in this theme.")
                new = "15"
                ex_themes.append(no)
                break
            new = input(f"\nPress enter for new word \nType 1 to change difficulty \nType 2 to change theme \nType 3 to finish")
            if not (new == "" or new == "1" or new == "2" or new == "3"):
                print("Write a valid option.")







                
