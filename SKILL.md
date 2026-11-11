---
name: andre-paper-writing
description: Draft, restructure and polish experimental high-energy-physics, detector and methods papers in the writing style of Andre Frankenthal, measured on six documents he led (a detector paper, a proceedings contribution, two CMS letters, a CMS review and his thesis). The style gives every result its reference, opens short paragraphs on the thing described, keeps "we" for decisions, studies and claims, writes sentences of about 20 words with sober verdicts, and gives every figure a pointing sentence and a noun-phrase caption. Use this skill whenever the user asks to write or polish paper text "in Andre's style" or "the way Andre writes", works on a paper co-authored with him or one that he will edit, or names this skill. Use it also for captions, abstracts, summaries, conclusions and thesis chapters in that style, and when notes written in Chinese must become English paper text in that style.
---

# Writing papers the way Andre Frankenthal writes them

This skill describes how Andre Frankenthal (experimental particle physicist, CMS and PADME) writes scientific papers: how he builds a piece, shapes paragraphs and sentences, chooses words, and treats numbers and figures. Use it to draft, restructure or polish. Its first use is to polish a co-authored draft until it reads as if he had written it, before he edits it by hand. He selected the six documents below. The numbers in this skill were measured on them, and every quote is verbatim, followed by its tag and the file and line of its source.

| Tag | Document | Voice |
|---|---|---|
| PROC | "Searching for Dark Photons with PADME", DPF 2019 proceedings, arXiv:1910.00764 | his own; single author |
| SAC | "Characterization and Performance of PADME's Cherenkov-Based Small-Angle Calorimeter", NIM A, arXiv:1809.10840 | his own; first author of 25; the closest model for a methods paper by a few authors |
| IDM | CMS search for inelastic dark matter with two displaced muons, PRL, arXiv:2305.11649 | CMS paper; he led the analysis and the writing |
| ETA | CMS observation of the η meson decay to four muons, PRL, arXiv:2305.04904 | CMS paper; he led the writing |
| SCOUT | CMS review of data scouting and data parking, Physics Reports, arXiv:2403.16134 | CMS paper with many contributors; he led the writing |
| THESIS | PhD thesis, Cornell University, 2020 | his own; single author; its chapter 14 reprints SAC |

OWN = PROC + SAC + THESIS is his own voice. CMS = IDM + ETA + SCOUT carries CMS house style on top of it. A habit counts as his when it holds in OWN; most of his habits also survive in the CMS papers. The thesis dominates the OWN pool, so where SAC and the pool differ, SAC is the guide for a paper.

## The style in one paragraph

He states a need before the thing that answers it, and gives every result the requirement or the reference value that it is judged against. The introduction reaches the work in a few short steps and states the purpose once, in a plain "In this paper we evaluate ..." sentence. A short paper has no roadmap paragraph and no limitations section, and it does not survey related work (IDM says in six sentences why earlier searches miss its signal). Paragraphs are short, open on the thing they describe and end on what was learned. The thing is the subject of the sentence, "we" marks what the authors decided, studied, ran or claim, and operations on recorded data are passive. Sentences run to about 20 words; short ones carry verdicts and long ones carry lists. The reason sits in the same sentence as the choice ("due to", "since"), and the consequence follows in a "This + verb" sentence of its own or in a tail. A caveat stands where it arises, followed by what still holds ("Nevertheless,"). Words are plain and verdicts sober: a result "meets" a requirement and is not called "excellent" (SCOUT, with many contributors, is the exception). A number carries its condition and its reference. Every figure is introduced by a sentence with the figure or the plotted thing as subject ("Figure 5 shows ..."), the next sentences read the figure for the reader, and the caption is a noun phrase plus, as a rule, one or two sentences.

## Eleven principles

### 1. Give every result its reference

*Why:* a reader can judge a number only against a reference. With the reference beside it, the result needs no adjective.

- Say as a number what the device or method must achieve before any result appears. Then close each result against that number in the same sentence. SAC gives its 200 ps requirement one sentence before its 81 ps result in the abstract and uses "meet(s)" seven times (his other own documents state no requirement): "The PbF2 resolution was found to be 81 ps, which comfortably meets the 200 ps timing requirement for a successful SAC performance." [SAC main.tex:421]
- Where the work has no external requirement, use the standard method under the same condition as the reference. Never invent a requirement. The value of the standard method may follow the result: "The efficiency to select AK4 and AK8 scouting jets is about 100% for pT > 300 GeV. In comparison, the standard trigger is fully efficient only from around 700–800 GeV." [SCOUT main.tex:1174]
- Introduce each device, algorithm or design choice right after the problem it solves: "To mitigate such backgrounds, a very fast Small-Angle Calorimeter (SAC) is placed behind the main ECAL, flush with the central hole." [SAC main.tex:153] Where an option has a cost, state it in the same sentence ("while doubling the cost" [SAC main.tex:211]).
- Where a choice was made, name the options, give the number that decided, say where the rejected option would be better, and close with a verdict: "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]

### 2. Build a plain structure: the object first, short steps, one purpose sentence

*Why:* a reader who skims finds at fixed places what the paper is about, what it claims and how the claim is tested.

