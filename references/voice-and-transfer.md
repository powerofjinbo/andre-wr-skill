# Personal voice, house style and the polishing procedure

> **When to read this file.** Read it before you polish a whole draft into his style, when you must decide between his own form and a CMS or journal form, or when you need the full table of targets.
> It holds ten habits of transfer (VOICE-1 to VOICE-10), Table A (whose habit each feature is), Table B (the measured targets), the seven-pass procedure, what to report back, the things not to copy and a checklist.
> The other six files give the evidence for each habit in depth; this file says which form to write and how far to go.

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

**Contents.**

- VOICE-1. "We" for decisions, studies and claims
- VOICE-2. An active thing-subject for a removed "we"; the passive for mechanics
- VOICE-3. A "This + verb" sentence after a statement
- VOICE-4. Several causal joins, and a rare ", so"
- VOICE-5. One sentence in ten opens with a connector
- VOICE-6. A sentence of its own for each figure
- VOICE-7. A caption of a noun phrase plus one or two sentences
- VOICE-8. Mixed sentence lengths
- VOICE-9. His own form where it differs from the CMS form
- VOICE-10. Light edits, and no change of content
- Table A. Whose habit it is
- Table B. Measured targets
- Procedure: seven passes; Do not copy; Checklist

**Summary.**

1. The six documents hold two layers: his own voice (PROC, SAC, THESIS) and CMS house style laid over it (IDM, ETA, SCOUT).
2. Where the two differ, write his own form. Where the target journal has a rule, follow the journal.
3. SAC is the model for a short methods paper by a few authors. The letters show how he reports a result. The thesis shows what he writes when nobody edits him.
4. A draft in a short-sentence, we-heavy style differs from him in five measurable ways: too many sentences that open with "We", one causal join (", so"), few connectors and few "This + verb" sentences, long captions, and figures cited as "see Fig. N".
5. Polish in seven passes and change only the form. Numbers, claims, citations, labels and LaTeX stay as they are.

## Habits

### VOICE-1. "We" for decisions, studies and claims

**Rule.** Keep "we" for decisions, studies, simulation runs and claims. Give every other sentence a thing as its subject. For a paper by a few authors that reports their own studies, "we" may stand in up to about one sentence in five and open up to about 8% of sentences, as in SAC. Do not remove a "we" to reach a number.

**Why.** "We" then marks where the authors chose, tested or concluded something. In a paper that compares a new method with an existing one, it also shows which steps are the authors' own.

**Evidence.** Sentences containing "we": PROC 3%, SAC 19%, IDM 6%, ETA 5%, SCOUT 2%, THESIS 6%. Sentences opening with "We": SAC 7.7%, all others 2.2% or less. The function is the same in all six. IDM has present, probe, focus, select, require, divide, choose, assess. ETA has report, study, conclude, define, assume, estimate. SAC adds the studies the authors ran and what they found: 11 of the 42 "we" sentences in its body narrate a step of a simulation or of a plot ("we simulate" [SAC main.tex:241], "we generated" [SAC main.tex:243], "We run 100 events per crystal length." [SAC main.tex:272]). Its two sections on operations on recorded data ("Charge reconstruction", "Timing resolution"; 31 sentences) contain no "we". No document lies between 6% and 19%, so the share follows the genre. The low rate in the CMS papers is partly collaboration convention. The function is his.

- "To decide between the R9880U-110 and the R13478UV PMTs, we completed a study to understand the signal distribution expected for each one." [SAC main.tex:217]
- "Based on these studies, we conclude that other decay modes of the η meson provide a negligible contribution to the selected events." [ETA main.tex:220-221]

**When not to apply.** The abstract and the conclusions may hold more "we" (SAC abstract: 3 of 6 sentences). Keep a "we" that separates the authors' work from other people's.

**Before.** We place the tile 2 m downstream of the reference detector. We digitize the signals at 5 GS/s. We choose a constant-fraction threshold of 20% because it minimizes the time walk.

**After.** The tile sits 2 m downstream of the reference detector. The signals are digitized at 5 GS/s. We choose a constant-fraction threshold of 20% because it minimizes the time walk.

### VOICE-2. An active thing-subject for a removed "we"; the passive for mechanics

**Rule.** Replace a removed "we" by an active sentence with a thing as subject. Use a passive for the mechanics of a procedure. Never use a passive that hides who decided.

**Why.** The active sentence is shorter and names what acts. A passive is acceptable only when the reader does not need the actor.

**Evidence.** Sentences with a passive: PROC 37%, SAC 43%, THESIS 40%; IDM 56%, ETA 53%, SCOUT 52%. The higher CMS share goes with the lower share of "we" and is house style. In all six a fit, a simulation, a requirement or a figure can be the subject of an active verb.

- "The jet pT requirement removes low-momentum jets produced in pileup interactions." [IDM main.tex:95]
- "The timing resolution was determined by extracting the sigmas of a Gaussian fit to each such distribution." [SAC main.tex:421]

**When not to apply.** Stop near 45% of sentences with a passive. When he states a choice in the passive, the reason sits in the same sentence: "The choice of threshold was made to mitigate the after-pulse ringing which can be seen in the figure." [SAC main.tex:362]. If the draft gives no reason, keep "we" and ask the authors for one.

