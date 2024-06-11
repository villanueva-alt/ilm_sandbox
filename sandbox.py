import re
## fix caps rules ###
##
## initial caps after any of these chars: whitespace, '-', '/', '.', '&', "'", '('.
## capitalize all of the following if they have a space on both sides: hs hr ms es avts pd
## capitalize first char after words that start with 'mc'

def fix_caps(str):

    specials = ("Hs", "Hr", "Ms", "Es", "Avts", "Pd")

    #strip white space on ends
    str = str.strip()
    #split string on special characters
    str_split = re.split(r"[\s\-\/\.\',&()]", str)
    #filter empty strings resulting from combo-special-character-match
    str_split = list(filter(None, str_split))

    i = 0
    while i < len(str_split):
        str[i].title()
        for special in specials:
            if str[i] == special:
                str[i].upper()
        i += 1


    # while(True):
    #     split = False
    #     for separator in separators:
    #         if separator in str:
    #             str_split = str.split(separator)
    #             split = True
    #             continue
    #         else
    #     break

    return str_split


def main():
    print(fix_caps('MR. SMITH- WIL&,SON'))


if __name__ == "__main__":
    main()