- **Abstract.** Open on the object of the paper or the experiment it serves, never on the field (6 of 6). Then give what is reported, the requirement or the reference, the measured numbers with their conditions, and one closing sentence. Use 4 to 6 sentences and 100 to 175 words. The abstracts of his two own papers say "we" (PROC once, SAC three times); the three CMS abstracts and his thesis abstract are passive.
- **Introduction.** Go from the general problem to the work in 3 to 6 short steps. Open on what is established set against what is not: "Despite the recent discovery of the Higgs boson at the LHC, solidifying our understanding of the standard model (SM) of particle physics, many lingering questions remain that the SM cannot yet explain." [SAC main.tex:136] (SAC, IDM, ETA and the thesis open with "remain(s)"; PROC opens on a definition.) Start each step from a noun that the previous step introduced. Cite little (the introductions of PROC and SAC hold 2 and 3 citations). Credit a borrowed method in one short sentence: "This procedure is adapted from Ref. [57]." [THESIS paper.txt:14662-14663] Keep the introduction to 10 to 15% of the body.
- **Purpose.** State it once in the introduction, at the head of a paragraph (PROC states it only in the last sentence of its abstract), with a plain verb (evaluate, present, report, describe) and the means. Do not write a bulleted list of contributions (0 of 6). "In this paper we evaluate the performance of a prototype of the SAC with a test beam done at LNF, using fast Lead Fluoride crystals (PbF2) and the newly developed Hamamatsu R13478UV photomultiplier tube (PMT), optimized for fast response." [SAC main.tex:155]
- **Sections.** Follow the order of the work and of the data. For a detector paper (SAC): the object, the design choices, the simulation, the setup, the reconstruction, the performance with one subsection per measured quantity, the conclusions. The corpus has no paper on an algorithm or a model; for one, keep the principle (each section uses only what earlier sections set up; one results subsection per measured quantity; conclusions last) and propose any reordering to the authors. Give each section a title of 1 to 4 plain words (84% of his own titles) in sentence case (PROC has title case) that names its content ("Timing resolution"). None of 217 section titles has a verb, a colon or a question mark.
- **No roadmap.** The four short papers have no roadmap paragraph. Use at most three one-line signposts: "These studies are discussed below." [SAC main.tex:374] Write no section named Limitations, Discussion or Related work.
- **Conclusions** (SAC is the one example in his own voice; PROC has none). Say what was done (present perfect), give the verdict, repeat every headline number of the abstract with the same digits and the same condition (SAC: 4 of 4; SAC changes two of the labels, which is not to be copied), add one statement on wider use, and end on a concrete next step. Use 6 to 8 sentences. Do not write "In conclusion".

### 3. Keep paragraphs short; open on the thing and end on what was learned

*Why:* first sentences then work as headings, and the last sentence is the one the reader carries forward.

