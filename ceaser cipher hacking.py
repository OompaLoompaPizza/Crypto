msg = raw_input(' What is your fate  Jolena? ')
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = msg.upper()
for key in range(len(ALPHABET) ) :
    result = ' '
    for symbol in msg:
        if symbol in ALPHABET:
            num =ALPHABET.find(symbol)
            num = num - key

            if num < 0:
                num  = num + len(ALPHABET)

            result = result + ALPHABET[num]

        else:
            result = result + symbol

    print(' The fates declare your number is.........%s! %s' % (key, result)) 
