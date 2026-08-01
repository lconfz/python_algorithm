"""
数组与列表 — 练习（🟢 Beginner）
打开 README.md 查看完整说明。用你的实现替换每个 TODO。
完成后运行:  python starter.py
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
# 任务 1：原地去重（有序数组）
# 给定有序数组 nums，原地删除重复元素，使每个元素只出现一次，
# 返回新长度。不要使用额外数组空间，空间复杂度 O(1)。
# 例：nums = [0,0,1,1,1,2,2,3,3,4] → 返回 5，nums 前 5 位为 [0,1,2,3,4]


def remove_duplicates(nums):
    # TODO: 实现：原地去重，快慢指针
    if not nums:
        return 0
    i = j = 1
    while j < len(nums):
        if nums[j] != nums[i-1]:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i


# 任务 2：旋转数组
# 原地旋转数组，将元素向右移动 k 步。
# 例：nums = [1,2,3,4,5,6,7], k = 3 → nums 变为 [5,6,7,1,2,3,4]
# 注意：k 可能大于数组长度（k=10 等价于 k=3），要求原地 O(1) 额外空间
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    # TODO: 实现
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums) - 1)


# 任务 3：移动零
# 把数组中所有 0 移到末尾，保持非零元素的相对顺序，原地修改。
# 例：nums = [0,1,0,3,12] → nums 变为 [1,3,12,0,0]
def move_zeros(nums):
    # TODO: 实现:双指针
    i, j = 1, 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i-1], nums[j] = nums[j], nums[i-1]
            i += 1
        j += 1
    return nums


# === 测试用例 ===
def run_tests():
    # 任务 1
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    n = remove_duplicates(nums1)
    assert n == 5 and nums1[:5] == [
        0, 1, 2, 3, 4], f"任务1失败: 返回 {n}, nums1={nums1}"
    print("✓ 任务 1 通过")

    # 任务 2
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums2, 3)
    assert nums2 == [5, 6, 7, 1, 2, 3, 4], f"任务2失败: {nums2}"
    rotate(nums2, 5)  # k > 长度
    assert nums2 == [7, 1, 2, 3, 4, 5, 6], f"任务2(大k)失败: {nums2}"
    print("✓ 任务 2 通过")

    # 任务 3
    nums3 = [0, 1, 0, 3, 12]
    move_zeros(nums3)
    assert nums3 == [1, 3, 12, 0, 0], f"任务3失败: {nums3}"
    nums4 = [0, 0, 1]
    move_zeros(nums4)
    assert nums4 == [1, 0, 0], f"任务3(连续0)失败: {nums4}"
    nums5 = [1, 0, 2]
    move_zeros(nums5)
    assert nums5 == [1, 2, 0], f"任务3(中间夹0)失败: {nums5}"
    print("✓ 任务 3 通过")

    print("🎉 全部通过！")


if __name__ == "__main__":
    run_tests()
