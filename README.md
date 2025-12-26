<h1>LLM Architecture Explainer (RAG System)</h1>

<p>
This project implements a <b>Retrieval-Augmented Generation (RAG)</b> system designed to answer
conceptual questions about <b>Large Language Model (LLM) architectures</b> using a curated set of
research papers.
</p>

<hr>

<h2>🔧 What This Project Does</h2>
<ul>
  <li>Loads research papers (PDF/DOCX) from a local folder</li>
  <li>Splits documents into overlapping chunks for better context preservation</li>
  <li>Embeds chunks using a sentence-transformer model</li>
  <li>Stores embeddings in a Chroma vector database</li>
  <li>Uses a history-aware retriever to handle follow-up questions</li>
  <li>Generates grounded answers via a multi-stage LangChain pipeline</li>
  <li>Includes a review step to verify answer relevance and context alignment</li>
</ul>

<hr>

<h2>🧠 Design Philosophy</h2>
<p>
The system is intentionally <b>strictly grounded</b>.  
Answers are generated only when sufficient information exists in the retrieved documents.
If the document corpus does not cover a concept, the model may refuse to answer rather than hallucinate.
</p>

<p>
This makes system performance <b>highly dependent on corpus quality and coverage</b>,
which is treated as a design feature rather than a limitation.
</p>

<hr>

<h3>📂 Recommended Papers to Expand the Corpus</h3>

<p>
The following papers are recommended additions to improve coverage of
LLM architectures, scaling behavior, alignment, and retrieval-based systems.
These papers complement the existing corpus without overlapping with it.
</p>

<ul>
  <li>Improving Language Understanding by Generative Pre-Training (GPT-1)</li>
  <li>Training Language Models to Follow Instructions (InstructGPT)</li>
  <li>PaLM: Scaling Language Modeling with Pathways</li>
  <li>OPT: Open Pre-trained Transformer Language Models</li>
  <li>LLaMA: Open and Efficient Foundation Language Models</li>
  <li>Switch Transformers: Scaling to Trillion Parameter Models</li>
  <li>Scaling Laws for Neural Language Models</li>
  <li>Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks</li>
  <li>Improving Factuality and Reasoning in Language Models through Retrieval</li>
  <li>Self-Consistency Improves Chain-of-Thought Reasoning in Language Models</li>
</ul>

<p>
Adding these papers increases architectural diversity and improves the retriever’s
ability to answer questions related to scaling, efficiency, alignment, and retrieval-enhanced reasoning.
</p>

<h2>🧪 Evaluation Utility</h2>
<p>
The repository includes an <code>eval.py</code> script that serves as a lightweight evaluation tool.
Rather than acting as a fixed benchmark, it is designed to:
</p>

<ul>
  <li>Sanity-check retrieval grounding</li>
  <li>Identify questions that fall outside corpus coverage</li>
  <li>Compare system behavior as new documents are added</li>
</ul>

<p>
This allows evaluation to be reused as an <b>iterative development tool</b> when expanding
or refining the document corpus.
</p>

<hr>

<h2>🚀 How to Run</h2>
<ol>
  <li>Add research papers to the document folder</li>
  <li>Set environment variables in a <code>.env</code> file</li>
  <li>Run the Streamlit app</li>
</ol>

<pre>
streamlit run app.py
</pre>

<hr>

<h2>📌 Key Takeaway</h2>
<p>
This project demonstrates a modular, grounded RAG system where
<b>data quality and coverage drive performance</b>,
mirroring real-world retrieval-based AI systems.
</p>
