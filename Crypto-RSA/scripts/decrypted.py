import text_chunk
import base64

print('Necessário inserir o caminho completo para os arquivos.')
# keyFile = input('Arquivo com chave para criptografar: ')
# source = input('Arquivo descriptografado: ')
# output = input('Arquivo para preencher com o conteúdo descriptografado: ')

keys = open('./files/public.txt').read()
source = open('./files/output.txt').read()
output = open('./files/outputDecrypted.txt', 'w')

mod = int(keys[0])
key = int(keys[1])

resultText = ''

result = base64.b64decode(bytes(source.encode())).decode()

for line in result:
    originalChunk = pow(int(line), key, mod)
    chunk = text_chunk._int_to_str(originalChunk)
    resultText += chunk

output.write(str(resultText))