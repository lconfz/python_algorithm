"""
队列 (Queue) — 🟢 Beginner
打开 README.md 查看完整说明。用你的实现替换 TODO。

任务 1:用列表实现 MyQueue
任务 2:实现击鼓传花 hot_potato(names, k)
"""
from collections import deque


class MyQueue:
    """基于 Python list 的队列,队尾在列表末尾。"""

    def __init__(self):
        # TODO: 初始化内部存储
        self._queue = deque()

    def enqueue(self, x):
        # TODO: 将 x 加入队尾
        self._queue.append(x)

    def dequeue(self):
        # TODO: 取出并返回队头元素;空队列返回 None
        if self.is_empty():
            return None
        return self._queue.popleft()

    def front(self):
        # TODO: 返回队头元素但不取出;空队列返回 None
        if self.is_empty():
            return None
        return self._queue[0]

    def is_empty(self):
        # TODO: 队列为空返回 True
        return not self._queue

    def size(self):
        # TODO: 返回元素个数
        return len(self._queue)

    def __repr__(self):
        return f"MyQueue:{self._queue}"


def hot_potato(names: list, k: int) -> str:
    """击鼓传花:names 围成一圈报数,数到 k 出局,返回最后留下的人。"""
    # TODO: 用队列实现
    if not names or k < 0:
        return ""

    queue = MyQueue()
    for name in names:
        queue.enqueue(name)

    while queue.size() != 1:
        steps = (k - 1) % queue.size()
        for _ in range(steps):
            tmp = queue.dequeue()
            queue.enqueue(tmp)

        queue.dequeue()

    return queue.front()


# === 测试用例 ===
def run_tests():
    # --- MyQueue ---
    q = MyQueue()
    assert q.is_empty() and q.size() == 0, "初始应为空队列"
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3, "enqueue 后 size 应为 3"
    assert q.front() == 1, "front 应返回 1 且不取出"
    assert q.size() == 3, "front 不应改变队列"
    assert q.dequeue() == 1, "dequeue 应返回 1"
    assert q.dequeue() == 2, "dequeue 应返回 2"
    assert not q.is_empty(), "队列还未空"
    assert q.dequeue() == 3
    assert q.is_empty(), "全部取出后应为空"
    assert q.dequeue() is None, "空队列 dequeue 应返回 None"
    assert q.front() is None, "空队列 front 应返回 None"

    # --- hot_potato ---
    assert hot_potato(["A", "B", "C", "D", "E"], 3) == "D", "5 人报数 3 应留下 D"
    assert hot_potato(["A", "B"], 1) == "B", "报数 1 每次淘汰队头,最后留下 B"
    assert hot_potato(["A"], 5) == "A", "只有一个人时直接返回"
    assert hot_potato(["A", "B", "C"], 5) == "A", "3 人报数 5 应留下 A"

    print("✅ 全部测试通过!")


if __name__ == "__main__":
    run_tests()
