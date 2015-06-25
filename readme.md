# SearchName

Exemplo de um sistema buscas utilizando ElasticSearch.

## Setup

Para executar a aplicação é necessário finalizar a configuração do arquivo "settings.py"

É necessário informar as seguintes variáveis de ambiente:

- CELERY_BROKER_URL 
- HAYSTACK_URL
- HAYSTACK_INDEX 

## Tecnologias utilizadas

- Celery + Django-Celery
- ElasticSearch + Django-Haystac
- Select2
- Django Rest Framework
- Requests