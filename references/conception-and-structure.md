# Conception and structure

> **When to read this file.** Read it before you plan, outline or restructure a paper, or write its title, abstract, introduction or conclusions.
> It holds twelve habits of construction (STRUCT-1 to STRUCT-12) with their evidence, quotes, limits and before/after pairs, then the measured targets, the things not to copy, the order of repair and a checklist.
> Work through it before any sentence is edited: a paragraph that must move is not worth polishing first.

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

Counts for SAC refer to its 14 headed units (9 sections, 5 subsections).

**Contents.**

- STRUCT-1. State the requirement before the result, and close the result against it
- STRUCT-2. Name the problem before the component that solves it
- STRUCT-3. Build the introduction as short steps from the general problem to the work
- STRUCT-4. State the purpose once, with a plain verb, after the steps
- STRUCT-5. Open the abstract on the object and give the numbers
- STRUCT-6. Order the sections as the work was done and as the data travel
- STRUCT-7. Write no roadmap paragraph in a short paper; signpost locally
- STRUCT-8. Open a section on its subject or purpose and close it on a verdict
- STRUCT-9. Report each limitation where it arises, then say what still holds
- STRUCT-10. Report rejected options fairly and close with a verdict
- STRUCT-11. In the conclusions, repeat the abstract's numbers and add one thing
- STRUCT-12. Use titles that name the content
- Measured targets; Do not copy; Order of repair; Checklist

**Summary.**

1. He states a need before the thing that answers it, and a requirement before the result that is judged against it.
2. The introduction goes from the general problem to the work in short steps and states the purpose once, in a plain "In this paper we ..." sentence.
3. Sections follow the order of the work and of the data. Each opens on its subject or purpose and closes on a verdict, a number or a decision.
4. Limitations, setbacks and rejected options are reported where they arise, with their cause and with what still holds. No section collects them.
5. The conclusions repeat the headline numbers of the abstract with the same digits and conditions, add one statement on wider use, and end on a concrete next step.

## Habits

### STRUCT-1. State the requirement before the result, and close the result against it

**Rule.** Say what the device or method must achieve, as a number, before any result appears. Then report each result in a sentence that also gives the verdict against that number.

**Why.** The reader can judge the result without the author's adjectives. A number without a reference forces the reader to guess whether it is good.

**Evidence.** Always in SAC, his closest model for a methods paper; his own. The abstract gives the 200 ps requirement one sentence before the 81 ps result. The introduction ends on six requirements, (a) to (f). "meet(s)" then occurs seven times: once in the purpose statement and six times to close a result (4 in the text, 2 in captions); THESIS chapter 14 reprints them. His other own documents state no requirement. The CMS papers have no external requirement. There the reference is the standard method at the same condition (ETA, SCOUT; usual). PROC reports no measurement.

- "The crucial requirement is a timing resolution of less than 200 ps, which is satisfied by the choice of PbF2 crystals and the newly released Hamamatsu R13478UV photomultiplier tubes (PMTs)." [SAC main.tex:116]
- "The PbF2 resolution was found to be 81 ps, which comfortably meets the 200 ps timing requirement for a successful SAC performance." [SAC main.tex:421]
- "These high-rate triggers were commissioned in 2017 and found to provide a rate of ∼2 kHz at the peak instantaneous luminosity of 2 × 10^34 cm^−2 s^−1, more than 60 times the rate of the standard muon triggers." [ETA main.tex:106-109]

**When not to apply.** The work may have no external requirement. Do not invent one. Use the existing method as the reference and give its value at the same condition. If the draft has neither, ask the authors.

**Before.** "We measure a time resolution of 38 ps, which is an excellent result."

**After.** In the introduction: "The telescope requires a time resolution below 50 ps to assign each track to a single beam particle." In the results: "The time resolution was found to be 38 ps at an overvoltage of 5 V, which meets the 50 ps requirement."

### STRUCT-2. Name the problem before the component that solves it

**Rule.** Introduce each device, algorithm or design choice directly after the sentence that states the problem it solves. Where it has a cost, state the cost in the same sentence ("while doubling the cost" [SAC main.tex:211]).

**Why.** The reader learns why a component exists at the moment it appears. Nothing has to be remembered unexplained.

