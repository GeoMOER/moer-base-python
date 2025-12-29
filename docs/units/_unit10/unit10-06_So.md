---
title: LM | Reliable and Correct Programming with AI
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u11/header.png
  image_description: "Reliable programming and responsible use of artificial intelligence"
  caption: "Conceptual illustration generated with the assistance of artificial intelligence."
---

Artificial Intelligence can support software development, but it can also produce  
**incorrect, incomplete, or misleading code**.

A central insight is:

> **AI systems generate plausible code, not guaranteed correct code.**

Understanding how errors arise is essential for using AI responsibly in programming.

---

## How AI can be “tricked” into producing poor code

### 1) Vague or incomplete task descriptions

If a programming task is not clearly defined, the AI must guess the intention.

**Example of a vague task:**
> "Analyze the data and create a visualization."

Typical consequences:
- wrong choice of variables
- unsuitable plot types
- missing labels or context
- code that runs but does not solve the real task

---

### 2) Incorrect assumptions in task summaries

AI follows the information it is given, even if it is incorrect.

**Original task:**
> "Calculate the mean temperature."

**User summary (incorrect):**
> "We need the maximum value."

AI will generate syntactically correct Python code that solves the **wrong problem**.

---

### 3) Invented functions and libraries (“hallucinated code”)

AI may generate function names that sound plausible but do not exist.

**Example of incorrect code:**
```python
df.calculate_average("temperature")
```

This error often occurs when:
- the task is underspecified
- the user invents API names
- the AI is asked to generate code quickly without constraints

---

### 4) Loss of context in growing programs

As programs grow and are extended multiple times, important context may be lost:
- variable names
- helper functions
- file paths
- earlier design decisions

This can result in:
- missing functions
- mismatched variable names
- broken dependencies
- programs that suddenly stop working

---

## Typical failure pattern in larger projects

1. A small program works correctly  
2. New features are added step by step  
3. Task descriptions become less precise  
4. The AI modifies or rewrites parts of the code  
5. Previously working components are broken  

This is a structural limitation of AI-assisted development, not a software bug.

---

## Best practices for creating reliable programs with AI

### 1) Use precise task definitions

A good task description includes:
- clear goal
- defined input and output
- constraints (what must not change)
- edge cases

---

### 2) Maintain a project summary (single source of truth)

Keep a short written overview of:
- program purpose
- folder and file structure
- key functions
- assumptions and rules

Include this summary when requesting code changes from AI.

---

### 3) Request minimal, controlled changes

Avoid large, vague requests such as:
> "Rewrite the whole program."

Prefer precise instructions:
- "Modify only function X"
- "Add function Y without changing existing code"
- "Show only the changed lines"

---

### 4) Build modular code

Large programs should be structured into:
- small, focused functions
- separate modules or files

Modular design reduces complexity and prevents unintended side effects.

---

### 5) Test after each change

Even small changes can introduce errors.

Basic checks include:
- Does the program run?
- Are all functions defined?
- Are variable names consistent?
- Do results match expectations?

Testing is a human responsibility that cannot be delegated to AI.

---

## Key takeaway

- AI can produce convincing but incorrect code
- Unclear tasks increase the risk of errors
- Larger projects require structure and discipline
- Reliable programming depends on human oversight

Artificial Intelligence is a powerful tool —  
but **correctness, responsibility, and understanding remain human tasks**.
