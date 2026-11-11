# The corpus and the measurements

> **When to read this file.** Read it when you need to know what the six documents are, how a number in this skill was measured, or the value of a feature for one document.
> It holds the corpus table, the method of measurement with its caveats, and the measured tables for the six documents and the two pools.
> The targets derived from these tables are in Table B of `voice-and-transfer.md`; this file gives the values behind them.

## The corpus

Andre Frankenthal selected six documents whose writing he led. The tags are used in every file of this skill.

| Tag | Document | Venue | His role | Genre | Words of running text |
|---|---|---|---|---|---:|
| PROC | "Searching for Dark Photons with PADME" | Proceedings of DPF 2019, arXiv:1910.00764 | single author | status report on an experiment | 1,349 |
| SAC | "Characterization and Performance of PADME's Cherenkov-Based Small-Angle Calorimeter" | Nuclear Instruments and Methods A, arXiv:1809.10840 | first author of 25 | detector paper with test-beam and simulation results | 5,138 |
| IDM | "Search for inelastic dark matter in events with two displaced muons and missing transverse momentum in proton-proton collisions at √s = 13 TeV" (CMS EXO-20-010) | Physical Review Letters, arXiv:2305.11649 | CMS Collaboration paper; he led the analysis and the writing | search letter | 3,398 |
| ETA | "Observation of the rare decay of the η meson to four muons" (CMS BPH-22-003) | Physical Review Letters, arXiv:2305.04904 | CMS Collaboration paper; he led the writing | observation letter | 2,880 |
| SCOUT | "Enriching the physics program of the CMS experiment via data scouting and data parking" (CMS EXO-23-007) | Physics Reports, arXiv:2403.16134 | CMS Collaboration paper with many contributors; he led the writing | long review | 37,175 |
| THESIS | "Search for dark matter decaying to two displaced muons produced in proton-proton collisions at 13 TeV with the CMS detector, and for dark photons produced in electron-positron fixed-target collisions at 500 MeV with the PADME detector" | PhD thesis, Cornell University, 2020, 318 pages | single author | thesis; its chapter 14 reprints SAC | 42,049 |

**Two pools.** OWN = PROC + SAC + THESIS is his own voice: 44,002 words, with the reprinted chapter counted once. CMS = IDM + ETA + SCOUT passed the style rules and the editing of the CMS Collaboration: 43,216 words. Read the OWN column as what he writes when left alone and the CMS column as what he signs in a collaboration paper. OWN is mostly the thesis and CMS is mostly the review, so for a paper in his own voice the SAC column is the better guide, and for a letter the IDM and ETA columns.

**Locators.** A quote in this skill is followed by its tag and by the file and line where it starts: `main.tex` is the LaTeX source of a paper as posted on arXiv, and `paper.txt` is the text of the thesis PDF. The sources are not part of this repository. The quotes are short excerpts used to describe style.

## How the measurements were made

A deterministic script (Python standard library only) cleaned the LaTeX sources of the five papers and the PDF text of the thesis, split them into paragraphs, sentences and captions, and counted. Running text is the abstract plus the body, with list items and footnotes; captions are measured apart. A word is a token between spaces that holds a letter or a digit. A math expression, any other macro in running text and a reference to a float each count as one word, and a citation counts as none. Acknowledgments, author lists and bibliographies are left out. Rates are given per 1,000 or per 10,000 words, and shares in percent of sentences, of paragraphs or of captions, as each table says.

The main caveats:

- **Weights.** OWN is dominated by the thesis and CMS by the review. A thesis is a different genre from a paper.
- **Repeated text.** Chapter 14 of the thesis reprints SAC. The OWN column leaves out those 56 paragraphs (212 sentences, 4,534 words) and 19 captions; the THESIS column still contains them.
- **House style.** The script cannot tell a style rule from an editor's taste. Differences between OWN and CMS such as "roughly" against "approximately", "due to" against "because of", the comma after "i.e." and "Fig." against "Figure" look like rules of the collaboration.
- **The thesis comes from PDF text.** Subscripts, formulas and bullet lists leave debris, and paragraph starts were read from the indentation. The same cleaner applied to the PDF text of IDM, ETA and SCOUT gives the same median sentence length as their LaTeX sources, a mean within about one word, a passive share within 1.5 percentage points and a share of sentences above 30 words within 4 points. Sentence-level numbers of the thesis are good to about one word and three percentage points; its paragraphs may come out a little too long.
- **Passive.** A passive is a form of "be" followed within three words by a past participle. Reduced passives ("data collected in 2018") are not counted; adjectival participles ("is expected") are.
- **Openers.** A sentence is put in a class by its first words only, in the order of the rows of the table.
- **Rough heuristics.** The causal use of "since", "so" as a conjunction and the class of a caption's last sentence rest on keyword tests. Use them for large differences only. Counts quoted in the other files as "by reading" or "hand count" come from reading the documents and can differ from the script.
- **Small documents.** PROC has 67 sentences and 7 captions, and the two letters have about 130 sentences each. One sentence is 1.5% of PROC, and one caption is 14%.

`scripts/andre_style_check.py` measures a draft in a similar way and prints the result next to the target ranges; see `scripts/README.md` for its definitions.

