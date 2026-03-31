class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # maximum length of result = m + n

        # Multiply each digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                mul = digit1 * digit2

                # Position in result array
                p1, p2 = i + j, i + j + 1

                # Add to current position
                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        # Skip leading zeros and convert to string
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str if result_str else "0"
