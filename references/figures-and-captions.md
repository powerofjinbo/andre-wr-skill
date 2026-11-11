# Figures, tables and captions

> **When to read this file.** Read it when you write or repair a caption, the sentence that introduces a figure or a table, or the sentences that read a figure for the reader.
> It holds twelve habits (FIG-1 to FIG-12) with their evidence, quotes, limits and before/after pairs, then caption templates, the measured targets, the things not to copy and a checklist.
> It covers the words around a figure, not the artwork; polishing cannot add or redraw a figure, so note a missing one for the authors.

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

**Contents.**

- FIG-1. Give each float one pointing sentence of its own
- FIG-2. After the pointer, read the figure for the reader
- FIG-3. Open the caption with a noun phrase, without article and without verb
- FIG-4. Order the caption: quantity, axis variable, condition, origin; then full sentences
- FIG-5. Put colors, line styles and panel positions in parentheses after the item they label
- FIG-6. Keep the caption short
- FIG-7. Keep a finding that the caption has; do not add one
- FIG-8. Use the same name for the plotted quantity in the pointer and in the caption
- FIG-9. Put the pointer where the figure is first needed, and cite each float once where it is introduced
- FIG-10. Treat a table like a figure, and keep its caption shorter
- FIG-11. Know what each figure is for
- FIG-12. Follow the venue for "Fig." and "Figure"
- Caption templates; Measured targets; Do not copy; Checklist

**Summary.**

1. Every float gets one pointing sentence of its own in the running text: the float is the subject of a plain verb ("Fig. N shows X"), or the plotted thing is the subject ("X is shown in Fig. N").
2. The sentences after the pointer read the figure for the reader: what is drawn, what to look at, one number, the reason, and what it decides.
3. A caption opens with a noun phrase without article and without verb that names what is plotted, then gives the axis variable, the condition and the origin of the numbers.
4. Colors, line styles and panel positions stand in parentheses right after the item they label. Captions are short: about 40 words and two sentences in his own voice.
5. In SAC and the thesis a caption may state a finding with its number (8 of 20 captions in SAC). PROC and the CMS papers keep every verdict in the text. "Fig." or "Figure" follows the venue.

## Habits

### FIG-1. Give each float one pointing sentence of its own

**Rule.** Write "Fig. N shows X as a function of Y." or "X is shown in Fig. N." as a complete sentence. Use a plain verb in the present tense. Make its object the thing that is drawn, not a claim about it. A condition that the draft ties to the figure goes into the pointer, in the words of the caption: "Figure N shows X as a function of Y, with <condition>."

**Why.** The reader learns what the picture is before being told what to conclude from it.

**Evidence.** All six documents. In OWN the float is the grammatical subject in 99 of 212 mentions (47%), and a participle with "in" ("is shown in", "is displayed in") takes 77 (36%). In CMS: 52 of 119 (44%) and 49 (41%). The verb after a figure is "shows" in 54 of 87 cases in OWN and 40 of 46 in CMS; the others are illustrates, compares, depicts, highlights, summarizes. "Fig. N shows that ..." occurs 0 times in PROC, SAC, IDM, ETA and THESIS, and 3 times in SCOUT. In PROC and SAC these sentences have 7 to 22 words, median 13.

Never, in all six: "see Fig. N" outside parentheses (0 of 331 mentions), the tag "as can be seen", a sentence that opens with "As shown in Fig. N", "Tab.". "X can be seen in Fig. N" is one of his pointer forms (SAC lines 169, 362, 413 and 431, as in "Two examples can be seen in Fig. 16." [SAC main.tex:413]; none in the CMS papers) and stays. Rare: "(see Fig. N)" in parentheses (twice, both in SAC: once in the text, once in a caption) and a trailing ", as shown in Fig. N" (0 in PROC, SAC and IDM, 2 in THESIS, 1 in ETA, 11 in SCOUT). No figure is first introduced inside parentheses in PROC, SAC, IDM or ETA; the thesis does it once.

