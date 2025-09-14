# OpenMemory Provider Configuration Guide

This guide explains how to configure different LLM and embedder providers in OpenMemory.

## Quick Start

1. **Set Environment Variables**: Create a `.env` file in the `api/` directory with your API keys:

```bash
# Copy the example file
cp .env.example .env

# Edit with your API keys
nano .env
```

2. **Configure via API**: Use the configuration API endpoints to set up your providers:

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

## Environment Variables

Create a `.env` file in the `api/` directory with the following variables:

```bash
# User Configuration
USER=default_user

# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Anthropic Configuration
ANTHROPIC_API_KEY=your-anthropic-api-key-here

# Together AI Configuration
TOGETHER_API_KEY=your-together-api-key-here

# Groq Configuration
GROQ_API_KEY=your-groq-api-key-here

# Mistral Configuration
MISTRAL_API_KEY=your-mistral-api-key-here

# Google Configuration
GOOGLE_API_KEY=your-google-api-key-here

# DeepSeek Configuration
DEEPSEEK_API_KEY=your-deepseek-api-key-here

# xAI Configuration
XAI_API_KEY=your-xai-api-key-here

# LiteLLM Configuration
LITELLM_API_KEY=your-litellm-api-key-here

# LangChain Configuration
LANGCHAIN_API_KEY=your-langchain-api-key-here

# Ollama Configuration (for Docker host resolution)
OLLAMA_HOST=http://host.docker.internal:11434

# Database Configuration
DATABASE_URL=sqlite:///./openmemory.db
```

## Supported Providers

### LLM Providers

| Provider | Description | Required Fields | Optional Fields |
|----------|-------------|----------------|-----------------|
| `openai` | OpenAI API and OpenAI-compatible APIs | `model`, `api_key` | `base_url`, `temperature`, `max_tokens` |
| `ollama` | Local models via Ollama | `model`, `ollama_base_url` | `temperature`, `max_tokens` |
| `anthropic` | Claude API | `model`, `anthropic_api_key` | `temperature`, `max_tokens` |
| `together` | Together AI API | `model`, `together_api_key` | `base_url`, `temperature`, `max_tokens` |
| `groq` | Groq API | `model`, `groq_api_key` | `base_url`, `temperature`, `max_tokens` |
| `mistral` | Mistral AI API | `model`, `mistral_api_key` | `base_url`, `temperature`, `max_tokens` |
| `google` | Google AI/Gemini API | `model`, `google_api_key` | `base_url`, `temperature`, `max_tokens` |
| `deepseek` | DeepSeek API | `model`, `deepseek_api_key` | `base_url`, `temperature`, `max_tokens` |
| `xai` | xAI API | `model`, `xai_api_key` | `base_url`, `temperature`, `max_tokens` |
| `litellm` | LiteLLM API | `model`, `litellm_api_key` | `base_url`, `temperature`, `max_tokens` |
| `langchain` | LangChain API | `model`, `langchain_api_key` | `base_url`, `temperature`, `max_tokens` |

### Embedder Providers

| Provider | Description | Required Fields | Optional Fields |
|----------|-------------|----------------|-----------------|
| `openai` | OpenAI Embeddings API and OpenAI-compatible APIs | `model`, `api_key` | `base_url` |
| `ollama` | Local embedding models via Ollama | `model`, `ollama_base_url` | - |
| `anthropic` | Claude API (for embeddings) | `model`, `anthropic_api_key` | - |
| `together` | Together AI API (for embeddings) | `model`, `together_api_key` | `base_url` |
| `groq` | Groq API (for embeddings) | `model`, `groq_api_key` | `base_url` |
| `mistral` | Mistral AI API (for embeddings) | `model`, `mistral_api_key` | `base_url` |
| `google` | Google AI/Gemini API (for embeddings) | `model`, `google_api_key` | `base_url` |
| `deepseek` | DeepSeek API (for embeddings) | `model`, `deepseek_api_key` | `base_url` |
| `xai` | xAI API (for embeddings) | `model`, `xai_api_key` | `base_url` |
| `litellm` | LiteLLM API (for embeddings) | `model`, `litellm_api_key` | `base_url` |
| `langchain` | LangChain API (for embeddings) | `model`, `langchain_api_key` | `base_url` |

## Configuration Examples

### Example 1: OpenAI + OpenAI Embeddings

