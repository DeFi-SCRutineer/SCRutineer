# SCRUTINEER

## Overview

**SCRUTINEER** is an automated and practical system for detecting **logic-level usage violations** of Smart Contract Reusable Components (SCRs). It features a multi-stage pipeline designed for high accuracy and scalability:

- We begin with a **composite feature extraction** approach that generates three complementary representations: a **composite signature**, a **logical sequence**, and a **latent structural embedding**. These provide comprehensive support for downstream analysis.

- We introduce an **LLM-powered knowledge base construction framework**, leveraging **comprehension-oriented prompts** and **domain-specific tools** to extract logic-level usage patterns and automatically build the SCR knowledge base.

- To detect violations, we develop a **Retrieval-Augmented Generation (RAG)**-driven inspector. It combines **fast retrieval** with both comprehensive and targeted analyses to reason about potentially insecure logic-level usages.

- Finally, we implement a **logic-level usage violation analysis engine**, integrating a **similarity-based checker** and a **snapshot-based inference conflict checker** for accurate and robust detection.


## Install

### Requirements

- Python 3.8 or higher
- Pip

### Install Python Packages

- Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Configure of LLM

- Set the environment variables for LLM service:

```bash
export DEEPSEEK_MODE=<"cloud" or "local">
export DEEPSEEK_API_BASE=<"base_url">
export DEEPSEEK_API_KEY=<"api_key">
```

## Usage

### Construction of SCR Knowledge Base

- Run UkeAgent to build the knowledge base:

```bash
cd UkeAgent
python UkeAgent.py
```


### Detection of Logic-level Usage Violations

- Run the analysis engine:

```bash
cd engine
python main.py 
``` 




*Note: we will release the full implementation of SCRUTINEER upon paper acceptance. Stay tuned!* 