def longest_uppercase(input, k):
    chars = []
    longest = 0
    for letter in input:
        if chars.count(letter) != 0:
            longest += 1
        elif len(chars) > k-1:
            return longest
        else:
            chars.append(letter)
            longest += 1
print(longest_uppercase("hello",3))