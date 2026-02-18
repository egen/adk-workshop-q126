# Google Agent Development Kit (ADK) Workshop

Build AI agents with Google's Agent Development Kit! In this workshop, you'll progressively build a Research Agent, starting from a simple single agent and evolving to a multi-agent hierarchical system.

## Workshop Overview

| Exercise | Description | Skills Learned |
|----------|-------------|----------------|
| **Exercise 1** | Simple Single Agent | ADK basics, Agent class, deployment |
| **Exercise 2** | Agent with Tools | Custom function tools, web scraping |
| **Exercise 3** | Multi-Agent Research Team | AgentTool pattern, orchestration, sub-agents |
| **Exercise 4** | Agent Evaluation | Eval framework, rubric-based metrics, prompt engineering |

## Prerequisites

- Python 3.10+
- Google API Key (from [AI Studio](https://aistudio.google.com/apikey))
- Git

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd adk-workshop-q126

# Create your workshop branch (use your name)
git checkout -b workshop/<your-name>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template and add your API key
cp .env.example .env
```

Edit `.env` and add your `GOOGLE_API_KEY`.

### 2. Run Locally

```bash
adk web
```

Open http://localhost:8080 to interact with your agent.

### 3. Deploy

```bash
git add .
git commit -m "My research agent"
git push -u origin workshop/<your-name>
```

Your agent will automatically deploy to Cloud Run.

## Your Deployment URL

After pushing, your agent will be available at:

```
https://<your-name>-adk-workshop-773815123342.us-central1.run.app
```

For example, branch `workshop/sam-gallagher` deploys to:
```
https://sam-gallagher-adk-workshop-773815123342.us-central1.run.app
```

## Exercises

Work through each exercise in order. Instructions are provided during the workshop.

### Exercise 1: Simple Single Agent

Create a basic research agent in `research_agent/agent.py`.

**Goal:** Define an `Agent` with a name, model, description, and instruction.

### Exercise 2: Agent with Tools

Extend your agent with a custom `fetch_webpage` tool for web research.

**Goal:** Build a custom function tool and attach it to an agent.

### Exercise 3: Multi-Agent Research Team

Build a research team using the `AgentTool` pattern where an orchestrator coordinates specialized sub-agents.

**Goal:** Create an orchestrator that delegates to researcher, fact_checker, and critic agents.

```
research_orchestrator (root)
├── researcher     (AgentTool) — web research via Google Search
├── fact_checker   (AgentTool) — independent claim verification
└── critic         (AgentTool) — identifies weaknesses and gaps
```

### Exercise 4: Agent Evaluation

Use ADK's evaluation framework to measure how prompt engineering affects agent quality. Run the same eval suite against a flawed agent and a fixed agent.

**Goal:** Run `adk eval`, interpret rubric-based metrics, and see how prompt changes improve scores.

See [solutions/exercise_4/INSTRUCTIONS.md](solutions/exercise_4/INSTRUCTIONS.md) for detailed instructions.

## Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [Gemini API](https://ai.google.dev/)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent returns `None` | Ensure `root_agent` is defined (not `None`) in `agent.py` |
| Tools not working | Check that tool functions have proper docstrings and type hints |
| Deployment fails | Check GitHub Actions logs; ensure branch matches `workshop/*` |
| API key errors | Verify `GOOGLE_API_KEY` is set in `.env` |

## Need Help?

Ask your workshop facilitator or check the `solutions/` folder for reference implementations.