## 1. Sizes

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Words of running text | 1349 | 5138 | 3398 | 2880 | 37175 | 42049 | 44002 | 43216 |
| Sentences | 67 | 234 | 134 | 121 | 1479 | 2008 | 2097 | 1725 |
| Body paragraphs | 14 | 61 | 17 | 17 | 315 | 492 | 512 | 347 |
| Words in the abstract | 75 | 174 | 110 | 113 | 158 | 202 | 451 | 381 |
| Captions | 7 | 20 | 6 | 7 | 76 | 184 | 192 | 89 |
| Words in captions | 179 | 869 | 395 | 344 | 4194 | 7319 | 7541 | 4933 |
| Section and subsection titles | 4 | 14 | 0 | 0 | 78 | 121 | 139 | 78 |

IDM and ETA are letters without section titles.

## 2. Sentence length (words per sentence, running text)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| median | 19.0 | 20.0 | 23.0 | 22.0 | 24.0 | 20.0 | 20.0 | 24.0 |
| mean | 20.1 | 22.0 | 25.4 | 23.8 | 25.1 | 20.9 | 21.0 | 25.1 |
| 10th percentile | 11.0 | 12.0 | 13.0 | 13.0 | 13.0 | 11.0 | 11.0 | 13.0 |
| 25th percentile | 14.0 | 15.0 | 17.0 | 16.0 | 18.0 | 14.0 | 14.0 | 18.0 |
| 75th percentile | 24.5 | 26.0 | 31.0 | 29.0 | 31.0 | 25.0 | 25.0 | 31.0 |
| 90th percentile | 31.2 | 33.7 | 40.0 | 37.0 | 38.0 | 33.0 | 33.0 | 38.6 |
| longest | 51 | 92 | 78 | 57 | 79 | 95 | 95 | 79 |
| share with 12 words or fewer (%) | 19.4 | 13.7 | 9.7 | 9.1 | 8.5 | 17.2 | 17.2 | 8.7 |
| share above 30 words (%) | 10.4 | 17.5 | 26.1 | 20.7 | 25.8 | 14.7 | 14.7 | 25.4 |
| share above 40 words (%) | 1.5 | 4.3 | 9.7 | 7.4 | 7.8 | 3.4 | 3.5 | 7.9 |

## 3. Paragraph length (body paragraphs)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| paragraphs | 14 | 61 | 17 | 17 | 315 | 492 | 512 | 347 |
| sentences per paragraph: median | 4.5 | 3.0 | 8.0 | 6.0 | 4.0 | 4.0 | 4.0 | 4.0 |
| … 25th percentile | 4.0 | 3.0 | 5.0 | 5.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| … 75th percentile | 6.0 | 5.0 | 10.0 | 8.0 | 6.0 | 5.0 | 5.0 | 6.0 |
| … mean | 4.5 | 3.7 | 7.6 | 6.9 | 4.6 | 4.0 | 4.0 | 4.9 |
| … max | 6 | 9 | 15 | 12 | 13 | 20 | 20 | 15 |
| words per paragraph: median | 93.0 | 74.0 | 176 | 151 | 106 | 76.0 | 76.0 | 111 |
| … 25th percentile | 67.5 | 60.0 | 140 | 144 | 76.0 | 55.0 | 55.0 | 77.0 |
| … 75th percentile | 114.2 | 104 | 212 | 181 | 149 | 110 | 109.2 | 157 |
| … mean | 91.0 | 81.1 | 193.4 | 162.8 | 116 | 84.8 | 84.8 | 122.1 |
| … max | 161 | 169 | 366 | 286 | 306 | 470 | 470 | 366 |
| one-sentence paragraphs (%) | 0.0 | 6.6 | 0.0 | 0.0 | 4.1 | 8.9 | 8.6 | 3.8 |
| two-sentence paragraphs (%) | 14.3 | 16.4 | 0.0 | 0.0 | 13.0 | 13.8 | 14.4 | 11.8 |
| paragraphs of 8+ sentences (%) | 0.0 | 3.3 | 52.9 | 29.4 | 12.1 | 6.1 | 5.9 | 15.0 |

## 4. First person (per 1,000 words)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| we | 1.48 | 9.15 | 2.35 | 2.08 | 0.75 | 2.85 | 2.86 | 0.97 |
| we + our + us | 1.48 | 11.09 | 2.35 | 2.43 | 0.89 | 3.47 | 3.48 | 1.11 |
| I | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.50 | 0.00 |
| I + my + me | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.55 | 0.52 | 0.00 |
| sentences containing "we" (%) | 2.99 | 19.23 | 5.97 | 4.96 | 1.89 | 5.78 | 5.82 | 2.43 |

"I" occurs only in the thesis.

## 5. Passive voice

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sentences with at least one passive (%) | 37.3 | 42.7 | 56.0 | 52.9 | 52.1 | 39.6 | 39.5 | 52.5 |
| passives per 1,000 words | 19.3 | 21.4 | 26.8 | 23.6 | 23.8 | 21.2 | 21.0 | 24.0 |
| passives per sentence | 0.39 | 0.47 | 0.68 | 0.56 | 0.60 | 0.44 | 0.44 | 0.60 |

## 6. Sentence openers (share of sentences, %)

