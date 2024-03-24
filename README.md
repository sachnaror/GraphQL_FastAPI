## GraphQL FastAPI Example

This repository contains a simple example of integrating GraphQL with FastAPI, a modern, fast (high-performance) web framework for building APIs with Python. The project demonstrates how to set up a GraphQL server using FastAPI and interact with it using GraphQL queries.

**Features**

* **FastAPI:** Utilizes FastAPI for building robust and high-performance APIs.
* **GraphQL Integration:** Demonstrates how to integrate GraphQL with FastAPI.
* **Sample Schema:** Provides a sample GraphQL schema with example queries and mutations.
* **Interactive API Documentation:** Utilizes Swagger UI and Redoc to generate interactive API documentation.

**Requirements**

* Python 3.7+
* pip

**Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/sachnaror/GraphQL_FastAPI.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GraphQL_FastAPI
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

**Usage**

1. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Access the GraphQL playground in your browser:

   ```bash
   http://localhost:8000/graphql
   ```

Use the GraphQL playground to interact with the API by executing queries and mutations.

**API Documentation**

* **Swagger UI:** Access the Swagger UI for interactive API documentation:

   ```bash
   http://localhost:8000/docs
   ```

* **Redoc:** Alternatively, access API documentation using Redoc:

   ```bash
   http://localhost:8000/redoc
   ```

**Contributing**

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.
