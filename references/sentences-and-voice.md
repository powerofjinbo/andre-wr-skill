# Sentences, voice and tense

> **When to read this file.** Read it when you draft or revise single sentences: their subject, voice, tense, length and punctuation, and the way purpose, reason and consequence are attached.
> It holds fifteen habits (SENT-1 to SENT-15) with their evidence, quotes, limits and before/after pairs, then the measured targets, the things not to copy and a checklist.
> Use it after the paragraphs are in shape (`paragraphs-and-flow.md`); for word choice go on to `words-and-phrases.md`.

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

**Reading the evidence.** Percentages are shares of sentences unless a unit is given. The numbers come from the measurements in `corpus-and-measurements.md` and from searches over the same sentence segmentation.

**Contents.**

- SENT-1. Make the thing the subject
- SENT-2. Keep "we" for decisions, studies and claims
- SENT-3. Keep the passive for operations on data
- SENT-4. Aim for 20 words and mix the lengths
- SENT-5. Let the tense follow the kind of statement
- SENT-6. Put the purpose first: "To <purpose>, <object> is ..."
- SENT-7. Give the reason in the same sentence
- SENT-8. Follow a statement with a "This + verb" sentence
- SENT-9. Attach a short consequence as a tail
- SENT-10. Put a trade-off in one sentence
- SENT-11. Announce the count, then list after a colon
- SENT-12. Use parentheses for specifications and glosses; keep dashes and semicolons rare
- SENT-13. Use commas lightly
- SENT-14. Edit lightly
- SENT-15. Lead a result with its evidence
- Measured targets; Do not copy; Checklist

**Summary.**

1. A sentence of his runs about 20 words. Short sentences carry verdicts, steps and pointers. The few long ones carry a list or a definition.
2. The subject is the thing described: the detector, the method, the fit, a figure. "We" marks what the authors decided, studied, ran or claim. What was done to the recorded data is passive.
3. Tense follows the kind of statement: present for what a thing is, does or shows, simple past for what was done once, present perfect to sum up.
4. Purpose, reason and consequence sit inside the sentence they belong to: "To ..., X is ...", "since" and "due to", a trailing ", which ..." or participle, or a "This + verb" sentence right after.
5. Punctuation is light: parentheses for specifications and glosses, a colon before an announced list, few semicolons, a dash once in a paper at most, few commas.

## Habits

### SENT-1. Make the thing the subject

**Rule.** Start the sentence with the thing being described (the detector, the algorithm, the sample, the fit, the figure) and give it an active verb when it has one.

**Why.** The first words tell the reader what the sentence is about. The authors do not stand between the reader and the object of the paper.

**Evidence.** 6 of 6, always, his own, kept under CMS editing. "The" opens 31% of OWN sentences and 40% in CMS. A figure or table is the subject in 47% of the float mentions in OWN and 44% in CMS. The voice mix:

| Sentences with | PROC | SAC | THESIS | IDM | ETA | SCOUT |
|---|---|---|---|---|---|---|
| "we" or "I" | 3% | 19% | 7% | 6% | 5% | 2% |
| a passive | 37% | 43% | 40% | 56% | 53% | 52% |
| neither | 60% | 41% | 54% | 39% | 43% | 46% |

"Neither" is a thing as subject with an active or linking verb. It never falls below 39%.

- "The fast performance of the SAC allows the individual identification of Bremsstrahlung photons, despite the large rate" [PROC main.tex:104]
- "Smaller electromagnetic showers reduce the detector occupancy, thus enhancing its rate capabilities." [SAC main.tex:177]
- "The jet pT requirement removes low-momentum jets produced in pileup interactions." [IDM main.tex:95]

**When not to apply.** The authors made a choice or a claim (SENT-2). Do not trade "we" for an abstract noun ("The usage of X enables ..."); name the concrete thing.

**Before.** We use a constant-fraction discriminator to reduce the dependence of the arrival time on the pulse amplitude.

**After.** A constant-fraction discriminator reduces the dependence of the arrival time on the pulse amplitude.

### SENT-2. Keep "we" for decisions, studies and claims

**Rule.** Write "we" where the authors chose, assumed, studied, estimated, found or concluded something, and for the steps of a study or a simulation that they designed and ran. Do not use it to narrate operations on recorded data.

**Why.** The reader can tell statements that rest on the authors' judgment from statements about how things are. A "we" on every sentence carries no such signal.

