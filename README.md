# Agents at Scale

This repository contains code samples and learning resources for **Strands Agents** and **Amazon Bedrock AgentCore** - AWS's new service for securely deploying and operating AI agents at any scale.

## Overview

Amazon Bedrock AgentCore is a fully managed service that enables you to build, deploy, and operate AI agents at scale. It provides the infrastructure and tools needed to create production-ready AI agents that can handle complex workflows, integrate with enterprise systems, and scale to meet your business needs.

## What You'll Find Here

- **Strands Agents Examples**: Code samples demonstrating how to build and deploy agents using the Strands framework
- **AgentCore Integration**: Examples showing how to leverage Amazon Bedrock AgentCore for production-scale agent deployments
- **Scaling Patterns**: Best practices and patterns for scaling AI agents in production environments
- **Security & Compliance**: Examples of secure agent deployment and operation
- **Monitoring & Observability**: Tools and patterns for monitoring agent performance and behavior

## Key Features of Amazon Bedrock AgentCore

- **Secure Deployment**: Built-in security controls and compliance features
- **Scalable Infrastructure**: Automatic scaling based on demand
- **Enterprise Integration**: Connect with existing business systems and data sources
- **Monitoring & Analytics**: Comprehensive observability and performance insights
- **Multi-Agent Orchestration**: Coordinate multiple agents for complex workflows

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**: Ensure you have Python 3.9 or later installed
- **uv**: Install the fast Python package installer and resolver
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **AWS CLI**: Configure AWS CLI with appropriate permissions for Bedrock services
- **GitHub Token**: For examples that use GitHub APIs, create a personal access token

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

### Next Steps

1. **Explore Examples**: Start with the basic examples in the `strands/` directory
2. **Deploy to AgentCore**: Follow the deployment examples in the `bedrock-agent-core/` directory

## Repository Structure

```
agents-at-scale/
├── strands/           # Strands Agents examples and implementations
├── bedrock-agent-core/ # AgentCore specific examples and configurations
└── README.md          # This file
```

## Resources

### Official Documentation
- [Amazon Bedrock AgentCore Announcement](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Strands Framework Documentation](https://strands.ai/)

### PyPI Packages
- [bedrock-agentcore](https://pypi.org/project/bedrock-agentcore/) - Official Python SDK for Amazon Bedrock AgentCore
- [bedrock-agentcore-starter-toolkit](https://pypi.org/project/bedrock-agentcore-starter-toolkit/) - Starter toolkit for building agents with Bedrock AgentCore
- [strands-agents](https://pypi.org/project/strands-agents/) - Python framework for building AI agents with Strands