- "Fig. 11 shows the average fraction of deposited energy in the crystal as a function of incident electron energy." [SAC main.tex:330]
- "Fig. 5 shows the four auxiliary detectors." [PROC main.tex:118]
- "The resulting resolutions for all channels and runs are shown in Fig. 17." [SAC main.tex:421]
- "Figure 6 shows the total efficiencies vs. pT, split by rapidity range." [ETA main.tex:236]

**When not to apply.** A later mention of a figure already introduced may sit inside a phrase: "From the slope of the solid fit line in Fig. 14, we find a light yield of 2.05 p.e./MeV." [SAC main.tex:387]. A diagram that only illustrates a statement may be attached to it: IDM ends a sentence with ", as illustrated in Fig. 1" [IDM main.tex:56]. Do not use that form for a plot that carries evidence. For a figure that illustrates one statement (an event display, a sketch, an example), the pointer carries that statement in a clause; do not split such a sentence in two: "Figure 10.14 represents the ideal scenario, in which the optimal bin shifts upward proportionally with increasing displacement." [THESIS paper.txt:13854-13855]

**Before.** The time resolution improves strongly with overvoltage and reaches 38 ps; see Fig. 5.

**After.** Figure 5 shows the time resolution as a function of overvoltage. The resolution improves from 46 ps at 2 V to 38 ps at 5 V.

### FIG-2. After the pointer, read the figure for the reader

**Rule.** Follow the pointer with one to four sentences in this order, leaving out what does not apply: how the points were obtained or how to read the plot; the feature to look at; one number; the physical reason; what it means for a choice or a requirement.

**Why.** A reader who is told where to look does not have to decode the plot alone. The consequence says why the figure is in the paper.

**Evidence.** Five of six documents. In SAC 18 of 20 floats get such sentences, by a hand count. In ETA every data figure gets three moves: what is plotted, one feature or number, why. In the first half of SCOUT 20 of 24 figures get a reading. PROC is the exception: 5 of its 7 pointers are followed by nothing. It is a six-page proceedings; do not imitate that.

- Pointer, then one number: "The MC Landau spread time is plotted in Fig. 8. There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282]
- Number, then the requirement: "The PbF2 resolution was found to be 81 ps, which comfortably meets the 200 ps timing requirement for a successful SAC performance." [SAC main.tex:421]
- Consequence for a choice: "This motivates the pT threshold of 5 GeV in the identification selection for both collections which corresponds roughly to the plateau onset of the efficiency curves." [THESIS paper.txt:7758]

**When not to apply.** A photograph or a layout needs no reading. Do not read more than one or two numbers off a plot; the rest stays in the plot or goes to a table.

**Before.** Figure 6 shows the time-difference distributions. The systematic uncertainties are discussed in Section 5.

**After.** Figure 6 shows the distribution of the time difference between the tile and the reference detector for 4 GeV electrons. Each distribution is fit with a Gaussian function, and the fitted width is taken as the combined resolution. The width decreases from 62 ps to 40 ps when the time-walk correction is applied. The correction is therefore used in all measurements that follow.

### FIG-3. Open the caption with a noun phrase, without article and without verb

**Rule.** Start the caption with the name of what is plotted and close that phrase with a period. Do not write "This figure shows", "Shown is", "Plot of" or a leading "The".

**Why.** The first words work as a title. A reader who scans the figures finds the plotted quantity at once.

**Evidence.** All six documents. In OWN 188 of 192 captions (98%) open with a bare noun phrase and 2 with an article; the first sentence has no finite verb in 95%. In CMS 72% open bare and 21% with "The" or "A" (18 of 76 in SCOUT, 1 of 7 in ETA, 0 in IDM), so the leading article belongs to the collaboration papers. By a hand classification of the first word, 43% of OWN captions name the kind of display ("Comparison of", "Distribution of", "Layout of", "Sketch of", "Schematic layout of", "Fraction of", "Feynman diagram of"), 45% name the quantity directly, and 12% start with the origin ("Expected", "Measured", "Simulated", "Projected"). No caption opens with "This figure shows" or "Shown is"; one ETA caption has "Also shown is ..." as its second sentence [ETA main.tex:205].

