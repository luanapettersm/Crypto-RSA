import text_chunk
import base64

print('Necessário inserir o caminho completo para os arquivos.')
keyFile = input('Arquivo com chave para criptografar: ')
source = input('Arquivo descriptografado: ')
output = input('Arquivo para preencher com o conteúdo descriptografado: ')

keyFile = open(keyFile)
source = open(source).readlines()
output = open(output, 'w')

keys = keyFile.readlines()

mod = int(keys[0])
key = int(keys[1])

resultText = ''

for line in source:
    originalChunk = pow(int(line), key, mod)
    chunk = text_chunk._int_to_str(originalChunk)
    resultText += chunk

result = base64.b64decode(bytes(resultText.encode())).decode()
    
output.write(str(result))