from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Digite o seu peso')],
    [sg.InputText(key='_peso_')],
    [sg.Text('Digite a sua altura')],
    [sg.InputText(key='_altura_')],
    [sg.Button('Calcular'), sg.Button('Cancelar')],
    [sg.Text('', key='_imc_')],
    [sg.Text('', key='_estado_')]
]

janela = sg.Window('Calculador de IMC', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Calcular':
        peso = float(valores['_peso_'])
        altura = float(valores['_altura_'])
        imc = peso / (altura ** 2)
        if imc < 18.5:
            janela['_imc_'].update('Seu IMC é: {:.2f}'.format(imc))
            janela['_estado_'].update('Seu estado corporal é: {}'.format('Abaixo do peso'))
    
        elif imc == 18.5 or imc <= 25:
            janela['_imc_'].update('Seu IMC é: {:.2f}'.format(imc))
            janela['_estado_'].update('Seu estado corporal é: {}'.format('Peso ideal'))
     
        elif imc == 25 or imc <= 30:
            janela['_imc_'].update('Seu IMC é: {:.2f}'.format(imc))
            janela['_estado_'].update('Seu estado corporal é: {}'.format('Sobrepeso'))

        elif imc == 30 or imc <= 40:
            janela['_imc_'].update('Seu IMC é: {:.2f}'.format(imc))
            janela['_estado_'].update('Seu estado corporal é: {}'.format('Obesidade mórbida'))
            

janela.close()