**Evidence.** Usual in all six; his own, and it survives CMS editing. PROC: each auxiliary detector follows the background it removes. SAC: the calorimeter enters in the third sentence of a paragraph that opens with the need. ETA: the standard trigger, where it fails, the remedy, its cost, and only then its name. SCOUT: five constraints as bullets, then the two techniques as the answer to two of them. THESIS: the standard muon reconstruction, where it fails, then the need for a combined strategy. IDM: a weakness of the new algorithm, its cause and the remedy in three consecutive sentences.

- "To mitigate such backgrounds, a very fast Small-Angle Calorimeter (SAC) is placed behind the main ECAL, flush with the central hole." [SAC main.tex:153]
- "For dimuon resonance masses below ∼40 GeV, the performance of the standard muon triggers deteriorates. To improve efficiency for those masses, a dedicated set of high-rate dimuon triggers was developed." [ETA main.tex:95-96]
- "Therefore a strategy that can incorporate both displaced standalone muon tracks and global muon tracks is desired." [THESIS paper.txt:6639]

**When not to apply.** A standard component (a common generator, a standard detector description) needs no problem statement. One clause is enough there.

**Before.** "The tile is read out by two SiPMs on opposite edges. The two arrival times are averaged."

**After.** "With a single SiPM, the measured time depends on where the particle crosses the tile. To remove this dependence, the tile is read out by two SiPMs on opposite edges and the two arrival times are averaged. This doubles the number of readout channels."

### STRUCT-3. Build the introduction as short steps from the general problem to the work

**Rule.** Give each step its own short paragraph of 2 to 4 sentences (shorter than the 3 to 5 sentences of a body paragraph) or, in a one-paragraph introduction, its own sentence. Open on the problem, set against what is established: "Despite <what is known or has been done>, <what> remain(s) <unknown or unmeasured>." Start each step from a noun that the previous step introduced. Stop when the reader knows what is needed and why. Do not survey the literature; credit a borrowed method in one short sentence or clause.

**Why.** Each step answers the question the previous one raised, so the purpose statement arrives as the expected next sentence.

**Evidence.** Always, 6 of 6. PROC: one paragraph, six sentences, six steps. SAC: six paragraphs (open problem, proposed solution, experiment, measurement principle, geometric constraint, need and device), then the purpose paragraph. IDM: eight sentences. ETA: nine. SCOUT: four. THESIS: nine short paragraphs. In his own voice the introduction has few citations (PROC 2, SAC 3, THESIS chapter 1 none) and no review of other work. The CMS letters cite more (18 and 12 citation commands), and IDM spends six sentences on why earlier searches miss the signal. The first move sets what is established against what is unknown, with the verb "remain(s)", in SAC (line 136), IDM (line 51), ETA (lines 46-48) and at both ends of the thesis (lines 1377-1379 and 18055-18056); PROC opens on a definition. A borrowed method is credited in one sentence: "This procedure is adapted from Ref. [57]." [THESIS paper.txt:14662-14663]

- "Despite the recent discovery of the Higgs boson at the LHC, solidifying our understanding of the standard model (SM) of particle physics, many lingering questions remain that the SM cannot yet explain." [SAC main.tex:136]
- "The ECAL has a central hole due to the high rate of Bremsstrahlung events, which are sharply peaked at small angles." [SAC main.tex:151]
- "A large chunk of this mystery comes in the form of the dark matter problem." [THESIS paper.txt:1380]
- "Some analyses rely on the detection of dimuon resonances, whereas muons in IDM are not resonantly produced." [IDM main.tex:57]

**When not to apply.** A letter has no room for seven paragraphs. Keep one step per sentence there. If the journal expects the work to be placed against earlier methods, add that as one step, in the form of the IDM sentence above: what the earlier approach relies on, and why that does not cover the present case.

**Before.** "Precise timing is of great importance in modern particle physics [1-15]. Many fast detectors have been developed in recent years [16-30]. In this paper we present a scintillator tile."

**After** (first sentences of four paragraphs). "At high beam rates, two particles can cross a beam telescope within one readout window." "A time stamp on each track removes this ambiguity if its resolution is below 50 ps." "A small scintillator tile read out by SiPMs is a compact candidate for this time stamp." "In this paper we evaluate the time resolution of such a tile with 4 GeV electrons."

### STRUCT-4. State the purpose once, with a plain verb, after the steps

