# Paragraphs and flow

> **When to read this file.** Read it when you shape or repair paragraphs: their length, their first and last sentences, the links between them, and the order of information inside a methods or results passage.
> It holds eleven habits (PARA-1 to PARA-11) with their evidence, quotes, limits and before/after pairs, then the measured targets, the things not to copy and a checklist.
> Use it after the structure is settled (`conception-and-structure.md`) and before the sentences are edited (`sentences-and-voice.md`).

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

**How the counts were made.** "Automatic" counts apply one classifier to the first and last sentence of every body paragraph. "Hand" counts come from reading the document in full.

**Contents.**

- PARA-1. Open the paragraph on the thing it describes
- PARA-2. Link by the key noun and write no bridge sentences
- PARA-3. End on what was learned
- PARA-4. Keep paragraphs short and uneven
- PARA-5. Put the reason next to the choice
- PARA-6. Order a methods passage from purpose to verdict
- PARA-7. Announce a count, then deliver in that order
- PARA-8. State the caveat where it arises, then say what still holds
- PARA-9. Read a result as observation, cause, consequence
- PARA-10. Describe first, name afterwards
- PARA-11. Signpost with single sentences, not with a roadmap
- Measured targets; Do not copy; Checklist

**Summary.**

1. His paragraph is short: three to five sentences and about 75 words, with real spread around that.
2. It opens with the thing it describes as grammatical subject and closes on what was learned: a verdict, a number, a consequence, or the pointer to the figure.
3. Paragraphs are joined by a repeated noun, not by bridge sentences. Sentences inside a paragraph are joined by "This" or "These".
4. A few shapes recur: the reason next to the choice, the purpose first in a methods passage, a count before a list, a caveat followed by what still holds, an observation followed by its cause and its consequence.
5. A new term is described before it is named. The reader is steered by a few one-line signposts, never by a roadmap paragraph.

## Habits

### PARA-1. Open the paragraph on the thing it describes

**Rule.** Make the object, quantity or procedure that the paragraph is about the grammatical subject of its first sentence.

**Why.** The first words then work as a heading. A reader who scans only first sentences can still follow the paper.

**Evidence.** Always; 6 of 6; his own, and CMS editing strengthens it. Automatic: a plain noun-phrase subject opens 11 of 14 paragraphs in PROC, 29 of 61 in SAC, 12 of 17 in IDM, 10 of 17 in ETA, 73% in SCOUT and 58% in THESIS; 59% in OWN and 72% in CMS. A figure or table label is the subject in a further 8% in OWN. "We" opens 3% of paragraphs in OWN and 1% in CMS. In SAC it opens 4 of 61: two studies and the two paragraphs of the conclusions; the purpose paragraph opens "In this paper we". Nine more SAC paragraphs open with "To ..., we ..." or "From ..., we ..."; that form is his for a study or a decision. The other opener classes are in the table of targets.

- "The ECAL has a central hole due to the high rate of Bremsstrahlung events, which are sharply peaked at small angles." [SAC main.tex:151]
- "The baseline muon selection requires at least two identified DSA muons." [IDM main.tex:118]
- "Simulated samples of rare η decays are generated at leading order with a custom workflow." [ETA main.tex:176]

**When not to apply.** A paragraph that starts a study, a check or a decision may open with its purpose or with "we" (PARA-6). Keep "we" as the subject of the opening sentence in at most about one paragraph in five (13 of 61 in SAC, 8% in OWN, 3% in CMS).

**Before.** We use a waveform digitizer to record the signals of both SiPMs. We then extract the arrival time with a constant-fraction threshold.

**After.** The signals of both SiPMs are recorded by a 5 GS/s waveform digitizer. The arrival time is taken where the rising edge crosses 20% of the pulse amplitude.

### PARA-2. Link by the key noun and write no bridge sentences

**Rule.** Start a new paragraph with a noun that the previous paragraph has just introduced, or with "this" or "these" plus that noun, an ordinal, or "also". Inside a paragraph, start each sentence from something the previous one delivered. Delete any sentence whose only job is to announce the next topic.

**Why.** Each sentence and each paragraph begins on known ground and ends on the new information. The reader sees the link at once, and no sentence is spent on the transition.

