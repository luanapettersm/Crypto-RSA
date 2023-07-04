import base64
import text_chunk

keys = open('./files/private.txt').readlines()
source = open('./files/primeList.txt')
output = open('./files/output.txt', 'w')

resultText = source.read()

print('String para criptografar: '+resultText)

chunkSize = text_chunk.block_size(len(resultText))
print('Defined a ' + str(chunkSize) +' chunkSize')

chunks = [resultText[i:i+chunkSize] for i in range(0, len(resultText), chunkSize)]
print(chunks)

originalChunk = ''

for chunk in chunks:
    
    originalChunk += str(text_chunk.TextChunk(chunk).int_value())
    originalChunk += ','

encoded = base64.b64encode(bytes(originalChunk.encode())).decode()
output.write(str(encoded))