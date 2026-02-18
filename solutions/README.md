# Exercise Solutions

This folder contains complete solutions for each workshop exercise.

## Using Solutions

To test a solution, you can either:

1. **Copy files to `research_agent/`:**
   ```bash
   # For Exercise 1
   cp solutions/exercise_1/agent.py research_agent/

   # For Exercise 2
   cp solutions/exercise_2/*.py research_agent/

   # For Exercise 3
   cp solutions/exercise_3/agent.py research_agent/
   cp -r solutions/exercise_3/agents research_agent/
   ```

2. **Run solutions directly:**
   ```bash
   # Modify main.py to point to solutions directory
   # Or use: adk web --agent-dir solutions/exercise_1
   ```

## Solution Structure

```
solutions/
├── exercise_1/
│   ├── __init__.py
│   └── agent.py          # Simple single agent
├── exercise_2/
│   ├── __init__.py
│   ├── agent.py          # Agent with tools
│   └── tools.py          # Custom tool definitions
└── exercise_3/
    ├── __init__.py
    ├── agent.py          # Orchestrator agent
    └── agents/
        ├── __init__.py
        ├── search_agent.py
        ├── summarizer_agent.py
        └── report_agent.py
```

## Notes

- Solutions are meant as reference implementations
- Feel free to modify and experiment with them
- Each solution builds on the previous exercise
  