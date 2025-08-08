# SCRutineer

## Introduction

**SCRutineer** is an automated and practical system for detecting **logic-level usage violations** of Smart Contract Reusable Components (SCRs). It features a multi-stage pipeline designed for high accuracy and scalability:

- ⚙️ We begin with a **composite feature extraction** approach that generates three complementary representations: a **composite signature**, a **logical sequence**, and a **latent structural embedding**. These provide comprehensive support for downstream analysis.

- 🧩 We introduce an **LLM-powered knowledge base construction framework**, leveraging **comprehension-oriented prompts** and **domain-specific tools** to extract logic-level usage patterns and automatically build the SCR knowledge base.

- 🔍 To detect violations, we develop a **Retrieval-Augmented Generation (RAG)**-driven inspector. It combines **fast retrieval** with rigorously designed **Chain-of-Thought (CoT)** prompts to reason about potentially insecure logic-level usages.

- 🛡️ Finally, we implement a **logic-level usage violation analysis engine**, integrating a **similarity-based checker** and a **snapshot-based inference conflict checker** for accurate and robust detection.

---

## Repository Status

We are currently refactoring and organizing the codebase. Components of the project will be open-sourced progressively in this repository. While the current version may still be incomplete, we are actively working to improve its:

- 🧹 Clarity  
- 🔁 Reproducibility  
- 📚 Documentation

📌 **Stay tuned — updates are on the way!**  
💬 *Have questions or feedback?* Feel free to open an issue or pull request — contributions and discussions are welcome! 🙌
