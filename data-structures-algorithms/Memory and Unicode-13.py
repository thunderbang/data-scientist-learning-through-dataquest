## 2. The Basics of Binary ##

# Let's say b is a binary number.  In python, we have to store binary numbers as strings.
# If we try to enter it directly as b = 10, Python will assume it's a base 10 integer.
b = "10"

# Now, we can convert b from a string to a binary number with the int function. We'll need to set the optional second argument, base, to 2 (binary is base two).
print(int(b, 2))
base_10_100 = int("100", 2)

## 3. Binary Addition ##

# a is in base 10 -- because we have 10 possible digits, the highest value we can represent with one digit is 9.
a = 9

# When we want to represent a value one higher, we need to add another digit.
a += 1
# a now has two digits -- we incremented the invisible leading digit, which was 0 and is now 1, and set the last digit back to zero.
print(a)

# When we add 1 to 19, we increment the leading 1 by 1, and then set the last digit to 0, giving us 20.
a = 19
a += 1

# When we add 1 to 99, we increment the last digit by 1, and add 1 to the first digit, but the first digit is now greater than 9, so we have to increment the invisible leading digit.
a = 99
a += 1

# Binary addition works the exact same way, except the highest value any single digit can represent is 1.
b = "1"

# We'll add binary values using a binary_add function that was made just for this exercise.
# It's not extremely important to know how it works right this second.
def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

c = binary_add(b, "1")

# We now see that c equals "10", which is exactly what happens in base 10 when we reach the highest possible digit.
print(c)

# c now equals "11"
c = binary_add(c, "1")
print(c)

# c now equals "100"
c = binary_add(c, "1")
print(c)
c = binary_add(c, "10")

## 4. Converting Binary Values to Other Bases ##

def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Start both at 0
a = 0
b = "0"

# Loop 10 times
for i in range(0, 10):
    # Add 1 to each
    a += 1
    b = binary_add(b, "1")

    # Check if they are equal
    print(int(b, 2) == a)

# The cool thing here is that a and b are always equal if we add the same amount to both.
# This is because base 2 and base 10 are just ways to write numbers.
# Counting 100 apples in base 2 or base 10 will always give us an equivalent result - we just have to convert between them.
# We can represent any number in binary; we just need to use more digits than we would in base 10.
base_10_1001 = int("1001", 2)

## 5. Converting Characters to Binary ##

# We can use the ord() function to get the integer for an ASCII character.
ord('a')

# Then, we use the bin() function to convert to binary.
# The bin function adds "0b" to the beginning of a string to indicate that it contains binary values.
bin(ord('a'))

# ÿ is the "last" ASCII character; it has the highest integer value of any ASCII character.
# This is because 255 is the highest value we can represent with eight binary digits.
ord('ÿ')
# As you can see, we get eight 1's, which shows that this is the highest possible eight-digit value.
bin(ord('ÿ'))

# Why is this?  Because a single binary digit is called a bit, and computers store values in sequences of eight bits (i.e., a byte).
# You might be more familiar with kilobytes or megabytes. A kilobyte is 1000 bytes, and a megabyte is 1000 kilobytes.
# There are 256 different ASCII symbols, because the largest amount of storage any single ASCII character can take up is one byte.
binary_w = bin(ord("w"))
binary_bracket = bin(ord("}"))

## 6. Introduction to Unicode ##

# We can initialize Unicode code points (the value for this code point is \u27F6, but you see it as a character here because the Dataquest system is automatically converting it).
code_point = "⟶"

# This particular code point maps to a right arrow character.
print(code_point)

# We can get the base 10 integer value of the code point with the ord function.
print(ord(code_point))

# As you can see, this takes up a lot more than 1 byte.
print(bin(ord(code_point)))
code_point = "မ"
binary_1019 = bin(ord(code_point))

## 7. Strings with Unicode ##

s1 = "café"
# The \u prefix means "the next four digits are a Unicode code point"
# It doesn't change the value at all (the last character in the string below is \u00e9)
s2 = "café"

# These strings are the same, because code points are equal to their corresponding Unicode characters.
# \u00e9 and é are equivalent.
print(s1 == s2)
s3 = "hello မ"

## 8. The Bytes Data Type ##

# We can make a string with some Unicode values
superman = "Clark Kent␦"
print(superman)

# This tells Python to encode the string superman as Unicode using the UTF-8 encoding system
# We end up with a sequence of bytes instead of a string
superman_bytes = "Clark Kent␦".encode("utf-8")

batman = "Bruce Wayne␦"
batman_bytes = batman.encode("utf-8")