- Write 3 to 5 sentences and 60 to 110 words per paragraph (OWN median: 4 sentences and 76 words; SAC: 3 and 74). A step of the introduction is shorter, 2 to 4 sentences (SAC: 2, 2, 2, 4, 2, 4 and 3); do not merge two-sentence paragraphs to reach three. Only a step-by-step procedure or the description of a setup runs past 7 sentences. A one-sentence paragraph only leads into an equation or a list, or signposts.
- Make the thing described the grammatical subject of the first sentence (59% of paragraphs in OWN, 48% in SAC, 72% in CMS): "The ECAL has a central hole due to the high rate of Bremsstrahlung events, which are sharply peaked at small angles." [SAC main.tex:151] In SAC "We" is the first word of 4 of 61 paragraphs, and 9 more open with "To ..., we ..." or "From ..., we ..."; that form is his for a study or a decision.
- Link paragraphs by repeating a noun (86% of first sentences share a content word with the paragraph before). Delete a sentence that only re-lists what the paragraph did, and one that only announces the next topic (up to three one-line signposts stay). Keep a closing sentence that draws the decision from what was found: "From these considerations, we conclude ..." [SAC main.tex:236]
- End on a verdict, a number, a consequence or the pointer to the figure (about two thirds of SAC's paragraphs; the others end on a plain detail). "These requirements remove more than 90% of the electroweak SM backgrounds without incurring a significant loss of signal efficiency." [IDM main.tex:119]
- Order a study or a check as purpose ("To ..."), setup, inputs and sample size, what is left out ("Note that"), figure, number, meaning: "We run 100 events per crystal length." [SAC main.tex:272]
- Say how many items follow, then give them in that order: "The total energy deposited in the crystal was reconstructed in three steps." [SAC main.tex:352]

### 4. Make the thing the subject; keep "we" for decisions, studies and claims

*Why:* when "we" is kept for the authors' own choices and work, it tells the reader which statements rest on their judgment.

- Start the sentence with the detector, the method, the sample, the fit or the figure, and give it an active verb: "The jet pT requirement removes low-momentum jets produced in pileup interactions." [IDM main.tex:95]
- Write "we" where the authors chose, assumed, studied, estimated, found, concluded or recommend, and for the steps of a study or a simulation that they designed and ran: "We run 100 events per crystal length." [SAC main.tex:272] The share follows the genre: 19% of sentences in SAC, 3% in PROC, 6% in THESIS, 2 to 6% in the CMS papers. For a paper by a few authors that reports their own studies SAC is the model: up to about one sentence in five, with "We" opening up to about 8%. Reduce "we" only above that, and never to reach a number. "From these considerations, we conclude the larger Hamamatsu R13478UV PMT, coupled to PbF2 crystals, is the best solution for PADME's requirements." [SAC main.tex:236]
- Describe operations on recorded data in the passive, with the means after "by" or "using" (the two SAC sections on recorded waveforms have no "we"). Aim for a passive in 35 to 45% of sentences (SAC 43%, CMS 52%). "The timing resolution was determined by extracting the sigmas of a Gaussian fit to each such distribution." [SAC main.tex:421]
- Replace a removed "we" by an active sentence about the thing where one exists. Never write a passive that hides who decided. If a choice has no stated reason, keep "we" and ask the authors for the reason.
- Let the tense follow the statement: present for what a thing is, does or shows and for what a result is; simple past for what was done once; present perfect to sum up. He is not strict: in SAC a simulation run is often in the present and a fitted value in the past.

### 5. Write sentences of about 20 words and mix their lengths

*Why:* short sentences hold the verdicts, steps and pointers, so the reader finds them; a long sentence that is a list can be scanned.

- Aim for a median of 19 to 22 words (his own documents: 19 to 20; the CMS papers: 22 to 24). Give 13 to 18% of sentences 12 words or fewer and 13 to 18% more than 30. Go past 40 words for a list or a definition (2 to 5% of sentences; 6 of the 8 such sentences in SAC).
- Keep a short sentence for a verdict, a step or a pointer: "We found zero events surviving the event selection." [THESIS paper.txt:9988] A run of short declaratives is his form for a chain of cause and effect, one link per sentence: "Increasing the length causes more Cherenkov photons to be lost along the way. At the same time, in a longer crystal photons have longer travel paths. Consequently, there is more opportunity for scattering, which broadens the arrival time profile of photons." [SAC main.tex:293] Do not chop a sentence into fragments, and do not leave three sentences of 12 words or fewer in a row when the middle one has no fact of its own.
- Punctuate lightly. Put specifications and glosses in parentheses after their noun. Put a colon before an announced list. Use semicolons between list items (PROC and SAC have no other; the thesis joins two clauses with one 11 times). Use a dash rarely: he has one dash construction in SAC, one pair in PROC, ten in the thesis and none in the two CMS letters. Never add one.
- Put no comma before a trailing "because" or "due to" phrase. Before a trailing "using" phrase the thesis has no comma and SAC has one in 5 of 10 cases: leave what the draft has. Keep the comma before a "with" phrase that adds a specification (", with pitch size 55 microns" [PROC main.tex:118]).
- Do not address the reader: "you" is in none of the five papers, and the only imperative that opens a sentence is "Note that". Write no question and no exclamation. Write no footnote (the five papers have one between them, a caveat [SAC main.tex:169]); an aside goes in parentheses or in a "Note that" sentence. Do not set a word in bold or italics for emphasis.

### 6. Put purpose, reason and consequence where they belong; use few connectors

*Why:* a choice with its reason attached does not look arbitrary, and a connector that is rare marks a real turn.

- Put the purpose first: "To maximize sensitivity, different variables are used in each match category." [IDM main.tex:131] A trailing "in order to" is as much his (7 in SAC).
- Give the reason in the same sentence with "due to" plus a noun phrase or "since" plus a clause: "The ECAL has a central hole due to the high rate of Bremsstrahlung events, which are sharply peaked at small angles." [SAC main.tex:151] In SAC "due to" is three times as frequent as "since" (17.5 against 5.8 per 10,000 words); in the thesis the order is reversed, and there he also writes "because" (35) and "because of" (11), which SAC and PROC lack. The CMS papers use "because of" at more than twice his rate. "Owing to" is rare in both voices (4 in the thesis, 2 in ETA). Keep at least four causal words in use.
- Leave ", so" where it is rare (SAC has one, and three when "and so" is counted; he kept all three in his thesis reprint). Above about 6 per 10,000 words, replace the extra ones (procedure, pass 4).
- Give the consequence in a sentence that starts with "This" and a verb, or in one tail (", which ..." or ", thus ...ing"). "This" opens 9.7% of the sentences in OWN and 6.8% in SAC, and a verb follows at once in about half of them: "This overestimates the total charge and introduces a bias in the linearity." [SAC main.tex:387] The "This" sentence is not a short one: in SAC the nine have 12 to 29 words, and the sentence before each has 16 to 32. After a sentence of 12 words or fewer, attach the consequence as a tail instead.
- State a trade-off in one sentence with "but" or ", while": "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost." [SAC main.tex:211]
- Open 7 to 11% of sentences with a connector, counted on the list in `references/corpus-and-measurements.md`. His frequent ones are Finally, However, Therefore, Furthermore, Nevertheless, Moreover and "Note that". First, Then, Hence, Thus, Consequently, "In particular,", "In this case,", "For this reason,", "For example," and "On the other hand," also open sentences in his own texts, and stay. Do not open with "In addition," or "As a result," (neither opens a sentence in OWN). "Additionally," and "Notably," each open two sentences of the thesis and none of his papers: do not add them.

### 7. State a caveat where it arises, then say what still holds

*Why:* the reader meets the weakness beside the number it affects and learns at once how much it matters. A limitations section leaves every earlier number unqualified.

- Put the limitation in the paragraph it concerns, in one flat sentence with its cause. Say which way the number errs: "Therefore the energy resolution quoted here is only an upper limit to the actual one achievable by PADME, and should be interpreted as a single-crystal SAC energy resolution." [SAC main.tex:346]
- Follow it with the sentence that says why the result still serves. In his own voice that sentence often opens with "Nevertheless," (15 in OWN, 1 in CMS; in SAC after a caveat on his own number at lines 245, 408 and 447): "Nevertheless, this separation resolution already meets the PADME tagging requirements." [SAC main.tex:447] A short concession stays inside the sentence with "but".
- Repeat in the abstract, as a condition, any caveat that changes a headline claim ("single-crystal energy resolution").
- In a polish, add "Nevertheless," only when three things hold: the sentence right before states a weakness, a limit or a rejected option; the sentence itself is already in the draft; and it speaks of the same result or object and says why that result still serves, or where the conclusion just drawn stops. All five uses in SAC pass this test (lines 211, 245, 295, 408, 447). A result for another range, sample or quantity is not what still holds: leave it without a connector. When you are not sure, do not add the word and put the question in the report; a connector of concession changes the logic, so it is never added first and asked about afterwards. If the authors have not said what still holds, ask them. Do not write that claim for them.
- Keep the plain adjective with which the authors name an approximation: "a simple threshold" [SAC main.tex:354], "the empirical function" [SAC main.tex:338], "an order-of-magnitude estimate" [SAC main.tex:245]. Where a choice has no physical basis he says so once, flatly: "The choice of a Landau fit was empirically driven and not based on underlying physical processes." [SAC main.tex:282] Never add such a label yourself; if a fit function or a setting has no stated basis, ask the authors.
- Report a setback or a surprise as a finding, in the order what was seen, its cause, what is being done: "From this original set of data, a new source of backgrounds not previously accounted for was identified: beam-induced backgrounds." [PROC main.tex:134] The five papers never say "unfortunately".

### 8. Use plain words and sober verdicts

*Why:* a plain verb costs the reader nothing, and a verdict that claims no more than the number shows is trusted.

- Write show, use, provide, allow, consist of, find, estimate, determine, measure. OWN has "utilize" 0 times, and none of the six documents has "outperform", "state-of-the-art" or "impressive".
- Judge a result by whether it is enough: meets, sufficient, acceptable, reasonable, negligible, safe, conservative, with at most one mild adverb (already; "comfortably" occurs once in the corpus). SAC has 14 such words against 2 words from a list of seventeen praise words, neither on its own result; outside that list it says "good linearity" (line 379) and "robust double-peak resolution" (line 451) of its own results. Do not add such words. "This has acceptable timing resolution while providing sufficient light yield for the low beam energies in the experiment, at a reasonable cost." [SAC main.tex:236]
- Give the two numbers instead of an intensifier (very, significantly, clearly). Word agreement as "agrees with", "in agreement with" or "consistent with" and put the reference value beside it; "good agreement" occurs in none of the six ("agrees well with" occurs twice in OWN).
- Mark an expectation with one modal verb (should, could, "is expected to"). Put no modal on a measured value.
- Describe a thing that the authors name first and name it second ("referred to as", "known as", or the full name with its acronym in parentheses). Then keep that one name (SAC does not, for its double-peak separation resolution; do not copy that). A term that readers of the journal know may come first with its gloss after it. "So-called" occurs once in the six documents and "we call" never. "Its magnitude is referred to as pTmiss." [IDM main.tex:57]
- Use American spelling, "Table" in full and lower-case "standard model" (PROC has capitals). Define "Monte Carlo (MC)" once; "MC simulation" is then his (SAC, ETA, IDM and THESIS have it), while a bare "MC" became "simulation" in his thesis reprint of SAC ("in simulation" [THESIS paper.txt:16814]). Write "selection" or "requirement" for a condition on events or objects and "threshold" for a value that a signal or a score must pass, where the draft's "cut" is not a defined term; "cut" is his own early word ("a cut was imposed", SAC lines 413 and 431), so it is no error. "Data set" in two words is the CMS form; his thesis has both forms. The three documents that refer to a section (SAC, SCOUT, THESIS) write "Section" in full; "Sec." occurs in none of the six.

### 9. Give every number its condition and its reference; keep headline values exact

*Why:* the reader can lift the sentence out of the paper and still use the number.

- Name the sample, energy, range or working point in the sentence that carries the number: "Assuming a minimum separation capability of r < 0.95, then roughly 90% of peaks with 1.8 ns separation can be distinguished." [SAC main.tex:439] SAC does not always do this in its results (line 421 names no beam energy); where the draft has the condition elsewhere, ask the authors whether it belongs in the sentence.
- Define each metric before its first value: numerator and denominator, or the fit and the parameter.
- Quote a headline value with its measured digits, identical in the abstract, the results and the conclusions. Put "roughly" or "about" only before a number that is rounded, read off a plot or extrapolated. "Roughly" is his word (0.95 per 1,000 words in OWN, 0.21 in CMS), "approximately" is the CMS word (0.04 and 0.53), and "about" is in both voices. "∼" before a number is also his (SAC 6, ETA 4): leave it, and never put a word hedge on top of it. In SAC the digits agree, but "roughly" on the 10% is in the results only, and one caption rounds 81 ps to "roughly 80 ps"; do not copy these slips.
- Word a gain as a factor or a percentage in a named quantity, against a named reference ("compared to"), with its cost in the same sentence where the option has one (SAC lines 211 and 215).
- Explain every trend, outlier and curve shape by its cause: "The light yield decreases with increasing length due to a higher chance of Cherenkov photons getting lost (absorbed or escaping) while traveling towards the PMT." [SAC main.tex:284]
- Wrap each displayed equation in a sentence: a lead-in clause that ends in a colon, then "where" for the symbols. "The plot was fit to the empirical function:" [SAC main.tex:338], then "where f(E) is the average fraction of energy deposited on the crystal." [SAC main.tex:344] All four equations of SAC and the one of PROC follow a colon. Keep displayed equations few (SAC 4, PROC 1, ETA 3, IDM 0).
- Describe methods in fixed orders. A procedure: counted steps with exact settings. A component: its role, "consists of" with count, material and dimensions, one performance number, the figure. A simulation: purpose and tool, contents, inputs and sample size, what is left out. An uncertainty: source, variation, comparison with the nominal, what "is taken as" the uncertainty, combination. A cross-check: purpose, test, verdict, consequence.

### 10. Give every figure a pointing sentence, a reading and a noun-phrase caption

*Why:* the reader learns what the picture is before being told what to conclude from it, and a reader who scans the figures finds the plotted quantity in the first words of the caption.

- Point with a sentence whose subject is the figure or the plotted thing: "Figure N shows X as a function of Y." or "X is shown in Fig. N." The figure or table (the float) is the subject in 47% of his mentions of one. He never writes "see Fig. N" outside parentheses (0 of 331 mentions) and never opens with "As can be seen in Fig. N," or "As shown in Fig. N,"; "Fig. N shows that" occurs only in SCOUT (3 times). "X can be seen in Fig. N." is his (4 in SAC, none in the CMS papers) and stays. "Fig. 14 shows the collected charge as a function of deposited energy." [SAC main.tex:383]
- Then read the figure in one to four sentences: how the points were obtained, what to look at, one number, the reason, what it decides. "The MC Landau spread time is plotted in Fig. 8. There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282] When the pointer closes a paragraph, the description of the figure stands before it (PROC does this for 4 of its 7 figures).
- Open the caption with a noun phrase without article and without verb (98% in OWN), in the order quantity, "as a function of" its variable (in a caption "versus" is also his: SAC lines 278 and 289), condition, origin of the numbers. Add full sentences with one job each. Give colors, line styles and panels in parentheses after the item they label. The norm is 25 to 50 words and 1 to 3 sentences (SAC: median 42 words and 2 sentences), without "we"; a result plot with several elements has four or more sentences in 5 of the 20 SAC captions. "PbF2 (red and blue) and SF57 (green) transparency profiles, compared to the Cherenkov spectrum (black, not to scale)." [SAC main.tex:173]
- A caption may state a finding. In SAC 8 of 20 captions do, also on design and simulation plots; in the thesis about a quarter; in PROC and the CMS papers none. Keep a finding that the draft's caption has, in one sentence, with the same statement and the same numbers as the text. Do not add one, and aim for at most two captions in five. "The fit yields a resolution of roughly 10% at 550 MeV, which meets PADME's requirements." [SAC main.tex:395]
- Use the same name for the plotted quantity in the pointer and in the caption. Treat a table like a figure ("Table N lists ...") and always write "Table" in full.

### 11. Edit lightly

*Why:* every rewrite can change a technical statement, and he will edit the text by hand afterwards.

- When he reprinted SAC as a chapter of his thesis, 145 of 215 sentences stayed word for word. Of the other 70, 27 differ only in commas, 42 by a few words or a number format, and one is new; none was restructured (he dropped the abstract and the first five paragraphs of the introduction). This is one case, of his own published paper: it shows which small things he changes (commas, "which" to "that", a bare "MC"), not how much a draft by other hands needs.
- Where a sentence breaks a habit above, change its form as far as the seven passes below require and no further. Leave a sentence alone when it already follows them.

## Personal voice and CMS house style

Where his own form and the CMS form differ, write his own form. Where the target journal has a rule, follow the journal and say so in the report. `references/voice-and-transfer.md` sorts every habit (Table A).

| Feature | His own voice: write this | CMS house style: only if the venue requires it |
|---|---|---|
| "we" | in up to one sentence in five, also in the abstract of a paper | nearly absent; passive abstract |
| Passive | in 35 to 45% of sentences | in more than half |
| Paragraph | 3 to 5 sentences | 6 to 8 sentences in a letter without headings |
| Approximator | "roughly" | "approximately"; "about" is in both |
| Reason and purpose | "due to", "since", "in order to" | "because of" at more than twice his rate |
| After a caveat | "Nevertheless,"; "but" inside the sentence for a short concession | "but" only: "Nevertheless," once, "Note that" never |
| Link to the last sentence | "This" + verb in about half of the cases, "This" + noun in the rest ("This procedure") | "This" + noun in four cases out of five |
| Possessive | 's on an experiment, a device or a particle: "PADME's requirements", "the PMT's QE" (about 20 in SAC, 7 in PROC) | "of the ..." (three or fewer in each CMS paper) |
| Caption | 25 to 50 words; may state the finding of the plot | 50 to 70 words in IDM and SCOUT (ETA 38), every symbol defined, no verdict, may open with "The" |
| Ranges | "between 100 and 400 MeV", "from 14 cm to 18 cm" | en dash ranges |
| Mirrored parentheses | rare (7 sentences in OWN, one in SAC); write the two cases out when the sentence allows | frequent in the letters: "12 (15) GeV at L1 in 2017 (2018)" [ETA main.tex:91] |
| Boilerplate | none | detector paragraph, "A search for ... is presented", "No significant excess", "In summary," |

"Note that" opens a sentence that says what a procedure leaves out or assumes, or where a result is valid (SAC lines 270, 346, 387). Add it only in front of such a sentence that the draft already has.

The journal decides four points of form: "Fig." or "Figure", "Sec." or "Section", the comma after "i.e." and "e.g.", and closed or hyphenated prefixes ("nonzero"). Thesis-only habits are not for a paper: "I", "This chapter describes ...", roadmaps at every level, colloquial words.

**Targets for a short methods paper by a few authors.** The ranges describe a whole paper in his practice; where a range and SAC disagree, SAC decides. They are not quotas.

| Feature | OWN | SAC | CMS | Aim for |
|---|---|---|---|---|
| Words per sentence, median | 20 | 20 | 24 | 19 to 22 |
| Sentences of 12 words or fewer; above 30; above 40 | 17%; 15%; 3.5% | 14%; 17.5%; 4.3% | 9%; 25%; 8% | 13 to 18%; 13 to 18%; 2 to 5% |
| Paragraph: sentences; words (medians) | 4; 76 | 3; 74 | 4; 111 | 3 to 5; 60 to 110 |
| Paragraphs of 8 or more sentences; of one sentence | 6%; 9% | 3%; 7% | 15%; 4% | at most 5%; at most 1 in 15 |
| Sentences containing "we"; opening with "We" | 5.8%; 1.9% | 19.2%; 7.7% | 2.4%; 0.5% | up to 20%; up to 8% |
| Sentences with a passive | 39.5% | 42.7% | 52.5% | 35 to 45% |
| Open with The, This, These, A, An, Each, All | 47% | 47% | 53% | 45 to 55% |
| Open with "This"; of these, verb next | 9.7%; 48% | 6.8%; 56% | 5.2%; 22% | 6 to 10%; about half |
| Open with a fronted phrase (In, For, To, Since, ...) | 12.3% | 15.4% | 13.6% | 11 to 16%; "For" at most 3%, "With" at most 1%, "To" 2 to 4% |
| Open with a connector | 8.3% | 10.7% | 7.4% | 7 to 11%; each connector at most about 2% |
| Causal words per 10,000 words: since (causal), due to, therefore, because, hence, thus, so (conjunction) | 18, 12, 11, 8, 4, 3, 5 | 6, 17.5, 6, 0, 8, 6, 6 | 3, 2.5, 5, 9, 1.4, 8, 0.7 | four or more in use, none above 20, "so" at most 6 |
| Per 1,000 words: all approximators; roughly; approximately | 1.5; 0.95; 0.04 | 2.3; 1.17; 0.20 | 2.0; 0.21; 0.53 | 1.5 to 2.5; 0.5 to 1.2; 0 to 0.2 |
| Per 1,000 words: colons; semicolons; dashes; parenthesis pairs | 4.2; 0.8; 0.5; 10.6 | 2.5; 1.0; 0.2; 12.9 | 1.2; 0.65; 0.07; 7.9 | 2 to 4; under 1; at most 0.2; 9 to 13 |
| Caption: median words; median sentences; share with 4 or more sentences | 37; 2; 13% | 42; 2; 25% | 50; 3; 31.5% | 25 to 50, none above 100; 1 to 3; at most a quarter |
| Caption opens with a noun phrase without article | 98% | 100% by reading (90% by the script) | 72% | all |
| Caption states a finding | 22% | 8 of 20 | 4.5% | at most 2 captions in 5; never added |
| Float as subject; "is shown in" and its variants (share of float mentions) | 47%; 36% | 31%; 41% | 44%; 41% | 30 to 50%; 35 to 45% |
| "see Fig. N" outside parentheses; "(see Fig. N)"; "as shown in" (counts) | 0; 2; 2 | 0; 2; 0 | 0; 0; 12 | 0; at most 1; at most 1 |
| Abstract: sentences; words | PROC 4, THESIS 9; 75, 202 | 6; 174 | 4 to 6; 110 to 158 | 4 to 6; 100 to 175 |

## How to work

### What never changes

Before the first edit, list every number with its unit and uncertainty, every hedge ("about", "could", "is expected to"), every claim, citation key, label, macro and equation. After the last edit, compare the lists with the new text. They must be identical. List each caveat, exclusion and condition together with the number or claim that it limits, and list a number once for every place where it stands (text, caption, table). After the last edit every caveat must still stand in the same sentence, paragraph or caption as that number. A statement that the draft makes twice, in the text and in a caption, keeps both copies unless the authors agree to drop one.

The style changes the form of a sentence and never what it says: do not change a number or its digits, a claim or its strength, a citation, a label, a defined technical term or a LaTeX command. One exception, always reported: a praise word or an intensifier on the authors' own result may be proposed for removal. Leave it in the text and list it in the report unless the user has asked for these removals. "Significantly" in front of a measured difference is a claim: never remove it, ask. If a number looks wrong, or two numbers disagree, report it and leave it.

### (a) Polishing a draft into his style

Before the first pass, make the lists of "What never changes". For a draft of more than about a page, also run `python3 scripts/andre_style_check.py draft.tex`. It prints the draft's measured style next to his ranges and lists the sentences to look at. It is a smoke detector, not an authority: judge every flag yourself.

When you polish a part of a paper, leave every form that the rest of the paper also has: a term that the draft defines, a naming formula, an abbreviation, a spelling. List each as a change for the whole paper in the report. A form changed in one passage only makes the paper inconsistent.

Then make seven passes, from the large scale to the small. A sentence in a paragraph that must change is not worth polishing first.

1. **Structure.** Check principles 1, 2 and 7: one purpose sentence, a reference for each result, each caveat where it applies, no roadmap. Keep every statement in its section. Propose moves between sections, and deletions, in the report; carry them out only when the user asks for a restructuring (then follow the order of repair in `references/conception-and-structure.md`).
2. **Paragraphs.** Aim for 3 to 5 sentences. Let the first name the thing described and the last give a number or a verdict. Leave a paragraph of 6 to 8 sentences alone. Split one above 8 sentences unless it is a step-by-step procedure; if a pointer or a split sentence of your own pushed it past 8, first fold the pointer into the sentence that reads it. Never place a break between a number and its caveat, its control or its reference value. Inside a section you may reorder sentences.
3. **Voice.** Sort every sentence that contains "we". Keep those with a choice, a study, a finding, a recommendation or a simulation run. Above one sentence in five, take those that narrate an operation on recorded data and turn each into a sentence about the thing: active where the thing acts, passive otherwise.
4. **Joins and connectors.** Leave ", so" where it is rare. Above about 6 per 10,000 words, replace the extra ones by the join that fits the length. When the whole sentence has fewer than about 25 words, keep it as one sentence: a fronted "Since", "due to" plus a noun phrase, or a tail (a participle as in ", making X a Y" or ", thus ...ing"; ", which" plus a verb). Split off a "This + verb" sentence only when the first clause has about 15 words or more, and a "Hence," sentence only for the verdict of the paragraph. "and hence" joins two phrases that share a subject; for a second clause with its own subject write "Hence, ..." or keep "and so" (SAC line 383). In front of sentences that already do those jobs, add "Furthermore,", "Finally," or "Note that"; add "Nevertheless," only by the test of principle 7. Move a fronted "For" or "With" phrase behind the subject where it reads well; leave it where it carries the condition of a number or sets one case against the next (he fronts "For" plus a case himself, SAC line 387).
5. **Words.** Apply principle 8 and the lexicon. Swap "approximately" for "roughly" where the draft already rounds; add no approximator. Turn "which we call Y" into "which we refer to as Y" when the authors coined the name, and into "referred to as Y" or "known as Y" when the name is in general use. When you propose the removal of a praise word or an intensifier ("excellent", "state-of-the-art", "significantly"), list it in the report, since it is part of what the authors claimed.
6. **Figures and captions.** Apply (c) below.
7. **Numbers.** Check principle 9 on every number. A missing condition, reference, definition or uncertainty is a question for the authors. Add nothing that the draft does not state.

Stop when a feature is inside its range. Never add a connector, a "This" or a passive only to move a number. The ranges describe a whole paper. On fewer than about 100 sentences use the checker for its list of sentences to look at and not for its marks: in SAC the median of 44 consecutive sentences runs from 18 to 23.5 words. Never choose between two wordings by the number of marked rows. When an edit that this skill asks for (a pointer, a split semicolon, a "Hence," verdict) moves a length feature out of its range, keep the edit and report the feature. Some features cannot move without new content and are not targets of a polish: sufficiency words, "roughly" and the other approximators, the number of citations, the numbers read off a plot, and the passive share of a text in which the things act. Then compare the text with the lists made before the first pass. `references/voice-and-transfer.md` gives the same seven passes with their evidence.

### (b) Drafting from notes

1. Collect the purpose in one sentence, the requirement or the reference method with its value, the headline numbers with conditions and uncertainties, and the list of figures. Where an item is missing, ask, or leave a visible placeholder such as [requirement?] or [uncertainty?]. Never invent it.
2. Outline the sections in the order of the work (principle 2) and give each measured quantity its own results subsection.
3. Draft the abstract and the introduction from the templates below. Then draft each section: an opener on its subject or purpose, methods passages in their fixed orders, result paragraphs that read each figure, a closing verdict.
4. Write the pointers and the captions (c), then the conclusions with the abstract's numbers, in the same digits and with the same conditions.
5. Check the draft with the checklist and the checker.

When the notes are in Chinese, write the paper text directly in his English patterns. Do not translate sentence by sentence. Keep every symbol, number and unit as given, and explain your choices in Chinese.

### (c) Captions and figure references

1. Open each figure before you edit its caption or its pointer. Note what the plot itself says (legend, notes, axis labels) and what only the caption says.
2. Introduce each figure and table by a sentence whose subject is the float ("Figure N shows X") or the plotted thing ("X is shown in Fig. N"), and cite all floats in numerical order. Put the sentence where the figure is first needed: at the start of the paragraph that discusses the figure, at the end of the paragraph whose product it is, or inside the paragraph, before the first statement that is read from the figure (6 of the 20 floats of SAC). Turn each trailing "see Fig. N" into such a sentence. Keep with the figure what the draft ties to it: a condition goes into the pointer, in the words of the caption ("Figure N shows X as a function of Y, with <condition>."). For a figure that illustrates one statement (an event display, a sketch, an example), the pointer carries that statement in a clause and is not split in two: "Figure 10.14 represents the ideal scenario, in which the optimal bin shifts upward proportionally with increasing displacement." [THESIS paper.txt:13854-13855]
3. After the pointer, say what to look at and give one number, using only what the draft states.
4. Shorten a caption only by moving out what explains or argues: a derivation, the physical reason, a second finding. Three kinds of sentence stay in the caption even when the text says the same: a limit of what the plot shows (what is left out, not drawn, scaled, or merged into a last bin), the definition of a plotted element, and how a point was obtained. He gives the last in both places (SAC lines 330 and 334), and 5 of the 20 SAC captions hold a fact that the text does not state: "Note that timing resolution is not significantly affected by beam energy due to our method of estimating the arrival time." [SAC main.tex:425]
5. If the caption is still above 50 words or three sentences, leave it and report its length. Propose to the authors, in this order, what could go: a key that repeats a complete legend; the finding that the text states with the same numbers. Carry out neither.
6. Never drop a sentence that you take out of a caption. Place it in the text after the pointer, and list the move in the report.
7. Use one name for the plotted quantity in the pointer and in the caption. Follow the journal for "Fig." and "Figure". Polishing cannot add or redraw a figure: note a missing sketch, key or unit for the authors.

### (d) What to report back

Return the text first, in the format of the input (LaTeX stays LaTeX), ready to paste. Then report, briefly and in the user's language:

- the main changes, one line each;
- the measured features before and after, when the checker was run, and each feature left outside its range with the reason;
- everything that moved, for example a sentence from a caption to the text, and every praise word or intensifier proposed for removal;
- questions for the authors: a choice without a reason, a number without a condition, a reference or an uncertainty, a caveat without what still holds, an unclear "This", numbers that disagree;
- suggestions on structure, and changes of form for the whole paper, that were not carried out;
- each point where the journal's rule and his own form differ, and which was used;
- a confirmation that numbers, claims, caveats, citations, labels and LaTeX are unchanged.

## Templates

Angle brackets are slots. Square brackets are optional parts. The templates give the form only: every fact comes from the user's material. Where a template has two forms, the first is for work with an external requirement (SAC). The second, for work with a reference method and no external requirement, is built from the Result sentence and from the ETA abstract ("This work achieves an improved precision of over five orders of magnitude compared to previous results" [ETA main.tex:34]); none of his own papers shows a baseline in the abstract.

**Abstract** (4 to 6 sentences). `<The object, or the experiment it serves, and what it is for>. We report here on <measurements or studies> of <the object>, <what it is built to do>. The crucial requirement is <quantity> of <less than or at least> <number>[, which is satisfied by <choice>]. We find <quantity> of <number> [and <quantity> of <number> at <condition>] using <sample or beam>. [We also propose <option> for <use>.]` Or: `<The object or the method, and what it is for>. We report here on <studies> of <the object> using <sample>. We find <quantity> of <number> at <condition>, compared to <number> for <the reference method> under the same condition. [<The gain as a factor in a named quantity, or what follows>.]`

**Introduction** (3 to 6 short paragraphs, then the purpose paragraph).
1. The open problem, set against what is established: `Despite <what is known or has been done>, <what> remain(s) <unknown or unmeasured>.`
2. The approach, and the experiment or method that carries it.
3. The principle of the measurement or the method.
4. The constraint that creates the need: `<X> has <limit> due to <cause>.`
5. The component that answers it: `To mitigate <problem>, <component> is <placed or used> <where>.`
6. `In this paper we evaluate <what> using <means>. We demonstrate that <object> meets the requirements for <purpose>, namely: (a) <requirement with its number>; (b) <...>; and (c) <...>.` Or: `In this paper we evaluate <what> using <means>. We compare it with <the reference method> on <the same sample and settings>, in terms of: (a) <quantity>; (b) <...>; and (c) <...>.`

**Section opener.** `<The object> consists of <count, material, dimensions>.` or `To <purpose>, we <did what> using <means>.` or `<Quantity> was reconstructed in <three> steps.` Close on the verdict: `Hence, <choice> is the preferred solution for <requirement>.`

**Methods passage.** `To <purpose>, <setup or action>. <What the setup contains>. We <ran or generated> <N> events <per condition>. Note that <what is left out or assumed>. <Pointer to the figure>. <What is seen, with one number>, due to <cause>. This <motivates or makes> <the choice>.` For a procedure: `First <step> (<setting>). <The next thing> was then <step>. Finally, <step>, and <value> was taken as <the quantity>.` For an equation: `<What is computed> was <fit to or calculated as> <the named function or quantity>: <equation> where <symbol> is <meaning>.`

**Result sentence.** `From <evidence>, we find <quantity> of <number> <at condition>.` or `<Quantity> was found to be <number>, which meets the <number> requirement.` or `<Quantity> is <number> for <condition>, compared to <number> for <the reference method>.` With a caveat: `Note that <limit>. <The number> should therefore be interpreted as <what>. Nevertheless, <what still holds>.` With a gain: `<Option> improves <quantity> by <a factor of N or roughly N%>, from <a> to <b>[, while <cost>].`

**Figure pointer and follow-up.** `Figure N shows <quantity> as a function of <variable>[ for <condition>].` or `<Quantity> is shown in Fig. N.` Then: `<How the points were obtained>. <The feature, with one number>, due to <cause>. <What it decides>.`

**Caption.** `<Quantity> as a function of <variable> for <sample or condition>[, as determined from <method or simulation>]. [<A> (red) and <B> (blue) are compared.] [Each point is <how obtained>.] [The <element> indicates <meaning>.] [<What is not shown or how the plot is limited>.] [The <quantity> of <number> meets <requirement>.]` Use the last sentence only where the text states the same finding.

**Summary** (6 to 8 sentences, one or two paragraphs). `We have characterized <object> with <means>. <The measured quantities> meet <the requirements>. <Object> has been found to provide <the headline numbers of the abstract, with the same digits and conditions>. <A measured feature> suggests that <object> might be suitable for <a wider use>. We recommend <the next step, with its expected gain>.` Or, in place of the second and third sentences: `<Object> has been found to provide <the headline numbers>, compared to <the numbers of the reference method> under the same conditions.`

## Lexicon

| | Words |
|---|---|
| Prefer | show, use, provide, allow, consist of, account for, lead to, find, estimate, determine, measure, mitigate; sufficient, reasonable, negligible, conservative, already, only; meets, acceptable, comfortably (SAC only: 7, 1 and 1 uses; one "comfortably" at most); roughly; about (in both voices); due to, since, because, therefore, hence, thus (as ", thus ...ing" and "and thus"), then; Finally, However, Furthermore, Nevertheless, Note that; as a function of, is taken as, a factor of, compared to, referred to as, known as, can be seen in Fig. N, There is + number, in order to |
| Use sparingly | demonstrate, enable, employ, exploit, obtain, perform, achieve; approximately (the CMS word); respectively (28 in OWN, 52 in CMS); novel (at most once, of the experiment or the technique, as at SAC line 147); robust (his word for a verdict, 11 in OWN: keep it where the draft has it); crucial, key, important, interesting (with the reason in the same sentence); significantly (5 in OWN, 19 in CMS; not on your own result without the number); very, highly (on a physical fact only); may, might, likely; Moreover; ", so"; a dash (one construction in a paper at most); i.e. and e.g. (inside parentheses) |
| Avoid | utilize, leverage, facilitate, showcase; outperform, state-of-the-art, impressive, superior, groundbreaking, pioneering, excellent on your own result; substantially, clearly, crucially as emphasis (1, 1 and 0 uses in OWN); good agreement; it should be noted; "As can be seen" as an opener; we observe, we see, we note, we believe, we call; so-called, etc., in other words, to this end; In addition, As a result as openers; In conclusion, Lastly; with respect to; Tab. |

Sixteen of the Avoid entries are absent from all six documents (outperform, state-of-the-art, impressive, good agreement, it should be noted, as can be seen, we observe, we see, we believe, we call, etc., in other words, to this end, In conclusion, Lastly, Tab.), so the evidence for them is absence in both voices. "Showcase" occurs once in his thesis and once in SCOUT; write "show".

## Guardrails

- **Faithfulness first.** Never change a number, a claim or its strength, a caveat or its place beside its number, a citation, a label or a LaTeX command. Never add a fact, a reason, a condition, a requirement or a statement of what still holds. A hedge is part of the claim: in an invented example, "about 38 ps, which could be sufficient" must not become "38 ps, comfortably meeting". Where the style needs something that the draft lacks, ask or leave a placeholder.
- **Invented examples are not facts.** The Before and After sentences in `references/` follow one made-up study (a test-beam measurement of the time resolution of a small scintillator timing detector) with made-up numbers. They show the form only. Never carry them into the user's text.
- **Do not copy CMS boilerplate or his slips.** Leave out the detector paragraph, "A search for ... is presented" and the passive recap. Do not imitate "Fig." at the start of a sentence, a restrictive "which" without comma, "10x" or "10k events", a fit parameter with two names, a quantity with two names, or a headline value without an uncertainty. Each reference file ends with a list of what not to copy.
- **Do not force a passive that hides the actor.** A decision keeps its "we", or carries its reason in the same sentence.
- **The style serves clarity.** These habits describe what makes his papers easy to follow. When a habit would make a passage less clear, keep the passage clear and say why in the report.
- **Language.** Write paper text in English. Write explanations, notes and questions in the user's language; if the user writes Chinese, explain in Chinese.
- **Plain notes.** Keep notes short and in words the user knows. Do not use this skill's labels (STRUCT-3, "tail", "signpost") without saying what they mean.

## Checklist before returning text

- [ ] Every number, unit, uncertainty, hedge, claim, citation, label and LaTeX command is as in the draft, and every caveat still stands beside the number it limits.
- [ ] The abstract opens on the object and gives the requirement or reference value and every headline number with its condition.
- [ ] The purpose is stated once, with "we" and a plain verb, and each result has its requirement or reference value.
- [ ] There is no roadmap paragraph, no limitations section and no praise added to the authors' own result.
- [ ] Most paragraphs have 3 to 5 sentences (the two-sentence steps of the introduction stay), most open on the thing described, and none ends on a recap or on an announcement of the next one.
- [ ] Every "we" marks a decision, a study, a finding, a recommendation or a run of the authors' own; no passive hides who decided.
- [ ] The median sentence is near 20 words, with short sentences for verdicts; a sentence above 40 words is a list or a definition.
- [ ] Each choice carries its purpose or its reason in the same sentence; at least four causal words are in use and ", so" is rare.
- [ ] Each measured feature is inside its range, or the report says why it was left outside; no connector, "This" or passive was added only to reach a range, and no "In addition," or "As a result," opens a sentence.
- [ ] Each caveat stands where it applies, followed by what still holds, in the authors' own words; no "Nevertheless," was added without the test of principle 7.
- [ ] Every number has its condition; rounded numbers carry the draft's "roughly" or "about"; headline values are identical in the abstract, the results and the conclusions.
- [ ] Every figure and table is introduced by a sentence with the float or the plotted thing as subject, cited in numerical order, with no "see Fig. N".
- [ ] Every caption opens with a noun phrase without article and keeps its limits, its definitions and how its points were obtained; no finding was added to a caption.
- [ ] The spelling is American, with "Table" in full; "Fig.", "Figure", "Sec." and "Section" follow the journal.
- [ ] The report lists what moved, the questions for the authors and the points left to the journal, in the user's language.

## Bundled resources

This file is enough for a paragraph-level edit. For a larger task, read only the one or two references that the task needs. Each holds numbered habits with the full evidence, more quotes, the case where a habit does not apply, before/after pairs, a table of targets, a list of what not to copy and a checklist.

| Task | Read | What it holds |
|---|---|---|
| Polishing a whole draft; own voice against CMS or journal style; all targets | `references/voice-and-transfer.md` | VOICE-1 to 10, Table A (whose habit it is), Table B (targets), the pass-by-pass procedure, what to report |
| Outline, title, abstract, introduction, conclusions, restructuring | `references/conception-and-structure.md` | STRUCT-1 to 12, structural targets, the order of repair |
| Paragraph shape, links between paragraphs, order inside a methods or results passage | `references/paragraphs-and-flow.md` | PARA-1 to 11, paragraph and opener targets |
| Voice, tense, sentence length, punctuation, commas | `references/sentences-and-voice.md` | SENT-1 to 15, sentence and punctuation targets |
| Word choice, connectors, hedges, fixed phrases, spelling | `references/words-and-phrases.md` | WORD-1 to 11, the full word lists with counts, word-rate targets |
| Captions, figure and table references | `references/figures-and-captions.md` | FIG-1 to 12, caption templates, caption targets |
| Numbers, comparisons, verdicts, caveats, uncertainties, equations, descriptions of methods | `references/numbers-results-methods.md` | NUM-1 to 15 |
| What the six documents are; how a number was measured; values per document | `references/corpus-and-measurements.md` | the corpus, the method and its caveats, the measured tables |

- `scripts/andre_style_check.py`: run `python3 scripts/andre_style_check.py draft.tex` on a `.tex`, `.md` or `.txt` draft. It prints the draft's measured style next to his ranges and lists the sentences to look at. It is a smoke detector, not an authority. `scripts/README.md` describes its options and its counting rules.