**Evidence.** The pattern holds in 6 of 6; the rate depends on the venue (table above). "We" opens 7.7% of SAC sentences, 1.9% in OWN, 0.5% in CMS. Verbs after "we" in SAC: simulate, find, describe, consider, estimate, adapt, measure, evaluate, demonstrate, conclude, predict, recommend. In IDM: present, probe, focus, select, require, divide, choose, assess. In ETA: report, study, conclude, define, assume, estimate. "We observe" occurs in none of the six. Of the 42 "we" sentences in the body of SAC, 11 narrate a step of a simulation or of a plot (lines 217, 241, 243, 254, 272, 299, 383, 431), as in "We run 100 events per crystal length." [SAC main.tex:272] The two SAC sections on operations on recorded waveforms (charge reconstruction, timing resolution) have no "we". No document lies between 6% and 19%: the share follows the genre. The SAC abstract has three "we"; CMS abstracts have none. "I" occurs only in the thesis, for signposts.

- "We therefore instrument the walls of the magnet with plastic scintillators to identify these lower-energy positrons" [PROC main.tex:102]
- "From these considerations, we conclude the larger Hamamatsu R13478UV PMT, coupled to PbF2 crystals, is the best solution for PADME's requirements." [SAC main.tex:236]
- "We choose a grid of bin boundaries centered around the optimal bins in each match category, for a total of 31 tests." [IDM main.tex:134]

**When not to apply.** Do not remove every "we": a paper by a few authors that reports their own studies may have "we" in up to about one sentence in five, as SAC has (19%), with "We" opening up to about 8%, and the CMS rate is house style. Reduce "we" only above that, first in passages on operations on recorded data, and never to reach a number. Do not write "the authors" or "this work" as the agent.

**Before.** We then fit each pulse with a template, and we take the crossing time of the fitted pulse as the arrival time. A resolution of 38 ps is found.

**After.** Each pulse is then fit with a template, and the crossing time of the fitted pulse is taken as the arrival time. We find a resolution of 38 ps.

### SENT-3. Keep the passive for operations on data

**Rule.** Describe what was done to the data or the device in the passive, with the means after "by" or "using". Do not turn passives into actives for their own sake.

**Why.** In a procedure the reader follows the object (the pulse, the event, the track) from step to step. The actor is always the same and carries no information.

**Evidence.** 6 of 6, always. A passive is in 37 to 43% of sentences in his own documents and 52% in CMS. The means follows as "by" + -ing in 3 to 6% of sentences in five documents; PROC fronts it instead ("By <verb>ing ..., X can be ...", twice).

- "The timing resolution was determined by extracting the sigmas of a Gaussian fit to each such distribution." [SAC main.tex:421]
- "A cosmic ray muon veto is implemented by discarding events containing at least one pair of back-to-back DSA muons." [IDM main.tex:118]
- "The signal region is defined by applying all selection groups in succession." [THESIS paper.txt:8737]

**When not to apply.** The step was a choice that needs an owner (SENT-2). The subject would run past 15 words before the verb arrives.

**Before.** We select events with exactly one beam particle by requiring a single pulse in the trigger counter. We then compute the time difference between the two channels.

**After.** Events with exactly one beam particle are selected by requiring a single pulse in the trigger counter. The time difference between the two channels is then computed for each event.

### SENT-4. Aim for 20 words and mix the lengths

**Rule.** Keep the median near 20 words. Let about one sentence in six have 12 words or fewer and one in six more than 30. Go past 40 only for a list or a definition.

**Why.** Short sentences hold the verdicts, pointers and steps, so the reader finds them. A long sentence that is a list can be scanned. Uniform 25-word sentences hide the result.

**Evidence.** The mix holds in 6 of 6; the length is his own. Median 19, 20, 20 words in PROC, SAC, THESIS; 23, 22, 24 in IDM, ETA, SCOUT. Twelve words or fewer: 17% in OWN, 9% in CMS. Above 30 words: 15% and 25%. Above 40: 3.5% and 7.9%. Of the 203 OWN sentences with 10 words or fewer, 38% close a paragraph, 37% sit inside one, 22% open one. The longest SAC sentence (92 words) is the list of requirements (a) to (f). Of the 8 sentences above 40 words in the body of SAC, 6 are a list or a definition. A run of short declaratives is his form for a list of facts or for a chain of cause and effect, one link per sentence: "Increasing the length causes more Cherenkov photons to be lost along the way. At the same time, in a longer crystal photons have longer travel paths. Consequently, there is more opportunity for scattering, which broadens the arrival time profile of photons." [SAC main.tex:293] Two short sentences together occur in SAC; three sentences of 12 words or fewer in a row inside a paragraph do not.

- "We run 100 events per crystal length." [SAC main.tex:272]
- "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]
- "The muon pair with the smallest χ² value is chosen." [IDM main.tex:119]
- "We found zero events surviving the event selection." [THESIS paper.txt:9988]

**When not to apply.** Do not chop a list or a sentence into fragments: his 10th percentile is 11 words. Join two short sentences only when the draft as a whole is below his range and one of the two has no fact of its own. The CMS length is not the target.

