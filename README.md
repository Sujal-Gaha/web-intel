# Web Intel Agent

**Intelligent web crawling and AI-powered content querying tool.**

Crawl websites with deep link traversal and query the content using local LLMs (Ollama). Built with a scalable, OOP-based architecture.

---

## ✨ Features

-   🕷️ **Deep Web Crawling** - Crawl websites with configurable depth using Crawl4AI
-   🤖 **AI-Powered Querying** - Ask questions about crawled content using Ollama
-   💬 **Conversation Memory** - Multi-turn conversations with session management
-   🎨 **Beautiful CLI** - Rich terminal UI with progress indicators
-   📦 **Flexible Storage** - File-based storage with easy extensibility
-   ⚡ **Async Everything** - Fast, non-blocking operations throughout

---

## 📋 Prerequisites

### 1. Python 3.10+

```bash
python --version  # Should be 3.10 or higher
```

### 2. Ollama (for AI querying)

Install Ollama from [ollama.ai](https://ollama.ai):

**On macOS/Linux:**

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**On Windows:**
Download from [ollama.ai/download](https://ollama.ai/download)

**Start Ollama and pull a model:**

```bash
# Start Ollama service
ollama serve

# In another terminal, pull a model
ollama pull llama2
# or
ollama pull mistral
```

### 3. Git (to clone the repository)

```bash
git --version
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sujal-Gaha/web-intel.git
cd web-intel
```

### 2. Create Virtual Environment

```bash
python -m venv .venv

# Activate it:
# On Linux/Mac:
source .venv/bin/activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# On Windows (CMD):
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -e ".[dev]"
```

### 4. Configure Environment Variables

```bash
# Copy example config
cp .env.example .env

# Edit .env with your settings
# Default values should work if Ollama is running locally
```

**`.env` file:**

```bash
WEB_INTEL_OLLAMA_HOST=http://localhost:11434
WEB_INTEL_OLLAMA_MODEL=llama2
WEB_INTEL_CRAWLER_TYPE=crawl4ai
WEB_INTEL_CRAWLER_TIMEOUT=30
WEB_INTEL_CRAWLER_MAX_DEPTH=5
WEB_INTEL_STORAGE_TYPE=file
WEB_INTEL_STORAGE_PATH=./data
WEB_INTEL_MAX_CONTEXT_LENGTH=4000
```

### 5. Verify Installation

```bash
wi --help
```

You should see the help menu! 🎉

---

## 📖 Usage

### Basic Workflow

**Step 1: Crawl a website**

```bash
wi crawl url https://example.com -o data/example.md
```

**Step 2: Query the content**

```bash
wi query ask "What is this website about?" -s data/example.md
```

---

## 🕷️ Crawling Commands

### Crawl a Single URL

```bash
# Basic crawl (depth=1)
wi crawl url https://example.com

# Crawl with custom depth
wi crawl url https://example.com -d 3

# Specify output file
wi crawl url https://example.com -o data/my-crawl.md

# Verbose mode (show progress)
wi crawl url https://example.com -v
```

### Crawl Options

| Option      | Short | Description                   | Default        |
| ----------- | ----- | ----------------------------- | -------------- |
| `--output`  | `-o`  | Output file path              | Auto-generated |
| `--depth`   | `-d`  | Crawling depth                | 5              |
| `--format`  | `-f`  | Output format (markdown/json) | markdown       |
| `--verbose` | `-v`  | Show detailed progress        | False          |

**Examples:**

```bash
# Deep crawl with JSON output
wi crawl url https://docs.example.com -d 5 -f json -o data/docs.json

# Quick shallow crawl
wi crawl url https://blog.example.com -d 1 -o data/blog.md
```

---

## 🤖 Query Commands

### Ask a Question (One-Time)

```bash
# Basic query
wi query ask "What is the main topic?" -s data/example.md

# Use different model
wi query ask "Summarize this" -s data/example.md -m mistral

# Stream response (see tokens as they generate)
wi query ask "Explain in detail" -s data/example.md --stream
```

### Interactive Mode (Multi-Turn Conversation)

```bash
# Start interactive session
wi query interactive -s data/example.md

# With session persistence
wi query interactive -s data/example.md --session my-research
```

**In interactive mode:**

```
You: What is this about?
Assistant: This website is about...

You: Tell me more about the pricing
Assistant: The pricing section mentions...

You: exit
```

### Query Options

| Option      | Short | Description                      | Default  |
| ----------- | ----- | -------------------------------- | -------- |
| `--source`  | `-s`  | Source file with crawled content | Required |
| `--session` |       | Session ID for conversation      | None     |
| `--model`   | `-m`  | Override default model           | llama2   |
| `--stream`  |       | Stream response token-by-token   | False    |

---

## 💬 Conversation Sessions

Sessions allow multi-turn conversations where the AI remembers context:

```bash
# First question
wi query ask "What services are offered?" \
  -s data/company.md \
  --session company-research

# Follow-up (remembers previous context)
wi query ask "What are the prices for those services?" \
  -s data/company.md \
  --session company-research

# Another follow-up
wi query ask "Are there any discounts?" \
  -s data/company.md \
  --session company-research
```

Sessions are saved in `./data/sessions/` and persist across CLI runs.

---

## 🎯 Real-World Examples

### Example 1: Research a Documentation Site

```bash
# Crawl the docs
wi crawl url https://docs.python.org/3/library/asyncio.html -d 2 -o data/asyncio-docs.md

# Ask questions
wi query ask "What is asyncio used for?" -s data/asyncio-docs.md
wi query ask "Show me examples of async/await" -s data/asyncio-docs.md
```

### Example 2: Analyze a Blog

```bash
# Crawl blog
wi crawl url https://blog.example.com -d 3 -o data/blog.md

# Interactive analysis
wi query interactive -s data/blog.md --session blog-analysis
```

### Example 3: Compare Multiple Sites

```bash
# Crawl competitor sites
wi crawl url https://competitor1.com -o data/comp1.md
wi crawl url https://competitor2.com -o data/comp2.md

# Analyze first site
wi query ask "What are their key features?" -s data/comp1.md

# Analyze second site
wi query ask "What are their key features?" -s data/comp2.md
```

---

## ⚙️ Configuration

### Environment Variables

All settings can be configured via environment variables with the `WEB_INTEL_` prefix:

```bash
# Ollama Configuration
WEB_INTEL_OLLAMA_HOST=http://localhost:11434
WEB_INTEL_OLLAMA_MODEL=llama2

# Crawler Configuration
WEB_INTEL_CRAWLER_TIMEOUT=30       # Timeout in seconds
WEB_INTEL_CRAWLER_MAX_DEPTH=5      # Default crawl depth

# Storage Configuration
WEB_INTEL_STORAGE_PATH=./data      # Where to save data

# Agent Configuration
WEB_INTEL_MAX_CONTEXT_LENGTH=4000  # Max tokens in context
WEB_INTEL_AGENT_TEMPERATURE=0.7    # LLM temperature (0.0-2.0)
```

### Using Different Models

```bash
# Set default model in .env
WEB_INTEL_OLLAMA_MODEL=mistral

# Or override per command
wi query ask "question" -s file.md -m codellama
```

**Available Ollama models:**

-   `llama2` - General purpose
-   `mistral` - Fast and capable
-   `codellama` - Good for technical content
-   `mixtral` - High quality
-   See [ollama.ai/library](https://ollama.ai/library) for more

---

## 🐛 Troubleshooting

### "Command not found: wi"

```bash
# Make sure you're in the virtual environment
source .venv/bin/activate  # or equivalent for your OS

# Reinstall in editable mode
pip install -e .
```

### "Ollama API error"

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# If not, start Ollama
ollama serve

# Pull a model if you haven't
ollama pull llama2
```

### "Storage error: File not found"

Make sure you specify the correct path to the crawled file:

```bash
# Check what files exist
ls data/

# Use the correct path
wi query ask "question" -s data/your-file.md
```

### "Crawl timed out"

Increase timeout in `.env`:

```bash
WEB_INTEL_CRAWLER_TIMEOUT=60  # Increase to 60 seconds
```

### "Empty response from Ollama"

Your model might not be loaded. Try:

```bash
# Check which models you have
ollama list

# Pull the model you want
ollama pull llama2
```

---

## 🧪 Development

### Run Tests

```bash
pytest tests/ -v
```

### Type Checking

```bash
pyright src/
# or
mypy src/
```

### Code Formatting

```bash
black src/ tests/
ruff check src/ tests/
```

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

---

## 📝 Examples of Output

### Crawl Output (Markdown)

```markdown
# Crawl Result: https://example.com

**Crawled at:** 2024-12-18T10:30:00
**Total pages:** 15
**Success rate:** 100.0%

---

--- From: https://example.com ---

# Welcome to Example.com

This is the home page...

--- From: https://example.com/about ---

# About Us

We are a company that...
```

### Query Output

```
Question
════════════════════════════════════════
What is this website about?

Answer:
════════════════════════════════════════
Based on the content, this website is about...

Model: llama2 | Tokens: 150
```

---

## 🙏 Acknowledgments

-   [Crawl4AI](https://github.com/unclecode/crawl4ai) - Web crawling engine
-   [Ollama](https://ollama.ai) - Local LLM runtime
-   [Typer](https://typer.tiangolo.com) - CLI framework
-   [Rich](https://rich.readthedocs.io) - Terminal formatting

---

## 📞 Support

-   **Issues**: [GitHub Issues](https://github.com/Sujal-Gaha/web-intel/issues)
-   **Documentation**: [Wiki](https://github.com/Sujal-Gaha/web-intel/wiki)

---

**Happy Crawling! 🕷️🤖**
