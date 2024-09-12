function findMaxAverage(nums: number[], k: number): number {
    
    let currentSum: number = nums.slice(0, k).reduce((acc, num) => acc + num, 0);
    let max_sum: number = currentSum;

    for (let i = k; i < nums.length; i++){
        currentSum += nums[i] - nums[i - k];
        max_sum = Math.max(max_sum, currentSum);
    }
    
    let average: number = max_sum / k;

    return average
};
