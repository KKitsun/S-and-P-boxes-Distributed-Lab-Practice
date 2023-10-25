# S-box table (forward and inverse)
s_box = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8]
]

# Forward S-box transformation
def s_box_forward(input_data):
    # divide 8-bit input
    t1, t2 = (input_data >> 4) & 0xF, input_data & 0xF
    # substitution using table
    s1, s2 = s_box[0][t1], s_box[1][t2]
    return (s1 << 4) | s2

# Reverse S-box transformation
def s_box_reverse(input_data):
    s1, s2 = (input_data >> 4) & 0xF, input_data & 0xF
    t1, t2 = s_box[0].index(s1), s_box[1].index(s2)
    return (t1 << 4) | t2

def p_box(input_data):
    # bit reverse as a p-box formula:
    output_data = 0
    for i in range(8):
        output_data |= ((input_data >> i) & 1) << (7 - i)

    return output_data

# Test function to verify forward and reverse transformations
def test_sbox_pbox():
    data = 0b11010101

    print("S-box test bin. input data = 0b11010101")
    sbox_forward_result = s_box_forward(data)
    print(bin(sbox_forward_result))
    sbox_reverse_result = s_box_reverse(sbox_forward_result)
    print(bin(sbox_reverse_result))
    assert sbox_reverse_result == data, "S-box transformation failed"

    print("P-box test bin. input data = 0b11010101")
    pbox_result = p_box(data)
    print(bin(pbox_result))
    pbox_reverse_result = p_box(pbox_result)
    print(bin(pbox_reverse_result))
    assert pbox_reverse_result == data, "P-box transformation failed"

    print("---------------------------------")

    data2 = 0xd5

    print("S-box test hex. input data = 0xd5")
    sbox_forward_result2 = s_box_forward(data2)
    print(hex(sbox_forward_result2))
    sbox_reverse_result2 = s_box_reverse(sbox_forward_result2)
    print(hex(sbox_reverse_result2))
    assert sbox_reverse_result2 == data2, "S-box transformation failed"

    print("P-box test hex. input data = 0xd5")
    pbox_result2 = p_box(data2)
    print(hex(pbox_result2))
    pbox_reverse_result2 = p_box(pbox_result2)
    print(hex(pbox_reverse_result2))
    assert pbox_reverse_result2 == data2, "P-box transformation failed"

    print("---------------------------------")
    data3 = 88

    print("S-box test dec. input data = 88")
    sbox_forward_result3 = s_box_forward(data3)
    print(sbox_forward_result3)
    sbox_reverse_result3 = s_box_reverse(sbox_forward_result3)
    print(sbox_reverse_result3)
    assert sbox_reverse_result3 == data3, "S-box transformation failed"

    print("P-box test dec. input data = 88")
    pbox_result3 = p_box(data3)
    print(pbox_result3)
    pbox_reverse_result3 = p_box(pbox_result3)
    print(pbox_reverse_result3)
    assert pbox_reverse_result3 == data3, "P-box transformation failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_sbox_pbox()
