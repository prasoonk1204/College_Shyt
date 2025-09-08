# ASCII (American Standard Code for Information Interchange) Codes

# A to Z: 65 to 90
# a to z: 97 to 122
# 0 to 9: 48 to 57
# Space: 32
# Enter: 13
# Backspace: 8
# Tab: 9
# Escape: 27
# Delete: 127

# It can be divides in to 2 parts
# 1. Normal ASCII Codes (0 to 127) - Printable characters
# 2. Extended ASCII Codes (128 to 255) - Non Printable characters

print(ord('A'), ord('a',), ord('Z'), ord('z'))

print(chr(65), chr(97), chr(90), chr(122))

ch = 'A'
print(ch, chr(ord(ch) + 32))

ch = 'a'
print(ch, chr(ord(ch) - 32))


# 'A' = 65 = 64 + 1 = 0100 0001 or 0010 0000 => 32 = 0x20
# 'a' = 97 = 96 + 1 = 0110 0001 and 1101 1111 => 0xdf =  ~0x20 = ~32

# Upper to lower case using bit manupulation
myChar = 'A'
print(myChar, chr(ord(myChar) | 0x20))

# Lower to upper case using bit manupulation
myChar = 'a'
print(myChar, chr(ord(myChar) & ~0x20))


# a xor a = 0
# a xor 0 = a
# a xor a' = 1
# a xor 1 = a'

myChar = 'A'
print(myChar, chr(ord(myChar) ^ 0x20))
myChar = 'a'
print(myChar, chr(ord(myChar) ^ 0x20))