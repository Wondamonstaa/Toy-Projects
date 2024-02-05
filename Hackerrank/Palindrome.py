def solution(inputString) -> bool:
    
    inputString = inputString.replace(" ", "").lower()
    
    return inputString == inputString[::-1]