**Before.** We fit the time-difference distribution with a Gaussian and we find a width of 40 ps. We then subtract the resolution of the reference detector in quadrature. It was decided to exclude the runs taken at the lowest overvoltage.

**After.** A Gaussian fit to the time-difference distribution yields a width of 40 ps. The resolution of the reference detector is then subtracted in quadrature. We exclude the runs taken at the lowest overvoltage.

### VOICE-3. A "This + verb" sentence after a statement

**Rule.** Follow a statement with a sentence of its own that starts with "This" and a verb. After a sentence of 12 words or fewer, attach the consequence as a tail instead (", which" plus a verb, or a participle).

**Why.** The fact comes first and its consequence or cause second, each with its own verb. The reader need not hold a long sentence to learn why the fact matters.

**Evidence.** "This" opens 6.0% (PROC), 6.8% (SAC), 6.0% (IDM), 8.3% (ETA), 4.9% (SCOUT) and 10.0% (THESIS) of sentences. A verb follows directly in 50%, 56%, 50%, 20%, 19% and 48% of them. The habit is his own and is kept in IDM. ETA and SCOUT prefer "This" + noun ("This uncertainty", "This requirement"); in SAC 7 of the 16 "This" openers also carry a noun ("This procedure"). The "This + verb" sentence is not a short one: the nine in SAC have 12 to 29 words (median 22), and the sentence before each has 16 to 32. No paragraph of SAC has three sentences of 12 words or fewer in a row.

- "This makes 140 mm a safe length to ensure we can harness most of the Cherenkov photons in a 500 MeV shower." [SAC main.tex:295]
- "This is due to the smaller lever arm and lack of tracker information." [IDM main.tex:121]

**When not to apply.** When "This" could mean two things in the previous sentence, add the noun ("This procedure"). Do not open more than one sentence in ten with "This".

**Before.** We average the times measured at the two ends of the tile for each event to give a single arrival time, so the result does not depend on where the particle crossed the tile.

**After.** The times measured at the two ends of the tile are averaged for each event to give a single arrival time. This removes the dependence on the position where the particle crossed the tile.

### VOICE-4. Several causal joins, and a rare ", so"

**Rule.** Spread the causal joins over "due to", "since", "because", "therefore", "hence", "thus" and a trailing participle clause. Keep ", so" rare: leave it where it is rare, and replace only the extra ones above about 6 per 10,000 words.

**Why.** Each join does a different job. "Since" puts the reason first, "due to" names a cause in a noun phrase, "therefore" marks a conclusion. One join repeated makes every step read alike.

**Evidence** (per 10,000 words). Own voice: since 18, due to 12, therefore 11, because 8, hence 4, thus 3, "so" as a conjunction 5. SAC: due to 17.5, hence 8, since 6, therefore 6, thus 6, so 6, because 0. CMS: because 9 (two thirds "because of"), thus 8, therefore 5, since 3, due to 2.5, so 0.7. ", so" occurs once in SAC (three times with "and so"; he kept all three in his thesis reprint), once in IDM, twice in SCOUT and 16 times in the 42,000 words of the thesis. "Because of" is more frequent in the CMS papers (26 uses, 6.0 per 10,000 words) than in the thesis (11 uses, 2.5); PROC and SAC have none, and no "because" either. "Owing to" is rare in both voices (4 in the thesis, 2 in ETA). Trailing participle clauses of consequence occur in all six.

- "Smaller electromagnetic showers reduce the detector occupancy, thus enhancing its rate capabilities." [SAC main.tex:177]
- "The spectrum of Bremsstrahlung radiation is highly peaked at small angles, so the SAC receives most of the radiation." [SAC main.tex:243]

**When not to apply.** Do not remove every ", so"; he uses it about once in 2,000 words. In a passage of fewer than about 2,000 words one ", so" may stay; keep the one that states a physical fact and what follows from it [SAC main.tex:243]. Keep "because" where the reason is the point of the sentence. Choose the join by the length: when the whole sentence has fewer than about 25 words, keep it as one sentence (a fronted "Since", "due to" plus a noun phrase, or a tail); split off a "This + verb" sentence only when the first clause has about 15 words or more. "and hence" joins two phrases that share a subject; a second clause with its own subject takes "Hence, ..." or keeps "and so" [SAC main.tex:383].

**Before.** The trigger counter is smaller than the tile, so we record only particles that cross its central 2 cm × 2 cm. The light yield is lower near the edges, so the resolution is worse there. The amplifier noise is much smaller than the signal, so we neglect it.

**After.** Since the trigger counter is smaller than the tile, only particles that cross its central 2 cm × 2 cm are recorded. The resolution is worse near the edges due to the lower light yield. The amplifier noise is much smaller than the signal, and we therefore neglect it.

### VOICE-5. One sentence in ten opens with a connector

**Rule.** Open about one sentence in ten (7 to 11%) with a connector, counted on the list of 31 in `corpus-and-measurements.md`.

**Why.** The connector tells the reader, before the sentence is read, whether it adds, turns, concludes or limits.

