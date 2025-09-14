# OpenMemory API

This directory contains the backend API for OpenMemory, built with FastAPI and SQLAlchemy. This also runs the Mem0 MCP Server that you can use with MCP clients to remember things.

## 🚀 New Features: Multi-Provider Support

OpenMemory now supports multiple LLM and embedder providers:

### Supported LLM Providers
- **OpenAI** - OpenAI API and OpenAI-compatible APIs
- **Ollama** - Local models via Ollama
- **Anthropic** - Claude API
- **Together AI** - Together AI API
- **Groq** - Groq API
- **Mistral** - Mistral AI API
- **Google** - Google AI/Gemini API
- **DeepSeek** - DeepSeek API
- **xAI** - xAI API
- **LiteLLM** - LiteLLM API
- **LangChain** - LangChain API

### Supported Embedder Providers
- **OpenAI** - OpenAI Embeddings API and OpenAI-compatible APIs
- **Ollama** - Local embedding models via Ollama
- **Anthropic** - Claude API (for embeddings)
- **Together AI** - Together AI API (for embeddings)
- **Groq** - Groq API (for embeddings)
- **Mistral** - Mistral AI API (for embeddings)
- **Google** - Google AI/Gemini API (for embeddings)
- **DeepSeek** - DeepSeek API (for embeddings)
- **xAI** - xAI API (for embeddings)
- **LiteLLM** - LiteLLM API (for embeddings)
- **LangChain** - LangChain API (for embeddings)

### Quick Configuration

Configure providers via API:

```bash
# Get current configuration
curl http://localhost:8765/api/v1/config/

# Update LLM to use Ollama
curl -X PUT http://localhost:8765/api/v1/config/mem0/llm \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "ollama",
    "config": {
      "model": "llama3.1:latest",
      "temperature": 0.1,
      "max_tokens": 2000,
      "ollama_base_url": "http://host.docker.internal:11434"
    }
  }'

# Update embedder to use OpenAI
curl -X PUT http://localhost:8765/api/v1/config/mem0/embedder \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "openai",
    "config": {
      "model": "text-embedding-3-small",
      "api_key": "env:OPENAI_API_KEY",
      "base_url": "https://api.openai.com/v1"
    }
  }'
```

For detailed configuration examples, see [PROVIDER_CONFIGURATION.md](./PROVIDER_CONFIGURATION.md).

## Quick Start with Docker (Recommended)

The easiest way to get started is using Docker. Make sure you have Docker and Docker Compose installed.

1. Build the containers:
```bash
make build
```

2. Create `.env` file:
```bash
make env
```

Once you run this command, edit the file `api/.env` and enter the `OPENAI_API_KEY`.

3. Start the services:
```bash
make up
```

The API will be available at `http://localhost:8765`

### Common Docker Commands

- View logs: `make logs`
- Open shell in container: `make shell`
- Run database migrations: `make migrate`
- Run tests: `make test`
- Run tests and clean up: `make test-clean`
- Stop containers: `make down`

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8765/docs`
- ReDoc: `http://localhost:8765/redoc`

## Project Structure

- `app/`: Main application code
  - `models.py`: Database models
  - `database.py`: Database configuration
  - `routers/`: API route handlers
- `migrations/`: Database migration files
- `tests/`: Test files
- `alembic/`: Alembic migration configuration
- `main.py`: Application entry point

## Development Guidelines

- Follow PEP 8 style guide
- Use type hints
- Write tests for new features
- Update documentation when making changes
- Run migrations for database changes
