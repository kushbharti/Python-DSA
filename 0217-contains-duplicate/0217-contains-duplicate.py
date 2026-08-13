class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: set = set()  # Initialize empty set
        
        for num in nums:  # Check every element
            if num not in seen:  # If element not yet seen, add it
                seen.add(num)
            else:  # If element has been seen, there's a duplicate
                return True
        return False  # All elements checked, no duplicates