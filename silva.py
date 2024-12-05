#solicita o valor da compra
valor_compra = float(input("digitep valor da compra")
                     
#solicita a forma de pagamento
print("escolha aforma de pagamento")
print("1-a vista(10%de desconto)")
print("2-cartao de credito(em ate 3x)")
opcao_pagamento = int(input("digiteo numero da opcao"))
    
#calcula o valor final
if opcao_pagamento == 1
   valor_final = valor_compra * 0.9
   print(f"valor com desconto r$ {valor_final.2f}")
   elif opcao_pagamento == 2
   parcela = valor_compra / 3
   print(f"valor por parcela (3x) r$ {parcela.2f}")
else:
    print("opcao invalida. tente novamente")
   

 