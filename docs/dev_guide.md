# Developer Guide

## Setting Up the Development Environment

### Prerequisites
- Python 3.x
- PostgreSQL
- MongoDB
- Redis

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/face-reco.git
    cd face-reco
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python src/utils/init_db.py
    ```

5. Run the application:
    ```bash
    python src/app.py
    ```

## Running Tests
To run the tests, execute:
```bash
python -m unittest discover -s src/tests
