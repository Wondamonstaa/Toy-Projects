class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        
        auto it = std::remove(nums.begin(), nums.end(), val);

        // Erase the unwanted elements
        nums.erase(it, nums.end());
        
        return nums.size();
    }
};
