# API Search Peoples

## Narrativa
Uma empresa precisa de uma api para calcular a taxa de sucesso de busca de pessoas baseado em algumas informações entregues por ela ou por terceiros
Quantos mais informações for aprovado das pessoas, mais vai ser a taxa de sucesso da busca.
Cada pessoa tem uma taxa que é determinado pela seguinte formula 
```
    T = If + Tf + C + Lf
       _______________
             4
```
T = Taxa de Encontro
I = Instagram calculo final
T = Twitter calculo final
C = Certidões pessoais
Lf = Local de Moradia calculo final  

As pessoas devem ser filtradas por essa taxa e entregues com base de quanto vai ser necessario no pedido.

Os calculos filtrados devem seguir esse padrão:
```
    IT = quantidade de paginas encontradas
    Para IT > 4 o calculo de Δf IT * 0.75
    Para IT > 6 o calculo deve ser desconsiderado retornando um valor -1 para invalidar a quantidade e recomendar reavaliação
```

Vai ser enviado uma taxa base e uma taxa limite, o backend deve entregar as pessoas com essa taxa
O backend deve conferir com certa frequencia se as pessoas encontradas nos filtros ainda estão validas, conferindo se o twitter ainda existe, se o instagram ainda existe, se ainda reside naquele local e se o cpf ainda está ativo.