### 6.1 Classes

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Connector from the list in the next table | 7.5 | 10.7 | 6.0 | 5.8 | 7.6 | 8.5 | 8.3 | 7.4 |
| Other connectors and sentence adverbs (Here, Instead, In general, ...) | 4.5 | 0.8 | 1.5 | 2.5 | 1.6 | 3.3 | 3.3 | 1.6 |
| The / This / These / A / An / Each / All | 44.8 | 47.0 | 51.5 | 58.7 | 52.6 | 47.0 | 47.0 | 52.9 |
| It / There / Such / Both / Some / Several / Most / Many / One ... | 9.0 | 4.7 | 7.5 | 1.6 | 4.5 | 6.9 | 7.0 | 4.6 |
| We / Our | 1.5 | 7.7 | 2.2 | 0.8 | 0.3 | 1.8 | 1.9 | 0.5 |
| I | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.3 | 0.3 | 0.0 |
| Fronted phrase: In, For, To, At, After, Since, With, ... | 11.9 | 15.4 | 11.2 | 14.1 | 13.7 | 12.3 | 12.3 | 13.6 |
| Other fronted phrases: Despite, During, Unlike, Based on, ... | 1.5 | 4.7 | 1.5 | 1.6 | 1.6 | 1.6 | 1.7 | 1.6 |
| a symbol (MATH or macro) | 0.0 | 0.4 | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0.0 |
| Figure / Fig. / Table | 6.0 | 3.9 | 0.8 | 3.3 | 2.4 | 4.8 | 4.8 | 2.4 |
| Section / Ref. / Equation | 0.0 | 0.0 | 0.0 | 0.0 | 0.6 | 0.5 | 0.5 | 0.5 |
| a number | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0.0 |
| an -ing word not listed above | 0.0 | 0.8 | 0.8 | 2.5 | 0.7 | 0.8 | 0.8 | 0.8 |
| an -ly adverb not listed above | 0.0 | 0.4 | 0.8 | 0.0 | 0.5 | 0.2 | 0.2 | 0.5 |
| anything else (mostly a bare noun phrase or name) | 13.4 | 3.4 | 16.4 | 9.1 | 13.8 | 11.8 | 11.8 | 13.6 |

### 6.2 Connectors at the start of a sentence (rows with any use)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| However | 0.00 | 0.85 | 0.75 | 0.83 | 0.47 | 1.20 | 1.14 | 0.52 |
| Therefore | 0.00 | 0.43 | 0.00 | 0.83 | 0.41 | 1.00 | 0.95 | 0.41 |
| Thus | 0.00 | 0.43 | 0.00 | 0.00 | 0.61 | 0.45 | 0.43 | 0.52 |
| Hence | 0.00 | 0.43 | 0.00 | 0.00 | 0.20 | 0.15 | 0.14 | 0.17 |
| Moreover | 2.99 | 0.00 | 0.75 | 0.00 | 0.54 | 0.45 | 0.52 | 0.52 |
| Furthermore | 1.49 | 1.28 | 0.00 | 0.83 | 0.54 | 0.95 | 0.95 | 0.52 |
| In addition | 0.00 | 0.00 | 0.00 | 0.00 | 0.61 | 0.00 | 0.00 | 0.52 |
| Additionally | 0.00 | 0.00 | 0.00 | 0.00 | 0.47 | 0.10 | 0.10 | 0.41 |
| Finally | 1.49 | 0.43 | 2.24 | 0.83 | 1.15 | 1.54 | 1.53 | 1.22 |
| Consequently | 0.00 | 0.43 | 0.00 | 0.00 | 0.27 | 0.05 | 0.05 | 0.23 |
| Nevertheless | 0.00 | 2.14 | 0.00 | 0.00 | 0.07 | 0.75 | 0.72 | 0.06 |
| Similarly | 0.00 | 0.00 | 0.00 | 0.00 | 0.27 | 0.15 | 0.14 | 0.23 |
| Indeed | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.05 | 0.05 | 0.06 |
| For example | 1.49 | 0.00 | 0.00 | 0.00 | 0.07 | 0.15 | 0.19 | 0.06 |
| For instance | 0.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.05 | 0.05 | 0.17 |
| In particular | 0.00 | 0.43 | 0.00 | 0.00 | 0.20 | 0.30 | 0.29 | 0.17 |
| Specifically | 0.00 | 0.00 | 1.49 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 |
| Note that | 0.00 | 1.71 | 0.00 | 0.00 | 0.00 | 0.40 | 0.38 | 0.00 |
| Also | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.05 | 0.00 |
| Then | 0.00 | 0.43 | 0.00 | 0.00 | 0.34 | 0.05 | 0.05 | 0.29 |
| Next | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.10 | 0.00 |
| First | 0.00 | 1.28 | 0.00 | 0.00 | 0.34 | 0.25 | 0.24 | 0.29 |
| Second | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.12 |
| On the other hand | 0.00 | 0.43 | 0.00 | 0.00 | 0.00 | 0.05 | 0.05 | 0.00 |
| In contrast | 0.00 | 0.00 | 0.00 | 0.83 | 0.20 | 0.10 | 0.10 | 0.23 |
| As a result | 0.00 | 0.00 | 0.00 | 0.00 | 0.34 | 0.00 | 0.00 | 0.29 |
| Overall | 0.00 | 0.00 | 0.00 | 0.83 | 0.07 | 0.15 | 0.14 | 0.12 |
| In summary | 0.00 | 0.00 | 0.75 | 0.83 | 0.07 | 0.00 | 0.00 | 0.17 |
| **Total** | 7.46 | 10.68 | 5.97 | 5.79 | 7.64 | 8.47 | 8.35 | 7.42 |

"In conclusion" and "Lastly" open no sentence in any of the six documents.

