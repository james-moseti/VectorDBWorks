# Semantic Search with Pinecone & Sentence Transformers

![Semantic Search](https://img.shields.io/badge/Semantic_Search-Pinecone-blue.svg)  
A high-performance **semantic search engine** using **Pinecone**, **Sentence Transformers**, and **OpenAI embeddings**.

## Project Overview
This project enables **fast and efficient similarity search** on text data by:
- Converting text into **vector embeddings** using `sentence-transformers`
- Storing vectors in **Pinecone**, a high-performance **vector database**
- Performing **semantic search** to find the most relevant text matches

Ideal for **chatbots, document retrieval, AI-powered search engines, and recommendation systems.**

---

## Features
✔ **Fast and Scalable**: Uses Pinecone’s **serverless** vector search  
✔ **Supports Large Datasets**: Handles millions of vectors efficiently  
✔ **Customizable Embeddings**: Compatible with **OpenAI, DeepSeek, BERT, and more**  
✔ **Batch Processing**: Efficiently processes large datasets with **batch inserts**  
✔ **Easy API Integration**: Can be integrated into **AI chatbots, recommendation engines, or NLP applications**  

---

## Tech Stack & Dependencies
| Dependency           | Purpose                                      |
|----------------------|----------------------------------------------|
| **Pinecone**        | Vector database for storing embeddings      |
| **SentenceTransformers** | Converts text into vector embeddings    |
| **Dotenv**          | Loads environment variables                 |
| **Jupyter Notebook** | Interactive testing environment           |
| **JSON**            | Stores and processes metadata               |

## Installation
1. **Clone the repository**:
```bash
git clone
```
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```
3. **Set up Pinecone**:
```bash
export PINECONE_API_KEY=your-api-key
```
4. **Run the Jupyter Notebook**:
```bash
jupyter notebook
```