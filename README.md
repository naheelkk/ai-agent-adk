# 🧠 AI Project Ideation & Refinement Agents

This project uses a multi-agent architecture powered by Google's ADK to help users brainstorm, refine, and deliver creative project ideas. The agents use the `gemini-2.0-flash-001` model along with tool integration (e.g. `google_search`) to enhance idea generation and validation.

---

## 🚀 Project Structure

### 🔁 Root Agent: `root_agent`
Acts as the **orchestrator**. It coordinates between two specialist agents to deliver high-quality, practical project ideas.

**Responsibilities:**
1. Delegates idea generation to `idea_agent`.
2. Sends generated ideas to `refiner_agent` for filtering.
3. Returns a refined project list with requirements and pre-requisites to the user.

---

### 💡 Idea Agent: `idea_agent`
A **creative brainstormer** designed to come up with innovative, exciting project ideas using Google Search to spark inspiration.

- **Model:** `gemini-2.0-flash-001`
- **Tool:** `google_search`
- **Output:** 3 unique project ideas based on user input.

---

### 🔍 Refiner Agent: `refiner_agent`
A **filtering expert** that ensures only the best and least saturated ideas are selected.

- **Model:** `gemini-2.0-flash-001`
- **Tool:** `google_search`
- **Output:** Refined list of project ideas that are novel and have low competition.

---

## 🛠️ Technologies Used

- Python 3.12+
- [Google Agent Developer Kit (ADK)](https://github.com/google/agent-developer-kit)
- Gemini Pro (via `gemini-2.0-flash-001`)
- Tool: `google_search` from ADK

---

## 💡 Example Use Case

1. User requests: "Give me project ideas in AI + Education"
2. `idea_agent` generates creative project ideas.
3. `refiner_agent` filters those for novelty and low implementation rate.
4. `root_agent` presents the best final idea(s) with requirements.

---

## 📁 Directory Structure

multi_tool_agent/ ├── init.py ├── agent.py # Agent definitions ├── .env # Model and API configurations
---

## 📌 Notes

- Tools using OpenAI function calling are **not supported**. Only tools that are callable or `BaseTool` instances (like `google_search`) should be passed.
- Avoid passing entire modules; import specific tool instances.

---

## 📦 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/naheelkk/ai-agent-adk.git
   cd ai-agent-adk
Install dependencies:

pip install -r requirements.txt
Configure your .env file (e.g., for API keys or model config).

Run the app using the ADK CLI:

bash
Copy
Edit
adk run multi_tool_agent
✨ Future Improvements
Add more tools like domain-specific search or trend analysis

Integrate with databases for storing and tracking idea feedback

Web UI for easier interaction

🧑‍💻 Author
Naheel KK

GitHub: @naheelkk

📜 License
MIT License

