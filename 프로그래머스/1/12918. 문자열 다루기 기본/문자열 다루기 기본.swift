func solution(_ s:String) -> Bool {
    if (s.count == 4) || (s.count == 6) {
        for word in s {
            if !word.isNumber {
                return false
            }
        }    
    } else {
        return false
    }
    return true
}