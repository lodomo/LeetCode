class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        BINARY = 2
        result = list(bin(num1)[2:])
        result_len = len(result)
        set_bits = bin(num2).count('1')
        cur_bits = bin(num1).count('1')

        if set_bits == cur_bits:
            return num1

        diff = abs(set_bits - cur_bits)

        if set_bits > cur_bits:
            for i in range(result_len - 1, -1, -1):
                if diff == 0:
                    break
                if result[i] == '0':
                    result[i] = '1'
                    diff -= 1

            if diff > 0:
                result = ['1'] * diff + result

        if set_bits < cur_bits:
            for i in range(result_len - 1, -1, -1):
                if diff == 0:
                    break
                if result[i] == '1':
                    result[i] = '0'
                    diff -= 1

        return int(''.join(result), BINARY)


num1 = 25
num2 = 72

print(Solution().minimizeXor(num1, num2))
