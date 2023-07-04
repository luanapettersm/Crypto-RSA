def _int_to_str(n: int) -> str:
    if n == 0:
        string_val = "0"
    else:
        string_val = ""

        while n > 0:
            quot, rem = divmod(n, 256)
            char_num = rem
            string_val += chr(char_num)
            n = quot

    return str(string_val)


def block_size(n: int) -> int:
    bsize = 0
    temp = n - 1

    while temp > 1:
        temp = int(temp / 2)
        bsize += 1

    return int(bsize/8)


class TextChunk:
    _string_val: str

    def __init__(self, n):
        if isinstance(n, str):
            self._string_val = n
        else:
            self._string_val = _int_to_str(n)

    def int_value(self) -> int:
        result = 0

        for c in reversed(self._string_val):
            result = result * 256
            result += ord(c)

        return result

    def __str__(self):
        return self._string_val
