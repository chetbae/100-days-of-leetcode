class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val complements = mutableMapOf<Int, Int>()
        for ((i, num) in nums.withIndex()) {
            val complement = target - num
            if (complements.containsKey(complement)) {
                return intArrayOf(i, complements[complement]!!)
            }

            complements.put(num, i)
        }

        throw IllegalArgumentException("no two sum")
    }
}