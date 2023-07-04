import base64
import text_chunk

print('Necessário inserir o caminho completo para os arquivos.')
# keyFile = input('Arquivo com chave para criptografar: ')
# source = input('Arquivo criptografado: ')
# output = input('Arquivo para preencher com o conteúdo criptografado: ')

# Abrir arquivos
keyFile = open('./files/private.txt')
source = open('./files/primeList.txt')
output = open('./files/output.txt', 'w')

# Lido o keyFiles
keys = keyFile.read()

mod = int(keys[0])
key = int(keys[1])

# Lido o source
resultText = source.read()

print('String para criptografar: '+resultText)

chunkSize = text_chunk.block_size(mod)
print('Defined a ' + str(chunkSize) +' chunkSize')

chunks = [resultText[i:i+chunkSize] for i in range(0, len(resultText), chunkSize)]
print(chunks)

result = ''

for chunk in chunks:
    
    originalChunk = text_chunk.TextChunk(chunk).int_value()

    result += pow(originalChunk, key, mod)   

encoded = base64.b64encode(bytes(resultText.encode())).decode()
output.write(str(encoded))