**Evidence.** Usual; 6 of 6; his own. Hand count in SAC: of the 47 paragraph changes inside a section, 39 carry a link in the first sentence: 26 a repeated noun, 5 a demonstrative with a noun, 8 "also", an ordinal or a sequence word. Apart from three one-line signposts (PARA-11), no paragraph of SAC, PROC, IDM or ETA ends on an announcement of the next one. Automatic: the first sentence shares a content word with the previous paragraph in 86% of cases in OWN and 90% in CMS, against 15% to 33% for a random pair. Inside paragraphs, "This" or "These" opens 12.6% of sentences in OWN and 8.8% in CMS. In his own voice about half of the "This" openers are followed directly by a verb (48%); in CMS a noun is usually added (22% bare). A connector opens 8.3% of sentences in OWN and 7.4% in CMS. The introduction of PROC has six sentences, each starting from the new noun of the one before (PROC line 47).

- "The second candidate considered was the Hamamatsu R13478, Q and UV versions." [SAC main.tex:213] (the paragraph before treated the first candidate)
- "For dimuon resonance masses below ∼40 GeV, the performance of the standard muon triggers deteriorates." [ETA main.tex:95] (the paragraph before defined the standard triggers)
- "These selections further suppress backgrounds by ensuring that the DM system is well isolated in the event." [IDM main.tex:96-97] (inside a paragraph, after four requirements)

**When not to apply.** The first paragraph of a section, or a paragraph that opens on a new figure, may start fresh. Use a bare "This" only when it can point to one thing.

**Before.** ... The tile is read out by two SiPMs. / Having described the detector, we now turn to the readout. Moreover, an amplifier is used. In addition, the digitizer records the pulses.

**After.** ... The tile is read out by two SiPMs, one on each of two opposite edges. / Each SiPM signal is amplified by a factor of 10 and recorded by a 5 GS/s waveform digitizer. These waveforms are the input to the timing analysis.

### PARA-3. End on what was learned

**Rule.** Make the last sentence a verdict, a number, a consequence, or the pointer to the figure. Do not end on a sentence that only re-lists what the paragraph did, or on an announcement of the next one (up to three one-line signposts stay, PARA-11). Keep a closing sentence or paragraph that draws the decision from what was found: "From these considerations, we conclude the larger Hamamatsu R13478UV PMT, coupled to PbF2 crystals, is the best solution for PADME's requirements." [SAC main.tex:236]

**Why.** The last sentence is the one the reader carries forward. A verdict or a number there says what the paragraph established.

**Evidence.** Usual; 6 of 6; the "Nevertheless" and "Hence" closers and the short closer are his own. Hand count of the 61 last sentences of SAC: 16 a verdict or decision, 12 a number, 9 a consequence or reason, 6 a figure pointer, 3 a signpost, 3 a caveat, 3 a lead-in to an equation, 9 a plain detail. None only re-lists what its paragraph did; one (line 293, "Thus the simulation reveals that ...") sums up what the paragraph found. In ETA 10 of 17 end on a conclusion or a total; in PROC 5 of 14 on a figure pointer. Automatic: the last sentence opens with "Hence", "Therefore", "Thus", "Nevertheless" or "Overall" in 7 of the 57 multi-sentence paragraphs of SAC, 4% in OWN and 2% in CMS. A short closer is occasional: 24% of multi-sentence paragraphs in OWN end on a sentence of 12 words or fewer (17% of all his sentences are that short); in CMS 7%.

- "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]
- "There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282]
- "These requirements remove more than 90% of the electroweak SM backgrounds without incurring a significant loss of signal efficiency." [IDM main.tex:119]

**When not to apply.** A paragraph that only describes a setup may end on its last detail. Do not add a verdict that the paragraph has not earned.

**Before.** A Gaussian fit gives a width of 40 ps, and the reference contributes 12 ps. In summary, this paragraph has shown how the resolution is obtained. Next we turn to its dependence on position.

**After.** A Gaussian fit to the time-difference distribution gives a width of 40 ps. Subtracting the 12 ps of the reference detector in quadrature leaves a tile resolution of 38 ps, which meets the 50 ps requirement.

### PARA-4. Keep paragraphs short and uneven

