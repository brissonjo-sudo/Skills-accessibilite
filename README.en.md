# Accessibility & Psychology Skills

A collection of Markdown skills for LLMs (large language models). Each skill programs the model's behavior to respond appropriately to users with specific cognitive, sensory, or neurobiological needs.

---

## Available skills

| Skill | Version | Description |
|---|---|---|
| `accessibilite-tdah` | V2.1 | ADHD-adapted communication: structure, anchoring, reduced cognitive load |
| `accessibilite-dys` | V3 | Dyslexia/dyscalculia/dyspraxia: readability, reformulation, visual structure |
| `accessibilite-tsa` | V4 | Autism-adapted: literality, predictability, no implied meaning |
| `accessibilite-haute-densite-cognitive` | V3 | High-density cognitive profiles (HPI/gifted): depth, nuance, no oversimplification |
| `accessibilite-douleur-chronique-fatigue-cognitive` | V3 | Chronic pain/fatigue (fibromyalgia, ME/CFS, long COVID): low-effort, no action injunctions |
| `accessibilite-visuelle` | V1 | Visual accessibility: image descriptions, semantic structure |
| `psychologie-rigoureuse` | V6 | Rigorous psychology: epistemic framework, confidence markers, non-dogmatic |

---

## How to use

### In Claude (recommended)

1. Go to **Settings → Capabilities → "+" → Create skill → Upload ZIP**
2. Download the ZIP for your skill from the [latest release](https://github.com/brissonjo-sudo/skills-accessibilite/releases/latest)
3. The skill activates automatically when conditions are met

### Via system prompt

Copy the content of `skills/<name>/SKILL.md` into the system prompt field of any LLM interface.

---

## Evaluation

Each skill is tested with [promptfoo](https://promptfoo.dev) across 3 LLMs (Mistral Large, Gemini 2.5 Flash, Claude Sonnet). See [`eval/`](eval/) for harnesses and result analyses.

---

## License

MIT — see [LICENSE](LICENSE)
