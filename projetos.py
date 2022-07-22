#apresentação

titulo = 'Poderia digitar o seu'
agradecimento = 'Obrigado!'

print('Olá usuário!Poderia me informar o seu nome?')

nome = input('Digite seu nome:')

print(('Muito prazer {}, sejá bem vindo ao meu projeto!' .format(nome)))
print('Esse projeto vem a recolher informações do usuário e entregar um relatorio todo detalhado!')
print('Lembrando que todos os dados serão assegurados pela lei do LGPD!')



cpf   = input(titulo + ' CPF:')
rg    = input(titulo + ' RG:')
phone = input(titulo + ' CELULAR:')
mail  = input(titulo + ' E-MAIL:')

print('Endereço conforme a seguir!')

end1 = input('RUA:')
end2 = input('NUMERO:')
end3 = input('COMPLEMENTO:')
end4 = input('BAIRRO:')
end5 = input('CIDADE:')
end6 = input('ESTADO:')

print('Eu, {}, inscrito no CPF:{}, e RG:{}, autorizo o uso dos dados para cadastro na empresa' .format(nome, cpf, rg))
print('Caso necessite entrar em contato utilize o telefone {}, ou email {}' .format(phone, mail))
print('Meu endereço é Rua {}, N°{} - Complemento {}, bairro {} localizada na cidade de {} - {}' .format(end1, end2, end3, end4, end5, end6))

ok = input('Confirma os dados acima?')

print(ok)
print(agradecimento +' por utilizar!')