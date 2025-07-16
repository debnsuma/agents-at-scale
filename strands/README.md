# Strands Demo Projects

This repository contains a collection of demo projects showcasing the capabilities of Strands AI framework. Each project demonstrates different aspects of AI-powered automation and content generation.

## Projects

### 1. Demo Summary Speak

A text-to-speech application that uses Claude 3.7 Sonnet to read and summarize documents. The application can:
- Read and summarize text files
- Convert summaries to Markdown format
- Provide natural-sounding text-to-speech output
- Manage files and directories

[View Demo Summary Speak Documentation](demo-summary-speak/README.md)

#### Demo Recording
[![Demo Summary Speak](https://img.youtube.com/vi/J3JaXz8hOxM/0.jpg)](https://youtu.be/J3JaXz8hOxM)

### 2. Demo Manim Video Generation

A project that combines Strands Agents with Manim to generate mathematical animations through an MCP (Model Context Protocol) server. Features include:
- Interactive chat interface for animation generation
- Real-time video rendering
- Custom animation creation
- MCP server integration

[View Manim Video Generation Documentation](demo-manim-video-gen/README.md)

#### Demo Recording
[![Demo Manim Video Generation](https://img.youtube.com/vi/QQmJlI4vR80/0.jpg)](https://youtu.be/QQmJlI4vR80)

### 3. Demo Agentic Voice-based RAG with Vision-based Retrieval

A multimodal AI tutor that combines visual document intelligence with voice response using ColPali, Bedrock, and Strands Agents. Features include:
- Vision-based document embedding and retrieval
- Voice-enabled educational assistance
- Multimodal RAG (Retrieval-Augmented Generation)
- Integration with Qdrant vector database

[View Agentic RAG Documentation](demo-agentic-voice-based-rag-with-vision-based-retrieval/README.md)

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/debnsuma/agents-at-scale.git
cd agents-at-scale/strands
```

2. Set up your Python environment:
```bash
python -m venv .venv
source .venv/bin/activate  
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Project Structure

```
agents-at-scale/
├── strands/
│   ├── demo-summary-speak/     # Text-to-speech and summarization demo
│   ├── demo-manim-video-gen/   # Mathematical animation generation demo
│   ├── demo-agentic-voice-based-rag-with-vision-based-retrieval/  # Multimodal RAG demo
│   ├── recording/             # Demo video recordings
│   │   ├── video_demo_summary_speak.mp4
│   │   └── video_demo_manim_video_gen.mp4
│   ├── pyproject.toml         # Project dependencies
│   └── README.md             # This file
└── bedrock-agent-core/       # Core Bedrock agent functionality
```

## Requirements

- Python 3.8 or higher
- uv (Python package manager)
- Strands AI framework
- Additional dependencies as specified in each project's README

## Contributing

Feel free to contribute to these demo projects by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

