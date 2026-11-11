# andre-paper-writing

A Claude skill for drafting, restructuring and polishing experimental high-energy-physics, detector and methods papers in the writing style of Andre Frankenthal (UC Irvine; CMS and PADME).

The skill was built at Andre Frankenthal's request, from six documents that he selected and whose writing he led. It describes how he builds a paper, shapes paragraphs and sentences, chooses words, and treats numbers, figures and captions. Each habit comes with the reason it helps the reader, numbers measured on the six documents, and verbatim quotes with their source lines. The skill keeps apart what is his own voice and what is CMS house style.

## The six documents

| Tag | Document |
|---|---|
| PROC | "Searching for Dark Photons with PADME", DPF 2019 proceedings, arXiv:1910.00764 |
| SAC | "Characterization and Performance of PADME's Cherenkov-Based Small-Angle Calorimeter", Nuclear Instruments and Methods A, arXiv:1809.10840 |
| IDM | CMS Collaboration, search for inelastic dark matter with two displaced muons, Physical Review Letters, arXiv:2305.11649 |
| ETA | CMS Collaboration, observation of the η meson decay to four muons, Physical Review Letters, arXiv:2305.04904 |
| SCOUT | CMS Collaboration, review of data scouting and data parking, Physics Reports, arXiv:2403.16134 |
| THESIS | PhD thesis, Cornell University, 2020 |

## Folder layout

```
SKILL.md                              principles, targets, procedures, templates, lexicon, guardrails, checklist
references/
  voice-and-transfer.md               own voice against CMS house style, all targets, the polishing procedure
  conception-and-structure.md         title, abstract, introduction, section order, conclusions
  paragraphs-and-flow.md              paragraph shape, links, order inside a passage
  sentences-and-voice.md              subject, voice, tense, length, punctuation
  words-and-phrases.md                verbs, verdict words, connectors, hedges, word lists, spelling
  figures-and-captions.md             figure references, captions, caption templates
  numbers-results-methods.md          numbers, comparisons, caveats, uncertainties, equations, methods
  corpus-and-measurements.md          the six documents, how the numbers were measured, the measured tables
scripts/
  andre_style_check.py                measures a draft and compares it with his ranges
  README.md                           options and counting rules of the checker
  example_draft.tex                   an invented passage for trying the checker
```

## Install

- **Claude Code.** Copy or clone this folder into your Claude skills directory, for example `~/.claude/skills/andre-paper-writing/`.
- **claude.ai.** Upload the folder as a skill (as a zip file).

## Use

Ask in your own words. Two examples:

- "Polish Section 3 of `draft.tex` the way Andre writes. Keep every number and all LaTeX as they are, and tell me what you changed."
- "Here are my notes, in Chinese, on the test-beam results. Write the results section and the figure captions in Andre's style."

Claude returns the text first, then a short report: what changed, what moved, the questions for the authors, and a confirmation that numbers, claims, citations and LaTeX are unchanged.

## The checker

```
python3 scripts/andre_style_check.py draft.tex
```

The script prints the measured style of a draft next to his ranges and lists the sentences to look at. It needs only the Python standard library. It is a smoke detector, not an authority: it counts surface features and cannot judge meaning.

## A note on the quotes and the examples

The quotes in this skill are short excerpts from the cited papers, used only to describe style. The papers themselves are not part of this repository. The before/after examples in `references/` follow one invented study (a test-beam measurement of the time resolution of a small scintillator timing detector) with invented numbers. None of them is a real result.
