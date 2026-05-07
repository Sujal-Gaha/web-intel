# Features to Implement

This document tracks the planned features and improvements for the Web Intel Agent project.

## 🔴 Incomplete/Missing Core Features

These features have placeholder files or are marked in the codebase but not yet implemented.

- [ ] **Database Storage Backend**: Implement `src/web_intel/storage/db_storage.py`.
  - Use SQLite/SQLAlchemy for persistent storage beyond simple files.
  - Support for indexing and searching through crawl results.
- [ ] **CLI Configuration Management**: Implement `src/web_intel/cli/commands/config.py`.
  - Commands to view current configuration (`wi config show`).
  - Commands to set/update configuration values (`wi config set KEY VALUE`).
  - Support for managing `.env` files through the CLI.
- [ ] **Enhanced Content Parsers**: Implement `src/web_intel/utils/parsers.py`.
  - Support for parsing PDF files.
  - Support for parsing Docx/Office files.
  - Improved HTML-to-Markdown cleaning logic.
- [ ] **Data Validators**: Implement `src/web_intel/utils/validators.py`.
  - URL validation beyond basic scheme checks.
  - Content sanitization and validation.
- [ ] **Crawl Depth Fix**: Ensure the `--depth` parameter in `wi crawl url` is correctly passed to the `Crawl4AICrawler`.

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

## 🟢 UX & Tooling

- [ ] **Better Progress Visualization**:
  - Real-time statistics during crawls (pages per second, bytes downloaded).
  - Nested progress bars for deep crawls.
- [ ] **Output Format Variety**:
  - Support for exporting results to CSV, JSONL, and PDF.
- [ ] **Web Dashboard**:
  - A simple local web UI (Streamlit or FastAPI/React) to browse crawls and chat with the agent.
- [ ] **Task Scheduling**:
  - Ability to schedule recurring crawls for monitoring site changes.

---

*Last updated: May 7, 2026*
