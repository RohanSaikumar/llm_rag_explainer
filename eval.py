from ragchain import rag_chain,Chroma_database_creation
import os

folder_path = os.getenv("DOCS_PATH")

def get_retriever():
    return Chroma_database_creation(folder_path)

retriever = get_retriever()

rag_chain = rag_chain(retriever)

eval_questions = [
    {
        "question": "Why does the Transformer architecture replace recurrence with self-attention, and what advantages does this bring?",
        "expected_keywords": [
            "self-attention",
            "parallel",
            "parallelization",
            "long-range",
            "dependencies",
            "recurrence",
            "sequential",
            "rnn"
        ]
    },
    {
        "question": "What role do positional encodings play in the Transformer, and why are they necessary?",
        "expected_keywords": [
            "positional encoding",
            "position",
            "order",
            "sequence",
            "token order",
            "no recurrence",
            "no convolution"
        ]
    },
    {
        "question": "How does multi-head attention improve the representational power of the Transformer model?",
        "expected_keywords": [
            "multi-head",
            "multiple heads",
            "subspaces",
            "different",
            "representations",
            "attention heads",
            "parallel attention"
        ]
    },
    {
        "question": "Why is dot-product attention scaled by the square root of the key dimension in the Transformer?",
        "expected_keywords": [
            "scaling",
            "sqrt",
            "softmax",
            "stability",
            "variance",
            "large values",
            "gradient"
        ]
    },
    {
        "question": "How do residual connections and layer normalization help stabilize training in the Transformer architecture?",
        "expected_keywords": [
            "residual",
            "skip connections",
            "layer normalization",
            "training stability",
            "gradient flow",
            "vanishing gradient",
            "deep networks"
        ]
    }
]



def keyword_score(answer: str, keywords: list[str]) -> float:
    answer_lower = answer.lower()
    hits = sum(1 for kw in keywords if kw in answer_lower)
    return hits / len(keywords)


results = []

for item in eval_questions:
    response = rag_chain.invoke({
        "input": item["question"],
        "chat_history": []
    })

    score = keyword_score(response, item["expected_keywords"])

    results.append({
        "question": item["question"],
        "score": round(score, 2),
        "answer": response[:200] + "..."
    })


avg_score = sum(r["score"] for r in results) / len(results)

print("\nRAG Evaluation Results")
print("-" * 30)

for r in results:
    print(f"Q: {r['question']}")
    print(f"Score: {r['score']}")
    print()

print(f"Average Score: {round(avg_score, 2)}")


