def count_progressions(N, k):
    count = 0
    
    # Iterate through all possible starting points
    for start in range(1, N + 1):
        # Calculate the last term of the AP
        last_term = start
        
        # Calculate the sum of the AP starting from 'start'
        ap_sum = start
        
        # Keep adding terms to the AP until the sum exceeds N
        while ap_sum <= N:
            if ap_sum == N:
                count += 1
                break
            last_term += k
            ap_sum += last_term
        
    return count

# Read input values
N, k = map(int, input().split(" "))

# Output the count of progressions
print(count_progressions(N, k))
