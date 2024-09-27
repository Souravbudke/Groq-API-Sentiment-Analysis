# Groq API Sentiment Analysis

This project uses the Groq API to analyze the sentiment of reviews provided in an uploaded file (CSV or Excel format). The Flask application reads the file, processes the reviews, and returns the sentiment analysis results.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Souravbudke/Groq-API-Sentiment-Analysis.git
    cd Groq-API-Sentiment-Analysis
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory of the project.
    - Add your Groq API key to the `.env` file:
        ```
        GROQ_API_KEY=your_groq_api_key_here
        ```

## Running the Project

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. The application will run on [`http://127.0.0.1:5000`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsouravbudke%2Fsenti%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A53%2C%22character%22%3A13%7D%7D%5D%2C%22e4b0adba-9772-4b9e-b4ad-6db84782cb0f%22%5D "Go to definition").

## Usage

- Endpoint: `/analyze`
- Method: [`POST`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fsouravbudke%2Fsenti%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A53%2C%22character%22%3A8%7D%7D%5D%2C%22e4b0adba-9772-4b9e-b4ad-6db84782cb0f%22%5D "Go to definition")
- Description: Upload a file (CSV or Excel) containing reviews to analyze their sentiment.

### Example Request

```sh
curl -X POST http://127.0.0.1:5000/analyze -F 'file=@path_to_your_file.csv'
