from opensearchpy import OpenSearch
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# OpenSearch connection details from .env
host = os.getenv('OPENSEARCH_HOST')
port = int(os.getenv('OPENSEARCH_PORT'))
auth = (os.getenv('OPENSEARCH_USERNAME'), os.getenv('OPENSEARCH_PASSWORD'))

# Initialize OpenSearch client
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_compress=True,
    http_auth=auth,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

index_name = 'epirecipes'