**Evidence.** A connector opens 7.5% (PROC), 10.7% (SAC), 6.0% (IDM), 5.8% (ETA), 7.6% (SCOUT) and 8.5% (THESIS) of sentences. His frequent ones, in percent of own-voice sentences: Finally 1.5, However 1.1, Therefore 0.95, Furthermore 0.95, Nevertheless 0.7, Moreover 0.5, Note that 0.4. First, Then, Hence, Thus, Consequently, "In particular,", "In this case,", "For this reason,", "For example," and "On the other hand," also open sentences in his own texts, and stay. "Nevertheless" (SAC 5, THESIS 10 more outside the reprinted chapter, CMS 1 as an opener) and "Note that" as an opener (SAC 4, THESIS 4 more, CMS 0) belong to his own voice only. As sentence openers, "Additionally" and "In addition," are absent from PROC, SAC, IDM and ETA (SCOUT 7 and 9, THESIS 2 and 0).

- "Nevertheless, we find that with a single crystal, the energy resolution is roughly 10% at 550 MeV, which already meets PADME's SAC requirements." [SAC main.tex:408]
- "Furthermore, this decay mode has never been observed." [ETA main.tex:217-218]

**When not to apply.** Do not add a connector where the sentences are a plain sequence. Paragraphs rarely open with one (SAC: 4 of 61). Add "Nevertheless," only when three things hold: the sentence right before states a weakness, a limit or a rejected option; the sentence itself is already in the draft; and it speaks of the same result or object and says why that result still serves, or where the conclusion just drawn stops. All five uses in SAC pass this test (lines 211, 245, 295, 408, 447). A result for another range, sample or quantity is not what still holds: leave it without a connector. When you are not sure, do not add the word and put the question in the report. Never write a new claim of what still holds.

**Before.** The Gaussian fit does not describe the tails of the distribution. The tails hold less than 2% of the events, and the fitted width changes by less than 1 ps when they are excluded.

**After.** The Gaussian fit does not describe the tails of the distribution. Nevertheless, the tails hold less than 2% of the events, and the fitted width changes by less than 1 ps when they are excluded.

### VOICE-6. A sentence of its own for each figure

**Rule.** Introduce each figure by a sentence with the figure as subject or in the form "X is shown in Fig. N". Put it where the figure is first needed: at the start of the paragraph that discusses the figure, at the end of the paragraph whose product it is, or inside the paragraph, before the first statement that is read from the figure. Never write a trailing "see Fig. N".

**Why.** The reader learns what is plotted before looking at it, and the sentence that states the result is not interrupted by a reference.

**Evidence.** The figure or table is the subject in 57% (PROC), 31% (SAC), 12% (IDM), 50% (ETA), 46% (SCOUT) and 46% (THESIS) of the float mentions. "Is shown in" and its variants take 36% to 75%. The verb is "shows" in 54 of his 87 own-voice cases. A "see Fig. N" outside parentheses occurs in 0 of 331 mentions; "(see Fig. N)" twice, both in SAC (once in the text, once in a caption). In SAC 6 of the 20 floats are first cited in the middle of a paragraph (lines 169, 177, 254, 282, 364, 421). "X can be seen in Fig. N" is also his (4 in SAC, none in the CMS papers). "As shown in" occurs 0 times in PROC, SAC and IDM, once in ETA, twice in THESIS and 11 times in SCOUT.

- "Fig. 15 shows the achieved energy resolution as a function of deposited energy on the crystal." [SAC main.tex:391]
- "The resulting resolutions for all channels and runs are shown in Fig. 17." [SAC main.tex:421]

**When not to apply.** "Fig." or "Figure" follows the venue: PROC and SAC print "Fig." everywhere, the thesis "Figure" everywhere, the letters "Fig." inside a sentence and "Figure" at its start. Use the journal's form. A diagram that only illustrates may be cited at the end of a clause ("as illustrated in", twice in IDM). For a figure that illustrates one statement (an event display, a sketch, an example), the pointer carries that statement in a clause and is not split in two: "Figure 10.14 represents the ideal scenario, in which the optimal bin shifts upward proportionally with increasing displacement." [THESIS paper.txt:13854-13855] A condition that the draft ties to a figure goes into the pointer, in the words of the caption.

**Before.** The resolution improves with the overvoltage and reaches 38 ps at 5 V; see Fig. 5.

**After.** Figure 5 shows the time resolution as a function of the overvoltage. The resolution improves with the overvoltage and reaches 38 ps at 5 V.

### VOICE-7. A caption of a noun phrase plus one or two sentences

**Rule.** Open each caption with a noun phrase without article. The norm is that phrase plus one or two sentences (SAC: median 2 sentences and 42 words); up to five sentences on a result plot with several elements. Trim a caption only when it argues or interprets, by moving out a derivation, the physical reason or a second finding.

**Why.** The caption tells the reader what is plotted and how to read it. An argument placed in a caption is cut off from the paragraph that needs it.

