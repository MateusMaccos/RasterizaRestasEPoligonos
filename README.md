# Rasterização de retas e polígonos

![RasterizacaoRetasPoligonos](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/548b568c-f271-467b-b38b-dff5adbb0285)

## Implementação
Na implementação/desenvolvimento do trabalho para rasterização de retas:
- Foram obtidas imagens da rasterização de 4 ou mais semirretas diferentes para 5 resoluções
diferentes e comparado as retas geradas. Para isto, foram definidas as posições das semirretas.
- Foi considerado que as semirretas são definidas no contínuo em um espaço normalizado
bidimensional com componentes (x1 e x2) na faixa [-1,+1] e então convertidos para as
resoluções 100 x 100, 300 x 300, 600 x 600, 800 x 600 e 1920 x 1080.
- Foi implementado tal algoritmo para as situações nas quais |Δx| > |Δy| e |Δy| > |Δx|.
- Foi implementado considerando situações em que as semirretas crescem (m > 0) ou
decrescem (m < 0).
- Foram avaliadas situações e ajuste o algoritmo para situações na qual se tem uma reta na
vertical ou na horizontal. Logo, adicionado duas semirretas, uma vertical e outra
horizontal.
- Foi avaliado e implementado considerando que há mais de uma semirreta ao mesmo tempo
na imagem.
Na implementação/desenvolvimento do trabalho para rasterização de polígonos:
- Foram obtidas imagens da rasterização de 6 ou mais polígonos (triângulo equiláteros,
quadrados e hexágonos – 2 para cada) também para 5 resoluções diferentes.
- Foi considerado que as polígonos são definidas no contínuo em um espaço normalizado
bidimensional com componentes (x1 e x2) na faixa [-1,+1] e então convertidos para as
resoluções 100 x 100, 300 x 300, 600 x 600, 800 x 600 e 1920 x 1080.
- Foi avaliado e implementado considerando que há mais de um polígono ao mesmo tempo na
imagem.
Foi criado uma interface gráfica para o usuário informar os pontos que compõem as retas e
os polígonos, bem como para que o mesmo informe a resolução dos objetos. Nela é mostrado o
modelo no contínuo e a imagem resultante na resolução escolhida.

## Imagem ilustrativa da interface da rasterização de retas:

![RasterizacaoRetas](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/ce0c6bd7-5c83-4354-ad01-d7107aa51dd4)

## Imagem ilustrativa da saída da interface da rasterização de retas:

![RetaRasterizada](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/298ac1bc-46ef-4a0a-847a-bd4ca9b65d43)

## Imagem ilustrativa da interface da rasterização de polígonos:

![RasterizacaoPoligonos](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/39af28b9-22ac-46f0-bc1a-74cd34f547e9)

## Imagem ilustrativa da saída da interface da rasterização de polígonos:

![PoligonosRasterizada](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/52b1dfef-ad83-4a2d-b4c1-f338835210c3)

