### Installation

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:harshit2786/tunestream-ws.git
cd project-directory
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:
```bash
pip install fastapi uvicorn openai python-decouple
```

4. Add .env file with OpenAI API key:

```bash
OPENAI_API_KEY=your_key
```

### Getting Started

To run the development server, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server on http://localhost:8000.