- "Schematic layout of the PADME experiment." [PROC main.tex:61]
- "Integrated charge distribution for 300 MeV electrons." [SAC main.tex:368]
- "Feynman diagram of pseudoscalar decays into four leptons, known as double-Dalitz decays." [ETA main.tex:64]

**When not to apply.** None in a journal paper. Remove a leading "The" even though the CMS papers allow it.

**Before.** This figure shows how the time resolution of the tile depends on the overvoltage.

**After.** Time resolution as a function of overvoltage for 4 GeV electrons.

### FIG-4. Order the caption: quantity, axis variable, condition, origin; then full sentences

**Rule.** Build the opening phrase in this order: the quantity; "as a function of" its variable; the sample or condition after "for"; the origin of the numbers after a comma ("as determined from", "based on", "estimated with"). Then add full sentences, one job each: how the points were obtained, how to read the plot, a presentation choice (a scaled curve, a cut range, an overflow bin, the meaning of the error bars), or the cause of an odd feature.

**Why.** The order follows the questions a reader asks of a plot: what, against what, for which case, from data or from simulation. An unexplained scaled curve or gap costs the plot its credit.

**Evidence.** All six documents. The opening phrase states the origin in 4 of 7 PROC captions (two with ", as determined from a Geant4-based Monte Carlo simulation"), 5 of 20 in SAC, 5 of 7 in ETA and 28 of 76 in SCOUT. SAC says how the plotted values were obtained in 11 of 20 captions, counting the full sentences after the opening. The link to the axis variable is "as a function of" in both pools (28 per 10,000 caption words in OWN, 49 in CMS); SAC also writes "versus" (lines 278 and 289); "vs." occurs in the thesis and in the CMS papers. In a caption keep the draft's word if it is "as a function of" or "versus". Presentation choices are declared in 17 captions across five documents (ETA: 4 of 7).

- "Light yield (red) and Landau time spread (green) versus crystal length for a 200 MeV incident photon, based on a detailed optical MC simulation. The light yield is estimated by convolving the energy distribution of arriving photons with the PMT's QE profile, and the timing resolution by a Landau fit of the arrival time distribution." [SAC main.tex:289]
- "The last plot is zoomed in to the displacement region between 0 and 60 cm, since global muons cannot be very displaced." [THESIS paper.txt:12196]
- "Uncertainties are statistical only." [ETA main.tex:172]

**When not to apply.** Skip the origin when every figure comes from the same data set and the text says so once. Do not list choices that change nothing for the reader.

**Before.** Using Gaussian fits and the reference detector we measured, for 4 GeV electrons, the resolution, which is plotted here against overvoltage.

**After.** Time resolution as a function of overvoltage for 4 GeV electrons, as determined from a Gaussian fit to the time difference with the reference detector. Each point is the mean of three runs.

### FIG-5. Put colors, line styles and panel positions in parentheses after the item they label

**Rule.** Name the item, then give its key in parentheses: "before (red) and after (blue) the correction", "A (left) and B (right)". Give a secondary element (a band, a reference line, a marker) a short sentence of its own with the element as subject and a plain verb. When the panels show unrelated things, write a key: "Left: A; right: B."

**Why.** The reader meets the meaning first and the key second, in one pass. A sentence built on the color makes the reader carry the color until the meaning arrives.

**Evidence.** Colors: five of six documents; PROC names none. Of the 73 captions that name a color, 49 give it in parentheses after the item (SAC 6 of 7, IDM 2 of 3, ETA 3 of 3, SCOUT 24 of 34, THESIS 14 of 26). About 25 captions add a sentence with the element as subject; the verb is "indicate" or "represent" in OWN and "denote" or "correspond to" in CMS. "The ... lines show" occurs once in 300 captions. Panels: a position in parentheses after the item in 59 captions (THESIS 36, SCOUT 22, IDM 1); a key with colons in 27 (THESIS 20, SCOUT 5, PROC 2); SAC writes "(a) ... (b)" once. From the thesis on he prefers "upper" and "lower" (68 and 62 per 10,000 caption words) to "top" and "bottom" (14 and 11).

