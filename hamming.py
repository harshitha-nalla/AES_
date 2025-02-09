def calculate_redundant_bits(m):
    """Calculate the number of redundant bits required."""
    for i in range(m):
        if (2 ** i) >= m + i + 1:
            return i

def position_redundant_bits(data, r):
    """Position the redundant bits in the data."""
    j = 0
    k = 1
    m = len(data)
    res = ""

    for i in range(1, m + r + 1):
        if i == (2 ** j):
            res += '0'  # Placeholder for redundant bit
            j += 1
        else:
            res += data[-1 * k]
            k += 1

    return res[::-1]

def calculate_parity_bits(arr, r):
    """Calculate the parity bits based on current data."""
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 * i)) == (2 * i):
                val ^= int(arr[-1 * j])
        arr = arr[:n - (2 * i)] + str(val) + arr[n - (2 * i) + 1:]

    return arr

def detect_error(arr, r):
    """Detect errors in the received data."""
    n = len(arr)
    res = 0

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2 * i)) == (2 * i):
                val ^= int(arr[-1 * j])
        res += val * (10 ** i)

    return int(str(res), 2)

# Main program
data = input("Enter the data bits: ")
m = len(data)
r = calculate_redundant_bits(m)

# Position and calculate parity bits
arr = position_redundant_bits(data, r)
arr = calculate_parity_bits(arr, r)
print("Data transferred is:", arr)

# Input received data for error detection
received = input("Enter the received data: ")
error_position = detect_error(received, r)

if error_position == 0:
    print("There is no error in the received message.")
else:
    print(f"The position of error is {len(received) - error_position} from the left.")