**Rule.** Write one purpose sentence of the form "In this paper we evaluate / present / report / describe <what>, using <means>". Make it the first sentence of a paragraph. Follow it with what is demonstrated, measured against the requirements. If priority is claimed, claim it in one flat sentence.

**Why.** A reader who skims finds the purpose at the head of a paragraph and learns in the same place how the claim will be tested.

**Evidence.** Always one purpose sentence, at the head of a paragraph, never the first sentence of the body: SAC (sentence 17), IDM (sentence 9), ETA (sentence 10), SCOUT (sentence 5), THESIS (paragraph 10 of 11, with "I will"). PROC has it only in the abstract. In his own voice the purpose paragraph ends the introduction; in the CMS letters it is the second paragraph and more material follows. Verbs: evaluate, demonstrate (SAC); present (IDM); report (ETA); describe (SCOUT, PROC). SAC frames the contribution as meeting a list of requirements, and states three goals of its simulation a second time (line 241). SAC as posted has a comma before "using" in this sentence; his thesis reprint has none ("with a test beam done at LNF using fast PbF2 crystals" [THESIS paper.txt:16331-16332]), so leave what the draft has. Priority is stated as a fact in IDM, ETA, SCOUT and THESIS. Bulleted lists of contributions: 0 of 6.

- "In this paper we evaluate the performance of a prototype of the SAC with a test beam done at LNF, using fast Lead Fluoride crystals (PbF2) and the newly developed Hamamatsu R13478UV photomultiplier tube (PMT), optimized for fast response." [SAC main.tex:155]
- "Here we describe PADME's design, status of the experiment, and future plans." [PROC main.tex:34]
- "This is the first search for inelastic dark matter at a hadron collider." [THESIS paper.txt:37]

**When not to apply.** There is no exception. In a letter write "In this Letter".

**Before.** "The main contributions of this work are threefold: (i) a novel tile design; (ii) state-of-the-art timing performance; (iii) a comprehensive set of studies."

**After.** "In this paper we evaluate the time resolution of a scintillator tile read out by two SiPMs, using 4 GeV electrons. We demonstrate that the tile meets the requirements of the telescope, namely: (a) a time resolution below 50 ps; and (b) a detection efficiency above 99%."

### STRUCT-5. Open the abstract on the object and give the numbers

**Rule.** Start the abstract with the object of the paper or the experiment it serves. Then say what is reported, the requirement, the measured numbers with their conditions, and one closing sentence on what follows or what the result means. Use four to six sentences.

**Why.** A reader who reads only the abstract leaves with the result and the reference to judge it by.

**Evidence.** No abstract opens with a sentence about the field (6 of 6). SAC gives two sentences on the host experiment first; the others name the work in the first sentence. The five papers have 4, 6, 5, 4 and 6 sentences and 75 to 174 words. Numbers appear when there is a result (SAC 12, ETA 9). His own abstracts use "we" (SAC: "We report here", "We find", "We also propose"). The three CMS abstracts are passive, which is house style; his thesis abstract is passive too ("Two novel searches for dark matter using particle accelerators are presented." [THESIS paper.txt:33]). The last sentence gives the scope (PROC), a proposal (SAC), the priority claim (IDM), the gain (ETA) or the status (THESIS).

- "PADME is a fixed-target, missing-mass experiment at the Laboratori Nazionali di Frascati (LNF) to search for evidence of dark photons." [PROC main.tex:34]
- "We find a timing resolution of 81 ps (with double-peak separation resolution of 1.8 ns) and a single-crystal energy resolution of 10% at 550 MeV with light yield of 2.05 photo-electrons per MeV, using 100 to 400 MeV electrons at the Beam Test Facility of LNF." [SAC main.tex:116]

**When not to apply.** If the journal sets a tighter limit, cut the context sentences first and keep the numbers.

**Before.** "Timing detectors are increasingly important in high-energy physics. In this work, a novel scintillator detector is proposed and studied in detail. Excellent performance is achieved."

**After.** "We report on a test-beam measurement of the time resolution of a scintillator tile read out by two SiPMs, built to time-stamp tracks in a beam telescope. The crucial requirement is a resolution below 50 ps. We find a resolution of 38 ps and an efficiency of 99.6%, using 4 GeV electrons. We also propose a thinner tile for low-momentum beams."

### STRUCT-6. Order the sections as the work was done and as the data travel

