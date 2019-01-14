from cryptopals import utils

message = "I'm killing your brain like a poisonous mushroom"
hex_str = ('49276d206b696c6c696e6720796f757220627261696e206c'
           '696b65206120706f69736f6e6f7573206d757368726f6f6d')
base64_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def test_ascii_to_hex():
    assert utils.ascii_to_hex(message) == hex_str


def test_hex_to_ascii():
    assert utils.hex_to_ascii(hex_str) == message


def test_base64_to_hex():
    assert utils.base64_to_hex(base64_str) == hex_str


def test_hex_to_base64():
    assert utils.hex_to_base64(hex_str) == base64_str