```json
{
  "openmemory": {
    "custom_instructions": null
  },
  "mem0": {
    "llm": {
      "provider": "openai",
      "config": {
        "model": "gpt-4o-mini",
        "temperature": 0.1,
        "max_tokens": 2000,
        "api_key": "env:OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1"
      }
    },
    "embedder": {
      "provider": "openai",
      "config": {
        "model": "text-embedding-3-small",
        "api_key": "env:OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1"
      }
    }
  }
}
```

### Example 2: Ollama + OpenAI Embeddings

```json
{
  "openmemory": {
    "custom_instructions": null
  },
  "mem0": {
    "llm": {
      "provider": "ollama",
      "config": {
        "model": "llama3.1:latest",
        "temperature": 0.1,
        "max_tokens": 2000,
        "ollama_base_url": "http://host.docker.internal:11434"
      }
    },
    "embedder": {
      "provider": "openai",
      "config": {
        "model": "text-embedding-3-small",
        "api_key": "env:OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1"
      }
    }
  }
}
```

### Example 3: Anthropic + Ollama Embeddings

```json
{
  "openmemory": {
    "custom_instructions": null
  },
  "mem0": {
    "llm": {
      "provider": "anthropic",
      "config": {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.1,
        "max_tokens": 2000,
        "anthropic_api_key": "env:ANTHROPIC_API_KEY"
      }
    },
    "embedder": {
      "provider": "ollama",
      "config": {
        "model": "nomic-embed-text:latest",
        "ollama_base_url": "http://host.docker.internal:11434"
      }
    }
  }
}
```

## API Endpoints

### Get Current Configuration
```bash
GET /api/v1/config/
```

### Update Full Configuration
```bash
PUT /api/v1/config/
Content-Type: application/json

{
  "mem0": {
    "llm": { ... },
    "embedder": { ... }
  }
}
```

### Get Supported Providers
```bash
GET /api/v1/config/providers
```

### Update Only LLM Configuration
```bash
PUT /api/v1/config/mem0/llm
Content-Type: application/json

{
  "provider": "ollama",
  "config": { ... }
}
```

### Update Only Embedder Configuration
```bash
PUT /api/v1/config/mem0/embedder
Content-Type: application/json

{
  "provider": "openai",
  "config": { ... }
}
```

### Reset to Default Configuration
```bash
POST /api/v1/config/reset
```

## Docker Configuration

When running in Docker, the system automatically detects the Docker environment and adjusts localhost URLs for Ollama to properly reach the host machine.

### Docker Host Resolution Strategies

1. `OLLAMA_HOST` environment variable (if set)
2. `host.docker.internal` (Docker Desktop for Mac/Windows)
3. Docker bridge gateway IP (typically 172.17.0.1 on Linux)
4. Fallback to 172.17.0.1

### Example Docker Compose

```yaml
services:
  openmemory-mcp:
    image: mem0/openmemory-mcp
    build: api/
    environment:
      - USER
      - OPENAI_API_KEY
      - ANTHROPIC_API_KEY
      - TOGETHER_API_KEY
      - GROQ_API_KEY
      - MISTRAL_API_KEY
      - GOOGLE_API_KEY
      - DEEPSEEK_API_KEY
      - XAI_API_KEY
      - LITELLM_API_KEY
      - LANGCHAIN_API_KEY
      - OLLAMA_HOST
    env_file:
      - api/.env
    depends_on:
      - mem0_store
    ports:
      - "8765:8765"
```

## Troubleshooting

### Common Issues

1. **Invalid Configuration**: The system validates provider configurations and falls back to defaults if invalid.

2. **Missing API Keys**: Ensure all required API keys are set in your environment variables.

3. **Docker Host Resolution**: If Ollama is not accessible from Docker, check the `OLLAMA_HOST` environment variable.

4. **Configuration Not Applied**: Configuration changes require a memory client reset. The system does this automatically when you update the configuration via API.

### Debugging

1. **Check Logs**: Look for configuration validation warnings in the application logs.

2. **Test Configuration**: Use the `/api/v1/config/providers` endpoint to see supported providers and their requirements.

3. **Validate Environment Variables**: Ensure all required environment variables are set and accessible.

## Migration from Old Configuration

If you're migrating from an older version of OpenMemory:

1. **Backup Current Configuration**: Export your current configuration using `GET /api/v1/config/`

2. **Update Configuration**: Use the new provider-specific fields in your configuration.

3. **Test Configuration**: Verify that your new configuration works by testing memory operations.

4. **Update Environment Variables**: Add any new environment variables you need for your chosen providers.