**Evidence.** Median caption: PROC 24 words and 1 sentence, SAC 42 and 2, ETA 38 and 2, THESIS 38 and 2, SCOUT 50 and 3, IDM 70 and 3.5. The caption opens with a noun phrase without article in 100% (PROC), 90% (SAC by the script; the other two open with the name of the crystal, also a noun phrase), 100% (IDM), 86% (ETA), 99% (THESIS) and 68% (SCOUT). A sentence that states the result is his own habit: 8 of 20 SAC captions by reading (6 by the script, which tests the last sentence only), 23% of thesis captions, 4.5% of CMS captions. Keys for colors and markers in parentheses occur in all venues, more often in CMS (53% of captions against 22%). In SAC 5 of 20 captions have four or more sentences (lines 205, 309, 358, 379, 425), and 5 hold a fact that the running text does not state (lines 173, 259, 358, 379, 425). He says how a point was obtained in the caption as well as in the text (SAC lines 334 and 330, 289 and 284, 417 and 413). "our" stands in four SAC captions; "we" in none.

- "Arrival time distribution of Cherenkov photons versus crystal length for a 200 MeV incident photon. The distribution shifts to the right and broadens with increasing length." [SAC main.tex:278]
- "The fit yields a resolution of roughly 10% at 550 MeV, which meets PADME's requirements." [SAC main.tex:395, last sentence of the caption]

**When not to apply.** Three kinds of sentence stay in the caption even when the text says the same: a limit of what the plot shows (what is left out, not drawn, scaled, or merged into a last bin), the definition of a plotted element (normalization, meaning of a band), and how a point was obtained. Keep a sentence with the finding where the draft's caption has one; do not add one. If a caption is still above 50 words or three sentences, leave it, report its length, and propose to the authors what could go: first a key that repeats a complete legend, then the finding that the text states with the same numbers. Never delete a sentence taken out of a caption; place it after the sentence that introduces the figure.

**Before (caption).** The time resolution of the tile for different overvoltages. We find that the resolution improves with the overvoltage because the gain of the SiPMs rises. At the highest overvoltages the curve flattens because the dark-count rate rises. The blue points use the leading-edge threshold and the red points the constant-fraction threshold. The best value is 38 ps, which meets the 50 ps requirement.

**After (caption).** Time resolution of the tile as a function of the overvoltage, for the leading-edge (blue) and constant-fraction (red) thresholds. The best value of 38 ps meets the 50 ps requirement.

**After (text).** The resolution improves with the overvoltage since the gain of the SiPMs rises. The curve flattens at the highest overvoltages due to the rise of the dark-count rate.

### VOICE-8. Mixed sentence lengths

**Rule.** Mix sentence lengths. Keep short sentences for verdicts, steps and pointers. Do not chop a sentence into fragments. Join two short sentences only when the draft as a whole is below his range and one of the two has no fact of its own.

**Why.** A short sentence gives a verdict weight. A longer one keeps a reason next to the fact it explains. A text made only of short sentences leaves the reader to supply the logic between them.

**Evidence.** The median is 19 to 20 words in PROC, SAC and THESIS and 22 to 24 in the CMS papers. In his own voice 17% of sentences have 12 words or fewer, 15% more than 30 and 3.5% more than 40 (SAC: 14%, 17.5%, 4.3%). In CMS the shares are 9%, 25% and 8%. A draft in a short-sentence style usually has his share of short sentences and too few above 30 words. A run of short declaratives is his form for a list of facts or for a chain of cause and effect, one link per sentence: SAC closes a section on five sentences of 9 to 14 words (lines 177-178), and "Increasing the length causes more Cherenkov photons to be lost along the way. At the same time, in a longer crystal photons have longer travel paths." [SAC main.tex:293]

- "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]
- "By measuring precisely the energy and impact position of the photon with the ECAL, its momentum can be determined, since it originates in a fixed target." [PROC main.tex:66]

**When not to apply.** Do not lengthen a sentence that states a result. Go beyond 40 words only for a list or a definition.

**Before.** The tile is wrapped in foil. The foil is reflective. This increases the light collection. A steeper leading edge results. A steeper edge reduces the time jitter.

**After.** The tile is wrapped in reflective foil, which increases the light collection and hence steepens the leading edge of the pulse. A steeper edge reduces the time jitter.

### VOICE-9. His own form where it differs from the CMS form

**Rule.** Where his own form and the CMS form differ, write his own form. Let the journal decide the mechanics.

**Why.** These are choices of taste. They do not change what the reader learns. They decide how much he must change by hand.

**Evidence.** Table A sorts the habits. The clearest case is the approximator. Per 10,000 words, "roughly" has 9.5 in his own voice and 2.1 in CMS; "approximately" has 0.5 and 5.3. "Roughly" survives CMS editing 9 times.

- "There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282]
- CMS form: "The jet uncertainties are larger in 2017 because of noise issues with the ECAL endcap." [IDM main.tex:161]

**When not to apply.** Follow the journal's style guide where it fixes a form ("Fig." or "Figure", "Eq." or "Equation", the comma after "i.e.", "data set", closed prefixes), and name each case in the report. Write "Section" in full, as he does in the three documents that refer to a section (SAC, SCOUT, THESIS; "Sec." occurs in none of the six); if the draft, the authors or the journal's guide have "Sec.", keep it and say so in the report. Do not copy an own-voice form that he corrects himself: a "which" without comma became "that" when he re-edited SAC for the thesis [THESIS paper.txt:17063].