**Rule.** Write paragraphs of three to five sentences and 60 to 110 words, one idea each. Let a step-by-step procedure or the description of a setup run longer and let a two-sentence paragraph stand. A step of the introduction has 2 to 4 sentences (SAC: 2, 2, 2, 4, 2, 4 and 3); do not merge two-sentence paragraphs to reach three. In a polish, leave a paragraph of 6 to 8 sentences alone, and never place a break between a number and its caveat, its control or its reference value. Use a one-sentence paragraph only to lead into an equation or a list, or to signpost. A figure pointer may stand alone, but it reads better at the end of the paragraph that describes what the figure shows.

**Why.** A short paragraph holds one idea, so its first sentence can name the idea and its last can close it. Lengths that follow the content show the reader which items are small and which are large.

**Evidence.** Always in his own voice: PROC, SAC, THESIS; the two letters differ because of their format. The median paragraph has 4 sentences (quartiles 3 and 5) and 76 words in OWN, 3 sentences and 74 words in SAC. In SAC 39 of 61 paragraphs have three to five sentences, 10 have two, and 4 have seven or more: two step-by-step procedures (lines 413 and 431) and two descriptions of a setup (lines 270 and 301). The letters have no section headings and reach a median of 8 sentences (IDM) and 6 (ETA). One-sentence paragraphs: 44 of 512 in OWN, 4 of 61 in SAC, none in PROC, IDM and ETA. Of the 44, at least 25 end on a colon or an equation; most others are figure pointers or signposts.

- A three-sentence paragraph: "The plot in Fig. 14 is a function of the actual deposited energy on the crystal, and not of incident beam energy. This is done to account for the fact that a single finite-sized crystal does not provide full energy containment. The correction used is shown in Fig. 11, as described in Section 6.1." [SAC main.tex:385]
- A one-sentence paragraph: "The plot was fit to the empirical function:" [SAC main.tex:338]

**When not to apply.** A letter without headings must merge paragraphs. A methods paper with sections should not.

**Before.** One paragraph of seven sentences: beam energy, beam spot, trigger, amplifier, digitizer, threshold, number of events.

**After.** Two paragraphs. The first has three sentences on the beam and the trigger. The second opens "Each SiPM signal is amplified ..." and has four sentences on the readout.

### PARA-5. Put the reason next to the choice

**Rule.** Give the reason for every setting or design choice in the same sentence or in the next one. If the reason is a property of the physics, state the property first and the choice second. If the choice is one item of a selection, state the requirement first and its purpose or effect second.

**Why.** The reader does not have to carry an unexplained number forward, and never wonders whether a choice was arbitrary.

**Evidence.** Always; 6 of 6; his own. Property, then choice: PROC lines 100 and 102, IDM line 94, SCOUT line 883, THESIS line 4777. Requirement, then reason: in the event-selection paragraph of IDM (lines 94-97) five of six requirements carry a purpose or an effect in the same or the next sentence (hand count). In his own voice the follow-up opens with "This" and a verb ("This ensures", "This reduces"): 52 such sentences in OWN, 8 in CMS, where the form is "These requirements" plus verb. One exception: SAC names crystal and photomultiplier in Section 2 and gives the reasons in Section 3, with a signpost (SAC line 162).

- "The distribution of Bremsstrahlung photons is sharply peaked toward small angles and low energies. To prevent these soft photons from impacting the hard photon energy measurements, the ECAL is built with a central square hole to let the Bremsstrahlung photons pass through." [PROC main.tex:100]
- "The muons are too soft to pass the trigger selection, so at least one energetic jet is required to boost the DM particles and enhance the pTmiss spectrum." [IDM main.tex:94]
- "Additional jets in the event are required to have at least 30 GeV pT. This reduces acceptance of soft pileup jets and also agrees with other analyses that use both pTmiss and jets (e.g. [107])." [THESIS paper.txt:8963-8967]

**When not to apply.** Standard settings that need no defense go to a table or a reference with one sentence.

**Before.** The arrival time is taken at 20% of the pulse amplitude. (Three sections later:) The threshold choice is related to time walk.

**After.** Pulses of different height cross a fixed threshold at different times. The arrival time is therefore taken at a fixed fraction, 20%, of the pulse amplitude.

### PARA-6. Order a methods passage from purpose to verdict

**Rule.** Open a study or a check with its purpose ("To <verb> ..., <action>"). Then say what the setup contains, give the inputs and the sample size as numbers, say what is left out or assumed, point to the figure, read it, and close on the number and what it means.