### 6.3 Determiners and pronouns at the start

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| The | 32.84 | 32.91 | 35.82 | 37.19 | 39.96 | 30.38 | 30.66 | 39.54 |
| This | 5.97 | 6.84 | 5.97 | 8.26 | 4.87 | 9.96 | 9.73 | 5.22 |
| These | 1.49 | 1.28 | 4.48 | 3.31 | 3.45 | 2.99 | 2.91 | 3.54 |
| A | 2.99 | 5.13 | 4.48 | 9.09 | 2.84 | 2.34 | 2.38 | 3.25 |
| An | 0.00 | 0.00 | 0.00 | 0.83 | 0.68 | 0.55 | 0.52 | 0.64 |
| Each | 0.00 | 0.85 | 0.00 | 0.00 | 0.27 | 0.60 | 0.57 | 0.23 |
| All | 1.49 | 0.00 | 0.75 | 0.00 | 0.54 | 0.15 | 0.19 | 0.52 |
| **Total of the seven above** | 44.78 | 47.01 | 51.49 | 58.68 | 52.60 | 46.96 | 46.97 | 52.93 |
| It | 4.48 | 0.43 | 0.00 | 0.00 | 1.08 | 2.09 | 2.15 | 0.93 |
| There | 1.49 | 1.28 | 0.00 | 0.00 | 0.14 | 1.44 | 1.43 | 0.12 |
| We | 1.49 | 7.69 | 2.24 | 0.83 | 0.34 | 1.79 | 1.91 | 0.52 |
| "This" followed directly by a verb (% of sentences that open with This) | 50.0 | 56.2 | 50.0 | 20.0 | 19.4 | 47.5 | 47.5 | 22.2 |

### 6.4 Fronted phrases at the start (the more frequent ones)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| In | 0.00 | 2.99 | 3.73 | 2.48 | 5.81 | 3.69 | 3.62 | 5.45 |
| For | 0.00 | 2.99 | 0.75 | 1.65 | 1.69 | 1.69 | 1.62 | 1.62 |
| To | 1.49 | 2.14 | 4.48 | 4.13 | 1.28 | 1.39 | 1.43 | 1.74 |
| At | 0.00 | 0.00 | 0.75 | 0.83 | 1.01 | 0.40 | 0.38 | 0.93 |
| After | 1.49 | 0.43 | 0.00 | 0.00 | 0.34 | 0.15 | 0.19 | 0.29 |
| Since | 0.00 | 1.28 | 0.75 | 0.83 | 0.68 | 1.10 | 1.05 | 0.70 |
| While | 0.00 | 0.00 | 0.00 | 0.00 | 0.47 | 0.50 | 0.48 | 0.41 |
| Because | 0.00 | 0.00 | 0.75 | 0.83 | 0.14 | 0.05 | 0.05 | 0.23 |
| As | 0.00 | 0.43 | 0.00 | 0.00 | 0.81 | 0.25 | 0.24 | 0.70 |
| If | 2.99 | 0.00 | 0.00 | 0.00 | 0.14 | 1.05 | 1.10 | 0.12 |
| With | 0.00 | 0.85 | 0.00 | 0.83 | 0.27 | 0.70 | 0.67 | 0.29 |
| By | 4.48 | 0.43 | 0.00 | 0.00 | 0.27 | 0.35 | 0.48 | 0.23 |
| From | 1.49 | 2.56 | 0.00 | 0.00 | 0.00 | 0.45 | 0.48 | 0.00 |
| Given | 0.00 | 0.85 | 0.00 | 0.83 | 0.54 | 0.15 | 0.14 | 0.52 |
| **Total of the 19 fronted words of the class (14 shown)** | 11.94 | 15.38 | 11.19 | 14.05 | 13.73 | 12.30 | 12.30 | 13.57 |

## 7. Causal words and other joins (per 10,000 words, anywhere in a sentence)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| because | 0.0 | 0.0 | 17.7 | 10.4 | 7.8 | 8.1 | 7.7 | 8.8 |
| because of | 0.0 | 0.0 | 14.7 | 3.5 | 5.4 | 2.6 | 2.5 | 6.0 |
| since (all) | 7.4 | 5.8 | 5.9 | 3.5 | 6.7 | 19.7 | 19.1 | 6.5 |
| since (causal, heuristic) | 7.4 | 5.8 | 5.9 | 3.5 | 3.0 | 19.0 | 18.4 | 3.2 |
| so (all) | 0.0 | 7.8 | 2.9 | 3.5 | 2.7 | 9.5 | 9.3 | 2.8 |
| so (conjunction: ", so", "and so", "so that", sentence-initial) | 0.0 | 5.8 | 2.9 | 0.0 | 0.5 | 5.0 | 4.8 | 0.7 |
| therefore | 14.8 | 5.8 | 5.9 | 3.5 | 4.6 | 11.2 | 11.1 | 4.6 |
| thus | 7.4 | 5.8 | 8.8 | 0.0 | 8.6 | 2.6 | 2.7 | 8.1 |
| hence | 0.0 | 7.8 | 0.0 | 3.5 | 1.3 | 4.3 | 4.3 | 1.4 |
| due to | 7.4 | 17.5 | 5.9 | 0.0 | 2.4 | 11.7 | 11.6 | 2.5 |
| owing to | 0.0 | 0.0 | 0.0 | 6.9 | 0.0 | 1.0 | 0.9 | 0.5 |
| as a result | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | 0.2 | 0.2 | 2.1 |
| which (all) | 22.2 | 50.6 | 44.1 | 24.3 | 33.4 | 37.8 | 37.7 | 33.8 |
| which after a comma | 14.8 | 33.1 | 41.2 | 17.4 | 28.0 | 22.8 | 23.0 | 28.5 |
| which after a preposition (in which, of which) | 0.0 | 5.8 | 2.9 | 6.9 | 4.8 | 5.2 | 5.0 | 4.9 |
| which with no comma and no preposition | 7.4 | 11.7 | 0.0 | 0.0 | 0.5 | 9.8 | 9.8 | 0.5 |
| while | 14.8 | 9.7 | 11.8 | 3.5 | 10.5 | 10.7 | 10.7 | 10.2 |
| but | 0.0 | 13.6 | 20.6 | 13.9 | 5.6 | 17.4 | 16.6 | 7.4 |
| however (all) | 0.0 | 5.8 | 2.9 | 6.9 | 2.4 | 7.4 | 7.3 | 2.8 |
| however, not sentence-initial | 0.0 | 1.9 | 0.0 | 3.5 | 0.5 | 1.7 | 1.8 | 0.7 |
| respectively | 0.0 | 1.9 | 8.8 | 10.4 | 10.2 | 5.7 | 5.5 | 10.2 |
| in order to | 0.0 | 15.6 | 0.0 | 0.0 | 1.9 | 5.0 | 5.0 | 1.6 |
| and thus | 7.4 | 1.9 | 0.0 | 0.0 | 3.0 | 0.2 | 0.5 | 2.5 |
| and therefore | 7.4 | 0.0 | 2.9 | 0.0 | 1.1 | 2.6 | 2.7 | 1.2 |
| and hence | 0.0 | 5.8 | 0.0 | 3.5 | 0.5 | 3.6 | 3.6 | 0.7 |
| compared to | 0.0 | 5.8 | 11.8 | 20.8 | 9.1 | 5.9 | 5.7 | 10.2 |
| compared with | 0.0 | 1.9 | 0.0 | 0.0 | 1.1 | 0.2 | 0.2 | 0.9 |

