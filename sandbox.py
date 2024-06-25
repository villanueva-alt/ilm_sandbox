import re
## fix caps rules ###
##
## initial caps after any of these chars: whitespace, '-', '/', '.', '&', "'", '('.
## capitalize all of the following if they have a space on both sides: hs hr ms es avts pd
## capitalize first char after words that start with 'mc'
## 
# Assume: 
# - str is all caps
# - str is two names split with space between : not always
#   -- will there ever be just one name entered? yes
#   -- will there be more than two? yes 

def fix_caps(str):

    str_split = str.strip().split(" ")
    
    separators = ["-", "/", ".", "&","(",")","\t"]
    specials = ("Hs", "Hr", "Ms", "Es", "Avts", "Pd")

    i = 0
    while i < len(str_split):
        
        str_split[i] = str_split[i].title()

        if str_split[i].startswith("Mc"):
            pre, root = str_split[i][0:2], str_split[i][2:]
            str_split[i] = pre + root.title()
        
        for special in specials:
            for sep in separators:
                if (str_split[i].startswith(special) and sep in str_split[i]) or (len(special) == len(str_split[i])):
                    str_split[i] = str_split[i].replace(special, special.upper())


        i += 1

    return " ".join(str_split)


def main():
    print(fix_caps('ESPINOSA HS'))


if __name__ == "__main__":
    main()