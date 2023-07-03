import base64
import text_chunk

print('Necessário inserir o caminho completo para os arquivos.')
keyFile = input('Arquivo com chave para criptografar: ')
source = input('Arquivo criptografado: ')
output = input('Arquivo para preencher com o conteúdo criptografado: ')

keyFile = open(keyFile)
source = open(source)
output = open(output, 'w')

keys = keyFile.readlines()

mod = int(keys[0])
key = int(keys[1])

text = source.readlines()
resultText = ''

for line in resultText:
    resultText += line

print('String para criptografar: '+resultText)

chunkSize = text_chunk.block_size(mod)
print('Defined a ' + str(chunkSize) +' chunkSize')

encoded = base64.b64encode(bytes(resultText.encode())).decode()

chunks = [encoded[i:i+chunkSize] for i in range(0, len(encoded), chunkSize)]
print(chunks)

for chunk in chunks:
    
    originalChunk = text_chunk.TextChunk(chunk).int_value()

    result = pow(originalChunk, key, mod)
    
    output.write(str(result))