**Before.** After applying the time-walk correction, which is derived from the correlation between the measured time and the pulse amplitude, we obtain a time resolution of 38 ps at an overvoltage of 5 V, which is better than the design requirement of 50 ps.

**After.** The time-walk correction is derived from the correlation between the measured time and the pulse amplitude. After the correction, the time resolution is 38 ps at an overvoltage of 5 V, which meets the 50 ps requirement.

### SENT-5. Let the tense follow the kind of statement

**Rule.** Use the present for what the device or method is and does, what a figure shows and what a result is. Use the simple past for what was done once: a test beam, a generated sample, a check. Use the present perfect to sum up in the conclusions and for the state of the field. Keep "will" for expectations and outlook.

**Why.** The tense tells the reader whether a statement is a standing property or a single action. A method described in the past reads as history.

**Evidence.** 6 of 6, always. Sentences with "was" or "were": 17.5% in SAC, 1.5% in PROC, 2% in THESIS outside the reprinted chapter, 1.5% in IDM (two completed checks), 6% in ETA, 12% in SCOUT (history sections). The summaries of SAC, IDM and SCOUT open in the present perfect. Word counts by section type in SAC:

| Section type | "we" | is/are | was/were | Reading |
|---|---|---|---|---|
| Introduction, detector (Sections 1 and 2) | 5 | 14 | 0 | present; "we" states the purpose |
| Design choices (Section 3) | 7 | 15 | 3 | "we considered", "we conclude" |
| Simulation (Sections 4, 5 and 6.1) | 17 | 31 | 11 | past for what was built and run, present for what it contains |
| Test-beam setup (Section 6) | 1 | 10 | 6 | present for the facility, past for the test |
| Reconstruction, timing (Sections 7 and 8.3) | 0 | 8 | 20 | past passive, no "we" |
| Results read from figures (rest of Section 8) | 11 | 24 | 5 | present; "we find", "we estimate" |
| Conclusions | 3 | 2 | 0 | present perfect |

- "We developed a full Monte Carlo (MC) simulation of the PADME detector with the Geant4 framework to study different aspects of the experiment." [SAC main.tex:241]
- "In the second, we directly simulate high-energy photons incident on the crystals." [SAC main.tex:241]
- "About 99% of four-muon combinations passed this selection in the signal mass window, compared to only 84% in the sideband." [ETA main.tex:198]

**When not to apply.** The share of past tense depends on content: high for a measurement campaign (SAC), near zero for an algorithm (IDM). Do not narrate the history of the development. He is not strict: in SAC a simulation run is often in the present ("we simulate", "We run 100 events per crystal length.") and a fitted value in the past ("was found to be 81 ps"), so do not change a tense that the draft uses consistently.

**Before.** The detector consisted of a scintillator tile read out by two silicon photomultipliers. Figure 4 showed the time difference between the two channels. We have recorded two million events in the test beam.

**After.** The detector consists of a scintillator tile read out by two silicon photomultipliers. Figure 4 shows the time difference between the two channels. Two million events were recorded in the test beam.

### SENT-6. Put the purpose first: "To <purpose>, <object> is ..."

**Rule.** When a step exists for a reason, open with the purpose as a "To" infinitive and follow with the step. Make the main clause passive or thing-led for a step; use "we" when the purpose leads to a study.

**Why.** The reader learns why before what, so the step needs no justification later.

**Evidence.** 6 of 6, usual. "To" opens 1.5% of sentences in PROC, 2.1% in SAC, 4.5% in IDM, 4.1% in ETA, 1.3% in SCOUT, 1.4% in THESIS. The main clause has "we" in 3 of 5 cases in SAC, 0 of 6 in IDM, 1 of 4 in ETA, 1 of 19 in SCOUT, 6 of 24 in THESIS. "In order to" is his own (8 in SAC, 7 of them inside the sentence; none in PROC, IDM, ETA). A trailing "in order to" is as much his as the fronted "To": the fronted form is more frequent in the two CMS letters than in his own texts.

- "To prevent these soft photons from impacting the hard photon energy measurements, the ECAL is built with a central square hole to let the Bremsstrahlung photons pass through." [PROC main.tex:100]
- "To maximize sensitivity, different variables are used in each match category." [IDM main.tex:131]
- "To further reduce these backgrounds, the long-lived nature of the dimuon pair is exploited." [THESIS paper.txt:4856]

**When not to apply.** About one sentence in 25 already opens this way, or the previous sentence does. The purpose is obvious.

**Before.** The two channels are read out by the same digitizer board. This is done so that clock jitter between boards does not enter the time difference.

**After.** To keep clock jitter between boards out of the time difference, the two channels are read out by the same digitizer board.