**Rule.** For a detector paper, put the sections in this order: the object, the design choices, the simulation, the setup, the reconstruction, the performance, the conclusions. Give each measured quantity its own results subsection. Inside a method section, follow the data from input to output. The corpus has no paper on an algorithm or a model: for one, keep the principle (each section uses only what earlier sections have set up; one results subsection per measured quantity; conclusions last) and propose any reordering to the authors.

**Why.** Each section uses only what earlier sections have set up. A reader looking for one number finds it under its own heading.

**Evidence.** The order depends on the genre; the principle holds in all six.

- Detector or methods paper (SAC): introduction; the device; crystal and PMT choices; two simulation sections; test beam setup; charge reconstruction; detector performance in four subsections, one quantity each; conclusions. Shares of the body: introduction 12%, device 3%, choices 17%, simulation 23%, setup 14%, reconstruction 7%, performance 20%, conclusions 4%. A performance subsection runs: how the quantity is obtained, the figure, the caveat, the number, the verdict.
- Search letter (IDM; the CMS order): motivation and claim, detector, data and simulation, selection, background, uncertainties, results, summary.
- Observation letter (ETA): the peak and its significance come before simulation, checks, efficiencies and uncertainties. This holds in one document only.
- Review (SCOUT): context, purpose, roadmap, constraints; then for each technique the strategy, what is recorded, performance per object, physics results; summary.
- Proceedings (PROC): physics idea, experiment, first data and a problem found in them, status and plans. No conclusions section.

Two sentences that follow the data:

- "The total energy deposited in the crystal was reconstructed in three steps." [SAC main.tex:352]
- "Events passing the high-rate trigger requirements are further selected to improve the signal-to-background discrimination." [ETA main.tex:130]

**When not to apply.** A letter has no headings. Keep the order there and open each paragraph with the noun that would have been its heading.

**Before** (outline). "1 Introduction. 2 Related work. 3 Results. 4 Details of the method. 5 Discussion. 6 Limitations. 7 Conclusion."

**After.** "1 Introduction. 2 The timing tile. 3 Scintillator and photosensor choices. 4 Test beam setup. 5 Time reconstruction. 6 Detector performance: 6.1 Efficiency, 6.2 Time resolution, 6.3 Dependence on impact position. 7 Conclusions."

### STRUCT-7. Write no roadmap paragraph in a short paper; signpost locally

**Rule.** Delete "This paper is organized as follows". Where the reader needs direction, add one signpost sentence at the end of a section's opening paragraph. Keep such signposts to three or fewer in the paper.

**Why.** In a paper of ten pages the headings already show the order. A signpost at the point of use tells the reader what comes next when that matters.

**Evidence.** The four short papers have no roadmap paragraph (PROC, SAC, IDM, ETA). The two long documents have one: SCOUT in a subsection of its own, THESIS at thesis, part and chapter level. The habit follows length, in his own voice and in CMS papers alike. SAC has three signpost sentences instead. IDM and ETA have one forward signpost each ("as described in the next paragraph" [IDM main.tex:132], "(described later)" [ETA main.tex:188]).

- "These studies are discussed below." [SAC main.tex:374]
- "In this section we describe our radiation damage study, while the other two questions are addressed further below." [SAC main.tex:241]
- The long-document form, for contrast: "This report is organized as follows." [SCOUT main.tex:251]

**When not to apply.** A long review or a thesis needs a roadmap: write one sentence per section with a plain verb ("Section 2 describes ..."). If the journal or an editor asks for a roadmap in a short paper, give it two sentences at the end of the introduction and nothing more.

**Before.** "The paper is organized as follows. Section 2 describes the detector. Section 3 describes the test beam. Section 4 presents the results. Section 5 concludes."

**After.** Delete the paragraph. At the end of the first paragraph of the performance section: "These studies are discussed below."

### STRUCT-8. Open a section on its subject or purpose and close it on a verdict

**Rule.** Start each section with the thing it describes, or with "To <purpose>, we <did what>". End it on the decision, number or verdict it was written to reach. A pointer to a figure or to another section may end a section when the detail is given elsewhere. Do not end on a sentence that only re-lists what the section did. Keep a closing sentence or paragraph that gathers what was found into the decision ("From these considerations, we conclude ..." [SAC main.tex:236]; "From the optical MC simulation, it is evident that shorter crystals are better" [SAC main.tex:293]).

