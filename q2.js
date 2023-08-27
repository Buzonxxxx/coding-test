// 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

// 輸出：
// 0 1
// 6 1
// A 4
// C 2
// E 5
// H 3
// ....(繼續印下去)

const charCount = s => {
    if (s.length === 0) return false
    
    const result = {}
    s = s.toUpperCase().split(' ').join('') // HELLOWELCOMETOCATHAY60THYEARANNIVERSARY
    s = s.split('').sort().join('') // 06AAAAACCEEEEEHHHILLLMNNOOORRRSTTTVWYYY

    // count each char
    for (let char of s) {
        if (result[char]) {
            result[char]++
        } else {
            result[char] = 1
        }
    }

    return result
}

console.log(charCount("Hello welcome to Cathay 60th year anniversary"));