### SENT-7. Give the reason in the same sentence

**Rule.** Attach the reason to the fact or the choice with "since" or "because" plus a clause, or "due to" plus a noun phrase. Put the reason first, with "Since", when it is the constraint that forces the step.

**Why.** A choice with its reason attached does not look arbitrary, and the reader does not wait for a later paragraph to learn why.

**Evidence.** 6 of 6, usual. A reason marker (since, because, due to, owing to, given that, causal "as") is in 8% of OWN sentences, 6% in SAC, 5% in CMS. The word depends on who edits. OWN, per 10,000 words: since 18 (causal uses), due to 12, because 8. CMS: because 9 (6 of them "because of"), since 3 (causal uses; 6.5 with the temporal ones), due to 2.5. SAC has 9 "due to" and no "because"; ETA has no "due to" and 2 "owing to". So "since" and "due to" are his; in SAC "due to" is three times as frequent as "since". "Because of" is the form the CMS papers prefer (6.0 against 2.5 per 10,000 words; 11 uses in the thesis, none in PROC and SAC), and "owing to" is rare in both voices (4 in the thesis, 2 in ETA). ", so" is rare in the papers (3 in SAC with "and so", 1 in IDM) and belongs to the thesis (about 20).

- "Since only one PbF2 crystal was available for testing, we adapted our dedicated MC simulation to characterize the average energy leakage and provide a correction factor to light yield and energy resolution measurements." [SAC main.tex:326]
- "The overall efficiency to correctly assign muon charges is greater than 97% because of the low-energy spectrum of IDM muons." [IDM main.tex:119]
- "Events with b-tagged jets are rejected, since heavy flavor processes do not contribute to the expected iDM signature." [THESIS paper.txt:8445]

**When not to apply.** The reason is common knowledge. Three reasons would chain in one sentence. "As" could be read as "while". If the journal bans "due to" in this use, follow the journal.

**Before.** The tile is wrapped in reflective foil. The reason is that a bare tile loses a large part of the scintillation light at its edges.

**After.** The tile is wrapped in reflective foil, since a bare tile loses a large part of the scintillation light at its edges.

### SENT-8. Follow a statement with a "This + verb" sentence

**Rule.** After a statement of design or procedure, add a sentence that starts with "This" and says what the statement buys, causes or means. Add a noun ("This requirement") when "This" could point at two things. After a sentence of 12 words or fewer, attach the consequence as a tail instead (SENT-9).

**Why.** Fact and consequence each get a sentence of their own, and the consequence arrives while the fact is still in mind.

**Evidence.** "This" opens 9.7% of OWN sentences (6.8% in SAC) and 5.2% in CMS: 6 of 6. The verb follows at once in 48% of these in OWN (9 of 16 in SAC) and 22% in CMS. "This is" occurs 13 times per 10,000 words in OWN and 2.5 in CMS. So the bare "This + verb" is his own, strong; CMS editing tends to add the noun. His verbs: is, leads to, ensures, allows, motivates, makes, overestimates. The "This + verb" sentence is not a short one: the nine in SAC have 12 to 29 words (median 22), and the sentence before each has 16 to 32. The other 7 of the 16 "This" openers in SAC carry a noun ("This procedure", "This ratio").

- "This leads to a large unexpected deposition of energy in the ECAL." [PROC main.tex:134]
- "This overestimates the total charge and introduces a bias in the linearity." [SAC main.tex:387]
- "This is due to the smaller lever arm and lack of tracker information." [IDM main.tex:121]
- "This ensures a pure sample of muons arriving in the outer muon chambers." [THESIS paper.txt:5219]

**When not to apply.** More than about one sentence in ten, two in a row, or at the start of a paragraph, where "This" has nothing to point at.

**Before.** The discriminator threshold is set at 20% of the pulse amplitude and not at a fixed voltage as in the earlier measurements, which has the effect of making the arrival time independent of the amplitude to first order, and the residual dependence is removed offline.

**After.** The discriminator threshold is set at 20% of the pulse amplitude and not at a fixed voltage as in the earlier measurements. This makes the arrival time independent of the amplitude to first order, and the residual dependence is removed offline.

### SENT-9. Attach a short consequence as a tail

**Rule.** When the consequence or the verdict is short, attach it to the end of the sentence with ", which" plus a verb, or with a comma and a participle (", thus improving ...", ", leading to ..."). Use one tail per sentence.

**Why.** The result and what it means arrive together, and no connector is needed to join two sentences.

**Evidence.** 6 of 6, usual, in his own and the CMS texts. ", which" is in 7.3% of SAC sentences and between 3% (PROC) and 10% (IDM) elsewhere. A comma plus an -ing word is in 9.4% of SAC sentences and between 4.4% (THESIS) and 16% (ETA) elsewhere. Both tails share a sentence in 2 of 2097 OWN sentences. Consequence words also sit inside the clause: "and hence", "and thus", "and therefore" occur 30 times in OWN and 19 in CMS.

