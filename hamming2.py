def hamming_code(data):
    n = len(data)
    r = 0
    while (2 ** r) < (n + r + 1):
        r += 1

    data = list(data[::-1])
    code = []
    j = 0
    for i in range(1, n + r + 1):
        if i == 2 ** j:
            code.append('0')  # Placeholder for parity bits
            j += 1
        else:
            code.append(data.pop(0))

    for i in range(r):
        parity_pos = 2 ** i
        parity_sum = 0
        for j in range(parity_pos, len(code) + 1):
            if j & parity_pos:
                parity_sum ^= int(code[j - 1])
        code[parity_pos - 1] = str(parity_sum)

    return ''.join(code[::-1])


dataword = input("Enter dataword: ")
encoded_data = hamming_code(dataword)
print(f"Encoded data with Hamming Code: {encoded_data}")