**Before.** Approximately 5% of the triggers are rejected because of a second beam particle in the same bunch.

**After.** Roughly 5% of the triggers are rejected due to a second beam particle in the same bunch.

### VOICE-10. Light edits, and no change of content

**Rule.** Edit as lightly as he edits himself. Never change a number, a claim or its strength, a citation, a label or a LaTeX command.

**Why.** The authors have checked the content. A change made to it by an editor is an error that nobody will look for. A light edit is also quicker for him to review.

**Evidence.** Chapter 14 of the thesis reprints SAC, edited by him alone two years later. Of its 215 sentences, 145 are identical word for word, 27 differ only in commas, 42 carry small changes of wording or number format, and one is new. He dropped the abstract and the first five paragraphs of the introduction. He removed commas before a trailing phrase, turned "In this paper we" into "Here, we", deleted one ", however," and turned "to order" into "to roughly". The measured values are the same. This is one comparison, of his own published paper: it shows which small things he changes, not how much a draft by other hands needs.

- "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost." [SAC main.tex:211]
- "Even coupling two of them provides only 11% of geometric acceptance while doubling the cost." [THESIS paper.txt:16451-16452]

**When not to apply.** There is no exception for content. If a number looks wrong, or two numbers disagree, report it and leave it.

**Before.** With the constant-fraction threshold we obtain a time resolution of about 38 ps, which could be sufficient for the 50 ps requirement [12].

**Wrong.** The constant-fraction threshold gives a time resolution of 38 ps, comfortably meeting the 50 ps requirement.

**After.** The constant-fraction threshold gives a time resolution of about 38 ps, which could be sufficient for the 50 ps requirement [12].

## Table A. Whose habit it is

OWN+ = his own: holds in PROC, SAC and THESIS and survives in the CMS papers. OWN = his own, in own-voice texts only. HOUSE = CMS or journal style. THESIS = thesis only.

| Habit | Where it holds | Class; in the target paper |
|---|---|---|
| Purpose stated with "we" and a plain verb late in the introduction; no roadmap paragraph | "In this paper we" SAC; "In this Letter, we" IDM, ETA; "Here we describe" PROC. Roadmaps only in SCOUT and thesis chapter openings | OWN+; use |
| Requirement or baseline before the result | SAC ("meet" or "meets" 7 times); prediction beside measurement in ETA | OWN+; use |
| Limitation stated where it arises, then what still holds | No limitations section in any of the six | OWN+; use |
| Count announced, items given in that order | All six | OWN+; use |
| Thing first, name second ("referred to as", "known as") | IDM 3, ETA 3, SCOUT 13, THESIS 19; "we call" 0 in six | OWN+; use |
| Paragraph opens with the thing described; 3 to 5 sentences | All six open so. The letters run to 6 to 8 sentences because they have no headings | OWN+; the long form is HOUSE |
| "We" for decisions, studies and claims | All six by function. One sentence in five in SAC; 6% or less in CMS, with passives in over half | OWN+; the low rate is HOUSE |
| "This" + verb | Half of the "This" openers in PROC, SAC, IDM, THESIS; a fifth in ETA, SCOUT | OWN+, weakened by editing; use |
| A connector opens about one sentence in ten | All six, 6% to 11% | OWN+; use |
| "Nevertheless,", "Note that" as sentence openers | SAC, THESIS; 1 and 0 in CMS | OWN; use |
| "since" (causal), "due to", "in order to" | Own 18, 12, 5 per 10,000 words; CMS 3, 2.5, 1.6 | OWN; use |
| "because of" | CMS 26 uses (6.0 per 10,000 words); THESIS 11 (2.5); none in PROC and SAC. "owing to": 4 in THESIS, 2 in ETA | more frequent in CMS; not needed |
| "Additionally,", "In addition,", "Crucially,"; "garnered", "pivotal", "leverage", "utilize" | SCOUT, parts by other contributors ("Additionally," twice and "Notably," twice also in THESIS) | HOUSE; avoid |
| Possessive 's on an experiment, a device or a particle ("PADME's requirements", "the PMT's QE") | SAC about 20, PROC 7; three or fewer in each CMS paper | OWN; keep |
| Trailing participle clause for a consequence | All six | OWN+; one per sentence |
| "roughly" + number | 49 in OWN, 9 in CMS; "approximately" is CMS (24 against 2); "about" + number is in both voices | OWN+; use |
| No praise of the method; words of sufficiency (sufficient, acceptable, negligible) | "state-of-the-art" 0 in six; "outperform", "utilize" 0 outside SCOUT | OWN+; use |
| "MC", "cut" | SAC ("MC" 12 times, "a cut was imposed" twice) and PROC ("MC" 6 times). His thesis reprint of SAC kept "MC simulation" eight times and "cut", and turned a bare "MC" into "simulation" [THESIS paper.txt:16814]; the thesis has "selection" 98 times against "cut" 13. CMS: "simulation", "requirement" | OWN+ for "MC simulation"; bare "MC" and "cut" are early OWN: no error, and a "cut" that the draft defines stays |
| Hyphen after "non" and "sub"; no comma after "i.e." | Own. CMS: closed prefixes, "i.e.," | OWN against HOUSE; follow the journal |
| Lower-case "standard model", serial comma, US spelling | Lower case in five of the six; PROC has capitals | OWN+; use |
| Figure as subject, or "is shown in Fig. N", in its own sentence | All six | OWN+; use |
| "Fig." or "Figure" | PROC and SAC, THESIS, and CMS each differ | HOUSE; journal form |
| "as shown in Fig. N" | SCOUT 11, ETA 1, THESIS 2, others 0 | HOUSE; avoid |
| Caption opens with a noun phrase without article | 86% to 100% in five; SCOUT 68% | OWN+; use |
| Caption of 25 to 50 words that may state the finding | SAC, THESIS (PROC states none). CMS: 50 to 70 words in IDM and SCOUT (ETA 38), every symbol defined, no conclusion | OWN; the long form is HOUSE |
| Number with its condition and baseline in the same sentence | All six | OWN+; use |
| Detector paragraph; "A search for ... is presented"; "No significant excess"; HEPData sentence; passive summary opening "In summary," | IDM, ETA | HOUSE; no |
| Paired values in mirrored parentheses, "A (B) ... x (y)" | Frequent in the letters (5 sentences in 6,800 words); 7 sentences in OWN, one of them in SAC | mostly HOUSE; write the two cases out when the sentence allows |
| A dash as punctuation | One construction in SAC, one pair in PROC, ten in THESIS; none in IDM and ETA, two in SCOUT | OWN, rare; never add one |
| "I"; "This chapter ..." openings; roadmaps at each level; "Equation" in full; colloquial words; evaluative adjectives | THESIS | THESIS; no |

