#Recursive Solution
class Solution:
    def climbing_stairs(self, n: int) -> int:
        return n if n <= 2 else self.climbing_stairs(n-1) + self.climbing_stairs(n-2)

    def run_test(self, input, expected_output):
        print(f'Input: {input}')
        output = self.climbing_stairs(input)
        print(f'Output: {output}')
        assert output == expected_output, f'Output: {output}, Expected output: {expected_output}'
        print()

# Tests
solution = Solution()
print('Tests:')
solution.run_test(2, 2)
solution.run_test(3, 3)
solution.run_test(4, 5)
solution.run_test(5, 8)
solution.run_test(6, 13)


#Iterative Solution
class Solution:
    def climbing_stairs(self, n: int) -> int:
        if n <= 2: 
            return n

        #Initialize pointers
        step_prev_2 = 1
        step_prev_1 = 2
        step_n = 0

        for step in range(3, n + 1):
            # Calculate current_step with 2 previous steps
            step_n =  step_prev_1 + step_prev_2
            # Update pointers for previous steps
            step_prev_2 = step_prev_1
            step_prev_1 = step_n
        return step_n

    def run_test(self, input, expected_output):
        print(f'Input: {input}')
        output = self.climbing_stairs(input)
        print(f'Output: {output}')
        assert output == expected_output, f'Output: {output}, Expected output: {expected_output}'
        print()

# Tests
solution = Solution()
print('Tests:')
solution.run_test(2, 2)
solution.run_test(3, 3)
solution.run_test(4, 5)
solution.run_test(5, 8)
solution.run_test(6, 13)