# Rasterização de retas e polígonos

![RasterizacaoRetasPoligonos](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/02d203e5-5189-4d48-ae38-5a2ab1cbb581)

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

![RasterizacaoRetas](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/7c2b8b97-fd58-4e66-94b0-43e2f1536093)

## Imagem ilustrativa da saída da interface da rasterização de retas:

![RetaRasterizada](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/2056d49e-6e2a-4056-801d-3c072a8503e8)

## Imagem ilustrativa da interface da rasterização de polígonos:

![RasterizacaoPoligonos](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/19838807-1e71-4eec-8071-124ee15bdf33)

## Imagem ilustrativa da saída da interface da rasterização de polígonos:

![PoligonosRasterizada](https://github.com/MateusMaccos/RasterizaRestasEPoligonos/assets/75508372/58f6c3e7-6c9a-466a-8cb2-4b7d51bc1a87)