Connector words counted anywhere in a sentence, also per 10,000 words. "Also" and "then" include uses that are not connectors.

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| however | 0.0 | 5.8 | 2.9 | 6.9 | 2.4 | 7.4 | 7.3 | 2.8 |
| therefore | 14.8 | 5.8 | 5.9 | 3.5 | 4.6 | 11.2 | 11.1 | 4.6 |
| thus | 7.4 | 5.8 | 8.8 | 0.0 | 8.6 | 2.6 | 2.7 | 8.1 |
| hence | 0.0 | 7.8 | 0.0 | 3.5 | 1.3 | 4.3 | 4.3 | 1.4 |
| moreover | 14.8 | 0.0 | 2.9 | 0.0 | 2.2 | 2.1 | 2.5 | 2.1 |
| furthermore | 7.4 | 5.8 | 0.0 | 3.5 | 2.2 | 4.8 | 4.8 | 2.1 |
| in addition | 7.4 | 1.9 | 0.0 | 0.0 | 4.6 | 2.4 | 2.5 | 3.9 |
| additionally | 0.0 | 0.0 | 0.0 | 3.5 | 1.9 | 1.2 | 1.1 | 1.9 |
| finally | 7.4 | 1.9 | 8.8 | 3.5 | 5.1 | 7.8 | 7.7 | 5.3 |
| nevertheless | 0.0 | 9.7 | 0.0 | 0.0 | 0.5 | 3.6 | 3.4 | 0.5 |
| note that | 0.0 | 9.7 | 0.0 | 0.0 | 0.5 | 2.1 | 2.0 | 0.5 |
| also | 22.2 | 21.4 | 5.9 | 13.9 | 15.9 | 27.8 | 27.5 | 15.0 |
| then | 14.8 | 25.3 | 5.9 | 6.9 | 6.5 | 11.2 | 11.1 | 6.5 |