- "PbF2 (red and blue) and SF57 (green) transparency profiles, compared to the Cherenkov spectrum (black, not to scale)." [SAC main.tex:173]
- "True pileup distributions measured in QCD simulation (black) and data (red) in 2018 (upper left), 2017 (upper right), and 2016 (lower center)." [THESIS paper.txt:5993]
- "Simulated muon reconstruction efficiency of standard (blue squares) and displaced (red circles) reconstruction algorithms as a function of transverse vertex displacement vxy. The two dashed vertical gray lines denote the ends of the fiducial tracker and muon detector regions, respectively." [IDM main.tex:112]

**When not to apply.** Do not repeat a legend that is complete and legible in the plot; ETA writes "as indicated in the legend" for that case. If the journal prints panel labels (a), (b), use them in the same slot.

**Before.** The red line shows the resolution before the correction. The blue line shows the resolution after the correction. The dashed line shows the requirement.

**After.** Time resolution before (red) and after (blue) the time-walk correction, as a function of signal amplitude. The dashed line indicates the 50 ps requirement.

### FIG-6. Keep the caption short

**Rule.** The norm is a noun phrase plus one or two sentences, 25 to 50 words in all; up to five sentences on a result plot with several elements. Shorten a caption only by moving out what explains or argues: a derivation, the physical reason, a second finding. Three kinds of sentence stay in the caption even when the text says the same: a limit of what the plot shows (what is left out, not drawn, scaled, or merged into a last bin), the definition of a plotted element, and how a point was obtained. Do not use "we" in a caption.

**Why.** A caption is read next to the plot. Past three sentences it starts to repeat the text.

**Evidence.** All six documents, strongest in his own voice. Median caption: 37 words and 2 sentences in OWN (PROC 24 words, SAC 42, THESIS 38), 50 words and 3 sentences in CMS. Captions of four or more sentences: 13% in OWN, 25% in SAC, 32% in CMS. One-sentence captions: 23% in OWN. The longest SAC caption has 97 words. "we" appears in no caption of PROC, SAC, IDM or ETA ("our" stands in four SAC captions). In SAC 5 of 20 captions have four or more sentences (lines 205, 309, 358, 379, 425), and 5 hold a fact that the running text does not state (lines 173, 259, 358, 379, 425), such as "Note that timing resolution is not significantly affected by beam energy due to our method of estimating the arrival time." [SAC main.tex:425] He says how a point was obtained in the caption as well as in the text (SAC lines 334 and 330, 289 and 284, 417 and 413).

- "Simulation of the charge distribution expected for each PMT for a given deposited energy. R13478UV (red) and R9880U-110 (green) PMTs are compared." [SAC main.tex:231]
- "Expected PADME sensitivity for 6 months and 2 years of data-taking. The dark photon mass range is constrained by the positron beam energy at LNF, 550 MeV." [PROC main.tex:182]

**When not to apply.** A final result plot with several overlaid elements may need four or five sentences, one per element (IDM: 92 words for the exclusion plot). In a polish, if a caption is still above 50 words or three sentences after the explanation has moved out, leave it and report its length. Propose to the authors, in this order, what could go: a key that repeats a complete legend; the finding that the text states with the same numbers. Carry out neither. Never drop a sentence that you take out of a caption: place it in the text after the pointer, and list the move in the report.

**Before.** Time resolution versus overvoltage. We first subtracted the pedestal, then we fitted the rising edge of each pulse and took the time at half height. The resolution of the reference detector, 12 ps, was subtracted in quadrature. One can see that the resolution improves and then saturates.

**After.** Time resolution as a function of overvoltage for 4 GeV electrons. The arrival time is taken at half height of a fit to the rising edge of each pulse. The 12 ps resolution of the reference detector is subtracted in quadrature. (The pedestal subtraction and the reading of the curve go into the text.)

### FIG-7. Keep a finding that the caption has; do not add one

