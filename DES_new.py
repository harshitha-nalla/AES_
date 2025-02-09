def S_box(m_48):  #takes 48-bit string as input and converts to 32-bit with 8 s-boxes
    sbox_table = [
    [[0b1110, 0b0100, 0b1101, 0b0001, 0b0010, 0b1111, 0b1011, 0b1000, 0b0011, 0b1010, 0b0110, 0b1100, 0b0101, 0b1001,
              0b0000, 0b0111],
             [0b0000, 0b1111, 0b0111, 0b0100, 0b1110, 0b0010, 0b1101, 0b0001, 0b1010, 0b0110, 0b1100, 0b1011, 0b1001, 0b0101,
              0b0011, 0b1000],
             [0b0100, 0b0001, 0b1110, 0b1000, 0b1101, 0b0110, 0b0010, 0b1011, 0b1111, 0b1100, 0b1001, 0b0111, 0b0011, 0b1010,
              0b0101, 0b0000],
             [0b1111, 0b1100, 0b1000, 0b0010, 0b0100, 0b1001, 0b0001, 0b0111, 0b0101, 0b1011, 0b0011, 0b1110, 0b1010, 0b0000,
              0b0110, 0b1101]],
            [[0b1111, 0b0001, 0b1000, 0b1110, 0b0110, 0b1011, 0b0011, 0b0100, 0b1001, 0b0111, 0b0010, 0b1101, 0b1100, 0b0000,
              0b0101, 0b1010],
             [0b0011, 0b1101, 0b0100, 0b0111, 0b1111, 0b0010, 0b1000, 0b1110, 0b1100, 0b0000, 0b0001, 0b1010, 0b0110, 0b1001,
              0b1011, 0b0101],
             [0b0000, 0b1110, 0b0111, 0b1011, 0b1010, 0b0100, 0b1101, 0b0001, 0b0101, 0b1000, 0b1100, 0b0110, 0b1001, 0b0011,
              0b0010, 0b1111],
             [0b1101, 0b1000, 0b1010, 0b0001, 0b0011, 0b1111, 0b0100, 0b0010, 0b1011, 0b0110, 0b0111, 0b1100, 0b0000, 0b0101,
              0b1110, 0b1001]],
            [[0b1010, 0b0000, 0b1001, 0b1110, 0b0110, 0b0011, 0b1111, 0b0101, 0b0001, 0b1101, 0b1100, 0b0111, 0b1011, 0b0100,
              0b0010, 0b1000],
             [0b1101, 0b0111, 0b0000, 0b1001, 0b0011, 0b0100, 0b0110, 0b1010, 0b0010, 0b1000, 0b0101, 0b1110, 0b1100, 0b1011,
              0b1111, 0b0001],
             [0b1101, 0b0110, 0b0100, 0b1001, 0b1000, 0b1111, 0b0011, 0b0000, 0b1011, 0b0001, 0b0010, 0b1100, 0b0101, 0b1010,
              0b1110, 0b0111],
             [0b0001, 0b1010, 0b1101, 0b0000, 0b0110, 0b1001, 0b1000, 0b0111, 0b0100, 0b1111, 0b1110, 0b0011, 0b1011, 0b0101,
              0b0010, 0b1100]],
            [[0b0111, 0b1101, 0b1110, 0b0011, 0b0000, 0b0110, 0b1001, 0b1010, 0b0001, 0b0010, 0b1000, 0b0101, 0b1011, 0b1100,
              0b0100, 0b1111],
             [0b1101, 0b1000, 0b1011, 0b0101, 0b0110, 0b1111, 0b0000, 0b0011, 0b0100, 0b0111, 0b0010, 0b1100, 0b0001, 0b1010,
              0b1110, 0b1001],
             [0b1010, 0b0110, 0b1001, 0b0000, 0b1100, 0b1011, 0b0111, 0b1101, 0b1111, 0b0001, 0b0011, 0b1110, 0b0101, 0b0010,
              0b1000, 0b0100],
             [0b0011, 0b1111, 0b0000, 0b0110, 0b1010, 0b0001, 0b1101, 0b1000, 0b1001, 0b0100, 0b0101, 0b1011, 0b1100, 0b0111,
              0b0010, 0b1110]],
            [[0b0010, 0b1100, 0b0100, 0b0001, 0b0111, 0b1010, 0b1011, 0b0110, 0b1000, 0b0101, 0b0011, 0b1111, 0b1101, 0b0000,
              0b1110, 0b1001],
             [0b1110, 0b1011, 0b0010, 0b1100, 0b0100, 0b0111, 0b1101, 0b0001, 0b0101, 0b0000, 0b1111, 0b1010, 0b0011, 0b1001,
              0b1000, 0b0110],
             [0b0100, 0b0010, 0b0001, 0b1011, 0b1010, 0b1101, 0b0111, 0b1000, 0b1111, 0b1001, 0b1100, 0b0101, 0b0110, 0b0011,
              0b0000, 0b1110],
             [0b1011, 0b1000, 0b1100, 0b0111, 0b0001, 0b1110, 0b0010, 0b1101, 0b0110, 0b1111, 0b0000, 0b1001, 0b1010, 0b0100,
              0b0101, 0b0011]],
            [[0b1100, 0b0001, 0b1010, 0b1111, 0b1001, 0b0010, 0b0110, 0b1000, 0b0000, 0b1101, 0b0011, 0b0100, 0b1110, 0b0111,
              0b0101, 0b1011],
             [0b1010, 0b1111, 0b0100, 0b0010, 0b0111, 0b1100, 0b1001, 0b0101, 0b0110, 0b0001, 0b1101, 0b1110, 0b0000, 0b1011,
              0b0011, 0b1000],
             [0b1001, 0b1110, 0b1111, 0b0101, 0b0010, 0b1000, 0b1100, 0b0011, 0b0111, 0b0000, 0b0100, 0b1010, 0b0001, 0b1101,
              0b1011, 0b0110],
             [0b0100, 0b0011, 0b0010, 0b1100, 0b1001, 0b0101, 0b1111, 0b1010, 0b1011, 0b1110, 0b0001, 0b0111, 0b0110, 0b0000,
              0b1000, 0b1101]],
            [[0b0100, 0b1011, 0b0010, 0b1110, 0b1111, 0b0000, 0b1000, 0b1101, 0b0011, 0b1100, 0b1001, 0b0111, 0b0101, 0b1010,
              0b0110, 0b0001],
             [0b1101, 0b0000, 0b1011, 0b0111, 0b0100, 0b1001, 0b0001, 0b1010, 0b1110, 0b0011, 0b0101, 0b1100, 0b0010, 0b1111,
              0b1000, 0b0110],
             [0b0001, 0b0100, 0b1011, 0b1101, 0b1100, 0b0011, 0b0111, 0b1110, 0b1010, 0b1111, 0b0110, 0b1000, 0b0000, 0b0101,
              0b1001, 0b0010],
             [0b0110, 0b1011, 0b1101, 0b1000, 0b0001, 0b0100, 0b1010, 0b0111, 0b1001, 0b0101, 0b0000, 0b1111, 0b1110, 0b0010,
              0b0011, 0b1100]],
            [[0b1101, 0b0010, 0b1000, 0b0100, 0b0110, 0b1111, 0b1011, 0b0001, 0b1010, 0b1001, 0b0011, 0b1110, 0b0101, 0b0000,
              0b1100, 0b0111],
             [0b0001, 0b1111, 0b1101, 0b1000, 0b1010, 0b0011, 0b0111, 0b0100, 0b1100, 0b0101, 0b0110, 0b1011, 0b0000, 0b1110,
              0b1001, 0b0010],
             [0b0111, 0b1011, 0b0100, 0b0001, 0b1001, 0b1100, 0b1110, 0b0010, 0b0000, 0b0110, 0b1010, 0b1101, 0b1111, 0b0011,
              0b0101, 0b1000],
             [0b0010, 0b0001, 0b1110, 0b0111, 0b0100, 0b1010, 0b1000, 0b1101, 0b1111, 0b1100, 0b1001, 0b0000, 0b0011, 0b0101,
              0b0110, 0b1011]]]

    m_32 = ""
    for i in range(1, 9):
        m_6 = m_48[6 * (i - 1):6 * (i)]
        row = int(m_6[0] + m_6[5], 2)
        col = int(m_6[1:5], 2)
        m_32 += format(sbox_table[i - 1][row][col], '04b')
    return m_32