- "The PbF2 resolution was found to be 81 ps, which comfortably meets the 200 ps timing requirement for a successful SAC performance." [SAC main.tex:421]
- "The ECAL is placed roughly 3 m downstream from the target, and thus has an angular acceptance between 20 and 95 mrad." [PROC main.tex:86]
- "Pixels where the collected charge does not meet this threshold are zero-suppressed, saving bandwidth and processing time." [THESIS paper.txt:6562]

**When not to apply.** The consequence is the main point of the paragraph; give it its own sentence (SENT-8). The "which" could attach to two nouns. The sentence already has a tail.

**Before.** The two channels share one clock. As a result, the clock jitter cancels in the time difference.

**After.** The two channels share one clock, which cancels the clock jitter in the time difference.

### SENT-10. Put a trade-off in one sentence

**Rule.** State a gain and its cost, or two contrasted cases, in one sentence joined by "but" or ", while". Open with "While" only when the first clause is a concession.

**Why.** The reader sees both sides at once. A separate "However" sentence gives the cost more weight than a clause does.

**Evidence.** "but" occurs 14, 21, 14 and 17 times per 10,000 words in SAC, IDM, ETA, THESIS, 6 in SCOUT, never in PROC: 5 of 6, usual. ", while" joins two clauses in 6 of 6. Sentence-initial "While" is occasional: THESIS 10, SCOUT 7, none elsewhere. "However" opens 1.1% of OWN sentences and 0.5% in CMS.

- "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost." [SAC main.tex:211]
- "The DSA muons have higher reconstruction efficiencies but degraded momentum resolution and impact parameter resolution compared to muons reconstructed with the standard algorithm." [IDM main.tex:121]
- "While the dSA reconstruction efficiency is higher than GM at large displacements, its performance is worse in general." [THESIS paper.txt:8240]

**When not to apply.** The cost needs its own number or explanation. Then give it a sentence; in his own voice that sentence often starts with "Nevertheless," (SAC 5, THESIS 10 more outside the reprinted chapter, CMS 1).

**Before.** A thicker tile gives more light. However, a thicker tile also increases the spread of the photon arrival times.

**After.** A thicker tile gives more light but also increases the spread of the photon arrival times.

### SENT-11. Announce the count, then list after a colon

**Rule.** Say how many items follow, put a colon, and give the items in the order in which the text treats them. For a procedure, announce the number of steps in a short sentence and walk through them with "First", "then", "Finally".

**Why.** The reader knows the size of what is coming and can tick the items off.

**Evidence.** 6 of 6, usual. A number word, a plural noun and a colon are in 3.0% of PROC sentences, 2.6% SAC, 2.2% IDM, 1.7% ETA, 1.1% SCOUT, 1.7% THESIS. Colons per 1,000 words: 4.2 in OWN (SAC 2.5), 1.2 in CMS. Of the 13 colons in SAC, 6 introduce a list and 4 an equation. All 6 in IDM follow a complete clause and introduce a list.

- "There are two main sources: the Beryllium window that is used to separate the accelerator vacuum from the detector vacuum, and the magnet that steers the beam from the injection point into the target." [PROC main.tex:134]
- "The total energy deposited in the crystal was reconstructed in three steps." [SAC main.tex:352]
- "Because the variables are independent, all four bins can be described using only three parameters: a normalization rate plus a vertical and a horizontal transfer coefficient." [IDM main.tex:127]

**When not to apply.** The list will not be delivered in that order. The clause before the colon is incomplete ("The dSA identification criteria are:" [THESIS paper.txt:8986] before a bullet list is a thesis form).

**Before.** The time resolution has contributions from photon statistics, as well as from electronic noise, and the clock jitter also contributes.

**After.** Three effects contribute to the time resolution: photon statistics, electronic noise, and clock jitter.

### SENT-12. Use parentheses for specifications and glosses; keep dashes and semicolons rare

**Rule.** Put a specification, a value, an acronym or a short gloss in parentheses right after the noun it belongs to. Use a dash rarely (one construction in a paper at most) and never add one. Use a semicolon between list items that contain commas. Do not address the reader, write no question, no exclamation and no footnote, and do not set a word in bold or italics for emphasis.

**Why.** The main clause still reads when the parentheses are skipped, and each number stays next to its noun.

