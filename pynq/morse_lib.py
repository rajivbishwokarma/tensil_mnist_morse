# Reference: https://en.wikipedia.org/wiki/Morse_code

def morse_code():
    DOT  = 0xf0
    DASH = 0xff 
    
    one   = [DOT, DASH, DASH, DASH, DASH]
    two   = [DOT, DOT, DASH, DASH, DASH]
    three = [DOT, DOT, DOT, DASH, DASH]
    four  = [DOT, DOT, DOT, DOT, DASH]
    five  = [DOT, DOT, DOT, DOT, DOT]
    six   = [DASH, DOT, DOT, DOT, DOT]
    seven = [DASH, DASH, DOT, DOT, DOT] 
    eight = [DASH, DASH, DASH, DOT, DOT]
    nine  = [DASH, DASH, DASH, DASH, DOT]
    zero  = [DASH, DASH, DASH, DASH, DASH]
    
    morse_list = [zero, one, two, three, four, five, six, seven, eight, nine]

    morse_dict = {}
    for i in range(len(morse_list)):
        morse_dict.update({i : morse_list[i]})

    return morse_dict
        
    # for i in range(len(morse_list)):
    #    print(f"{i} : {morse_dict[i]}")


if __name__ == '__main__':
    morse_code()