def lcs(m):
    return m[1:] + m[0]


def PC_1(key):  # takes 64-bit key and makes it into 56-bit left and right keys
    l_key = [57, 49, 41, 33, 25, 17, 9,
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36]
    r_key = [63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4]
    left_key = ""
    right_key = ""
    for i in l_key:
        left_key += key[i - 1]
    for i in r_key:
        right_key += key[i - 1]
    return left_key, right_key


def PC_2(key):  # takes 56 bits key and makes it to 48 bits
    pc2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]
    n_key = ""
    for i in pc2:
        n_key += key[i - 1]
    return n_key


def round(l, r, key):
    exp = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17,
           18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    r_exp = ""
    for i in exp:
        r_exp += r[i - 1]
    xor_msg = ""
    for i in range(0, 48):
        xor_msg += str(int(r_exp[i]) ^ int(key[i]))
    r_s = S_box(xor_msg)
    p_lst = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
             11, 4, 25]
    n_r = ""
    for i in p_lst:
        n_r += r_s[i - 1]
    round_msg = ""
    for i in range(0, 32):
        round_msg += str(int(l[i]) ^ int(n_r[i]))
    return r + round_msg


def DES(msg, key):
    initial_p_matrix = [58, 50, 42, 34, 26, 18, 10, 2,
                        60, 52, 44, 36, 28, 20, 12, 4,
                        62, 54, 46, 38, 30, 22, 14, 6,
                        64, 56, 48, 40, 32, 24, 16, 8,
                        57, 49, 41, 33, 25, 17, 9, 1,
                        59, 51, 43, 35, 27, 19, 11, 3,
                        61, 53, 45, 37, 29, 21, 13, 5,
                        63, 55, 47, 39, 31, 23, 15, 7]

    inverse_p_matrix = [40, 8, 48, 16, 56, 24, 64, 32,
                        39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28,
                        35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26,
                        33, 1, 41, 9, 49, 17, 57, 25]
    m1 = ""
    for i in initial_p_matrix:
        m1 += msg[i - 1]
    lkey1, rkey1 = PC_1(key)
    for r in range(0, 16):
        if (r + 1 == 1 or r + 1 == 2 or r + 1 == 9 or r + 1 == 16):
            l_key = lcs(lkey1)
            r_key = lcs(rkey1)
        else:
            l_key = lcs(lcs(lkey1))
            r_key = lcs(lcs(rkey1))

        lkey1 = l_key
        rkey1 = r_key
        new_key = PC_2(l_key + r_key)
        m1 = round(m1[0:32], m1[32:64], new_key)
        print("Round " + str(r + 1) + " msg:" + m1)
    m_32_bit_swap = m1[32:64] + m1[0:32]
    cipher_text = ""
    for i in inverse_p_matrix:
        cipher_text += m_32_bit_swap[i - 1]
    return cipher_text


