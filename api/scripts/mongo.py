import os

mongo_url = 'https://ap-southeast-1.aws.data.mongodb-api.com/app/data-dlwtatk/endpoint/data/v1/action/find'

mongo_payload = {
    'collection': 'instagram',
    'database': 'instagram',
    'dataSource': 'cluster-e0925482',
    'limit': 49000
}

mongo_headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': os.environ['MONGO_API_KEY']
}