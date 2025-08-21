# API Search Peoples

## Narrativa
Uma empresa precisa de uma api para encontrar pessoas com algumas informações entregues por ela ou por terceiros
Quantos mais informações for aprovado das pessoas, mais vai ser a taxa de sucesso da busca.
Cada pessoa tem uma taxa que é determinado pela seguinte formula 
```
    T = I + T + C + L
       _______________
             4
```
T = Taxa de Encontro
I = Instagram
T = Twitter
C = Certidões pessoais
L = Local de Moradia  

As pessoas devem ser filtradas por essa taxa e entregues com base de quanto vai ser necessario no pedido.

Vai ser enviado uma taxa base e uma taxa limite, o backend deve entregar as pessoas com essa taxa
O backend deve conferir com certa frequencia se as pessoas encontradas nos filtros ainda estão validas, conferindo se o twitter ainda existe, se o instagram ainda existe, se ainda reside naquele local e se o cpf ainda está ativo.
