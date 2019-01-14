from cryptopals import repeatingkey_xor
from cryptopals import utils

key = 'ICE'
message = (
        "Burning 'em, if you ain't quick and nimble\n"
        "I go crazy when I hear a cymbal")
encoded_message = (
        '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d'
        '63343c2a26226324272765272a282b2f20430a652e2c652a31'
        '24333a653e2b2027630c692b20283165286326302e27282f')


def test_repeatingkey_xor():
    assert utils.ascii_to_hex(
            repeatingkey_xor.repeatingkey_xor(message, key)) == encoded_message


def test_detect_keysize():
    assert repeatingkey_xor.detect_keysize(
            utils.hex_to_ascii(encoded_message),
            num_samples=3, ks_max=10) == len(key)


def test_edit_distance():
    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    assert repeatingkey_xor.edit_distance(s1, s2) == 37