## 8. Approximators, modals and intensifiers (per 1,000 words)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| approximately | 0.00 | 0.20 | 0.59 | 0.69 | 0.51 | 0.05 | 0.04 | 0.53 |
| roughly | 0.74 | 1.17 | 0.00 | 0.35 | 0.21 | 1.00 | 0.95 | 0.21 |
| about | 0.00 | 1.17 | 1.18 | 2.43 | 0.86 | 0.69 | 0.68 | 0.99 |
| around | 0.74 | 0.39 | 0.29 | 0.69 | 0.59 | 0.55 | 0.55 | 0.58 |
| nearly | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.07 |
| almost | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.10 | 0.09 | 0.09 |
| about (+number) | 0.00 | 0.78 | 1.18 | 2.43 | 0.70 | 0.21 | 0.20 | 0.86 |
| around (+number) | 0.00 | 0.20 | 0.00 | 0.35 | 0.30 | 0.24 | 0.23 | 0.28 |
| TOTAL approximators (approximately, roughly, about+num, around+num, nearly, almost) | 0.74 | 2.34 | 1.77 | 3.82 | 1.91 | 1.59 | 1.52 | 2.04 |

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| can | 2.22 | 3.31 | 1.77 | 1.39 | 1.59 | 2.64 | 2.64 | 1.55 |
| could | 1.48 | 0.39 | 0.29 | 0.35 | 0.27 | 1.26 | 1.25 | 0.28 |
| may | 0.00 | 0.00 | 0.88 | 0.00 | 0.40 | 0.24 | 0.23 | 0.42 |
| might | 0.00 | 0.39 | 0.00 | 0.00 | 0.08 | 0.28 | 0.27 | 0.07 |
| would | 0.74 | 0.20 | 1.18 | 0.35 | 0.46 | 0.69 | 0.68 | 0.51 |
| should | 1.48 | 0.39 | 0.29 | 0.00 | 0.00 | 0.48 | 0.50 | 0.02 |
| must | 0.00 | 0.39 | 0.88 | 0.35 | 0.38 | 0.64 | 0.64 | 0.42 |
| will | 5.93 | 0.78 | 0.29 | 0.35 | 0.38 | 0.69 | 0.89 | 0.37 |
| cannot | 0.00 | 0.20 | 0.29 | 0.35 | 0.00 | 0.17 | 0.18 | 0.05 |
| TOTAL (can..must) | 5.93 | 5.06 | 5.30 | 2.43 | 3.17 | 6.23 | 6.20 | 3.26 |

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| very | 0.00 | 0.39 | 0.00 | 0.35 | 0.48 | 0.48 | 0.48 | 0.44 |
| significantly | 0.00 | 0.00 | 0.29 | 0.00 | 0.48 | 0.10 | 0.09 | 0.44 |
| highly | 0.00 | 0.20 | 0.88 | 0.35 | 0.08 | 0.12 | 0.11 | 0.16 |
| extremely | 0.00 | 0.00 | 0.00 | 0.35 | 0.00 | 0.28 | 0.27 | 0.02 |
| strongly | 0.00 | 0.00 | 0.59 | 0.00 | 0.05 | 0.05 | 0.04 | 0.09 |
| clearly | 0.00 | 0.20 | 0.00 | 0.00 | 0.16 | 0.02 | 0.02 | 0.14 |
| well (not "as well") | 0.74 | 0.00 | 0.88 | 0.35 | 0.35 | 0.40 | 0.41 | 0.39 |
| TOTAL | 0.74 | 0.78 | 2.65 | 1.39 | 1.61 | 1.45 | 1.43 | 1.69 |

## 9. Punctuation (per 1,000 words)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Semicolons | 0.00 | 0.97 | 0.59 | 1.04 | 0.62 | 0.83 | 0.80 | 0.65 |
| Colons | 4.45 | 2.53 | 1.77 | 1.04 | 1.10 | 4.28 | 4.23 | 1.16 |
| Dashes used as punctuation | 1.48 | 0.20 | 0.00 | 0.00 | 0.08 | 0.48 | 0.52 | 0.07 |
| En dashes in number ranges | 0.00 | 0.00 | 2.65 | 3.82 | 0.94 | 0.02 | 0.02 | 1.27 |
| Parenthesis pairs | 11.86 | 12.85 | 15.60 | 9.03 | 7.08 | 10.42 | 10.64 | 7.87 |
| "i.e." | 0.00 | 0.78 | 0.00 | 0.35 | 0.38 | 0.48 | 0.48 | 0.35 |
| "e.g." | 0.00 | 0.78 | 0.59 | 0.00 | 0.35 | 0.21 | 0.25 | 0.35 |
| "respectively" | 0.00 | 0.20 | 0.88 | 1.04 | 1.02 | 0.57 | 0.55 | 1.02 |
| Quotation marks (opening) | 0.00 | 0.97 | 0.59 | 1.04 | 1.29 | 1.09 | 1.07 | 1.23 |
| Question marks | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Exclamation marks | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Commas | 40.77 | 46.52 | 42.97 | 51.04 | 45.73 | 38.05 | 38.79 | 45.77 |