**Why.** The reader knows why each detail is there before reading it, and can judge the result against the stated purpose.

**Evidence.** Usual; 5 of 6; the purpose-first opener is absent from PROC. Automatic: "To ..." opens 3 of 61 paragraphs in SAC, 2 of 17 in IDM, 2 of 17 in ETA, and 4% in both OWN and CMS. All are studies, checks or selections. Sections 4 and 5 of SAC follow the full order (SAC lines 241-254 and 268-295). "The primary goal was to ..." is the second sentence of a study twice in SAC (lines 268 and 328). The sample size gets a short sentence of its own. What is left out is said with "Note that" or "We do not".

- "To establish our crystal specifications and to study different aspects of light collection efficiency, timing and energy resolution, we adapted our detector MC simulation to include a detailed optical description of physics inside the crystals." [SAC main.tex:268]
- "Note that we do not simulate the entire detector here, just a single crystal in the SAC." [SAC main.tex:270]
- "We run 100 events per crystal length." [SAC main.tex:272]
- "To maximize the signal efficiency for reconstructing and identifying candidate η meson decays, no additional selection is applied." [ETA main.tex:137-138]

**When not to apply.** A fixed component is described in another order: what it is, what it consists of, what that implies, one performance number, the figure (PROC line 86; THESIS lines 5332-5337).

**Before.** We recorded 50,000 events per position. The scan used 1 mm steps. A position scan matters because the resolution can depend on the impact point.

**After.** To measure how the resolution depends on the impact point, the tile was moved across the beam in steps of 1 mm. For each position 50,000 events were recorded. Note that the beam spot is 2 mm wide, so neighboring points are correlated.

### PARA-7. Announce a count, then deliver in that order

**Rule.** Before a list of steps, options, sources or parts, say how many there are. Then give them in the announced order: in one sentence after a colon if they are short, otherwise one per sentence or paragraph with "First", "then", "Finally," or "The first", "The second".

**Why.** The reader knows how long the list is, can tick the items off, and knows when it has ended.

**Evidence.** Always; 6 of 6; his own. Hand count: 10 announcers in SAC ("two options", "two candidates", "two corrections", "Three major goals", "three steps" among them), 6 in PROC, at least 4 each in IDM and ETA. Automatic: a number word with a plural noun before a colon occurs 42 times in OWN and 17 in CMS. "Finally," marks the last item and is his most frequent paragraph-opening connector (13 of 41 in OWN). The order is kept, with one slip in PROC (line 118).

- "The total energy deposited in the crystal was reconstructed in three steps." [SAC main.tex:352]
- "There are two main sources: the Beryllium window that is used to separate the accelerator vacuum from the detector vacuum, and the magnet that steers the beam from the injection point into the target." [PROC main.tex:134]
- "This type of uncertainty is subdivided into three parts: (i) on the track pT threshold, 9.0%; (ii) on the trigger pT threshold, 8.4%; and (iii) on the efficiency plateau, 3.2%." [ETA main.tex:267-268]

**When not to apply.** Do not count two items that sit inside one clause. Do not announce a count and then change the order.

**Before.** The arrival time is extracted as follows. The baseline is computed. Also, the rising edge is fit. Additionally, a threshold is applied.

**After.** The arrival time of each pulse was extracted in three steps. First the baseline was calculated from the 50 samples before the pulse. The rising edge was then fit to a straight line. Finally, the time at which the fit crosses 20% of the amplitude was taken as the arrival time.

### PARA-8. State the caveat where it arises, then say what still holds

**Rule.** Put each limitation in the paragraph it concerns, in one flat sentence. Follow it in the same paragraph with a sentence that says why the result still serves. Treat a rejected alternative the same way: what it is, why it appeals, its problem with a number, the verdict.

**Why.** A reader who meets the weakness and its bound together can use the number at once. A list of limitations at the end leaves every earlier number unqualified.

**Evidence.** Usual; the shape holds in 6 of 6; the word "Nevertheless" is his own. "Nevertheless" opens 5 sentences in SAC and 10 more in THESIS outside the reprinted chapter, against 1 in all of CMS (in SCOUT, which has a second use inside a sentence). Four of the five in SAC are the last sentence of a paragraph that has just admitted a weakness (SAC lines 211, 245, 408, 447). The CMS papers keep the shape with other words: weakness, cause and remedy in consecutive sentences (IDM line 121), or the cost after "but" in the same sentence (ETA lines 96-97). Rejected options: SAC lines 209-211, IDM line 57, THESIS lines 10172-10191. No document has a limitations section.

