"""
栈 (Stack) — 🟢 Beginner
打开 README.md 查看完整说明。用你的实现替换 TODO。

任务 1:用列表实现 MyStack
任务 2:实现括号匹配 is_balanced(s)
"""

import sys

# Windows 控制台默认 GBK 编码,无法输出 emoji,强制切换为 UTF-8
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


class MyStack:
    """基于 Python list 的栈,栈顶在列表末尾。"""

    def __init__(self):
        # TODO: 初始化内部存储
        self._stack = []

    def push(self, x):
        # TODO: 将 x 压入栈顶
        self._stack.append(x)

    def pop(self):
        # TODO: 弹出并返回栈顶元素;空栈返回 None
        if self.is_empty():
            return None
        return self._stack.pop()

    def top(self):
        # TODO: 返回栈顶元素但不弹出;空栈返回 None
        if self.is_empty():
            return None
        return self._stack[-1]

    def is_empty(self):
        # TODO: 栈为空返回 True
        return not self._stack

    def size(self):
        # TODO: 返回元素个数
        return len(self._stack)

    def __repr__(self):
        return f"MyStack({self._stack})"


def is_balanced(s: str) -> bool:
    """判断括号串 s 是否匹配,匹配返回 True。"""
    # TODO: 用栈实现
    pattern = {")": "(", "}": "{", "]": "["}
    front = ('(', '[', '{')
    back = (')', ']', '}')

    if not s:
        return True
    stack = MyStack()
    for ch in s:
        if ch in front:
            stack.push(ch)
        elif ch in back:
            if stack.is_empty() or stack.top() != pattern[ch]:
                return False
            stack.pop()
    return stack.is_empty()


# === 测试用例 ===
def run_tests():
    # --- MyStack ---
    st = MyStack()
    assert st.is_empty() and st.size() == 0, "初始应为空栈"
    st.push(1)
    st.push(2)
    st.push(3)
    assert st.size() == 3, "push 后 size 应为 3"
    assert st.top() == 3, "top 应返回 3 且不弹出"
    assert st.size() == 3, "top 不应改变栈"
    assert st.pop() == 3, "pop 应返回 3"
    assert st.pop() == 2, "pop 应返回 2"
    assert not st.is_empty(), "栈还未空"
    assert st.pop() == 1
    assert st.is_empty(), "全部弹出后应为空"
    assert st.pop() is None, "空栈 pop 应返回 None"
    assert st.top() is None, "空栈 top 应返回 None"

    # --- is_balanced ---
    balanced_cases = ["", "()", "([])", "{[()]}", "((()))", "[{()}([])]"]
    unbalanced_cases = ["(", ")", ")(", "([)]", "({})[", "((()", "[}]"]

    for case in balanced_cases:
        assert is_balanced(case), f"应匹配: {case!r}"
    for case in unbalanced_cases:
        assert not is_balanced(case), f"不应匹配: {case!r}"

    print("✅ 全部测试通过!")


if __name__ == "__main__":
    run_tests()
