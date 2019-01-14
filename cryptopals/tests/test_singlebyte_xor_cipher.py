from cryptopals import singlebyte_xor_cipher


def test_singlebyte_xor_cipher():
    hex_str = \
        '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    message, key, score = singlebyte_xor_cipher(hex_str)
    assert message == "Cooking MC's like a pound of bacon"