**Evidence.** 6 of 6, always. Parenthesis pairs per 1,000 words: 10.6 in OWN (12.9 in SAC), 7.9 in CMS. Dashes as punctuation: one pair in PROC (line 102), one dash in SAC (line 136, "the dark matter problem -- the fact that we have abundant evidence for its existence yet few clues about its composition"), none in IDM and ETA, about ten sentences in THESIS; 17 dashes in OWN against 3 in CMS, all in SCOUT. Semicolons are in about 1% of sentences (ETA 1.6%); the five in SAC separate the items (a) to (f), none in PROC, SAC or IDM joins two clauses, and the thesis joins two clauses with one 11 times. "you" occurs in none of the five papers, and the only imperative that opens a sentence is "Note that". The five papers have one footnote between them, a caveat [SAC main.tex:169]. The four short papers have no bold in the running text and italics for emphasis in one sentence, for a contrasted pair [SAC main.tex:406]. "i.e." follows an opening parenthesis in 19 of its 21 uses in OWN. In OWN no comma follows "i.e." or "e.g." (0 of 32); CMS style adds it (29 of 30). "respectively" is half as frequent in OWN (0.55 per 1,000 words, once in SAC) as in CMS (1.0). No document has a question mark, an exclamation mark or a contraction.

- "A R13478UV PMT (voltage: 1600 V) was coupled to a PbF2 crystal using optical grease and then connected to a 12-bit, 5 GSPS, 1024-sample digitizer (model CAEN V1742) for data acquisition." [SAC main.tex:305]
- "First a run-level pedestal was calculated by averaging the ADC counts of each 1000-sample empty event in the run (i.e. only noise, no signal peaks)." [SAC main.tex:352]
- "Several sets of ABCD bins are defined in the VR and the agreement between predicted and observed yields in bin D (the bin with the smallest backgrounds) is confirmed for each set." [IDM main.tex:134]

**When not to apply.** The aside is a full sentence, or parentheses would nest. More than one sentence in five already has one. For the comma after "i.e." and "e.g.", follow the journal.

**Before.** Each photomultiplier, which is a silicon device with an active area of 3 × 3 mm², was operated at a bias voltage of 56 V; this value is 5 V above breakdown.

**After.** Each silicon photomultiplier (active area 3 × 3 mm²) was operated at a bias voltage of 56 V (5 V above breakdown).

### SENT-13. Use commas lightly

**Rule.** Put a comma after a fronted phrase or clause, between the items of a series including before "and", and before a non-restrictive "which". Do not put one before a trailing phrase that starts with "and" plus a verb, "because", "due to" or "in order to". Before a trailing "using" phrase the thesis has no comma and SAC has one in 5 of 10 cases, the purpose sentence among them: leave what the draft has. Keep the comma before a "with" phrase that adds a specification (", with pitch size 55 microns" [PROC main.tex:118]). Before a trailing "since" clause the comma is optional: he omits it in 35 of 56 cases in the thesis.

**Why.** A comma makes the reader look for a clause boundary. Where there is none, the pause costs attention and gives nothing.

**Evidence.** His own, usual: THESIS and his re-edit of SAC. Commas per 1,000 words: 38 in THESIS, 41 in PROC, 47 in SAC, 46 in CMS. When he re-edited SAC alone into thesis chapter 14, he removed 32 commas in 28 sentences (14 before "and", 3 before "using", 3 before "with") and added a few, after a fronted phrase and in a series. The rest of the thesis agrees: trailing "since" has no comma 35 times and one 21 times, "because" 31 to 2, "using" 11 to 1, "due to" 38 to 1. A comma follows a fronted opener in 222 of 242 thesis sentences and 35 of 39 in SAC. A comma before a "with" phrase that adds a specification occurs 29 times in OWN, and his reprint of SAC kept 7 of the 10 in SAC. He writes the serial comma (about 70 lists with it in THESIS, few without; nearly always in CMS). Caveat: the corpus holds the arXiv version of SAC, so some removed commas may be the journal copy editor's.

- "To estimate single-crystal performance, we measured linearity and energy resolution, using only single-electron events, at different incident electron energies." [SAC main.tex:374] became "To estimate single-crystal performance, we measured linearity and energy resolution using only single-electron events at different incident electron energies." [THESIS paper.txt:17184]
- "By varying τ we simulated increasingly overlapping pulses." [SAC main.tex:431] became "By varying τ, we simulated increasingly overlapping pulses." [THESIS paper.txt:17498]

**When not to apply.** Keep the comma before "while", "whereas" and "but" when they join two full clauses (THESIS: ", while" 19, without 11). Keep any comma whose removal lets two nouns run together.

**Before.** The time difference is computed for each event, and filled into a histogram, in order to extract the resolution.

**After.** The time difference is computed for each event and filled into a histogram in order to extract the resolution.

### SENT-14. Edit lightly

**Rule.** Change the fewest words that fix a problem. Leave a sentence alone when it already follows the habits above.