def DES_decrypt(cipher_text, key):
    initial_p_matrix = [58, 50, 42, 34, 26, 18, 10, 2,
                        60, 52, 44, 36, 28, 20, 12, 4,
                        62, 54, 46, 38, 30, 22, 14, 6,
                        64, 56, 48, 40, 32, 24, 16, 8,
                        57, 49, 41, 33, 25, 17, 9, 1,
                        59, 51, 43, 35, 27, 19, 11, 3,
                        61, 53, 45, 37, 29, 21, 13, 5,
                        63, 55, 47, 39, 31, 23, 15, 7]

    inverse_p_matrix = [40, 8, 48, 16, 56, 24, 64, 32,
                        39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28,
                        35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26,
                        33, 1, 41, 9, 49, 17, 57, 25]

    # Generate all round keys first
    lkey1, rkey1 = PC_1(key)
    round_keys = []
    for r in range(0, 16):
        if (r + 1 == 1 or r + 1 == 2 or r + 1 == 9 or r + 1 == 16):
            lkey1 = lcs(lkey1)
            rkey1 = lcs(rkey1)
        else:
            lkey1 = lcs(lcs(lkey1))
            rkey1 = lcs(lcs(rkey1))
        round_keys.append(PC_2(lkey1 + rkey1))

    # Reverse the round keys for decryption
    round_keys.reverse()

    # Initial permutation
    m1 = ""
    for i in initial_p_matrix:
        m1 += cipher_text[i - 1]

    # 16 rounds of decryption
    for r in range(0, 16):
        m1 = round(m1[0:32], m1[32:64], round_keys[r])
        print("Round " + str(r + 1) + " msg:" + m1)

    # 32-bit swap
    m_32_bit_swap = m1[32:64] + m1[0:32]

    # Final permutation
    plain_text = ""
    for i in inverse_p_matrix:
        plain_text += m_32_bit_swap[i - 1]

    return plain_text


# Function to convert binary string to original message
def binary_to_string(binary_str):
    if len(binary_str) % 8 != 0:
        binary_str = binary_str.zfill(len(binary_str) + (8 - len(binary_str) % 8))
    char_bits = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
    message = ''.join(chr(int(b, 2)) for b in char_bits)
    return message


# Main program
msg = input("Enter the message: ")
msg = msg.replace(" ", "")
msg_bin = ''.join(format(ord(c), '08b') for c in msg)

# Pad the message to a multiple of 64 bits
if len(msg_bin) % 64 != 0:
    padding_length = 64 - (len(msg_bin) % 64)
    msg_bin += '0' * padding_length

# Fix key processing
main_key = "srmapuni"
key_bin = ''.join(format(ord(c), '08b') for c in main_key)
if len(key_bin) < 64:
    padding_length = 64 - len(key_bin)
    key_bin += '0' * padding_length

# Encryption
Encrypted_msg = ""
for i in range(0, len(msg_bin), 64):
    Encrypted_msg += DES(msg_bin[i:i + 64], key_bin)
Encrypted_msg = binary_to_string(Encrypted_msg)

print("The encrypted message is: " + Encrypted_msg)

# Decryption
Encrypted_msg_bin = ''.join(format(ord(c), '08b') for c in Encrypted_msg)
Decrypted_msg = ""
for i in range(0, len(Encrypted_msg_bin), 64):
    Decrypted_msg += DES_decrypt(Encrypted_msg_bin[i:i + 64], key_bin)

# Remove padding
Decrypted_msg = binary_to_string(Decrypted_msg).rstrip('0')

print("The decrypted message is: " + Decrypted_msg)