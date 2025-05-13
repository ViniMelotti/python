divida=float(input('Digite dívida: '))
juros=10
parcelas=3
calc_juros=1.1
x=0

print('Valor da divida\t Valor dos juros\t Quant. parcelas\t Valor da parcela')
print('%.2f\t \t 0\t \t \t 1\t \t \t %.2f'%(divida,(divida*1)/1))

while(x<4):
    print('%.2f\t \t %d\t \t \t %d\t \t \t %2.f'%(divida,juros,parcelas,(divida*calc_juros)/parcelas))
    x+=1
    juros+=5
    parcelas+=3
    calc_juros+=0.05