**Rule.** Keep a finding that the draft's caption already states, in one sober sentence, with the same statement and the same numbers as the text; do not reorder the draft's clauses to make the two identical. In a polish, do not add one. When you draft, a plot that backs a requirement or a headline number may close on one sentence that gives the number and what it meets; aim for at most two captions in five. For every other plot, close on how the points were made or on the cause of a visible feature. Never close on praise.

**Why.** Many readers read only the abstract and the captions. One sentence on the few result plots gives them the result. A verdict on every plot would turn the captions into a second results section.

**Evidence.** This habit differs by venue, so apply it with care. In SAC 8 of 20 captions state a finding (lines 173, 205, 250, 259, 278, 379, 395, 425); five of them are on design, simulation or literature plots, three have two finding sentences, and one rounds the 81 ps of the text to "roughly 80 ps" (line 425). In the thesis about a quarter do (23% by the keyword heuristic, 42 of the 160 captions read in detail). In PROC none does. In IDM, ETA and SCOUT none states a verdict by reading (4.5% by the heuristic); there the last sentence is a reading aid in 71% of captions. For a short methods paper by a few authors SAC shows the form and the upper end: two captions in five.

- "The fit yields a resolution of roughly 10% at 550 MeV, which meets PADME's requirements." [SAC main.tex:395]
- "The distribution shifts to the right and broadens with increasing length." [SAC main.tex:278]
- "GMs perform better than dSA muons, with roughly 3 times better resolution." [THESIS paper.txt:8300]
- CMS, a cause and not a verdict: "The sensitivity is higher in the region near m1 ≈ 30 GeV or mA′ ≈ 90 GeV because of the A′ mixing with the Z boson in that mass range." [IDM main.tex:201]

**When not to apply.** Sketches, layouts, photographs, sample traces and intermediate plots get no finding. If the venue or a co-author follows collaboration style, drop the finding sentence and keep the cause.

**Before.** Time resolution versus overvoltage. The detector performs extremely well and clearly outperforms the requirement, which opens the way to large timing layers.

**After.** Time resolution as a function of overvoltage for 4 GeV electrons. The resolution of 38 ps at 5 V meets the 50 ps requirement.

### FIG-8. Use the same name for the plotted quantity in the pointer and in the caption

**Rule.** Choose one noun phrase for what a figure shows. Use it in the pointing sentence and as the opening of the caption. Give parallel figures parallel captions that differ only in the words that changed.

**Why.** The reader matches text and figure by the name. Two names for one quantity suggest two quantities.

**Evidence.** All six documents. The pointer and the caption share the head noun phrase for 6 of 7 floats in PROC and 17 of 20 in SAC, by a hand count; IDM repeats it word for word. In the thesis Figures 9.12 to 9.19 share one caption that differs in the region and in "except for" against "including".

- Text: "A sample digitized trace, with two electron peaks and thresholds identified, is shown in Fig. 12." [SAC main.tex:354] Caption: "Sample digitized trace with two electron peaks." [SAC main.tex:358]
- Text: "Fig. 15 shows the achieved energy resolution as a function of deposited energy on the crystal." [SAC main.tex:391] Caption: "SAC energy resolution as a function of deposited energy." [SAC main.tex:395]

**When not to apply.** The pointer may add what the caption omits (range, selection), and the caption may add the key. Only the name must agree.

**Before.** Text: Figure 5 shows the timing performance versus bias. Caption: Resolution as a function of overvoltage.

**After.** Text: Figure 5 shows the time resolution as a function of overvoltage. Caption: Time resolution as a function of overvoltage for 4 GeV electrons.

### FIG-9. Put the pointer where the figure is first needed, and cite each float once where it is introduced

**Rule.** Open the paragraph with the pointer when the paragraph discusses the figure. Close the paragraph with the pointer when the paragraph describes a procedure or an object and the figure is its product. Otherwise put it inside the paragraph, before the first statement that is read from the figure. Cite every float by number, in numerical order.

**Why.** The reader meets the figure where the text first needs it. At the edge of a paragraph the pointer is also easy to find again when the reader comes back from the figure.

