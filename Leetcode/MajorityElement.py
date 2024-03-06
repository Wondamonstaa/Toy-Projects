class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #Moore Voting Algorithm
        '''
        The algorithm starts by assuming the first element as the majority candidate and sets the count to 1.
        As it iterates through the array, it compares each element with the candidate:
        a. If the current element matches the candidate, it suggests that it reinforces the majority element because it appears again. Therefore, the count is incremented by 1.
        b. If the current element is different from the candidate, it suggests that there might be an equal number of occurrences of the majority element and other elements. Therefore, the count is decremented by 1.
            Note that decrementing the count doesn't change the fact that the majority element occurs more than n/2 times.
        If the count becomes 0, it means that the current candidate is no longer a potential majority element. In this case, a new candidate is chosen from the remaining elements.
        The algorithm continues this process until it has traversed the entire array.
        The final value of the candidate variable will hold the majority element.
        '''
        count: int = 0
        candidate: None = None

        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)

        return candidate