**Why.** His own second pass over his text leaves most sentences untouched. Every rewrite can change a technical statement, and he will edit the text by hand afterwards.

**Evidence.** One comparison: SAC against thesis chapter 14, edited by him alone two years later. Of 215 thesis sentences, 145 are word for word the same. Of the other 70, 27 differ only in commas, 42 by a few words or a number format, and one is new. None is restructured; he dropped the abstract and the first five paragraphs of the introduction. This is a reprint of his own published paper: it shows which small things he changes, not how much a draft by other hands needs. What he changed:

- commas (SENT-13);
- a mid-sentence ", however," deleted ([SAC main.tex:211]);
- restrictive "which" to "that", once;
- "used e.g. in" [SAC main.tex:167] to "used for example in" [THESIS paper.txt:16370];
- "scaled down to order 0.1 pC" [SAC main.tex:352] to "scaled down to roughly 0.1 pC" [THESIS paper.txt:17058];
- "MC" to "simulation" three times, and one acronym expanded at first use;
- one tense: "The primary goal was" [SAC main.tex:268] to "The primary goal is" [THESIS paper.txt:16726];
- two hedges cut from a caption: "should absorb a dose of only" [SAC main.tex:250] to "absorbs a dose of" [THESIS paper.txt:16683];
- self-reference adapted to the thesis ("In this paper" to "Here").

Two sentences before and after his edit:

- "The choice of threshold was made to mitigate the after-pulse ringing which can be seen in the figure." [SAC main.tex:362] became "The choice of threshold was made to mitigate the after-pulse ringing that can be seen in the figure." [THESIS paper.txt:17063]
- "There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282] became "There is a roughly 16% increase when going from 14 cm to 18 cm." [THESIS paper.txt:16818]

**When not to apply.** A sentence breaks several habits at once (a "we" on a routine step, no reason, 45 words). Then rewrite it.

**Before.** We measured the time resolution, using only single-particle events, at three overvoltages.

**After.** We measured the time resolution using only single-particle events at three overvoltages.

**Not.** The time resolution was measured at three overvoltages with single-particle events only. (Nothing called for a change of voice or word order.)

### SENT-15. Lead a result with its evidence

**Rule.** When a number is read off a fit or a figure, name the evidence first: "From <evidence>, we find ..." or "From <evidence>, X was determined to be ...".

**Why.** The reader knows where the number comes from before reading it.

**Evidence.** His own, occasional, 3 of 6: "From" opens 6 sentences in SAC, 1 in PROC, 3 in THESIS outside the reprinted chapter, none in CMS. A second own-voice frame, "There is" or "There are" plus a number, states a trend or an inventory (9 sentences in SAC, 3% of THESIS, none in IDM and ETA).

- "From the slope of the solid fit line in Fig. 14, we find a light yield of 2.05 p.e./MeV." [SAC main.tex:387]
- "From the two-finger distributions, the finger resolution was determined to be 174 ps." [SAC main.tex:421]

**When not to apply.** The evidence is the sentence before; then the bare result is enough. Not more than a few times in a paper.

**Before.** We find a time resolution of 38 ps. This comes from the width of a Gaussian fit to the time-difference distribution.

**After.** From the width of a Gaussian fit to the time-difference distribution, we find a time resolution of 38 ps.

## Measured targets

Shares are percentages of sentences. "Aim for" applies to a short methods paper by a few authors. The full set of targets is Table B of `voice-and-transfer.md`; word rates are in `words-and-phrases.md`.

| Quantity | OWN | SAC | CMS | Aim for | Reason |
|---|---|---|---|---|---|
| Words per sentence, median | 20 | 20 | 24 | 19 to 22 | his papers sit at 19 to 20 |
| Words per sentence, mean | 21.0 | 22.0 | 25.1 | 20 to 23 | same |
| 12 words or fewer | 17% | 14% | 9% | 13 to 18% | verdicts, steps, pointers |
| More than 30 words | 15% | 17.5% | 25% | 13 to 18% | a reason, a list or a definition |
| More than 40 words | 3.5% | 4.3% | 7.9% | 2 to 5%, each a list or a definition | CMS letters pack more per sentence |
| Contain "we" | 6% | 19% | 2.4% | up to 20% | few authors: SAC is the model; no document lies between 6% and 19% |
| Open with "We" | 1.9% | 7.7% | 0.5% | up to 8% | the thing comes first |
| Contain a passive | 40% | 43% | 52% | 35 to 45% | procedure stays passive |
| Neither "we" nor passive | 54% | 41% | 45% | 40 to 55% | thing as subject |
| Open with "This" | 9.7% | 6.8% | 5.2% | 6 to 10%, half "This + verb" | his link between sentences |
| Open with "To" | 1.4% | 2.1% | 1.7% | 2 to 4% | IDM, ETA reach 4.5% |
| Contain ", which" | 4.8% | 7.3% | 7.1% | 5 to 8% | one tail per sentence |
| Contain a comma + -ing tail | 5.1% | 9.4% | 10% | 5 to 10% | same |
| Contain a reason marker | 8% | 6% | 5% | 6 to 9% | reason where the choice is made |
| Colons per 1,000 words | 4.2 | 2.5 | 1.2 | 2 to 4 | announced lists |
| Semicolons per 1,000 words | 0.8 | 1.0 | 0.65 | under 1 | only inside lists |
| Dashes per 1,000 words | 0.5 | 0.2 | 0.07 | at most 0.2 | one construction in a paper; never add one |
| Parenthesis pairs per 1,000 words | 10.6 | 12.9 | 7.9 | 9 to 13 | specifications, glosses |
| Commas per 1,000 words | 39 | 47 | 46 | 38 to 45 | his solo level is 38 |
| "respectively" per 1,000 words | 0.55 | 0.2 | 1.0 | at most 0.5 | the CMS rate is house style |