**Evidence.** Usual in his own voice. Of the 27 floats of PROC and SAC, 20 are introduced at a paragraph edge (10 open a paragraph, 8 close one, 2 are a paragraph of one sentence). In SAC 7 of the 9 sentences with a float as subject open a paragraph, and 6 of its 20 floats are first cited in the middle of a paragraph (lines 169, 177, 254, 282, 364, 421); in PROC 4 of 7 pointers close one, with the description of the figure before them. The CMS letters have paragraphs of six to eight sentences, and there the pointer stands where the discussion of the figure begins (10 of 16 mentions in IDM and ETA are mid-paragraph). Every float is cited in the text, in numerical order, in PROC, SAC, IDM and ETA (40 of 40).

- Opens the paragraph: "Fig. 14 shows the collected charge as a function of deposited energy." [SAC main.tex:383]
- Closes the paragraph on the calorimeter: "Fig. 3 shows a schematic diagram of the ECAL." [PROC main.tex:86]
- Closes the paragraph on one uncertainty: "The uncertainties are reported in Table 11.5." [THESIS paper.txt:14884]

**When not to apply.** In a letter with long paragraphs keep the pointer inside the paragraph, as its own sentence, at the point where the figure is first needed.

**Before.** Data were taken at three overvoltages, and the resolution (Fig. 5) was extracted at each one, after which we checked the stability of the reference detector.

**After.** Data were taken at three overvoltages between 2 V and 5 V. The time resolution at each setting is shown in Fig. 5.

### FIG-10. Treat a table like a figure, and keep its caption shorter

**Rule.** Introduce a table with "Table N lists / summarizes / contrasts X." or "X are reported in Table N.". Open the caption with "Comparison of", "Summary of", "List of", "Definition of" or the quantity. One sentence is enough when the column heads are clear. Always write "Table" in full.

**Why.** A table is evidence like a plot. The reader needs to know what it holds and which entry matters.

**Evidence.** The five documents that have tables; PROC has none. The table is the subject in 12 of 31 mentions in OWN and 6 of 27 in CMS. Verbs: lists, shows, summarizes, reports, contrasts. In chapters 9 to 12 of the thesis 14 of 24 table captions are one sentence. The CMS letters write long table captions with notes on rows and columns (61 and 78 words in IDM, 87 in ETA). "Tab." occurs nowhere.

- "Table 1 contrasts some PbF2 and SF57 properties which are relevant for Cherenkov-based calorimetry." [SAC main.tex:177] Caption: "Comparison between PbF2 and SF57 of some properties relevant to Cherenkov calorimetry." [SAC main.tex:181]
- "Summary of systematic uncertainties in the analysis (in percent)." [THESIS paper.txt:14959]

**When not to apply.** Add a caption sentence for a row or column that needs a note, as ETA does: "The last column reports the fraction of selected events accepted by each path." [ETA main.tex:117]. IDM brings in its two tables inside parentheses: "(with a yearly breakdown shown in Table 2)" [IDM main.tex:157]. Accept that only for supporting detail in a letter short of space.

**Before.** The systematic uncertainties can be found in the table below.

**After.** Table 2 lists the systematic uncertainties in the time resolution. The resolution of the reference detector is the dominant source. Caption: Summary of systematic uncertainties in the time resolution (in ps).

### FIG-11. Know what each figure is for

**Rule.** Check that each figure has one of these jobs, and let the pointer or the caption say which: a sketch or layout of the setup or the procedure; one representative example of the raw material; a comparison of two things in one frame; a requirement plot that shows a quantity against the value it must meet. Call an example "representative" or "sample" when it is one case of many.

**Why.** A reader who knows the job of a figure knows how to read it. An example is not a result.

**Evidence.** As far as the texts show. The first float is a layout, a sketch or a diagram in all five papers, and method chapters of the thesis open with one. "Comparison of" or "between" is the most frequent caption opening in OWN (8.3%) and the second in CMS (9.0%). Two SAC captions and seven thesis captions (Figures 9.2 to 9.8) state the requirement or the chosen threshold. Examples are flagged as such in SAC, IDM, SCOUT and THESIS.