**Why.** The first sentence tells the reader what the section is for. The last sentence tells the reader what to carry forward.

**Evidence.** Usual; his own. SAC openers: none of the 14 units opens with "This section" or a remark on organization; 4 front a purpose, a constraint or the requirements ("To ...", "Since ...", "Given the requirements ..."); the others open on the object, the data or a figure. SAC endings: a verdict or decision in 6 units, a pointer in 2, a caveat or an instruction on how to read a number in 2, a plain fact in 2, a recommendation in 2. PROC: all four sections open with their subject. None of the four short papers ends a section on a recap. Openers such as "This chapter describes" (11 thesis chapters) and section-end summaries (one in SCOUT, one in THESIS chapter 2) belong to the long genres.

- "To estimate single-crystal performance, we measured linearity and energy resolution, using only single-electron events, at different incident electron energies." [SAC main.tex:374]
- "This makes 140 mm a safe length to ensure we can harness most of the Cherenkov photons in a 500 MeV shower." [SAC main.tex:295]
- "Based on these studies, we conclude that other decay modes of the η meson provide a negligible contribution to the selected events." [ETA main.tex:220-221]

**When not to apply.** A section that only describes apparatus has no verdict. End it on the last fact or on the pointer to its figure.

**Before.** Opening: "In this section, we discuss the time reconstruction in detail." Closing: "In the next section, we present the results."

**After.** Opening: "The arrival time of each pulse was reconstructed in three steps." Closing: "With this threshold the time walk stays below 5 ps, which is negligible compared to the 50 ps requirement."

### STRUCT-9. Report each limitation where it arises, then say what still holds

**Rule.** State a limitation at the point where it applies, in a flat sentence with its cause. Follow it with one sentence on why the result still serves its purpose, or on how to read the number. Report a setback as a finding: what was seen, its cause, the evidence, the remedy. Do not write a limitations section.

**Why.** The reader meets the caveat while weighing the number it affects, and learns at once how much it matters.

**Evidence.** Always local, 6 of 6: none of the 217 section titles in PROC, SAC, SCOUT and THESIS is named Limitations or Discussion, and the two letters have no such paragraph. SAC states at least six caveats in place; three are followed by "Nevertheless," in the same paragraph. "Nevertheless" is his own word for this turn (SAC 5, THESIS 10 more outside the reprinted chapter, the three CMS papers 2 in total, both in SCOUT). The CMS form is weakness, cause, remedy in consecutive sentences (IDM), a subordinate clause with the size of the effect (ETA), or a defect and its fix in two sentences [SCOUT main.tex:1951]. PROC gives a newly found background its own section: name, effect, causes, evidence, remedy, expected outcome. "Unfortunately" does not occur in the five papers.

- "The assumption of uniformity is not accurate, as most of the energy deposits happen early on during the shower development inside a crystal. Nevertheless, we are only interested in an order-of-magnitude estimate of radiation dose, to show that radiation damage on the crystals will be negligible throughout the experiment and that we can safely mitigate concerns about transparency losses." [SAC main.tex:245]
- "Therefore the energy resolution quoted here is only an upper limit to the actual one achievable by PADME, and should be interpreted as a single-crystal SAC energy resolution." [SAC main.tex:346]

**When not to apply.** If the authors have not assessed the effect, state the limitation alone. Do not add a "Nevertheless" that the data do not support. A caveat that changes the headline claim must also appear as a condition in the abstract, as in "single-crystal energy resolution".

**Before** (a last section). "Limitations. Our study has several limitations. First, only normal incidence was studied."

**After** (in the results). "Note that all data were taken at normal incidence. The resolution quoted here should therefore be interpreted as the resolution for perpendicular tracks. Nevertheless, tracks in the telescope are inclined by less than 2 degrees, and the 38 ps result therefore applies to its operating conditions."

### STRUCT-10. Report rejected options fairly and close with a verdict

**Rule.** Where a choice was made, name the options considered, give the number that decided, say where the losing option would be the better one, and close with a short verdict tied to the requirements.

**Why.** The reader sees that the choice was tested and can reuse the comparison under a different requirement.

