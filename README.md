# OpenSearch Recipe Indexing Script

This project contains a Python script designed to index recipe data into an OpenSearch cluster. The dataset used is sourced from [Kaggle's Epicurious Recipes dataset](https://www.kaggle.com/datasets/hugodarwood/epirecipes), which provides a collection of recipes including information like ingredients, categories, calories, and ratings.

## Requirements

- Python 3.8+
- Libraries:
  - `opensearch-py`: For interacting with OpenSearch
  - `python-dotenv`: For loading environment variables
  - `json`: For loading recipe data
- OpenSearch cluster instance

### Python Packages

You can install the required Python packages using:

```bash
pip install opensearch-py python-dotenv
```

## How It Works

- Environment Setup: The script loads the OpenSearch connection details (host, port, username, and password) from a .env file using the python-dotenv library.
  OpenSearch Client Initialization: The client is configured to connect securely to an OpenSearch cluster.
- Index Mapping: A custom mapping is created for the epirecipes index, defining various fields such as title, ingredients, categories, and nutritional information.
- Data Loading: The dataset is loaded from a JSON file, and the data is processed into individual documents.
- Bulk Indexing: The documents are indexed in bulk into the OpenSearch cluster.
- Environment Variables
- Ensure that the following variables are set in your .env file:

```bash
OPENSEARCH_HOST=<your_opensearch_host>
OPENSEARCH_PORT=<your_opensearch_port>
OPENSEARCH_USERNAME=<your_opensearch_username>
OPENSEARCH_PASSWORD=<your_opensearch_password>
```

### Dataset

The dataset used in this script can be downloaded from Kaggle using the following link: [Epicurious Recipes dataset](https://www.kaggle.com/datasets/hugodarwood/epirecipes). Once downloaded, place the dataset in a data/ folder and ensure the path in the script matches.

### Running the Script

Once the environment is set up, you can run the script as follows:

```bash
python index_recipes.py
```

This will connect to the OpenSearch cluster and index all recipes from the dataset.

## Additional Information

- This script assumes the OpenSearch cluster is already running and accessible via the provided host and port.
- It creates the index if it does not exist already.
- For bulk indexing, the script uses the helpers.bulk method from opensearch-py.

# Recipe Search API

This is a FastAPI-based API that provides recipe search functionality. The API interacts with an OpenSearch instance to perform various search and filtering operations on a collection of recipes. It supports searching by query keywords, filtering by category, ingredients, and nutritional information, and retrieving available categories and ingredients from the dataset.

# Full Stack Recipe Search Platform (FastAPI + Vite)

This project consists of a **FastAPI** backend and a **Vite** frontend for a recipe search platform. This guide will help you clone the repository and set it up on your local machine.

## Features

- **Search Recipes**: Search for recipes using keywords in titles, ingredients, or instructions, with additional filters such as categories, ingredients, ratings, and protein content.
- **Filter by Categories**: Retrieve a list of unique categories from the dataset.
- **Filter by Ingredients**: Retrieve a list of unique ingredients from the dataset.
- **Pagination**: Supports pagination for search results.

## Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **Node.js** and **npm** (or **yarn**)
- **Git**

## Step-by-Step Setup Instructions

### 1. Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

### 2. Backend Setup (FastAPI)

1. Navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\\Scripts\\activate'
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create an **.env** file with the necessary environment variables:

   ```
   OPENSEARCH_HOST=localhost
   OPENSEARCH_PORT=9200
   OPENSEARCH_USERNAME=admin
   OPENSEARCH_PASSWORD=admin
   ```

5. Run the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be running on \`http://localhost:8000\`.

### 3. Frontend Setup (Vite)

1. Navigate to the frontend folder:

   ```bash
   cd ../frontend
   ```

2. Install the frontend dependencies:

   ```bash
   npm install
   ```

3. Create a **.env** file in the frontend folder with the following content:

   ```
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. Start the Vite development server:
   ```bash
   npm run dev
   ```
   The frontend will be running on \`http://localhost:5173\` (or a different port, depending on availability).

### 4. CORS Configuration for FastAPI

To allow communication between the Vite frontend and FastAPI backend, add CORS middleware to the FastAPI app:

In **main.py**:

```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # Vite frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 5. Running Both Frontend and Backend Together

1. **Start the backend**:

   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. **Start the frontend**:
   Open a new terminal window and run:
   ```bash
   cd frontend
   npm run dev
   ```

Now, your Vite-based React frontend will communicate with the FastAPI backend for recipe searching.

### License

This project is licensed under the MIT License.
