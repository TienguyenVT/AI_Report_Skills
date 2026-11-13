# Appraise only the issues relevant to the claim

Adapted from the reviewed scientific-critical-thinking workflow; see the repository's provenance and third-party notice. This is a question set, not a formal scoring instrument.

## Design and measurement

- Can the design answer the descriptive, predictive, or causal question being asked?
- Does the measured variable represent the concept named in the conclusion?
- Are the sample, baseline, reporting period, exclusions, and measurement procedure comparable?
- Could selection, changes over time, measurement drift, regression to the mean, or attrition explain the observation?
- Are important assumptions reported, plausible, and distinguishable from facts?

## Numbers and analysis

- What is the independent sampling/assignment unit? Repeated readings from the same unit do not automatically increase the independent sample count.
- Are pooled percentages, means of group percentages, and transformed-scale means being distinguished?
- Are effect size, uncertainty, and practical relevance considered together when the data support them?
- Is a p-value being misread as the probability that a hypothesis is true? Is lack of significance being called proof of no effect?
- Were outcomes, subgroups, or analysis choices changed after seeing the data? Are those analyses labelled accordingly?
- Are missing values and exclusions explained? Could they alter the conclusion?

Do not demand a statistical test for a purely descriptive report. Do not reconstruct a test from insufficient summaries or assign an arbitrary pass threshold.

## Predictive or technical evaluations

- Were training, tuning, and evaluation kept separate, including learned preprocessing?
- Could related observations, time ordering, duplicate inputs, or shared sources leak information across partitions?
- Does the baseline use compatible data, constraints, and measurement boundaries?
- Is performance on one dataset or environment being generalized beyond what was evaluated?

## Synthesis and recommendations

- Are cited results independent, or do they reuse the same data or assumptions?
- Are dissimilar definitions, populations, interventions, or metrics pooled without justification?
- Has conflicting or inconclusive evidence been omitted?
- Does the recommendation add unexamined assumptions about cost, feasibility, risk, or stakeholder priorities?

For each material concern, give the source location, observation, impact, uncertainty, and a feasible next check. Separate reporting omissions from demonstrated flaws. A checklist total is not evidence certainty.
