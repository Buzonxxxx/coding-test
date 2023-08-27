// QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
// 請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

// 輸入：n值(0-100)
// 輸出：第幾順位

const rank = num => {
    if (num < 0 || num > 100) return false

    // create all people array
    let people = []
    for (let i = 1; i <= num; i++) {
        people.push(i);
    }

    // filter people
    let result = []
    for (let person of people) {
        if (person % 3 !== 0) {
            result.push(person)
        }
    }
    console.log(result);
    
    // return rank
    return result[result.length -1]
}

console.log(rank(3));