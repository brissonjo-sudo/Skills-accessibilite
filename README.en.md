# Accessibility & Psychology Skills

A collection of Markdown skills for LLMs (large language models). Each skill programs the model's behavior to respond appropriately to users with specific cognitive, sensory, or neurobiological needs.

---

## Available skills

| Skill | Version on `main` | Status | Released (1.19.1) | Description |
|---|---|---|---|---|
| `psychologie-rigoureuse` | V6.3 | candidate | V6.1 | Rigorous psychology: epistemic framework, confidence markers, non-dogmatic |
| `accessibilite-tdah` | V2.4 | candidate | V2.2 | ADHD-adapted communication: structure, anchoring, reduced cognitive load |
| `accessibilite-dys` | V3.2 | production | V3.1 | Dyslexia/dyscalculia/dyspraxia: readability, reformulation, visual structure |
| `accessibilite-tsa` | V4.2 | production | V4.1 | Autism-adapted: literality, predictability, no implied meaning |
| `accessibilite-haute-densite-cognitive` | V3.3 | candidate | V3.1 | High-density cognitive profiles: depth, nuance, no oversimplification |
| `accessibilite-douleur-chronique-fatigue-cognitive` | V3.3 | candidate | V3.1 | Chronic pain/fatigue (fibromyalgia, ME/CFS, long COVID): low-effort, no action injunctions |
| `accessibilite-visuelle` | V1.3 | candidate | V1.1 | Low vision and blindness: linear structure, text alternatives, screen-reader compatibility |

"Released" is the version shipped in the ZIPs of the latest release: that is what you install. "Version on `main`" is the state of the repository, which may be ahead. A "candidate" skill has changed since its last validation and will be released after an independent validation wave.

The skills are written in French and target French-speaking users. This page is a summary; the reference documentation is in French:

- [`README.md`](README.md) — full documentation
- [`docs/index_skills.md`](docs/index_skills.md) — canonical index: versions, triggers, statuses
- [`docs/note_ethique.md`](docs/note_ethique.md) — ethical limits: these skills adapt communication; they do not diagnose, treat, or replace a professional
- [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md) — contribution rules

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

Each skill is validated in **waves**: every test case is answered twice — with and without the skill, same question, isolated contexts — then the pairs are graded blind by three independent judges. See [`eval/`](eval/) for the case bank, the protocol and archived analyses.

---

## License

MIT — see [LICENSE](LICENSE)