**Evidence.** Usual; his own. SAC gives 17% of its body (10 paragraphs) to the choice of crystal and photomultiplier: the options announced by count, the loser's number, a concession, a verdict. The losing two-PMT option is then proposed for other uses in the abstract, the introduction and the conclusions. THESIS has a subsection "Other selections" for attempts that were dropped. The CMS texts compress this into the description of the standard method before the new one (ETA, SCOUT, IDM). PROC has no choice to report.

- "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost." [SAC main.tex:211]
- "Nevertheless, for higher energy applications, the two-PMT setup could be an interesting solution to explore." [SAC main.tex:211]
- "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]
- "Lowering this threshold to 3 GeV would increase the signal acceptance two-fold. However, we found that it also leads to a much larger fraction of misidentified muons." [THESIS paper.txt:10195-10197]

**When not to apply.** A conventional choice (standard software, a common setting) needs one clause. Do not give a rejected option more space than a result.

**Before.** "We chose the two-SiPM readout because it performs best."

**After.** "Two readout options were considered: one SiPM on one edge, and two SiPMs on opposite edges. The single-SiPM readout halves the number of channels. However, its resolution is 54 ps, which does not meet the 50 ps requirement. Hence, the two-SiPM readout is the preferred solution for the telescope. For applications that tolerate 60 ps, the single-SiPM readout could be an interesting option."

### STRUCT-11. In the conclusions, repeat the abstract's numbers and add one thing

**Rule.** Build the conclusions in this order: what was done (present perfect), the verdict against the requirements, all headline numbers of the abstract in one sentence, with the same digits and the same conditions, one new statement on wider use, a concrete next step. Add no new caveat. Do not retell the method or the motivation.

**Why.** A reader who jumps from the abstract to the conclusions finds the same numbers, so nothing has to be reconciled, and one statement more.

**Evidence.** Usual in the papers with a result; SAC is the one example in his own voice (PROC has no conclusions section and the thesis none of this form). SAC: 8 sentences in 2 paragraphs, 4% of the body, opening "We have characterized". All four headline numbers of the abstract return with the same digits; the words around them differ ("single-crystal energy resolution" becomes "an energy resolution", "double-peak separation resolution" becomes "double-peak separation capability"), which is not to be copied. New is one hedged sentence on wider use. The second paragraph recommends the two-PMT option that the abstract proposed. The physics motivation does not return. IDM (6 sentences) and ETA (7) restate the abstract in the same order and partly in identical clauses, which is CMS practice; IDM adds the reach gained, ETA a ratio and two sentences of outlook. PROC has no conclusions and ends on plans. The next step is specific in PROC, SAC, ETA and THESIS: an option and its gain, never "future work will explore". A last sentence that returns to the opening motivation occurs in ETA and THESIS chapter 16 only (occasional).

- "The PbF2 crystal coupled to the newly developed Hamamatsu R13478UV PMT has been found to provide a light yield of 2.05 p.e./MeV, an energy resolution of 10% at 550 MeV, and a timing resolution of 81 ps, with a double-peak separation capability of 1.8 ns." [SAC main.tex:451]
- "The robust double-peak resolution achieved suggests that the present setup might be suitable for a variety of high-intensity applications, being able to cope with rates higher than 100 MHz." [SAC main.tex:451]
- "Another possibility is moving the detector to Jefferson Lab, where a 12 GeV positron beam would increase the mass reach by a factor of 20." [PROC main.tex:190]

**When not to apply.** A status report or proceedings may end on plans without a conclusions section.

**Before.** "In conclusion, we have presented a novel timing detector with excellent performance. Precise timing will be crucial for future experiments. In future work we will explore many promising directions."

**After.** "We have characterized the time resolution of a scintillator tile read out by two SiPMs, using 4 GeV electrons. The tile has been found to provide a time resolution of 38 ps and an efficiency of 99.6%, which meet the requirements of the telescope. The margin to the 50 ps requirement suggests that the tile might also be suitable for higher beam rates. We recommend the further study of a thinner tile for low-momentum beams."

### STRUCT-12. Use titles that name the content

**Rule.** Title the paper with a noun or gerund for the act, then the object, then the instrument or means. Title each section with one to four plain words (84% of his own titles; six at most in SAC) in sentence case, a noun phrase that names the object, the step or the measured quantity.

**Why.** A title that names the content lets the reader find a section from the list of headings alone. A title that claims or asks does not.

