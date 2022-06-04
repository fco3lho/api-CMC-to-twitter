# Coleta de preços para postagem no Twitter

<p> 
  O seguinte código tem a função de coletar o preço de 8 diferentes criptomoedas do site <a href="https://coinmarketcap.com">CoinMarketCap</a> usando a API disponibilizada pelo site para salvar os preços em variáveis utilizadas posteriormente para serem postadas no <a href="twitter.com">Twitter</a> de forma automatizada.
</p>
 
## Metodologia
 
<p>
 Inicialmente, para se conseguir acesso às APIs, foi necessário criar contas de desenvolvedor nas duas diferentes plataformas para conseguir as chaves de acesso pelo código. Exemplo do consumo das chaves abaixo:
</p><br>

 <p align="center"><i>Consumo de chaves do Twitter</i></p>
 
```python
consumer_key = 'e5li8B6cfykjNEeyqxX4GNwzn' #Insert the API Key obtained from your Twitter account.
consumer_secret = 'Flum69PWJQjk7cI7SiYfRlT6JT3tAo0MQRBVT83LSgc7Tjo2BA' #Insert the API Key Secret obtained from your Twitter account.
access_token = '1395928461425710088-v7XvUYOpYwjASuzAVa9cIphHQiZBKd' #Insert the Access Key obtained from your Twitter account.
access_token_secret = 'WBBdXonBp20MhZXulp5JZvx7CWA9pdVf7LJwXHTdTDs01' #Insert the Access Key Secret obtained from your Twitter account.

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication, wait_on_rate_limit = True)
```
<br>

<p align="center"><i>Consumo de chaves do CoinMarketCap</i></p>

```python
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7b3r6u13-e0ap-3400-816f-ba9a0a4af7b4' #Insert the key obtained from your CoinMarketCap account.
}

session = Session()
session.headers.update(headers)
```

<br>

<p>
Foi passado o endereço onde continham os preços atualizados a todo momento de todas as criptomoedas existentes no site e salvo na variável <code>url</code>. Após isso, foram criados parâmetros para a coleta dos preços atuais, a variação dessas moedas nas últimas 24 horas. Agora utilizando os parâmetros passados e recursos disponibilizados pela API, foi usado o XPath para a coleta do preço, salvo na variável <code>price_btc</code> e para a coleta da variação nas últimas 24 horas, salvo na variável <code>change_24h_btc</code>. Exemplo do código da coleta de dados do Bitcoin abaixo:
</p>

<br>

```python
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters_btc = {
 'slug': 'bitcoin',
 'convert': 'USD'
}

response = session.get(url, params = parameters_btc)
price_btc = float(json.loads(response.text)['data']['1']['quote']['USD']['price'])
change_24h_btc = float(json.loads(response.text)['data']['1']['quote']['USD']['percent_change_24h'])
```

<br>

<p>
 Possuindo o preço e a variação salvos em uma variável, agora é só utilizar a API do Twitter para postar o preço dessas moedas utilizando essas variáveis. Exemplo de código abaixo:
</p>

<br>

```python
  api.update_status('BTC: ${:.2f}'.format(price_btc) + ' ↔️ % 24h: {:.2f}'.format(change_24h_btc))
```
<p align="center"><i>Obs.: O comando <code>api.update_status()</code> serve para fazer a postagem de uma string no Twitter.</i></p>

<br>

### Observações

<ul>
 <li>Todo o código apresentado acima foi implementado dentro de um laço de repetição para durar até que o programa seja interrompido ou encontre um erro, mas o laço é repetido de tempo em tempo específicado no código usando a função <code>time.sleep()</code>, sendo o padrão programado para repetir de 15 em 15 minutos.</li>
 
 <li>Foi descrito na metodologia a coleta de dados de apenas uma criptomoeda.</li>
</ul>

## Resultados

Serão apresentados aqui algumas imagens das postagens feitas pelo código sendo executado, mas você também pode conferir as postagens feitas na conta clicando <a href="https://twitter.com/yourcryptocoins">aqui</a>. Clicando nas postagens feitas, é possível analisar ao lado do horário e data da postagem como aquele tweet foi feito, estará escrito o nome do projeto criado para o consumo de API, nomeado de <code>cmc_bot_twitter</code>.

### Imagens

<p align="center">
 <img height="250rem" src="/imgs/1.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/2.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/3.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/4.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/5.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/6.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/7.jpg">
</p>

<p align="center">
 <img height="250rem" src="/imgs/8.jpg">
</p>

## Considerações

Este é um projeto básico, mas que pode ser utilizado para diferentes nichos de diversas formas. Pensando na coleta de dados dos preços feita aqui, uma boa utilização que pode ser feita utilizando um projeto como esse, é a coleta de dados de ativos para fundos de investimento ou para cálculos financeiros que requerem um retorno rápido.
