import base64
import text_chunk

keys = open('./files/public.txt').readlines()
source = open('./files/primeList.txt')
output = open('./files/output.txt', 'w')

resultText = source.read()

encoded_source = base64.b64encode(bytes(resultText, "utf-8"))

print('String para criptografar: '+resultText)

chunkSize = text_chunk.block_size(int(keys[0]))
print('Defined a ' + str(chunkSize) +' chunkSize')

chunks = [encoded_source[i:i+chunkSize] for i in range(0, len(encoded_source), chunkSize)]
print(chunks)

originalChunk = ''

for chunk in chunks:
    original_chunk = text_chunk.TextChunk(chunk.decode('utf-8')).int_value()
    encoded = pow(original_chunk, int(keys[1]), int(keys[0]))
    output.write(str(encoded))
    output.write('\n')
output.close()