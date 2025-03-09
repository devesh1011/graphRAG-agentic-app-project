## Inspiration
Financial fraud targeting **elderly individuals** is a critical issue, with the **FBI's Internet Crime Complaint Center (IC3)** reporting that **seniors lost over $3.4 billion** to fraud in **2023 alone**, marking an **11% increase** from the previous year. This alarming figure underscores the **vulnerability of the elderly** to sophisticated scams and **organized fraud rings** that exploit trust and **lack of technological familiarity.** 
 
With nearly **101,068 complaints** filed by those **over 60**, and an **average loss of $33,915 per complaint**, it is evident that **traditional fraud detection systems** often **fall short** in protecting this demographic.
 
Inspired by these challenges and the potential of advanced technologies, we aim to develop an **agentic financial fraud ring detection system**. By leveraging **GraphRAG** for **complex network analysis**, **AI agents** for **autonomous pattern recognition**, and **GPU-accelerated analytics** for real-time processing, our goal is to **identify influential fraudsters, uncover hidden fraud networks**, and provide **financial institutions** with the **tools needed to protect the elderly** and ensure **financial security.**

## What it does
Our AI-powered system detects fraud rings by **analyzing transactional relationships using graph-based AI and RAG (Retrieval-Augmented Generation).** It:

🔹 **Builds a fraud network graph** from financial transactions.
 
🔹 **Identifies influential fraudsters** using PageRank and centrality measures.
 
🔹 **Detects hidden fraud rings** using GraphRAG and GPU-accelerated graph traversal.
 
🔹 **Answers complex fraud queries** dynamically using AI agents.
 
🔹 **Generates explainable fraud insights** to assist financial analysts.
 
## How we built it
🚀 **Tech Stack & Methodologies**

1️⃣ **Graph-based Fraud Detection**: We used **ArangoDB** as a multi-model graph database to represent transactions and fraud rings.

2️⃣ **Agentic Query Processing:** Built an **AI agent using LangChain + NVIDIA cuGraph** to classify queries and retrieve fraud insights dynamically.
 
3️⃣ **GraphRAG for Enhanced Retrieval**: Integrated **GraphRAG** to **retrieve fraud evidence efficiently** using context-aware AI.
 
4️⃣ **GPU-Accelerated Graph Analytics**: Leveraged **NVIDIA cuGraph** to speed up fraud detection using parallel processing.
 
5️⃣ **Hybrid Query Execution**: Combined **AQL (ArangoDB Query Language) with NetworkX** to handle **both structured** (graph traversal) and unstructured (fraud influence analysis) queries.
 
6️⃣ **Explainability with LLMs:** Used **langchain-groq** to generate natural language fraud explanations from graph-based insights.
 
## Challenges we ran into
🔸 **Data Availability** – Finding a **realistic financial fraud dataset** was difficult, so we experimented with **synthetic and open datasets.**
 
🔸 **Hybrid Query Execution Complexity** – Ensuring smooth integration between **AQL-based fraud retrieval and NetworkX-based fraud influence analysis** was challenging.
 
🔸 **Dynamic AI Agent Reliability** – The agent sometimes misclassified hybrid queries, requiring **better prompt engineering and tool selection logic.**

## Accomplishments that we're proud of
✅ **Built an AI agent that dynamically processes fraud-related queries**
 
✅ **Successfully integrated GraphRAG for intelligent retrieval of fraud evidence**
 
✅ **Implemented GPU-accelerated graph analytics to detect fraud rings efficiently**
 
✅ **Developed an explainable AI system that generates natural language fraud insights**
## What we learned
📌 **Graph-based fraud detection is highly effective** for uncovering hidden fraud rings.
 
📌 **Hybrid query execution (AQL + NetworkX) enables deeper fraud insights.**
 
📌 **AI agents need robust prompt engineering** to correctly classify and execute queries.

## What's next for ElderShield AI
🔹 **Real-world dataset integration** with **banking and financial institutions.**
 
🔹 **Expanding multi-agent capabilities** to **handle real-time fraud case investigations.**