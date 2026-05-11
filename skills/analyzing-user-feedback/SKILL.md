---
name: analyzing-user-feedback
description: Synthesize user feedback from NPS, support tickets, interviews, sales notes, reviews, surveys, and churn reasons into themes, evidence, opportunities, and next actions.
---

# Analyzing User Feedback

Use this skill when the user has raw feedback, NPS comments, support tickets, interview snippets, sales notes, app reviews, survey responses, or churn notes and needs product insight.

Source note: inspired by RefoundAI Lenny Skills `analyzing-user-feedback` (MIT). This version is written for this kit.

## Workflow

1. Identify sources, sample size, segment, time period, and collection bias.
2. Cleanly separate raw feedback, inferred problem, requested solution, and product implication.
3. Cluster feedback into themes by user job, pain, trigger, and impact.
4. Score each theme by frequency, severity, revenue/user importance, confidence, and actionability.
5. Extract evidence: representative quotes, ticket links, NPS bands, account type, or behavioral data.
6. Turn themes into opportunities, discovery questions, roadmap candidates, or support/process fixes.

## Output

- Feedback source summary
- Theme table
- Evidence quotes or examples
- Segment differences
- Severity and confidence
- Product opportunities
- Non-product fixes
- Recommended next actions

## Guardrails

- Do not overgeneralize from biased samples such as only support tickets or only sales escalations.
- Preserve minority but high-severity feedback, especially from strategic customers or risk-heavy workflows.
- Do not convert solution requests into requirements without problem validation.
