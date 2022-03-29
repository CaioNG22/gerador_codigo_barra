from barcode import EAN13
from barcode.writer import ImageWriter

# recebe o caminho do arquivo
caminhoDoCodigo = input('Cole o caminho onde será salvo o arquivo:')

# recebe o nome do codigo
nomeDoCodigo = input('Digite o nome do arquivo:')

# recebe o codigo
numeroDoCodigo = input('Digite o código: (OBS: O código deve ter 13 números)')

# conta quantos numeros tem o codigo
qntNumeros = len(numeroDoCodigo)

# verifica e certifica a quantidade de numero do codigo
while qntNumeros != 13:
    numeroDoCodigo = input(
        'digite novamente (OBS: Deve conter exatamente 13 dígitos, se tiver menos, complete com 0): ')
    qntNumeros = len(numeroDoCodigo)

# gera e salva o codigo de barra no diretório especificado:
with open(rf'{caminhoDoCodigo}\{nomeDoCodigo}.png', 'wb') as f:
    EAN13(f'{numeroDoCodigo}', writer=ImageWriter()).write(f)
# mensagem de êxito
print('Arquivo criado com êxito!')
