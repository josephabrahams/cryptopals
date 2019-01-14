from cryptopals import fixed_xor


def test_fixed_xor():
    buffer1 = '1c0111001f010100061a024b53535009181c'
    buffer2 = '686974207468652062756c6c277320657965'
    result = '746865206b696420646f6e277420706c6179'
    assert fixed_xor(buffer1, buffer2) == result