- "Sketch of the optimization procedure with the N-1 method." [THESIS paper.txt:8779]
- "A representative example, for 300 MeV electrons, is shown in Fig. 13." [SAC main.tex:364]

**When not to apply.** Polishing cannot add a figure. If a draft has no sketch of the method, note it for the authors.

**Before.** Figure 3 shows a waveform.

**After.** A representative waveform, for a 4 GeV electron at an overvoltage of 5 V, is shown in Fig. 3.

### FIG-12. Follow the venue for "Fig." and "Figure"

**Rule.** In a Physical Review paper write "Figure N" at the start of a sentence and "Fig. N" inside it, "Figs. N and M" for two, and "Table N" always in full. Change only the word, never the construction.

**Why.** The abbreviation is house style and carries no meaning. A sentence that starts with an abbreviation reads as a slip in most journals.

**Evidence.** The habit is the venue's, not his. PROC and SAC have "Fig." everywhere, also at the start of a sentence (4 and 8 sentences). The thesis has "Figure" everywhere (81 at the start, 93 inside). The CMS papers have "Figure" at the start (35) and "Fig." inside (57). "Table" is in full in all 58 mentions.

- "A layout of the ECAL is shown in Figure 6.9." [THESIS paper.txt:5345]
- "The results are reported in Fig. 5." [ETA main.tex:212]

**When not to apply.** If the journal's own guide says otherwise, the guide wins.

**Before.** Fig. 5 shows the time resolution, and the uncertainties are given in Tab. 2 and in Figure 6.

**After.** Figure 5 shows the time resolution. The uncertainties are given in Table 2 and in Fig. 6.

## Caption templates

Fill the slots and delete what does not apply. Square brackets mark optional parts.

- **Performance plot.** `<Quantity> as a function of <variable> for <sample or condition>[, as determined from <method or simulation>]. [Each point is <how obtained>.] [The <element> indicates <meaning>.] [<What is not shown, or how the plot is limited>.] [The <quantity> of roughly <number> meets <requirement>.]`
- **Comparison plot.** `<Quantity> for <A> (<key>) and <B> (<key>)[, as a function of <variable>]. [<Secondary element> is also shown for comparison.] [<Presentation choice>.]`
- **Distribution.** `<Quantity> distribution for <sample>[, after <selection>]. [The <fit or overlay> (<key>) is <how obtained>.]`
- **Multi-panel figure.** `<Quantity A> (left) and <quantity B> (right) for <sample>.` or `<Common title>. Left: <A>; right: <B>.`
- **Sketch or layout.** `Sketch of <procedure>.` or `Schematic layout of <setup>. [<One or two sentences that follow the data flow>.]`
- **Representative example.** `Sample <object> for <condition>. [<Which quantities it defines>.]`
- **Table.** `Summary of / Comparison of / List of <content>[ (in <unit>)]. [<Note on one row or column>.]`
- **Pointer in the text.** `Figure N shows <the same quantity> as a function of <variable>.` or `<The same quantity> is shown in Fig. N.` Then: how obtained; what to see; one number; why; what it decides.

## Measured targets

| Measure | OWN | SAC | CMS | Aim for | Reason |
|---|---|---|---|---|---|
| Float mentions per 1,000 words of running text | 4.8 | 5.6 | 2.8 | 3 to 6 | Each float is introduced once and named again where its number is used. |
| Float as subject, share of mentions | 47% | 31% | 44% | 30 to 50% | "Fig. N shows X" is the standard pointer. |
| "X is shown in Fig. N" and its variants, share of mentions | 36% | 41% | 41% | 35 to 45% | The plotted thing is the subject. |
| "see Fig. N" outside parentheses; the tag "as can be seen" | 0 | 0 | 0 | 0 | He writes neither; "X can be seen in Fig. N" is his. |
| Trailing ", as shown in Fig. N" | 2 of 212 | 0 | 12 of 119 | 0 or 1 | For a diagram only, never for evidence. |
| "(see Fig. N)" in parentheses | 2 of 212 | 2 | 0 | 0 or 1 | For a second mention only. |
| Words in the pointing sentence, median | 13 (PROC, SAC) | 13 | about 25 | 10 to 20 | The pointer names the plot; the reading follows. |
| Caption words and sentences, median | 37 and 2 | 42 and 2 | 50 and 3 | 25 to 50 words, 1 to 3 sentences; none above 100 words | A title phrase plus one or two jobs. |
| Captions of four or more sentences | 13% | 25% | 32% | at most a quarter | For a result plot with several elements, or a caveat needed to read the plot. |
| Caption opens with a bare noun phrase | 98% | 100% by reading (90% by the script) | 72% | 100% | The article is collaboration style. |
| Caption names a color or line style | 22% | 35% | 53% | each plot with two or more series and no full legend | Keys in parentheses after the item. |
| Caption states a finding | 22% | 8 of 20 by reading (30% by the script, which tests the last sentence only) | 4.5% | at most 2 captions in 5; never added in a polish | SAC is the measured upper end. |

