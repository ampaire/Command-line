import click
import requests


import requests


usersChoice = "Choose from:BBC, CBC News, MSNBC, ABC News(AU)"


@click.command()
@click.option('--source', prompt=usersChoice)
def cli(source):

    if source == 'BBC':
        url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=b31b5993d4494c6db43c1a986fe4fc6f&pagesize=10"

    elif source == 'CBC News':
        url = "https://newsapi.org/v2/top-headlines?sources=cbc-news&apiKey=b31b5993d4494c6db43c1a986fe4fc6f&pagesize=10"

    elif source == 'MSNBC':

        url = "https://newsapi.org/v2/top-headlines?sources=msnbc&apiKey=b31b5993d4494c6db43c1a986fe4fc6f&pagesize=10"

    elif source == 'ABC News(AU)':
        url = "https://newsapi.org/v2/top-headlines?sources=abc-news-au&apiKey=b31b5993d4494c6db43c1a986fe4fc6f&pagesize=10"

    else:
        raise TypeError('Invalid Input')

    news_request = requests.get(url)
    main_dict = news_request.json()
    articles = main_dict['articles']
    countArticles = 1
    for article in articles:
        click.echo(countArticles)
        click.echo(article['title'])
        click.echo(article['description'])
        click.echo(article['url'])
        countArticles += 1


cli()

