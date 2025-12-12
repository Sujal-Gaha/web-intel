from pydantic import Field
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    # Ollama settings
    ollama_host: str = Field(default="http://localhost:11434")
    ollama_model: str = Field(default="llama2")
    
    # Crawl4AI settings
    crawler_type: str = Field(default="crawl4ai")
    crawler_timeout: int = Field(default=30)
    
    # Storage settings
    storage_type: str = Field(default="file")
    storage_path: str = Field(default="./data")
    
    # Agent settings
    max_context_length: int = Field(default=4000)
    
    class Config:
        env_file = ".env"
        env_prefix = "WEB_INTEL_"