"Aim for" applies to a short methods paper by a few authors. In the SAC column, the two captions that the script files under "opens with a symbol" start with the crystal's name, which is a noun phrase. The full set of targets is Table B of `voice-and-transfer.md`.

## Do not copy

**Slips.**

- "Fig." at the start of a sentence (PROC, SAC).
- Panels listed against the reading order: "for data (right) and MC (left)" [PROC main.tex:136]. Go left to right and top to bottom.
- A pointer with no reading after it (5 of 7 in PROC).
- Missing or stray words in captions: "Missing mass spectrum PADME backgrounds" [PROC main.tex:113]; "front the back" [THESIS paper.txt:16209].
- The six-sentence, 97-word caption of the linearity figure in SAC (line 379): do not draft one of that length. A caption of that kind in a draft stays, and its length is reported.

**CMS boilerplate.**

- A leading "The" in captions: "The total efficiencies for the four-muon" [ETA main.tex:246].
- The source line of the review: "Figure taken from Ref." [SCOUT main.tex:687].
- Limit-plot formulas outside a limit plot: "Solid (dashed) curves denote the observed (expected) exclusion limits" [IDM main.tex:201].
- Table captions of 60 to 90 words that explain every column.
- "as shown in Fig. N" as a routine tag (SCOUT).

**Thesis-only habits.**

- "Figure" in full inside a sentence.
- A region tag in parentheses before the caption title, "(nJets)" or "(Barrel, 2018)" (33 captions).
- Evaluative words in captions of the literature chapters ("striking", "compelling", "remarkably well"), and the verdict "The agreement is remarkable." [THESIS paper.txt:1672] in the text.
- Image credits in captions, "pads" for panels, "statistics" for sample size.
- One figure for every requirement, and eight near-identical figures in a row. A paper shows one representative case.

## Checklist

1. Is every figure and table cited by number in the text, in numerical order?
2. Does each float have a pointing sentence of its own, "Figure N shows X" or "X is shown in Fig. N", with the thing drawn as the object and no "that" clause?
3. Is the text free of "see Fig. N" outside parentheses, the tag "as can be seen", "As shown in Fig. N," and "Tab."?
4. Do one to four sentences after the pointer say how to read the plot, what to look at, one number, and what it means?
5. Does the pointer stand where the figure is first needed: at the start or the end of its paragraph, or before the first statement that is read from the figure?
6. Does every caption open with a noun phrase without article and without finite verb, closed by a period?
7. Does the opening give the quantity, then the axis variable, then the condition, then the origin of the numbers, and are scaled curves, cut ranges, overflow bins and the meaning of error bars declared?
8. Are colors, line styles and panel positions in parentheses right after the item they label?
9. Is each caption without "we", and does it keep its limits, its definitions and how its points were obtained? Is the length of each caption above 50 words or three sentences reported?
10. Was no finding added to a caption, and does each finding that a caption has agree with the text in statement and numbers?
11. Do the pointer and the caption use the same name for the plotted quantity, and do parallel figures have parallel captions?
12. Is each table introduced like a figure, with a short noun-phrase caption?
13. Is it "Figure" at the start of a sentence, "Fig." inside, and "Table" in full?
