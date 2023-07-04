import text_chunk
import base64

keys = open('./files/public.txt').readlines()
source = open('./files/output.txt').read()
output = open('./files/outputDecrypted.txt', 'w')

chunk = ''

result = base64.b64decode(bytes(source.encode())).decode()

for line in result.split(','):
    if line == '\n' or line == '':
        chunk += '\n'
    else:
        chunk += text_chunk._int_to_str(int(line))

output.write(str(chunk))