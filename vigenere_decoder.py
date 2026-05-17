message_length = int(input())
keyword_length = int(input())

cipher_values = list(map(int, input().split()))

keyword = input()

extended_key = keyword + keyword[:message_length-keyword_length]

BASE = ord('A')

decoded_chars = []


for i, value in enumerate(cipher_values):
    shift = ord(extended_key[i]) - BASE
    decode_value = value - shift
    decoded_chars.append(chr(decode_value + BASE))

print("word: ", "".join(decoded_chars))