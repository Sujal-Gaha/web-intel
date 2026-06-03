# Features to Implement

This document tracks the planned features and improvements for the Web Intel Agent project.

## 🔴 Incomplete/Missing Core Features

These features have placeholder files or are marked in the codebase but not yet implemented.

- [ ] **Database Storage Backend**: Implement `src/web_intel/storage/db_storage.py`. (Current: Placeholder)
  - Use SQLite/SQLAlchemy for persistent storage beyond simple files.
  - Support for indexing and searching through crawl results.
- [ ] **CLI Configuration Management**: Implement `src/web_intel/cli/commands/config.py`. (Current: Empty)
  - Commands to view current configuration (`wi config show`).
  - Commands to set/update configuration values (`wi config set KEY VALUE`).
  - Support for managing `.env` files through the CLI.
- [ ] **Enhanced Content Parsers**: Implement `src/web_intel/utils/parsers.py`. (Current: Empty)
  - Support for parsing PDF files.
  - Support for parsing Docx/Office files.
  - Improved HTML-to-Markdown cleaning logic.
- [ ] **Data Validators**: Implement `src/web_intel/utils/validators.py`. (Current: Empty)
  - URL validation beyond basic scheme checks.
  - Content sanitization and validation.

## 🟡 Technical Debt & Robustness

- [ ] **Expand Test Coverage**:
  - [ ] Add unit tests for `Crawl4AICrawler` (mocking the internal crawler).
  - [ ] Add unit tests for `OllamaAgent` (mocking API responses).
  - [ ] Integration tests for the full `Orchestrator` workflow.
- [ ] **Error Handling Refinement**:
  - Implement more granular exception types in `utils/exceptions.py`.
  - Add retry logic for transient crawler/LLM failures.
- [ ] **Logging System**:
  - Replace `print` statements with structured logging (e.g., `loguru` or standard `logging`).
  - Support for log file rotation and levels.

## 🟡 Planned Enhancements

- [ ] **Multi-Provider AI Support**:
  - Add `OpenAIAgent` for GPT-4/GPT-3.5 support.
  - Add `GeminiAgent` for Google's Gemini models.
  - Add `AnthropicAgent` for Claude models.
- [ ] **Session Management CLI**:
  - `wi session list`: List all saved conversation sessions.
  - `wi session show <id>`: Show history of a specific session.
  - `wi session delete <id>`: Remove a session.
- [ ] **Advanced Crawling Capabilities**:
  - **Sitemap Support**: Crawl all URLs found in a `sitemap.xml`.
  - **Concurrent Crawling**: Crawl multiple starting URLs in parallel.
  - **Domain Filtering**: Strict white/blacklisting of domains and paths.
  - **Authentication**: Support for Basic Auth or Bearer tokens for protected sites.
- [ ] **RAG (Retrieval-Augmented Generation)**:
  - Integrate a vector database (e.g., ChromaDB or FAISS).
  - Enable querying over massive crawl results that exceed LLM context limits.
  - Semantic search within crawled content.

## 🔵 Web UI & Server (Phase 2)

This is a major upcoming phase to transition the tool from CLI-only to a full-stack application.

- [ ] **FastAPI Backend**:
  - Implement a REST API to expose crawler and agent functionality.
  - Endpoint for triggering crawls and monitoring progress via WebSockets.
  - Endpoint for querying sessions and history.
  - Secure API authentication (JWT/API Keys).
- [ ] **Frontend Application**:
  - A modern web interface built with **React** and **Tailwind CSS**.
  - Dashboard for visualizing crawl results and statistics.
  - Interactive chat interface for querying with markdown rendering and code highlighting.
- [ ] **Dockerization**:
  - Create a `Dockerfile` for the entire application (Backend + Frontend).
  - `docker-compose.yml` to orchestrate the backend, frontend, database, and Ollama server.

## 🟢 UX & Tooling

- [ ] **Better Progress Visualization**:
  - Real-time statistics during crawls (pages per second, bytes downloaded).
  - Nested progress bars for deep crawls.
- [ ] **Output Format Variety**:
  - Support for exporting results to CSV, JSONL, and PDF.
- [ ] **Task Scheduling**:
  - Ability to schedule recurring crawls for monitoring site changes.

---

_Last updated: June 3, 2026_
