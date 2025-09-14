# OpenMemory Provider Configuration Examples

This document provides examples of how to configure different LLM and embedder providers in OpenMemory.

## Supported Providers

### LLM Providers
- **OpenAI**: OpenAI API and OpenAI-compatible APIs
- **Ollama**: Local models via Ollama
- **Anthropic**: Claude API
- **Together**: Together AI API
- **Groq**: Groq API
- **Mistral**: Mistral AI API
- **Google**: Google AI/Gemini API
- **DeepSeek**: DeepSeek API
- **xAI**: xAI API
- **LiteLLM**: LiteLLM API
- **LangChain**: LangChain API

### Embedder Providers
- **OpenAI**: OpenAI Embeddings API and OpenAI-compatible APIs
- **Ollama**: Local embedding models via Ollama
- **Anthropic**: Claude API (for embeddings)
- **Together**: Together AI API (for embeddings)
- **Groq**: Groq API (for embeddings)
- **Mistral**: Mistral AI API (for embeddings)
- **Google**: Google AI/Gemini API (for embeddings)
- **DeepSeek**: DeepSeek API (for embeddings)
- **xAI**: xAI API (for embeddings)
- **LiteLLM**: LiteLLM API (for embeddings)
- **LangChain**: LangChain API (for embeddings)

## Configuration Examples

### 1. OpenAI Configuration

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

### 2. OpenAI-Compatible API (e.g., Azure OpenAI)

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
        "api_key": "env:AZURE_OPENAI_API_KEY",
        "base_url": "https://your-resource.openai.azure.com/openai/deployments/your-deployment"
      }
    },
    "embedder": {
      "provider": "openai",
      "config": {
        "model": "text-embedding-3-small",
        "api_key": "env:AZURE_OPENAI_API_KEY",
        "base_url": "https://your-resource.openai.azure.com/openai/deployments/your-embedding-deployment"
      }
    }
  }
}
```

### 3. Ollama Configuration

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
      "provider": "ollama",
      "config": {
        "model": "nomic-embed-text:latest",
        "ollama_base_url": "http://host.docker.internal:11434"
      }
    }
  }
}
```

### 4. Anthropic Configuration

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

### 5. Together AI Configuration

```json
{
  "openmemory": {
    "custom_instructions": null
  },
  "mem0": {
    "llm": {
      "provider": "together",
      "config": {
        "model": "meta-llama/Llama-3.1-8B-Instruct-Turbo",
        "temperature": 0.1,
        "max_tokens": 2000,
        "together_api_key": "env:TOGETHER_API_KEY",
        "base_url": "https://api.together.xyz/v1"
      }
    },
    "embedder": {
      "provider": "together",
      "config": {
        "model": "togethercomputer/m2-bert-80M-32k-retrieval",
        "together_api_key": "env:TOGETHER_API_KEY",
        "base_url": "https://api.together.xyz/v1"
      }
    }
  }
}
```

### 6. Groq Configuration

```json
{
  "openmemory": {
    "custom_instructions": null
  },
  "mem0": {
    "llm": {
      "provider": "groq",
      "config": {
        "model": "llama-3.1-8b-instant",
        "temperature": 0.1,
        "max_tokens": 2000,
        "groq_api_key": "env:GROQ_API_KEY",
        "base_url": "https://api.groq.com/openai/v1"
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

### 7. Mixed Configuration (Ollama LLM + OpenAI Embedder)

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

## Environment Variables

Make sure to set the appropriate environment variables for your chosen providers:

```bash
# OpenAI
export OPENAI_API_KEY="your-openai-api-key"

# Azure OpenAI
export AZURE_OPENAI_API_KEY="your-azure-openai-api-key"

# Anthropic
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# Together AI
export TOGETHER_API_KEY="your-together-api-key"

# Groq
export GROQ_API_KEY="your-groq-api-key"

# Mistral
export MISTRAL_API_KEY="your-mistral-api-key"

# Google
export GOOGLE_API_KEY="your-google-api-key"

# DeepSeek
export DEEPSEEK_API_KEY="your-deepseek-api-key"

# xAI
export XAI_API_KEY="your-xai-api-key"

# LiteLLM
export LITELLM_API_KEY="your-litellm-api-key"

# LangChain
export LANGCHAIN_API_KEY="your-langchain-api-key"
```

## API Endpoints

### Get Current Configuration
```bash
GET /api/v1/config/
```

### Update Configuration
```bash
PUT /api/v1/config/
Content-Type: application/json

{
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
  "config": {
    "model": "llama3.1:latest",
    "temperature": 0.1,
    "max_tokens": 2000,
    "ollama_base_url": "http://host.docker.internal:11434"
  }
}
```

### Update Only Embedder Configuration
```bash
PUT /api/v1/config/mem0/embedder
Content-Type: application/json

{
  "provider": "openai",
  "config": {
    "model": "text-embedding-3-small",
    "api_key": "env:OPENAI_API_KEY",
    "base_url": "https://api.openai.com/v1"
  }
}
```

## Docker Configuration

When running in Docker, the system automatically detects the Docker environment and adjusts localhost URLs for Ollama to properly reach the host machine. The following host resolution strategies are used (in order of preference):

1. `OLLAMA_HOST` environment variable (if set)
2. `host.docker.internal` (Docker Desktop for Mac/Windows)
3. Docker bridge gateway IP (typically 172.17.0.1 on Linux)
4. Fallback to 172.17.0.1

## Notes

- All API keys can be set using environment variables with the `env:` prefix (e.g., `"env:OPENAI_API_KEY"`)
- The system automatically validates provider configurations and falls back to defaults if invalid
- Ollama URLs are automatically adjusted for Docker environments
- Configuration changes require a memory client reset to take effect
- The system supports mixed configurations (different providers for LLM and embedder)
