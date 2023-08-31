"""
國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，請用一個函數來將學生的成績修正。

輸入: [35, 46, 57, 91, 29]
輸出: [53, 64, 75, 19, 92]
"""


def correctScore(scores):
    if len(scores) == 0: return False
    result = []
    for score in scores:
        score = int(str(score)[::-1])
        result.append(score)
    return result


print(correctScore([35, 46, 57, 91, 29]))
