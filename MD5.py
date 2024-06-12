import math

def F(X, Y, Z):
    return (X & Y) | (~X & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y ^ (X | ~Z)

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    # Pre-processing
    message = bytearray(message, 'ascii')
    original_length_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += original_length_bits.to_bytes(8, byteorder='little')

    # Initialize variables
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    # Constants
    shifts = [7, 12, 17, 22] * 4
    constants = [int(abs(math.sin(i+1)) * 2**32) for i in range(64)]

    # Process the message in 512-bit chunks
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]

        # Initialize hash value for this chunk
        a = A
        b = B
        c = C
        d = D

        # Main loop
        for j in range(64):
            if j < 16:
                F_result = F(b, c, d)
                g = j
            elif j < 32:
                F_result = G(b, c, d)
                g = (5*j + 1) % 16
            elif j < 48:
                F_result = H(b, c, d)
                g = (3*j + 5) % 16
            else:
                F_result = I(b, c, d)
                g = (7*j) % 16

            d_temp = d
            d = c
            c = b
            b = (b + left_rotate((a + F_result + int.from_bytes(chunk[4*g:4*g+4], byteorder='little') + 
                        constants[j]), shifts[j%4])) & 0xFFFFFFFF
            a = d_temp

            # Print function values in each round
            print(f"Runda {j+1}: \nF={F_result}, \ng={g}, \na={a}, \nb={b}, \nc={c}, \nd={d}\n\n")

        # Update hash value for this chunk
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Produce the final hash value
    return "%08x%08x%08x%08x" % (A, B, C, D)

print(md5('abc').upper(),'\n\n')

