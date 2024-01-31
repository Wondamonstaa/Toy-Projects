class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::set<int> s;

        //  std::unique algorithm will move duplicates to the end
        auto it = std::unique(nums.begin(), nums.end());

        // Erase the duplicates from the vector
        nums.erase(it, nums.end());

        return nums.size();
    }
};