## Do not copy

Slips of unedited text:

- A second tail on a sentence that has one: "Thus the simulation reveals that increasing the crystal length leads to broader signals and longer tails, affecting the double-peak separation capability, which is a crucial parameter for PADME SAC performance." [SAC main.tex:293]
- A comma between two verbs of one subject: "Its purpose is to monitor the non-interacting beam, and measure the positron momentum distribution." [PROC main.tex:118] His own re-edit removes such commas.
- A long subject before a late passive verb (17 words before "is shown" at [PROC main.tex:84]).
- Restrictive "which" without a comma (about 35 in OWN, 2 in CMS). Write "that".
- No comma after an opening "Thus", "First" or "Therefore", as in "First a cut was imposed" [SAC main.tex:413]. He often omits it; most journals add it.
- Wrong articles and agreement: "A R13478UV PMT" [SAC main.tex:305], "which consist of" [THESIS paper.txt:9986].

CMS house style and boilerplate:

- The passive abstract and the near absence of "we".
- Chains of "is required to" and "are required to" (6.5 per 10,000 words in CMS, 0.9 in OWN).
- Mirrored parentheses: "larger than 12 (15) GeV at L1 in 2017 (2018)" [ETA main.tex:91]. Rare in his own text (7 sentences in OWN, one of them in SAC: "a value near 1 (0) implying challenging (easier) separation" [SAC main.tex:443]); write the two cases out when the sentence allows.
- "because of" as a forced replacement for "due to", and the comma after "i.e." and "e.g.", unless the target journal wants them.
- A median of 24 words in paragraphs of 8 to 15 sentences (IDM, ETA): an effect of the letter format.
- The ornate register in parts of SCOUT, from other contributors: "This demonstrates the remarkable capabilities of data scouting in boosting the muon-based physics program of CMS." [SCOUT main.tex:783]

Thesis and proceedings only:

- "I" for signposts and "This chapter ..." openers.
- Sentences that start with "And" or "But" (8 in THESIS, 1 in SAC), emphatic "do" as in "do look uncorrelated" [THESIS paper.txt:12062], colloquial words as in "a bit opaque" [THESIS paper.txt:3064].
- More than one dash construction (the thesis has ten).
- "will" to narrate a mechanism (5 of the 8 uses in PROC). Describe mechanisms in the present.

## Checklist

1. Does the sentence start with the thing it is about, not with "we" or a connector?
2. Does every "we" mark a decision, a study, an estimate, a finding, a conclusion or a run of the authors' own?
3. Are operations on recorded data in the passive, with the means after "by" or "using"?
4. Is the median sentence at 19 to 22 words, with 13 to 18% of sentences at 12 words or fewer and 13 to 18% above 30?
5. Is every sentence over 40 words a list or a definition?
6. Is the present used for what the method does, what a figure shows and what a result is, and the simple past only for what was done once?
7. Does each choice carry its purpose ("To ...,") or its reason ("since", "due to", "because") in the same sentence?
8. Does a "This + verb" sentence or a single tail (", which ..." or a participle) give the consequence where one is needed, with no three sentences of 12 words or fewer in a row?
9. Is each trade-off stated in one sentence with "but" or ", while"?
10. Does a count come before each list, with a colon after a complete clause?
11. Are specifications, values and glosses in parentheses next to their noun?
12. Is the text free of added dashes, semicolons outside lists, question marks, exclamation marks, footnotes, direct address and contractions?
13. Is there a comma after each fronted phrase and in each series, and none before a trailing "and" + verb, "because" or "due to" phrase?
14. Were sentences that already worked left as they were?
