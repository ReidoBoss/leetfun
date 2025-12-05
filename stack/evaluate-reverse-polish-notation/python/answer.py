from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNums = []

        for token in tokens:
            isOperation = token == "+" or token == "-" or token == "/" or token == "*"
            if isOperation:
                first = stackNums.pop()
                second = stackNums.pop()
                opResult = int(eval(f"{second} {token} {first}"))
                stackNums.append(opResult)

            else:
                stackNums.append(token)

        return int(stackNums[-1])


print(Solution.evalRPN(Solution(), ["2", "1", "+", "3", "*"]))  # 9
print(Solution.evalRPN(Solution(), ["4", "13", "5", "/", "+"]))  # 6


print(
    Solution.evalRPN(
        Solution(),
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    )
)  # 22
