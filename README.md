# Agents at Scale using Bedrock AgentCore

This repository contains comprehensive code samples and learning resources for **Strands Agents** and **Amazon Bedrock AgentCore** - AWS's new service for securely deploying and operating AI agents at any scale.

## Overview

Amazon Bedrock AgentCore is a fully managed service that enables you to build, deploy, and operate AI agents at scale. It provides the infrastructure and tools needed to create production-ready AI agents that can handle complex workflows, integrate with enterprise systems, and scale to meet your business needs.

## What You'll Find Here

### 🚀 **Strands Agents Examples** (`strands/`)
Real-world demonstrations of AI agent capabilities using the Strands framework:

- **📖 Demo Summary Speak**: Text-to-speech application using Claude 3.7 Sonnet to read and summarize documents with natural voice output
- **🎬 Demo Manim Video Generation**: Mathematical animation generation through MCP (Model Context Protocol) server integration
- **🎓 Demo Agentic Voice-based RAG with Vision-based Retrieval**: Multimodal AI tutor combining visual document intelligence with voice response using ColPali, Bedrock, and Strands Agents

### 🔧 **AgentCore Integration** (`bedrock-agent-core/`)
Production-ready examples showing how to deploy agents to Amazon Bedrock AgentCore:

- **Demo Deploying Strands**: Complete example of deploying a Strands agent to AgentCore Runtime with file operations and speech capabilities
- **Framework Flexibility**: Support for any framework (Strands, LangChain, LangGraph, CrewAI) with any model

### 📊 **Scaling Patterns & Best Practices**
- Secure deployment patterns
- Enterprise integration examples
- Monitoring and observability tools
- Multi-agent orchestration

## Key Features of Amazon Bedrock AgentCore

- **🔒 Secure Deployment**: Built-in security controls and compliance features
- **📈 Scalable Infrastructure**: Automatic scaling based on demand
- **🏢 Enterprise Integration**: Connect with existing business systems and data sources
- **📊 Monitoring & Analytics**: Comprehensive observability and performance insights
- **🤖 Multi-Agent Orchestration**: Coordinate multiple agents for complex workflows
- **🔄 Framework Flexibility**: Deploy agents from any framework (Strands, LangChain, LangGraph, CrewAI)
- **🧠 Model Agnostic**: Use any model from Amazon Bedrock or external providers

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**: Ensure you have Python 3.9 or later installed
- **uv**: Install the fast Python package installer and resolver
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **AWS CLI**: Configure AWS CLI with appropriate permissions for Bedrock services
- **GitHub Token**: For examples that use GitHub APIs, create a personal access token
- **Conda** (for some examples): Required for the multimodal RAG demo

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/debnsuma/agents-at-scale.git
cd agents-at-scale
```

### 2. Set up the development environment

```bash
# Initialize a new uv project (creates/updates pyproject.toml)
uv init

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install core dependencies (will be added to pyproject.toml)
uv add strands-agents strands-agents-tools
uv add bedrock-agentcore bedrock-agentcore-starter-toolkit

# Install Jupyter support
uv add ipython ipykernel
python -m ipykernel install --user --name=agents-at-scale --display-name "Python (agents-at-scale)"
```

**Note**: The `uv add` commands will automatically update the `pyproject.toml` file with the dependencies, making it easy to recreate the environment on other machines or share with others.

**Alternative**: If you have an existing `pyproject.toml` file with dependencies already defined, you can simply run:
```bash
uv sync
```
This will install all dependencies listed in the `pyproject.toml` file.

### 3. Configure environment variables

```bash
export AWS_REGION=us-east-1  # or your preferred region
```

### 4. Start Jupyter (optional)

For interactive development with notebooks:

```bash
uv run jupyter notebook
```

Or for JupyterLab:

```bash
uv run jupyter lab
```

## Quick Start Examples

### 🎯 **Strands Agents Examples**

#### Text-to-Speech Document Summarization
```bash
cd strands/demo-summary-speak
uv run app.py
```
- Read and summarize text files
- Convert summaries to Markdown format
- Natural-sounding text-to-speech output

#### Mathematical Animation Generation
```bash
cd strands/demo-manim-video-gen
# Terminal 1: Start MCP server
uv run start_mcp_server.py
# Terminal 2: Start chat interface
uv run app.py
```
- Interactive chat interface for animation generation
- Real-time video rendering with Manim
- MCP server integration

#### Multimodal Voice-based RAG
```bash
cd strands/demo-agentic-voice-based-rag-with-vision-based-retrieval
conda create --name rag_env python=3.12
conda activate rag_env
pip install -r requirements.txt
jupyter notebook
```
- Vision-based document embedding and retrieval
- Voice-enabled educational assistance
- Integration with Qdrant vector database

### 🚀 **AgentCore Deployment Examples**

#### Deploy Strands Agent to AgentCore
```bash
cd bedrock-agent-core/demo-deploying-strands
# Deploy the agent
bedrock-agentcore deploy
# Invoke the agent
bedrock-agentcore invoke --prompt "Hello, can you help me with file operations?"
```
- Deploy Strands agents to production
- File operations and speech capabilities
- Secure, scalable runtime

## Repository Structure

```
agents-at-scale/
├── strands/           # Strands Agents examples and implementations
│   ├── demo-summary-speak/     # Text-to-speech and summarization demo
│   ├── demo-manim-video-gen/   # Mathematical animation generation demo
│   ├── demo-agentic-voice-based-rag-with-vision-based-retrieval/  # Multimodal RAG demo
│   ├── recording/             # Demo video recordings
│   └── pyproject.toml         # Project dependencies
├── bedrock-agent-core/ # AgentCore specific examples and configurations
│   ├── demo-deploying-strands/ # Complete AgentCore deployment example
│   ├── demo-deploying-crewai/  # CrewAI deployment example (coming soon)
│   └── imgs/                  # Documentation images
└── README.md          # This file
```

## Demo Videos

- **Demo Summary Speak**: [Watch on YouTube](https://youtu.be/J3JaXz8hOxM)
- **Demo Manim Video Generation**: [Watch on YouTube](https://youtu.be/QQmJlI4vR80)

## Resources

### Official Documentation
- [Amazon Bedrock AgentCore Announcement](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Strands Framework Documentation](https://strands.ai/)

### PyPI Packages
- [bedrock-agentcore](https://pypi.org/project/bedrock-agentcore/) - Official Python SDK for Amazon Bedrock AgentCore
- [bedrock-agentcore-starter-toolkit](https://pypi.org/project/bedrock-agentcore-starter-toolkit/) - Starter toolkit for building agents with Bedrock AgentCore
- [strands-agents](https://pypi.org/project/strands-agents/) - Python framework for building AI agents with Strands

### Next Steps

1. **Explore Examples**: Start with the basic examples in the `strands/` directory
2. **Deploy to AgentCore**: Follow the deployment examples in the `bedrock-agent-core/` directory
3. **Build Your Own**: Use the patterns and examples to create your own AI agents
4. **Scale Up**: Deploy your agents to production using Amazon Bedrock AgentCore