## Table B. Measured targets

"Aim for" applies to a short methods paper by a few authors. Shares are percent of sentences unless stated. Sentence-level numbers are good to about one word and three percentage points. This table is the reference for every range: the other files of this skill and `scripts/andre_style_check.py` use the same values. Paragraph openers are in `paragraphs-and-flow.md`, punctuation in `sentences-and-voice.md`, word rates in `words-and-phrases.md` and `numbers-results-methods.md`, abstract, introduction and conclusions in `conception-and-structure.md`.

| Feature | Own voice | SAC | CMS | Aim for | Reason |
|---|---|---|---|---|---|
| Words per sentence, median | 20 | 20 | 24 | 19 to 22 | His papers and thesis agree |
| Sentences of 12 words or fewer; above 30; above 40 | 17%; 15%; 3.5% | 14%; 17.5%; 4.3% | 9%; 25%; 8% | 13% to 18%; 13% to 18%; 2% to 5% | Short for verdicts, long for a reason or a list |
| Paragraph: sentences (quartiles); words | 4 (3, 5); 76 | 3 (3, 5); 74 | 4 (3, 6); 111; letters 8 and 6 sentences | 3 to 5; 60 to 110 | The journal has headings |
| Paragraphs of 8 or more sentences; of one sentence | 6%; 9% | 3%; 7% | 15%; 4% | At most 5%; at most 1 in 15 | Long only for step-by-step descriptions |
| Sentences containing "we"; opening with "We" | 5.8%; 1.9% | 19.2%; 7.7% | 2.4%; 0.5% | Up to 20%; up to 8% | SAC is the model for a paper by a few authors; no document lies between 6% and 19% |
| Sentences with a passive | 39.5% | 42.7% | 52.5% | 35% to 45% | Own voice; more hides the actor |
| Open with The, This, These, A, An, Each, All | 47% | 47% | 53% | 45% to 55% | The thing described comes first |
| Open with "This"; of these, verb next | 9.7%; 48% | 6.8%; 56% | 5.2%; 22% | 6% to 10%; about half | His main link between sentences |
| Open with a fronted phrase (In, For, To, Since, ...) | 12.3% | 15.4% | 13.6% | 11% to 16%; "For" at most 3%, "With" at most 1%, "To" 2% to 4% | More delays the subject |
| Open with a connector | 8.3% | 10.7% | 7.4% | 7% to 11% | Stable across all six |
| Finally, However, Therefore, Furthermore, Nevertheless, Moreover, Note that | 1.5, 1.1, 0.95, 0.95, 0.7, 0.5, 0.4 | 0.4, 0.85, 0.4, 1.3, 2.1, 0, 1.7 | 1.2, 0.5, 0.4, 0.5, 0.06, 0.5, 0 | Each at most about 2% | No connector dominates |
| Per 10,000 words: since (causal), due to, therefore, because, hence, thus, so | 18, 12, 11, 8, 4, 3, 5 | 6, 17.5, 6, 0, 8, 6, 6 | 3, 2.5, 5, 9, 1.4, 8, 0.7 | Four or more in use, none above 20, "so" at most 6 | Variety is the habit |
| Per 1,000 words: all approximators, roughly, approximately | 1.5, 0.95, 0.04 | 2.3, 1.17, 0.20 | 2.0, 0.21, 0.53 | 1.5 to 2.5; 0.5 to 1.2; 0 to 0.2 | "Roughly" is his word |
| Per 1,000 words: colons; semicolons; dashes; parenthesis pairs | 4.2; 0.8; 0.5; 10.6 | 2.5; 1.0; 0.2; 12.9 | 1.2; 0.65; 0.07; 7.9 | 2 to 4; under 1; at most 0.2; 9 to 13 | Announced lists and specifications; one dash construction in a paper at most |
| Caption: median words; median sentences; share with 4 or more | 37; 2; 13% | 42; 2; 25% | 50; 3; 31.5% | 25 to 50, none above 100; 1 to 3; at most a quarter | SAC's longest has 97 words |
| Caption opens with a noun phrase without article | 98% | 100% by reading (90% by the script) | 72% | All | Holds in five of six |
| Caption states a finding | 22% | 8 of 20 by reading (30% by the script) | 4.5% | At most 2 captions in 5; never added in a polish | SAC is the measured upper end; CMS leaves it to the text |
| Figure or table as subject; "is shown in" and its variants (share of float mentions) | 47%; 36% | 31%; 41% | 44%; 41% | 30% to 50%; 35% to 45% | Each gives the figure its own clause |
| Counts: "see Fig. N" outside parentheses; "(see Fig. N)"; "as shown in" | 0; 2; 2 | 0; 2; 0 | 0; 0; 12 | 0; at most 1; at most 1 | He does not use them |
| Section titles: median words; case | 2; sentence case | 3; sentence case (11 of 14) | 3; sentence case (60 of 78) | 1 to 4 words, median 2 to 3, noun phrase, sentence case | SAC: "Test beam setup", "Energy resolution" |
| Abstract: sentences; words | PROC 4, THESIS 9; 75, 202 | 6; 174 | 4 to 6; 110 to 158 | 4 to 6; 100 to 175 | One job per sentence, with room for the numbers |

