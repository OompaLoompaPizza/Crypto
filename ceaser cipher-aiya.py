#msg = 'Codecraft Lab rocks!'

msg = raw_input('What is your message Joelena?? ')

#key = 4

key = int(raw_input(' What key Joelena? '))

#mode = 'encrypt'

mode = raw_input('What is your mode Joelena? [encrypt/decrypt]')


ALPHABET= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''
msg = msg.upper()


for symbol in msg:
    if symbol in ALPHABET:
        num = ALPHABET.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(ALPHABET) :
            num = num - len(ALPHABET)
        elif num < 0:
            num = num = len(ALPHABET)
        result = result + ALPHABET[num]
    else:
        result = result + symbol
print(result)

            






             
