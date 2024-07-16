func solution(_ s:String) -> String {
    let words = s.components(separatedBy: " ")
    
    print(words)
    var answer: String = ""
    
    for j in words {
        for i in 0 ..< j.count {
            let index = j.index(s.startIndex, offsetBy: i)

            if i % 2 != 0 {
                answer += j[index].lowercased()
            }
            else {
                answer += j[index].uppercased()
            }
        }
        
        answer += " "
    }
    answer = String(answer.dropLast())
    
    return answer
}