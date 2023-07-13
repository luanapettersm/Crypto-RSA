import text_chunk
import base64

keys = open('./files/private.txt').readlines()
source = open('./files/output.txt').readlines()
output = open('./files/outputDecrypted.txt', 'w')

result_string = ''

for line in source:
    decoded = pow(int(line), int(keys[1]), int(keys[0]))
    result_string += str(text_chunk.TextChunk(decoded))

decoded_string = base64.b64decode(bytes(result_string, "utf-8")).decode("utf-8", "ignore")
output.write(decoded_string)