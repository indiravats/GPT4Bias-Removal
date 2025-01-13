# Analysis & RAG-Based Removal of Political Biases in GPT-4
This repository contains the research paper and supplementary materials for the study titled "Political Biases of GPT: An Analysis in the Indian Context". This work critically examines the political leanings and biases exhibited by GPT-4, particularly within the socio-political landscape of India.

# Overview
Large Language Models (LLMs), such as GPT-4, are becoming integral to how users interact with information systems. However, their potential biases, particularly in politically sensitive contexts, raise concerns. This study explores:

Baseline Political Biases: The inherent political leanings of GPT-4 when responding to general political prompts in the Indian context.
Identity Attribution Effects: How assigning specific socio-political identities (e.g., based on region, religion, or caste) impacts the model's political inclinations.
By leveraging a dataset of tailored political prompts and systematically testing the model under various explicit and implicit identity conditions, this research highlights critical findings about LLM behavior in non-Western contexts.
More details for our results can be found [here](Paper.pdf). The code for our analysis is available [here](analysis).

# RAG-Based Removal
## Pipeline
### Data Preprocessing:
All comments from a given thread are aggregated into a single tuple to ensure cohesive tokenization. Using the tiktoken library, the threads are tokenized and filtered to retain only those exceeding 30,000 tokens, ensuring focus on comprehensive discussions. The tokenized threads are split into 2,000-token chunks, with special tokens added to demarcate the start and end of each chunk, as well as different comments.
### Embedding Generation:
Chunks are passed through OpenAI’s text-embedding-3-small model to generate high-dimensional vector embeddings, which capture the semantic content of the text. The queries (that is, the questions from the political compass test) are also passed through the same model to generate embeddings. 
### Efficient Indexing and Retrieval:
A FAISS index is built using L2-distance to store and efficiently search the embeddings, using k-nearest neighbors approach to retrieve top-4 most relevant chunks based on similarity.
### Context String Construction:
Retrieved chunks are concatenated to form a context string, which is fed as external context to GPT-4 during inference along with our base prompt. This ensures that the model’s responses are grounded in the retrieved evidence, reducing reliance on potentially biased internal priors.

## Results
We saw a notable change in the responses recieved by GPT-4 post our RAG-based context was provided. Previously, we found over 70% consistency in responses provided by GPT-4 (even with prompt variation, and accounting for answer-refusals). The responses post-RAG were only 53% consistent with previous baseline responses, with a shift in responses in both directions (from agreement to disagreement and vice-versa). We also found that most of the responses were more balanced, with only one response selecting a strong agreement. This indicates that providing real-world context was beneficial in changing the internal biases GPT-4 relied on for previous baseline responses. 
