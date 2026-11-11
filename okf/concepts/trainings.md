---
type: Website
title: "MESA Trainings"
description: "MESA Trainings: short, single-task tutorials for the MESA Portal at mesa.cyverse.org and its apps, written for training participants and for anyone using MESA"
resource: https://idss-mesa.github.io/trainings/
tags: [training, tutorials, portal, jupyterlab, cyverse]
status: draft
generated: { by: "claude-code/2.1.224", at: "2026-11-11T00:00:00Z" }
stale_after: "2027-05-11T00:00:00Z"
sources:
  - id: trainings-repo
    resource: https://github.com/idss-mesa/trainings
    title: "idss-mesa/trainings repository"
    author: "team:idss-mesa"
---

# MESA Trainings

Short tutorials for getting things done on MESA, at
<https://idss-mesa.github.io/trainings/>.[^trainings-repo] Each one takes a
reader through a single task in five to ten minutes: what you will have at
the end, what you need, the steps with what you should see at each, a check,
the most likely slip, and what to do next. They are written for people
preparing for a MESA training session and for anyone using the
[MESA Portal](mesa-portal.md).

The first tutorials cover signing in to the portal, finding MESA's community
data, launching [MESA JupyterLab](jupyterlab.md) with the Data Store mounted,
saving work where it survives the session, and stopping an app. They link to
the [MESA Documentation](docs.md) for the full picture of each screen instead
of repeating it.

The tutorials are drafts: they were written from the documentation and have
not yet been validated step by step on the live portal. Each page says so.
Training content is licensed CC BY 4.0; code is BSD 3-Clause.

## For agents

The training site is its own OKF v0.2 bundle, built with Zensical from the
[idss-mesa/trainings](https://github.com/idss-mesa/trainings) repository:

- Outline: <https://idss-mesa.github.io/trainings/llms.txt>
- Full corpus: <https://idss-mesa.github.io/trainings/llms-full.txt>
- Any page's Markdown source: its URL plus `index.md`
- Agent guide: <https://idss-mesa.github.io/trainings/about/ai-agents/>

Crawling of `/trainings/` is governed by this origin's
<https://idss-mesa.github.io/robots.txt>.

[^trainings-repo]: idss-mesa/trainings repository
