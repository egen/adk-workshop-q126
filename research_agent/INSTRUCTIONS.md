# Exercise 4: Agent Evaluation

In this exercise, you'll use ADK's built-in evaluation framework to measure
agent quality. You'll run the same test suite against a **flawed** agent and
a **fixed** agent to see how evaluation catches prompt engineering problems.

## What We're Testing

The eval suite checks two things:

| Metric | What it measures | Threshold |
|--------|-----------------|-----------|
| `rubric_based_tool_use_quality_v1` | Did the agent use all three tools (researcher, fact_checker, critic)? Uses an LLM judge to evaluate tool usage against rubrics. | 0.8 |
| `final_response_match_v2` | Does the final report contain verified claims and address limitations? Uses an LLM judge for semantic matching. | 0.7 |

Each eval case defines three rubrics that the LLM judge checks:
1. Did the agent use `researcher` to search for information?
2. Did the agent use `fact_checker` to verify claims?
3. Did the agent use `critic` to identify weaknesses and gaps?

## Step 1: Run the Eval Against the Flawed Agent

`agent.py` starts by importing the flawed agent. Run the eval:

```bash
adk eval solutions/exercise_4 solutions/exercise_4/eval/research_eval.test.json \
    --config_file_path=solutions/exercise_4/eval/test_config.json \
    --print_detailed_results
```

You should see **failures**:

- `rubric_based_tool_use_quality_v1` fails because the flawed agent only calls
  `researcher` and skips `fact_checker` and `critic`
- `final_response_match_v2` fails because the report has no verified claims
  and no limitations section

## Step 2: Look at Why It Failed

Open `flawed_agent.py` and notice the problems:

1. The instruction says "use researcher to find information and then write up
   a report" — it skips verification and critique entirely
2. No enforced workflow — just "try to be helpful"
3. All three agents are available as tools, but the prompt doesn't require
   using them

Now open `fixed_agent.py` and compare:

1. Explicit 4-step workflow: RESEARCH → VERIFY → CRITIQUE → REPORT
2. "You MUST use all three agents in sequence"
3. Report requirements include verified claims and a limitations section

## Step 3: Switch to the Fixed Agent

Update `agent.py` to import the fixed agent instead:

```python
# Comment out the flawed agent:
# from .flawed_agent import root_agent

# Uncomment the fixed agent:
from .fixed_agent import root_agent
```

## Step 4: Run the Eval Again

```bash
adk eval solutions/exercise_4 solutions/exercise_4/eval/research_eval.test.json \
    --config_file_path=solutions/exercise_4/eval/test_config.json \
    --print_detailed_results
```

You should now see **passes** on both metrics. The fixed agent calls all three
sub-agents in order, and the final report includes verified claims and
addresses the critic's feedback.

## Key Takeaway

The only difference between the two agents is the **instruction prompt**. Same
model, same tools, same sub-agents. Evaluation lets you measure the impact of
prompt engineering changes quantitatively rather than relying on vibes.
