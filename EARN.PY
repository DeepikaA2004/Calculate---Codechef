# Function to calculate the minimum amount to invest
def calculate_investment(X, Y):
    return max(0, X - Y)

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    X, Y = map(int, input().split())
    investment = calculate_investment(X, Y)
    print(investment)