## 10. Fixed phrases (per 10,000 words)

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| in order to | 0.0 | 15.6 | 0.0 | 0.0 | 1.9 | 5.0 | 5.0 | 1.6 |
| as a function of | 0.0 | 15.6 | 8.8 | 0.0 | 5.1 | 6.4 | 6.1 | 5.1 |
| is required to | 0.0 | 0.0 | 5.9 | 3.5 | 1.9 | 0.2 | 0.2 | 2.3 |
| are required to | 0.0 | 0.0 | 0.0 | 0.0 | 4.8 | 0.7 | 0.7 | 4.2 |
| is shown in | 22.2 | 9.7 | 0.0 | 0.0 | 0.8 | 3.6 | 4.1 | 0.7 |
| are shown in | 0.0 | 3.9 | 2.9 | 0.0 | 1.1 | 2.4 | 2.3 | 1.2 |
| as shown in | 0.0 | 0.0 | 0.0 | 3.5 | 3.0 | 0.5 | 0.5 | 2.8 |
| with respect to | 0.0 | 0.0 | 0.0 | 0.0 | 4.8 | 0.2 | 0.2 | 4.2 |
| so-called | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| it is | 7.4 | 3.9 | 0.0 | 3.5 | 3.8 | 13.6 | 13.2 | 3.5 |
| there is | 0.0 | 11.7 | 0.0 | 0.0 | 1.3 | 8.6 | 8.2 | 1.2 |
| there are | 7.4 | 5.8 | 0.0 | 0.0 | 2.4 | 7.6 | 7.5 | 2.1 |
| note that | 0.0 | 9.7 | 0.0 | 0.0 | 0.5 | 2.1 | 2.0 | 0.5 |
| in this Letter | 0.0 | 0.0 | 2.9 | 3.5 | 0.0 | 0.0 | 0.0 | 0.5 |
| in this paper | 0.0 | 5.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.7 | 0.0 |
| we present | 0.0 | 0.0 | 2.9 | 0.0 | 0.3 | 0.0 | 0.0 | 0.5 |
| we report | 0.0 | 1.9 | 0.0 | 3.5 | 0.3 | 0.0 | 0.2 | 0.5 |
| we describe | 7.4 | 3.9 | 0.0 | 0.0 | 0.8 | 0.7 | 0.9 | 0.7 |
| we find | 0.0 | 5.8 | 0.0 | 0.0 | 0.0 | 0.5 | 0.7 | 0.0 |
| we observe | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 11. Captions

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| captions | 7 | 20 | 6 | 7 | 76 | 184 | 192 | 89 |
| words: median | 24.0 | 42.0 | 69.5 | 38.0 | 50.0 | 38.0 | 37.0 | 50.0 |
| … 25th percentile | 22.5 | 29.0 | 45.2 | 33.5 | 35.0 | 22.0 | 22.0 | 35.0 |
| … 75th percentile | 25.5 | 50.5 | 88.5 | 70.0 | 69.5 | 52.2 | 52.0 | 72.0 |
| … mean | 25.6 | 43.5 | 65.8 | 49.1 | 55.2 | 39.8 | 39.3 | 55.4 |
| … shortest | 6 | 12 | 32 | 12 | 17 | 5 | 5 | 12 |
| … longest | 53 | 97 | 92 | 87 | 148 | 179 | 179 | 148 |
| sentences: median | 1.0 | 2.0 | 3.5 | 2.0 | 3.0 | 2.0 | 2.0 | 3.0 |
| … 25th percentile | 1.0 | 2.0 | 2.2 | 1.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| … 75th percentile | 2.0 | 3.2 | 4.8 | 3.5 | 4.0 | 3.0 | 3.0 | 4.0 |
| … mean | 1.4 | 2.8 | 3.7 | 2.7 | 2.9 | 2.4 | 2.3 | 2.9 |
| one-sentence captions (%) | 57.1 | 5.0 | 0.0 | 42.9 | 11.8 | 22.3 | 23.4 | 13.5 |
| captions of 4+ sentences (%) | 0.0 | 25.0 | 50.0 | 28.6 | 30.3 | 13.6 | 13.0 | 31.5 |
| opens with: bare noun phrase (%) | 100 | 90.0 | 100 | 85.7 | 68.4 | 98.9 | 97.9 | 71.9 |
| opens with: article (The/A/An) (%) | 0.0 | 0.0 | 0.0 | 14.3 | 23.7 | 1.1 | 1.0 | 21.4 |
| opens with: symbol (%) | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 |
| starts with a label in parentheses, e.g. "(a)" or "(nJets)"; openings are judged after it (%) | 0.0 | 5.0 | 0.0 | 0.0 | 0.0 | 17.9 | 17.2 | 0.0 |
| first sentence is a fragment without a finite verb (%) | 100 | 95.0 | 83.3 | 100 | 90.8 | 95.1 | 95.3 | 91.0 |
| mentions a color (%) | 0.0 | 35.0 | 50.0 | 42.9 | 44.7 | 15.2 | 15.1 | 44.9 |
| mentions a line or marker style (%) | 14.3 | 10.0 | 50.0 | 28.6 | 35.5 | 13.6 | 13.5 | 36.0 |
| mentions a color or a style (%) | 14.3 | 35.0 | 50.0 | 42.9 | 54.0 | 22.3 | 22.4 | 52.8 |
| mentions a panel: left/right/upper/(a) ... (%) | 28.6 | 20.0 | 16.7 | 28.6 | 51.3 | 37.5 | 37.5 | 47.2 |
| ends with a period (%) | 100 | 100 | 100 | 100 | 100 | 97.8 | 97.9 | 100 |
| last sentence states a conclusion (%) | 0.0 | 30.0 | 16.7 | 0.0 | 4.0 | 22.8 | 21.9 | 4.5 |
| last sentence is a reading aid (%) | 28.6 | 40.0 | 66.7 | 28.6 | 75.0 | 26.6 | 27.1 | 70.8 |
| last sentence is plain description (%) | 14.3 | 25.0 | 16.7 | 28.6 | 9.2 | 28.3 | 27.6 | 11.2 |
| **last sentence: conclusion or reading aid (%)** | 28.6 | 70.0 | 83.3 | 28.6 | 79.0 | 49.5 | 49.0 | 75.3 |

The preamble of SAC is not in the corpus, so the macro for the name of its crystal counts as a symbol: the two SAC captions under "opens with: symbol" start with that name, which is a noun phrase. The class of the last sentence is a keyword test on captions of two or more sentences: a conclusion has a causal or evaluative cue or a result verb (because, due to, agrees, meets, negligible, better, shifts), a reading aid names a plot element or says how a value was obtained (line, band, bin, denote, represent, estimated), and anything else is plain description. About a quarter of these labels are arguable. By reading, 8 of the 20 SAC captions state a finding somewhere in the caption.

