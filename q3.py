"""
QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

輸入：n值(0-100)
輸出：第幾順位
"""

def rank(num):
    if num <= 0 or num > 100: return False
    result = []
    
    # create all people array
    people = list(range(1, num + 1))
    
    # filter people
    for n in people:
        if n % 3 != 0:
            result.append(n)
    return result[-1]

print(rank(0))
print(rank(30))
print(rank(100))