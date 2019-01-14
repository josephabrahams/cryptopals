"""
Implement repeating-key XOR
"""


def repeatingkey_xor(message, key):
    encoded_message = []

    for i, letter in enumerate(message):
        encoded_message.append(ord(letter) ^ ord(key[i % len(key)]))

    return bytes(encoded_message).decode('ascii')


# https://stackoverflow.com/a/31007358
def edit_distance(str1, str2):
    s1 = ''.join(format(ord(l), '8b') for l in str1)
    s2 = ''.join(format(ord(l), '8b') for l in str2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def detect_keysize(data, num_samples=2, ks_min=2, ks_max=40):

    edit_distances = []

    if num_samples <= 1:
        raise Exception('num_samples must be greater than 1')

    if ks_min <= 1:
        raise Exception('ks_min must be greater than 1')

    if ks_max < ks_min:
        raise Exception('ks_max must be greater than ks_min')

    if 2 * ks_max * num_samples > len(data):
        raise Exception(
                'length of data must be greater than 2 * ks_mas * num_samples')

    for ks in range(ks_min, ks_max+1):
        samples = []
        sample_size = 2*ks
        for i in range(0, num_samples):
            offset = sample_size * i
            str1 = data[offset:offset+ks]
            str2 = data[offset+ks:offset+ks*2]
            ed = edit_distance(str1, str2)
            ed_norm = ed / ks
            samples.append(ed_norm)
            samples_mean = sum(samples) / num_samples
        edit_distances.append(samples_mean)

    return edit_distances.index(min(edit_distances)) + ks_min