## 12. References to figures and tables in running text

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| float mentions (Figure/Table + number) (per 1,000 words) | 5.19 | 5.64 | 2.35 | 2.78 | 2.77 | 4.88 | 4.82 | 2.75 |
| float mentions (Figure/Table + number) (count) | 7 | 29 | 8 | 8 | 103 | 205 | 212 | 119 |
| figure mentions (count) | 7 | 28 | 5 | 7 | 80 | 174 | 181 | 92 |
| table mentions (count) | 0 | 1 | 3 | 1 | 23 | 31 | 31 | 27 |
| float as subject: Figure N shows/illustrates/... (% of mentions; count) | 57.1; 4 | 28.6; 8 | 20.0; 1 | 57.1; 4 | 51.2; 41 | 47.7; 83 | 48.1; 87 | 50.0; 46 |
| float as subject: Table N lists/summarizes/shows/... (% of mentions; count) | 0.0; 0 | 100; 1 | 0.0; 0 | 0.0; 0 | 26.1; 6 | 38.7; 12 | 38.7; 12 | 22.2; 6 |
| float as subject: total (% of mentions; count) | 57.1; 4 | 31.0; 9 | 12.5; 1 | 50.0; 4 | 45.6; 47 | 46.3; 95 | 46.7; 99 | 43.7; 52 |
| participle + in: (as) shown in / seen in / listed in ... Fig. N (% of mentions; count) | 42.9; 3 | 41.4; 12 | 75.0; 6 | 50.0; 4 | 37.9; 39 | 36.1; 74 | 36.3; 77 | 41.2; 49 |
| parenthetical: (see Fig. N) (% of mentions; count) | 0.0; 0 | 6.9; 2 | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.9; 2 | 0.0; 0 |
| see Fig. N, not in parentheses (% of mentions; count) | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.0; 0 | 0.0; 0 |
| Figure at sentence start (count) | 0 | 0 | 1 | 4 | 30 | 81 | 73 | 35 |
| Fig. at sentence start (count) | 4 | 8 | 0 | 0 | 0 | 0 | 12 | 0 |
| Figure inside sentence (count) | 0 | 0 | 0 | 0 | 0 | 93 | 73 | 0 |
| Fig. inside sentence (count) | 3 | 20 | 4 | 3 | 50 | 0 | 23 | 57 |
| Table at sentence start (count) | 0 | 1 | 0 | 0 | 6 | 15 | 15 | 6 |
| Table inside sentence (count) | 0 | 0 | 3 | 1 | 17 | 16 | 16 | 21 |

Verbs after a figure or a table used as the subject (counts):

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Figure show | 4 | 7 | 1 | 3 | 36 | 50 | 54 | 40 |
| Figure illustrate | 0 | 1 | 0 | 0 | 2 | 7 | 7 | 2 |
| Figure compare | 0 | 0 | 0 | 1 | 1 | 5 | 5 | 2 |
| Table list | 0 | 0 | 0 | 0 | 2 | 3 | 3 | 2 |
| Figure depict | 0 | 0 | 0 | 0 | 0 | 5 | 5 | 0 |
| Table show | 0 | 0 | 0 | 0 | 1 | 4 | 4 | 1 |
| Table summarize | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3 |
| Table contrast | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |

Participle phrases before a float (counts):

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| as shown in Fig./Table N | 0 | 0 | 0 | 1 | 8 | 2 | 2 | 9 |
| shown in Fig./Table N | 3 | 7 | 3 | 1 | 12 | 35 | 38 | 16 |
| seen in Fig./Table N | 0 | 3 | 0 | 0 | 0 | 4 | 4 | 0 |
| illustrated in Fig./Table N | 0 | 0 | 0 | 0 | 2 | 6 | 6 | 2 |
| displayed in Fig./Table N | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| reported in Fig./Table N | 0 | 0 | 1 | 1 | 5 | 6 | 6 | 7 |
| plotted in Fig./Table N | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| as illustrated in Fig./Table N | 0 | 0 | 2 | 0 | 0 | 1 | 1 | 2 |

The phrase "as shown in" occurs 11 times in SCOUT in all; in three of them the float does not follow at once.

## 13. Abstracts

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS |
|---|---:|---:|---:|---:|---:|---:|
| sentences | 4 | 6 | 5 | 4 | 6 | 9 |
| words | 75 | 174 | 110 | 113 | 158 | 202 |
| words per sentence (mean) | 18.8 | 29.0 | 22.0 | 28.2 | 26.3 | 22.4 |
| longest sentence (words) | 23 | 46 | 42 | 40 | 42 | 37 |
| numbers | 3 | 12 | 4 | 9 | 1 | 6 |
| "we" | 1 | 3 | 0 | 0 | 0 | 0 |
| sentences with a passive | 2 | 1 | 4 | 4 | 4 | 2 |

## 14. Section and subsection titles

| Metric | PROC | SAC | IDM | ETA | SCOUT | THESIS | OWN | CMS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| titles | 4 | 14 | 0 | 0 | 78 | 121 | 139 | 78 |
| words per title: median | 2.5 | 3.0 | 0 | 0 | 3.0 | 2.0 | 2.0 | 3.0 |
| words per title: mean | 2.75 | 2.93 | 0 | 0 | 3.76 | 2.96 | 2.95 | 3.76 |
| capitalization: Sentence case | 0 | 11 | 0 | 0 | 60 | 76 | 87 | 60 |
| capitalization: Title Case | 2 | 0 | 0 | 0 | 0 | 6 | 8 | 0 |
| capitalization: ALL CAPS | 0 | 0 | 0 | 0 | 0 | 14 | 14 | 0 |
| capitalization: mixed | 0 | 1 | 0 | 0 | 8 | 3 | 4 | 8 |
| capitalization: one word / n.a. | 2 | 2 | 0 | 0 | 10 | 22 | 26 | 10 |
| titles that start with "The" | 0 | 1 | 0 | 0 | 9 | 5 | 6 | 9 |
| titles that start with an -ing word | 0 | 1 | 0 | 0 | 2 | 2 | 3 | 2 |

Capitalization is judged on the words after the first, leaving out short function words and acronyms. The title case of PROC and the capitals of the thesis chapter titles come from templates.