**Evidence.** Always. All six titles open with the act: "Searching for", "Characterization and Performance of", "Search for" (IDM and THESIS), "Observation of", "Enriching". None has a colon, a question mark, a coined name for the method or a word of praise. Of the 217 section titles in PROC, SAC, SCOUT and THESIS, none has a finite verb, a colon or a question mark. Median length is 3 words in SAC and SCOUT and 2 in THESIS. Sentence case holds in SAC (11 of 14; the others are one word or mixed) and SCOUT (60 of 78); the title case of PROC and the capitals of thesis chapter titles come from templates. Results subsections carry the name of the quantity.

- "Characterization and Performance of PADME's Cherenkov-Based Small-Angle Calorimeter" [SAC main.tex:49]
- "Searching for Dark Photons with PADME" [PROC main.tex:28]
- Section titles: "Crystal/glass and PMT choices" [SAC main.tex:164], "Charge reconstruction" [SAC main.tex:348], "Timing resolution" [SAC main.tex:411]

**When not to apply.** Where the collaboration or the journal fixes the form (the long CMS title ending in the collision energy; a journal's own heading capitals), follow the form and keep the wording plain.

**Before.** Title: "TileTime: A Novel Ultra-Fast Detector for Next-Generation Timing". Section: "How well does the tile perform?"

**After.** Title: "Test-beam measurement of the time resolution of a scintillator timing tile". Section: "Time resolution".

## Measured targets

"Aim for" applies to a short methods paper by a few authors. OWN is listed as PROC / SAC / THESIS and CMS as IDM / ETA / SCOUT. A dash means the document has no such element. The full set of targets is Table B of `voice-and-transfer.md`.

| Quantity | OWN | SAC | CMS | Aim for | Reason |
|---|---|---|---|---|---|
| Abstract, sentences | 4 / 6 / 9 | 6 | 5 / 4 / 6 | 4 to 6 | one job per sentence |
| Abstract, words | 75 / 174 / 202 | 174 | 110 / 113 / 158 | 100 to 175, within the journal limit | room for the numbers |
| Abstract, numbers | 3 / 12 / 6 | 12 | 4 / 9 / 1 | the reference value and every headline result | the result must be judgeable |
| Abstract, "we" | 1 / 3 / 0 | 3 | 0 / 0 / 0 | 1 to 3 | the passive form is CMS style |
| Steps before the purpose sentence | 6 sentences / 6 paragraphs / 9 paragraphs | 6 paragraphs | 8 / 9 / 4 sentences | 3 to 6 short paragraphs | a short paper needs fewer than SAC |
| Introduction, share of body words | 9% / 12% / - | 12% | 27% / 14% / - | 10 to 15% | IDM also describes its signal there |
| Introduction, citation commands | 2 / 3 / 0 | 3 | 18 / 12 / - | few, each tied to a step | no survey in his own voice |
| Roadmap paragraph | no / no / yes | no | no / no / yes | none; 0 to 3 one-line signposts | only the long documents have one |
| Section titles, words | median 2.5 / 3 / 2 | median 3 | - / - / median 3 | 1 to 4, median 2 to 3 | plain nouns |
| Section titles with a verb, colon or question mark | 0 of 139 | 0 of 14 | 0 of 78 | 0 | titles name the content |
| Verdict sentences with "meet(s)" | 0 / 7 / reprint | 7 | 0 | one verdict per measured quantity | CMS compares with the standard method |
| Conclusions: sentences, paragraphs, share of body | - / 8, 2, 4% / - | 8, 2, 4% | 6, 1, 4% / 7, 1, 6% / long | 6 to 8 sentences, 1 or 2 paragraphs, 4 to 6% | repeat, add one thing, stop |
| Abstract headline numbers repeated in the conclusions | - / 4 of 4 / - | 4 of 4 | ETA: the branching fraction | all | abstract and conclusions must agree |
| Sections named Limitations, Discussion or Related work | 0 | 0 | 0 | 0 | caveats are local |

## Do not copy

Slips of unedited drafts:

- SAC leaves two of its six listed requirements (light yield, wavelength acceptance) without a verdict sentence, and lists a light yield "between 0.5 and 2" [SAC main.tex:155] against a result of 2.05 without comment. Close every requirement.
- SAC names its fit parameters differently in the equation and in the text [SAC main.tex:401-406]. PROC has "If carbon electrons and protons annihilate" where positrons are meant [PROC main.tex:66].
- A one-sentence paragraph that only points to a photograph [SAC main.tex:313], and a facility paragraph with operating details that no later step uses [SAC main.tex:301]. He kept both when he reprinted SAC in the thesis [THESIS paper.txt:16903, 16944]. In a short paper, attach the pointer to the paragraph on the setup.
- PROC points to figures without reading a value from them and states its purpose only in the abstract.

CMS and letter conventions (use only if the venue requires them):

- The abstract formulas "A search for ... is presented" and "Upper limits are set on" [IDM main.tex:40], the passive abstract without "we", and the summary that opens "In summary," and mirrors the abstract clause by clause.
- The standard detector paragraph, the sentence "Tabulated results are provided in the HEPData record for this analysis" [IDM main.tex:54], and the long title ending in the collision energy.
- The letter layout: no headings, paragraphs of 8 to 15 sentences, an introduction of 27% of the body.
- The two broad-interest sentences of IDM with "pioneering" and "foreshadows" [IDM main.tex:54]. That register occurs nowhere else in that paper.
- A result used before it is derived, bridged with "(described later)" [ETA main.tex:188].

Review-only habits (SCOUT):

- A "Report structure" subsection, an opener of the form "This section introduces ..." at every level, and bullets with bold run-in heads.
- An opening on praise, "has achieved remarkable success" [SCOUT main.tex:242], and the ornate words of the summary such as "stand poised" [SCOUT main.tex:2066]. Other contributors wrote much of this text.

Thesis-only habits:

- "This chapter describes the event selection applied to both data and simulated samples." [THESIS paper.txt:8727] and an opener of the same form ("This chapter" plus a verb) in ten other chapters; "I"; roadmaps at thesis, part and chapter level.
- A subsection for every dropped attempt, opened by "For completeness and future reference, I list other selections studied or that have potential for additional enhancements in subsequent iterations of this analysis:" [THESIS paper.txt:10152]. A paper gives one paragraph to a rejected option that mattered.
- A figure and a justification for every single requirement, and textbook recap chapters.
- The essay register of chapters 1 and 16, as in "We do not understand 95% of the universe." [THESIS paper.txt:1376]. Keep the short declarative first sentence; leave the register.

## Order of repair

Apply these steps when you draft, or when the authors ask for a restructuring; do them before editing any sentence. When the task is to polish a finished draft, keep every statement in its section and list these points as suggestions in the report (see the procedure in `voice-and-transfer.md`).

1. Write down the purpose in one sentence and the reference for judging the results (requirements, or the values of the standard method). If the draft lacks them, ask the authors.
2. Compare the abstract, the purpose paragraph and the conclusions. They must make the same claim with the same numbers and the same conditions.
3. Rebuild the introduction (STRUCT-3 and STRUCT-4) and reorder the sections (STRUCT-6).
4. Give each quantity a results subsection that ends on a verdict (STRUCT-1 and STRUCT-8).
5. Move every component behind its problem and every caveat to the place where it applies. Delete the limitations section and the roadmap paragraph (STRUCT-2, STRUCT-7, STRUCT-9).
6. Check each design choice (STRUCT-10) and rename the titles (STRUCT-12).

## Checklist

1. Does the abstract open on the object of the paper or its host experiment, with no sentence about the field?
2. Does the abstract give the requirement or reference value and every headline number with its condition?
3. Does the introduction reach the work in three to six steps, without a literature survey?
4. Is there exactly one purpose sentence, at the head of a paragraph, with a plain verb and the means?
5. Are the requirements, or the values of the standard method, stated as numbers before the first result?
6. Does every measured quantity have its own subsection that ends on a verdict?
7. Does every component appear directly after the problem it solves, with its cost stated where it has one?
8. Do the sections follow the order of the work, and does each method section follow the data?
9. Is the paper free of a roadmap paragraph, with three or fewer one-line signposts?
10. Does every section open on its subject or purpose and end without a recap?
11. Is every limitation stated where it arises, with its cause and with what still holds?
12. Is the paper free of sections named Limitations, Discussion or Related work?
13. For each design choice, are the alternatives, the deciding number and a verdict given?
14. Do the conclusions repeat the abstract's numbers with the same digits and conditions, add one statement on wider use, and end on a concrete next step?
15. Are all titles noun phrases without a verb, a colon or a question mark?