- "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost. Given PADME's relatively low beam energy, this light yield is unacceptably small. Nevertheless, for higher energy applications, the two-PMT setup could be an interesting solution to explore." [SAC main.tex:211]
- "The DSA muons have higher reconstruction efficiencies but degraded momentum resolution and impact parameter resolution compared to muons reconstructed with the standard algorithm. This is due to the smaller lever arm and lack of tracker information." [IDM main.tex:121]
- "The composition of events with lower pTmiss is not well understood and therefore the higher acceptance was not worth the spoiled independence between the observables." [THESIS paper.txt:10187-10191]

**When not to apply.** Do not write "Nevertheless" unless a stated weakness comes right before it. In a polish, add it only when three things hold: the sentence right before states a weakness, a limit or a rejected option; the sentence itself is already in the draft; and it speaks of the same result or object and says why that result still serves, or where the conclusion just drawn stops. A result for another range, sample or quantity is not what still holds: leave it without a connector, and when you are not sure, put the question in the report. Do not invent a caveat, or a statement of what still holds, to fill the shape; if the authors have not said what still holds, ask them.

**Before.** Our method achieves excellent time resolution. Several limitations of this study are collected in Section 7.

**After.** The correction assumes that the two SiPMs have equal gain. This assumption is not accurate, as the measured gains differ by roughly 5%. Nevertheless, the difference shifts the resolution by less than 1 ps, which is negligible against the 50 ps requirement.

### PARA-9. Read a result as observation, cause, consequence

**Rule.** After the sentence that brings in the figure, say what is seen, with a number. Then say why it is so. Then say what follows for the design or the claim.

**Why.** The cause shows that the effect is understood. The consequence tells the reader why the plot is in the paper.

**Evidence.** Usual; 5 of 6; not in PROC, which points to its figures without reading them. SAC lines 284 and 293; ETA lines 198-199 and 237-241; THESIS lines 8850-8855; SCOUT line 658. The consequence often opens with "This" and a verb ("This informs the choice of", THESIS line 8853) or with "Thus" or "Therefore". Automatic: a figure or table label opens 7% of his own paragraphs; a float is named somewhere in the first sentence of 13% and in the last sentence of 15%.

- "The light yield decreases with increasing length due to a higher chance of Cherenkov photons getting lost (absorbed or escaping) while traveling towards the PMT. In particular, there is a drop of about 14% in collected light between lengths of 18 cm and 14 cm." [SAC main.tex:284]
- "About 99% of four-muon combinations passed this selection in the signal mass window, compared to only 84% in the sideband. Since the sidebands presumably contain more hadrons misidentified as muons, this indicates a negligible contamination of such hadrons in the signal region." [ETA main.tex:198-199]

**When not to apply.** A layout or a schematic needs only the pointer.

**Before.** As shown in Fig. 5, the performance is significantly worse near the edge, which is an interesting result.

**After.** Figure 5 shows the time resolution as a function of the distance from the tile edge. The resolution degrades from 38 ps at the center to 46 ps at 2 mm from the edge. Near the edge part of the light escapes before it reaches the far SiPM. The fiducial region is therefore restricted to impact points at least 2 mm from the edge.

### PARA-10. Describe first, name afterwards

**Rule.** Introduce a new tool, quantity or term by what it does or how it is built. Give its name or symbol at the end of that sentence or in the next one. Define an acronym in parentheses inside a working sentence. Then reuse the same name.

**Why.** A name means nothing before the reader knows the thing. When the description comes first, the name arrives as a label for something already understood.

**Evidence.** Usual; 6 of 6; his own. Automatic: a naming verb after the description ("referred to as", "known as", "called", "dubbed", "labeled", "termed") occurs about 35 times in OWN and 30 in CMS; 15 naming sentences in THESIS open with "This" or "These". PROC and SAC name no new term with a naming verb (SAC has "labeled" once, for a plot label). There the name follows a colon (PROC line 134), or the device enters as the answer to a need stated just before (SAC line 153), or the symbol follows the construction of the quantity (SAC line 431). At paragraph scale the same order gives: where the standard tool falls short, the remedy, its price, its name (ETA lines 95-100; IDM lines 99-101; THESIS lines 6635-6641). All six documents put the acronym in parentheses after the full name at first use for their main terms, inside a sentence about the thing ("MC" in PROC and "ADC" in SAC are left undefined).

