# OpenMemory Multi-Provider

OpenMemory Multi-Provider is an enhanced version of OpenMemory - your personal memory layer for LLMs with support for multiple AI model providers. This version is private, portable, and open-source, giving you complete control over your data while supporting various AI providers. Build AI applications with personalized memories while keeping your data secure.

## 🆕 New Features

- **Multi-Provider Support**: Choose from multiple AI model providers including OpenAI, Anthropic, Together AI, Groq, Mistral, Google, DeepSeek, xAI, LiteLLM, and LangChain
- **Flexible Configuration**: Easy switching between different AI providers without code changes
- **Ollama Integration**: Support for local Ollama models for complete privacy
- **Enhanced Provider Management**: Simplified configuration and management of different AI providers

![OpenMemory](https://github.com/user-attachments/assets/3c701757-ad82-4afa-bfbe-e049c2b4320b)

## Easy Setup

### Prerequisites
- Docker
- At least one AI provider API key (OpenAI, Anthropic, Together AI, Groq, Mistral, Google, DeepSeek, xAI, LiteLLM, or LangChain)

You can quickly run OpenMemory by running the following command:

```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | bash
```

You should set your preferred AI provider API key as a global environment variable:

```bash
# For OpenAI
export OPENAI_API_KEY=your_openai_api_key

# For Anthropic
export ANTHROPIC_API_KEY=your_anthropic_api_key

# For other providers, see the configuration section below
```

You can also set the API key as a parameter to the script:

```bash
curl -sL https://raw.githubusercontent.com/mem0ai/mem0/main/openmemory/run.sh | OPENAI_API_KEY=your_api_key bash
```

## Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for backend development)
- Node.js (for frontend development)
- At least one AI provider API key (required for LLM interactions, run `cp api/.env.example api/.env` then configure your preferred provider)

## Quickstart

### 1. Set Up Environment Variables

Before running the project, you need to configure environment variables for both the API and the UI.

You can do this in one of the following ways:

- **Manually**:  
  Create a `.env` file in each of the following directories:
  - `/api/.env`
  - `/ui/.env`

- **Using `.env.example` files**:  
  Copy and rename the example files:

  ```bash
  cp api/.env.example api/.env
  cp ui/.env.example ui/.env
  ```

 - **Using Makefile** (if supported):  
    Run:
  
   ```bash
   make env
   ```
- #### Example `/api/.env`

```env
# Choose one or more AI providers
OPENAI_API_KEY=sk-xxx
# ANTHROPIC_API_KEY=your_anthropic_key
# TOGETHER_API_KEY=your_together_key
# GROQ_API_KEY=your_groq_key
# MISTRAL_API_KEY=your_mistral_key
# GOOGLE_API_KEY=your_google_key
# DEEPSEEK_API_KEY=your_deepseek_key
# XAI_API_KEY=your_xai_key
# LITELLM_API_KEY=your_litellm_key
# LANGCHAIN_API_KEY=your_langchain_key

USER=<user-id> # The User Id you want to associate the memories with 
```
- #### Example `/ui/.env`

```env
NEXT_PUBLIC_API_URL=http://localhost:8765
NEXT_PUBLIC_USER_ID=<user-id> # Same as the user id for environment variable in api
```

### 2. Build and Run the Project
You can run the project using the following two commands:
```bash
make build # builds the mcp server and ui
make up  # runs openmemory mcp server and ui
```

After running these commands, you will have:
- OpenMemory MCP server running at: http://localhost:8765 (API documentation available at http://localhost:8765/docs)
- OpenMemory UI running at: http://localhost:3000

#### UI not working on `localhost:3000`?

If the UI does not start properly on [http://localhost:3000](http://localhost:3000), try running it manually:

```bash
cd ui
pnpm install
pnpm dev
```

## AI Provider Configuration

This version supports multiple AI providers. You can configure one or more providers in your `/api/.env` file:

### Supported Providers

| Provider | Environment Variable | Example |
|----------|---------------------|---------|
| OpenAI | `OPENAI_API_KEY` | `sk-...` |
| Anthropic | `ANTHROPIC_API_KEY` | `sk-ant-...` |
| Together AI | `TOGETHER_API_KEY` | `...` |
| Groq | `GROQ_API_KEY` | `gsk_...` |
| Mistral | `MISTRAL_API_KEY` | `...` |
| Google | `GOOGLE_API_KEY` | `...` |
| DeepSeek | `DEEPSEEK_API_KEY` | `...` |
| xAI | `XAI_API_KEY` | `...` |
| LiteLLM | `LITELLM_API_KEY` | `...` |
| LangChain | `LANGCHAIN_API_KEY` | `...` |
| Ollama | `OLLAMA_HOST` | `http://localhost:11434` |

### Provider Selection

The system will automatically use the first available provider from your configuration. You can also specify the provider in your configuration files.

### MCP Client Setup

Use the following one step command to configure OpenMemory Local MCP to a client. The general command format is as follows:

```bash
npx @openmemory/install local http://localhost:8765/mcp/<client-name>/sse/<user-id> --client <client-name>
```

Replace `<client-name>` with the desired client name and `<user-id>` with the value specified in your environment variables.


## Project Structure

- `api/` - Backend APIs + MCP server
- `ui/` - Frontend React application

## Contributing

We are a team of developers passionate about the future of AI and open-source software. With years of experience in both fields, we believe in the power of community-driven development and are excited to build tools that make AI more accessible and personalized.

We welcome all forms of contributions:
- Bug reports and feature requests
- Documentation improvements
- Code contributions
- Testing and feedback
- Community support

How to contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b openmemory/feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin openmemory/feature/amazing-feature`)
5. Open a Pull Request

Join us in building the future of AI memory management! Your contributions help make OpenMemory better for everyone.

## License

This project is licensed under the Apache License 2.0. This is a modified version of the original OpenMemory project with enhanced multi-provider support.

### Original Project
This project is based on the original [OpenMemory](https://github.com/mem0ai/mem0) project, which has been enhanced with multi-provider support and additional features.

### License Details
- **License**: Apache License 2.0
- **Modifications**: This version includes significant modifications and enhancements by the maintainer
- **Attribution**: Based on the original OpenMemory project by mem0ai

For the full license text, see the [LICENSE](LICENSE) file in this repository.
