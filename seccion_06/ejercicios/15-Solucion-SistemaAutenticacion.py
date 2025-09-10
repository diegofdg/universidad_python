print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_ingresado = input('Cual es tu usuario? ')
password_ingresado = input('Cual es tu password? ')

son_datos_correctos = (usuario_ingresado.strip() == USUARIO_VALIDO
                       and password_ingresado.strip() == PASSWORD_VALIDO)

print(f'Datos son correctos? {son_datos_correctos}')