# Seletor de Frutas
### Projeto de Automação com Sistemas Embarcados e Inteligência Artificial para seleção automática de maçãs.

## Descrição
O projeto consiste na classificação e seleção automática de maçãs boas e podres.

Uma esteira transporta maçãs. Em um determinado ponto da esteira um sensor IR detecta a passagem de uma maçã e ativa uma câmera que tira uma foto da fruta.
A foto é submetida à uma Rede InceptionV3 (Rede Neural Convolucional) treinada a partir do dataset "Fruits fresh and rotten for classification" 
disponível na plataforma [Kaggle](https://www.kaggle.com/sriramr/fruits-fresh-and-rotten-for-classification). Se a maçã for classificada como podre
um braço robótico é acionado e retira a maçã da esteira. A quantidade de maçãs podres e boas são transmitidas através do protocolo MQTT e apresentadas em um dashboard
pela plataforma FRED.
