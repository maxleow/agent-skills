# agent-skills

Reusable AI agent skills installable with `npx skills`.

## Available skills

| Skill | Description |
| --- | --- |
| [aws-architecture-diagrams](skills/aws-architecture-diagrams/SKILL.md) | Draw and edit AWS architecture diagrams using bundled official icons and light-theme guidance. |

## Repository layout

```text
skills/
└── aws-architecture-diagrams/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

## Install

List the available skills:

```sh
npx skills add maxleow/agent-skills --list
```

Install the AWS architecture skill:

```sh
npx skills add maxleow/agent-skills --skill aws-architecture-diagrams
```

To check discovery in a local clone before publishing:

```sh
npx skills add . --list
```

Each skill folder keeps its instructions, references, scripts, and assets together. The `name` in `SKILL.md` matches its containing folder.