- "This carrier is called the dark photon." [THESIS paper.txt:1410]
- "This strategy, first introduced by the CMS Collaboration in 2012, is referred to as “data scouting”." [ETA main.tex:99-100]
- "From this original set of data, a new source of backgrounds not previously accounted for was identified: beam-induced backgrounds." [PROC main.tex:134]

**When not to apply.** A term every reader of the journal knows needs only its acronym in parentheses.

**Before.** We introduce the Dual-Edge Timing (DET) algorithm. In DET, the times of both SiPMs are averaged.

**After.** The arrival times measured by the two SiPMs are averaged for each event. This average does not depend on the impact point to first order, since a longer light path to one SiPM is compensated by a shorter path to the other. We refer to it as the mean time.

### PARA-11. Signpost with single sentences, not with a roadmap

**Rule.** Do not write a paragraph that lists the sections. Where a section splits into several studies, end its opening paragraph with one sentence that says what follows. Keep such signposts to three or fewer in the paper.

**Why.** In a short paper the section titles already give the plan. A one-line signpost where the text branches tells the reader where the remaining items are.

**Evidence.** Always in the four papers; his own. None of PROC, SAC, IDM and ETA has a roadmap paragraph. SAC has three forward signposts, each a single sentence that ends a paragraph (SAC lines 162, 241, 374). IDM has one forward signpost (line 132) and ETA one parenthesis, "(described later)" (line 188). The scope is stated once: in the last sentence of the abstract in PROC, in the first sentence of the last introduction paragraph in SAC (line 155). Roadmaps and "This chapter" or "This section" openers belong to the thesis and the review. Automatic: they open 19 of 492 paragraphs in THESIS, 7 of 315 in SCOUT, and none in the four papers.

- "We describe below the investigation that led to the choices of crystal and PMT, as it offers some interesting directions for future similar experiments." [SAC main.tex:162]
- "These studies are discussed below." [SAC main.tex:374]
- "Here we describe PADME's design, status of the experiment, and future plans." [PROC main.tex:34]

**When not to apply.** If the journal or an editor asks for a roadmap in a short paper, give it two sentences at the end of the introduction and nothing more. A long review or a thesis needs a roadmap: one sentence per section with a plain verb.

**Before.** The rest of this paper is organized as follows. Section 2 describes the detector. Section 3 describes the beam. Section 4 presents the reconstruction. Section 5 shows the results.

**After.** (No roadmap. At the end of the first paragraph of the results section:) We measured the time resolution at the tile center, its dependence on the impact point, and its dependence on the overvoltage. These studies are discussed below.

## Measured targets

"Aim for" applies to a short methods paper by a few authors. Opener shares are percentages of all body paragraphs (automatic), not of sentences; the sentence-level shares are in `sentences-and-voice.md`, and the full set of targets is Table B of `voice-and-transfer.md`. Last-sentence shares are percentages of paragraphs with two or more sentences. A few percent of paragraphs open with "This", "These", "There" or "It" and are not listed.

