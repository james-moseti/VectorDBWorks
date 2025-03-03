# Helper utility that handles openai and pinecone key management

import os
from dotenv import load_dotenv, find_dotenv

class Utils:
    def __init__(self):
        pass

    def create_dlai_index_name(self, index_name):
        openai_key = self.get_openai_api_key()
        if not openai_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        
        return f'{index_name}-{openai_key[-36:].lower().replace("_", "-")}'
    
    def get_openai_api_key(self):
        """Load OpenAI API key from .env file"""
        load_dotenv(find_dotenv())
        return os.getenv("OPENAI_API_KEY")
    
    def get_pinecone_api_key(self):
        """Load Pinecone API key from .env file"""
        load_dotenv(find_dotenv())
        return os.getenv("PINECONE_API_KEY")
