"""
國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

輸出：
0 1
6 1
A 4
C 2
E 5
H 3
....(繼續印下去)
"""


def charCount(s):
    if len(s) == 0: return False
    result = {}
    s = s.replace(' ', '').upper()  # HELLOWELCOMETOCATHAY60THYEARANNIVERSARY
    sorted_str = ''.join(sorted(s))  # 06AAAAACCEEEEEHHHILLLMNNOOORRRSTTTVWYYY

    for char in sorted_str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    for char, count in result.items():
        print(char, count)


charCount("Hello welcome to Cathay 60th year anniversary")
