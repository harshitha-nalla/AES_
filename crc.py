def compute_crc(data, divisor):
    data += '0' * (len(divisor) - 1)  # Append zeros
    data = list(data)
    divisor = list(divisor)

    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':  # Perform XOR
            for j in range(len(divisor)):
                data[i + j] = '0' if data[i + j] == divisor[j] else '1'

    return ''.join(data[-(len(divisor) - 1):])


dataword = input("Enter dataword (binary): ")
divisor = input("Enter divisor (binary): ")
remainder = compute_crc(dataword, divisor)
print(f"CRC remainder: {remainder}")
print(f"Transmitted data: {dataword + remainder}")
