class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for x in logs:
            if x== "../":
                if depth != 0:
                    depth -= 1
            elif x != "./":
                depth += 1
        return depth if depth>0 else 0