| Measure | OWN | SAC | CMS | Aim for | Reason |
|---|---|---|---|---|---|
| Sentences per paragraph, median (quartiles) | 4 (3, 5) | 3 (3, 5) | 4 (3, 6); letters 8 and 6 | 3 to 5 | the letters are long only because they have no headings |
| Words per paragraph, median (quartiles) | 76 (55, 109) | 74 (60, 104) | 111 (77, 157) | 60 to 110 | same |
| Paragraphs of 8 or more sentences | 5.9% | 3.3% | 15.0% | at most 5% (1 in 20) | only procedures run long |
| Two-sentence paragraphs | 14.4% | 16.4% | 11.8% | 10% to 20% | the spread is part of the habit |
| One-sentence paragraphs | 8.6% | 6.6% | 3.8% | at most 1 in 15 (about 7%) | lead-ins and signposts; a lone figure pointer now and then |
| Opener: the thing as subject | 59% | 48% | 72% | 50% to 70% | PARA-1 |
| Opener: figure or table label | 8% | 11% | 5% | 5% to 10% | a paragraph that reads a figure |
| Opener: fronted case or condition (In, For, Since, Given, From) | 12% | 16% | 12% | 10% to 15% | scope of what follows |
| Opener: "To <purpose>," | 4% | 5% | 4% | about 5% | studies and checks |
| Opener: connector | 8% | 7% | 3% | under 10% | mostly "Finally," |
| Opener: "We" | 3% | 7% | 1% | under 10% | studies, conclusions |
| Opener: signpost ("This section ...") | 4% | 0 | 2% | 0 | thesis and review genre |
| Last sentence of 12 words or fewer | 24% | 18% | 7% | 15% to 25% | an occasional short verdict |
| Last sentence opens with Hence, Therefore, Thus, Nevertheless, Overall | 4% | 12% | 2% | up to 10% | a marked verdict, not in every paragraph |
| First sentence shares a content word with the previous paragraph | 86% | 85% | 90% | above 80% | chance is 15% to 33% |
| Forward signposts in the paper | not applicable | 3 | 1 in each letter | 0 to 3 | PARA-11 |

## Do not copy

**Thesis only.**

- "This chapter describes ..." and "In this section, I present ..." openers, and roadmaps at chapter and section level.
- Bullet lists of requirements, each led in by a one-sentence paragraph that ends on a colon.
- A dedicated subsection for rejected attempts. In a paper a rejected option gets a few sentences (PARA-8).
- Paragraph endings that point to another chapter.
- Colloquial turns: "A further wrinkle is that", "Unfortunately,", "At first glance".

**CMS and letter format.**

- Paragraphs of 8 to 15 sentences. In IDM 9 of 17 paragraphs have eight or more, because a letter has no headings.
- The standard detector paragraph and the generator and pileup sentences.
- A last paragraph that opens "In summary," and repeats the abstract in the passive.
- Paired alternatives in parentheses, as in "12 (15) GeV at L1 in 2017 (2018)".

**Review genre (SCOUT).**

- Roadmaps at three levels, back-pointers of the kind "as discussed in Section N", and one-sentence bridge paragraphs.
- Ornate section openers and closers written by other contributors.

**Slips.**

- PROC line 118 announces two beam monitors and describes them in the reverse order.
- PROC defines PMT, POT and ALPs and never uses them again, and uses MC without defining it. Define an acronym only if it returns.
- SAC line 313 is a one-sentence paragraph that holds only a figure pointer (he kept it in his thesis reprint [THESIS paper.txt:16944]). In a short paper, attach the pointer to the paragraph that describes the setup.
- SAC line 406 calls the fit parameters p1 and p2 where the equation has p0 and p1.
- THESIS defines CMB twice and alternates "SR" with "signal region". Name once and keep the name.

## Checklist

1. Does every paragraph open with the thing it describes as subject, unless it starts a study, a check or the purpose statement?
2. Does "We" open fewer than one paragraph in ten, and is "we" the subject of the opening sentence in at most about one paragraph in five?
3. Inside a section, does the first sentence of each paragraph repeat a noun from the previous paragraph, or carry "this" or "these", an ordinal or "also"?
4. Is the text free of sentences whose only job is to announce the next paragraph or to re-list what the current one did?
5. Do most paragraphs end on a verdict, a number, a consequence or a figure pointer, and none on a recap?
6. Do most paragraphs have three to five sentences and 60 to 110 words (two to four in the steps of the introduction), and is every paragraph above eight sentences a step-by-step procedure or the description of a setup?
7. Is every one-sentence paragraph a lead-in to an equation or a list, a signpost or a figure pointer that has no better place, and are there at most one in fifteen?
8. Does every setting or design choice have its reason in the same sentence or the next?
9. Does each study or check open with its purpose and give sample size, omissions and assumptions before the result?
10. Is every list of three or more items announced with its count and delivered in that order?
11. Does each caveat sit where it applies, followed by what still holds?
12. After each data figure, does the text give an observation with a number, its cause and its consequence?
13. Is each new term described before it is named, and is the name then reused unchanged?
14. Is there no roadmap paragraph, and are there three or fewer one-line signposts?
