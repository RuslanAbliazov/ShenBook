# import WithoutArrays
# these code is just training for python course
def get_sum_of_numerals(text: str) -> int:
    def is_numeral(char: str) -> bool:
        if len(char) == 1 and char in '0123456789':
            return True
    i = 0
    ans = 0

    while i < len(text):
        if is_numeral(text[i]):
            ans += int(text[i])
            i += 1
        while i < len(text) and not is_numeral(text[i]):
            i += 1
    return ans


print(get_sum_of_numerals('ah-ha123abrcadabra'))