## Procedure: seven passes

**Before the first pass.** List every number with its unit, every citation key, label, macro and equation, and every claim with its hedge ("about", "could", "is expected to"). List each caveat, exclusion and condition together with the number or claim that it limits, and list a number once for every place where it stands (text, caption, table). After the last edit every caveat must still stand in the same sentence, paragraph or caption as that number. A statement that the draft makes twice, in the text and in a caption, keeps both copies unless the authors agree to drop one. Measure the features of Table B.

**Polishing a part of a paper.** Leave every form that the rest of the paper also has: a term that the draft defines, a naming formula, an abbreviation, a spelling. List each as a change for the whole paper in the report. A form changed in one passage only makes the paper inconsistent.

**The typical starting draft.** A draft in a short-sentence, we-heavy style usually looks like this. The sentences are short and of one length. "We" opens far more than one sentence in ten. ", so" is the main causal join; "since" and "due to" are missing. Few sentences open with a connector or with "This"; many open with "For" or "With". The captions explain the physics. Figures are cited with a trailing "see Fig. N". New terms are introduced by their name first.

The seven passes are those of `SKILL.md`, word for word; the principles they name are the eleven of that file.

1. **Structure.** Check principles 1, 2 and 7: one purpose sentence, a reference for each result, each caveat where it applies, no roadmap. Keep every statement in its section. Propose moves between sections, and deletions, in the report; carry them out only when the user asks for a restructuring (then follow the order of repair in `references/conception-and-structure.md`).
2. **Paragraphs.** Aim for 3 to 5 sentences. Let the first name the thing described and the last give a number or a verdict. Leave a paragraph of 6 to 8 sentences alone. Split one above 8 sentences unless it is a step-by-step procedure; if a pointer or a split sentence of your own pushed it past 8, first fold the pointer into the sentence that reads it. Never place a break between a number and its caveat, its control or its reference value. Inside a section you may reorder sentences.
3. **Voice.** Sort every sentence that contains "we". Keep those with a choice, a study, a finding, a recommendation or a simulation run. Above one sentence in five, take those that narrate an operation on recorded data and turn each into a sentence about the thing: active where the thing acts, passive otherwise.
4. **Joins and connectors.** Leave ", so" where it is rare. Above about 6 per 10,000 words, replace the extra ones by the join that fits the length. When the whole sentence has fewer than about 25 words, keep it as one sentence: a fronted "Since", "due to" plus a noun phrase, or a tail (a participle as in ", making X a Y" or ", thus ...ing"; ", which" plus a verb). Split off a "This + verb" sentence only when the first clause has about 15 words or more, and a "Hence," sentence only for the verdict of the paragraph. "and hence" joins two phrases that share a subject; for a second clause with its own subject write "Hence, ..." or keep "and so" (SAC line 383). In front of sentences that already do those jobs, add "Furthermore,", "Finally," or "Note that"; add "Nevertheless," only by the test of principle 7. Move a fronted "For" or "With" phrase behind the subject where it reads well; leave it where it carries the condition of a number or sets one case against the next (he fronts "For" plus a case himself, SAC line 387).
5. **Words.** Apply principle 8 and the lexicon. Swap "approximately" for "roughly" where the draft already rounds; add no approximator. Turn "which we call Y" into "which we refer to as Y" when the authors coined the name, and into "referred to as Y" or "known as Y" when the name is in general use. When you propose the removal of a praise word or an intensifier ("excellent", "state-of-the-art", "significantly"), list it in the report, since it is part of what the authors claimed.
6. **Figures and captions.** Apply (c) below.
7. **Numbers.** Check principle 9 on every number. A missing condition, reference, definition or uncertainty is a question for the authors. Add nothing that the draft does not state.

