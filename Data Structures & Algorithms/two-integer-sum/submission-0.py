class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 初始化一个空字典，用来记录 "数字 -> 该数字在数组中的下标"
        indices = {}  # val -> index
        
        # 2. 第一次遍历：把数组里的所有数字和它们的下标存入字典
        # enumerate(nums) 会同时返回元素的下标 i 和值 n
        for i, n in enumerate(nums):
            indices[n] = i  # 以数字 n 为键，下标 i 为值存入字典

        # 3. 第二次遍历：寻找符合条件的两个数
        for i, n in enumerate(nums):
            # 计算当前数字 n 需要的另一半数字是多少
            diff = target - n
            
            # 检查 diff 是否在字典中，并且 diff 的下标不能等于当前数字 n 的下标 i
            # （因为题目要求同一个元素不能使用两次）
            if diff in indices and indices[diff] != i:
                # 找到了！返回当前数字的下标 i，以及字典中记录的 diff 的下标
                return [i, indices[diff]]
        
        # 4. 如果遍历完都没找到（虽然题目保证一定有解，但加上这行更严谨）
        return []