In pass 6, "(c) below" is section (c) of `SKILL.md`; VOICE-6 and VOICE-7 give its evidence. "Note that" opens a sentence that says what a procedure leaves out or assumes, or where a result is valid (SAC lines 270, 346, 387). Add it only in front of such a sentence that the draft already has. After pass 7, compare the lists made before the first pass with the edited text. They must be identical.

**How far to go.** The ranges of Table B describe a whole paper in his practice; where a range and SAC disagree, SAC decides. They are not quotas. Stop when a feature is inside its range. Never add a connector, a "This" or a passive only to move a number. On fewer than about 100 sentences use the checker for its list of sentences to look at and not for its marks: in SAC the median of 44 consecutive sentences runs from 18 to 23.5 words. Never choose between two wordings by the number of marked rows. When an edit that this skill asks for (a pointer, a split semicolon, a "Hence," verdict) moves a length feature out of its range, keep the edit and report the feature. Some features cannot move without new content and are not targets of a polish: sufficiency words, "roughly" and the other approximators, the number of citations, the numbers read off a plot, and the passive share of a text in which the things act. Leave a sentence alone when it is clear and already in his manner; he left two thirds of his own sentences untouched. Keep "we" for decisions, studies and claims whatever its share.

**What to report back.**

- The features of Table B before and after.
- Every number, hedge, caveat or citation that moved, for example from a caption to the text, and every praise word or intensifier proposed for removal.
- Questions to the authors: a choice without a reason, a number without a condition or baseline, an unclear "This", numbers that disagree.
- Suggestions on structure that were not carried out.
- Points where the journal's style and his own form differ, and which was used.
- Confirmation that numbers, claims, citations, labels and LaTeX are unchanged.

## Do not copy

- **Slips.** "If carbon electrons and protons annihilate" (positrons are meant) [PROC main.tex:66]; "for two different number of" [PROC main.tex:173]; "p1 and p2" for parameters that the equation calls p0 and p1 [SAC main.tex:406]; one PMT model spelled three ways [SAC main.tex:213, 227, 453]; "this data" beside "The data were" [SAC main.tex:254, 399]; "10x", "5x5", "10k events"; "comic locations", "dark mater density" [THESIS paper.txt:1491, 1517].
- **Own-voice habits that editing removes.** "Fig." at the start of a sentence (PROC 4, SAC 8). "Which" without comma for a restrictive clause. A comma before a trailing "while" or "using" phrase is in SAC and gone from his thesis reprint, which removed about 30 such commas; leave what the draft has.
- **CMS boilerplate.** The detector paragraph. "A search for ... is presented." "No significant excess ... is observed." The HEPData sentence. A passive summary that repeats the abstract. Values in parentheses for a second case.
- **Letter register.** The two broad-interest sentences of IDM ("pioneering sensitivity", "foreshadows") [IDM main.tex:54] have no parallel in his own texts.
- **Review register from other contributors.** "garnered", "pivotal", "groundbreaking", "leverages", "utilizing", "kinematical", "Crucially,". ("paramount", "Notably," and "Additionally," also occur in THESIS, once or twice each, and in none of his papers.)
- **Thesis only.** "I". "This chapter describes ...". Roadmaps at every level. Bullet lists of requirements. Colloquial words ("a bit", "quite", "plethora", "dubbed"). Evaluative adjectives ("striking", "remarkable").

## Checklist

1. Are all numbers, units, hedges, citations, labels and LaTeX commands identical before and after?
2. Does every remaining "we" state a choice, a study, a finding, a recommendation or a simulation run?
3. Do at most about 20% of sentences contain "we", and at most about 8% open with it, and was no "we" removed only to reach a number?
4. Do 35% to 45% of sentences hold a passive, with none that hides who decided?
5. Does "This" open 6% to 10% of sentences, with a verb next in about half?
6. Are at least four causal words in use, with ", so" at most six times per 10,000 words?
7. Does a connector open 7% to 11% of sentences, with no "In addition," or "As a result," and no "Nevertheless," added without its test?
8. Are 13% to 18% of sentences above 30 words, and as many at 12 words or fewer?
9. Do most paragraphs have 3 to 5 sentences and open with the thing described?
10. Is every figure introduced by a sentence with the float or the plotted thing as subject, with no "see Fig. N"?
11. Does every caption open with a noun phrase without article, and does it keep its limits, its definitions and how its points were obtained?
12. Was every sentence removed from a caption placed in the text, and does every caveat still stand beside the number it limits?
13. Is his own form used wherever it differs from the CMS form and the journal has no rule?
14. Is the text free of CMS boilerplate, thesis-only habits and the listed slips?
15. Does the report give the features before and after, the questions to the authors and the points left to the journal?
