# Words and phrases

> **When to read this file.** Read it when you choose or replace words: verbs, verdict words, approximators, causal words, connectors, hedges, intensifiers, fixed phrases, names and spelling.
> It holds eleven habits (WORD-1 to WORD-11) with their evidence, quotes, limits and before/after pairs, then three word lists (prefer, use sparingly, avoid), the measured targets, the things not to copy and a checklist.
> Use it in the word pass of a polish, after the sentences are in shape (`sentences-and-voice.md`).

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

**How to read the evidence.** The thesis chapter that reprints SAC is counted once in OWN. SCOUT has many contributing authors. Counts are occurrences in running text (44,002 words in OWN, 43,216 in CMS, 5,138 in SAC) unless captions are named. A pair "a / b" means OWN / CMS. Rates are per 10,000 words unless marked. All counts were checked by search on the cleaned corpus text.

**Contents.**

- WORD-1. Use the plain verb
- WORD-2. Judge by sufficiency, not by praise
- WORD-3. Round with "roughly" or "about"; leave exact values bare
- WORD-4. Put the reason inside the sentence
- WORD-5. Open few sentences with a connector, and use the ones he uses
- WORD-6. Hedge an expectation with one modal verb
- WORD-7. Give the number instead of an intensifier
- WORD-8. Reuse his fixed phrases
- WORD-9. Describe first, name second, and keep the name
- WORD-10. State your own work with plain verbs of saying and finding
- WORD-11. Spelling and mechanics
- Three word lists; Measured targets; Do not copy; Checklist

**Summary.**

1. He writes with plain verbs (show, use, provide, allow, consist of). The documents he wrote alone contain no "utilize", "outperform" or "state-of-the-art".
2. He rates a result by whether it is enough for a stated need (sufficient, acceptable, reasonable, negligible) and keeps praise words off his own results.
3. He rounds with "roughly" or "about". "Approximately" is the CMS word. A value quoted at its measured precision carries no approximator.
4. The reason sits inside the sentence (since, due to, because). About 8% of sentences open with a connector, and "Nevertheless," follows an admitted weakness.
5. Mechanics are stable: American spelling, "Table" spelled out, lower-case "standard model" (PROC has capitals), hyphenated compound modifiers. "Fig." or "Figure" and "Sec." or "Section" follow the venue.

## Habits

### WORD-1. Use the plain verb

**Rule.** Write show, use, provide, allow, consist of, find, estimate, determine, measure. Replace utilize, leverage, facilitate and showcase.

**Why.** A plain verb costs the reader nothing, so attention goes to the object and the number. A rare verb makes the reader ask whether a special meaning is intended.

**Evidence.** Always; 6 of 6 documents; his own. show 123 / 89 (28.0 / 20.6 per 10,000 words; 37.0 in SAC). provide 70 / 73. consist of 42 / 13. allow 34 against enable 10 in OWN (8 against 2 in SAC); in CMS enable leads, 38 against 28, and 36 of the 38 are in SCOUT. utilize 0 / 10, leverage 1 / 6, facilitate 0 / 3: every CMS use is in SCOUT, the review with many hands. outperform is absent from all six documents. For what a particle or a signal does he takes a concrete verb: strike occurs 21 times in OWN and once in CMS.

- "Fig. 14 shows the collected charge as a function of deposited energy." [SAC main.tex:383]
- "The ECAL consists of 616 BGO scintillating crystals (from the old L3 experiment at LEP) with dimensions 21x21x230 mm^3 each, arranged in a cylindrical orientation." [PROC main.tex:86]
- "These triggers allow considerably lower muon pT thresholds, but store only a limited amount of information per event, ensuring that the total data transfer bandwidth remains affordable." [ETA main.tex:96]

**When not to apply.** Keep the technical verbs of the field (reconstruct, simulate, fit, veto, tag). Do not purge employ, exploit, obtain, perform or achieve: he uses each (16, 7, 13, 18, 7 in OWN), only two to four times less often than the CMS papers (28, 24, 50, 48, 30). Thin them out if a draft leans on them.

**Before.** We leverage a fast digitizer to facilitate the extraction of the arrival time, and the setup is able to achieve a resolution of 38 ps.

**After.** A fast digitizer records each pulse, which allows the arrival time to be extracted. We find a time resolution of 38 ps.

### WORD-2. Judge by sufficiency, not by praise

**Rule.** State the need first. Then say that the result meets it, with sufficient, acceptable, reasonable, moderate, negligible, manageable, safe or conservative. Remove praise of your own result: excellent, superior, impressive, state-of-the-art, outperforms.

**Why.** "Excellent" gives the reader nothing to check. A result that "meets the 200 ps timing requirement" [SAC main.tex:421] gives the number, the benchmark and the verdict, and the reader can verify all three.

**Evidence.** Always in SAC, usual elsewhere; his own. Twelve sufficiency words and their adverbs (moderate, acceptable, sufficient, reasonable, negligible, manageable, satisfactory, safe, comfortably, adequate, modest, conservative) occur 14 times in SAC, against 2 uses of a set of seventeen praise words (novel, excellent, powerful, unprecedented, remarkable, groundbreaking, pioneering, superior, outstanding, innovative, state-of-the-art, impressive, exciting, compelling, pivotal, paramount, unique). Neither of the 2 describes his result: "novel" is said of the experiment and "excellent" of a requirement. In OWN the sets stand at 46 and 28; most of the 28 are in the introductory and closing chapters of the thesis and describe other people's evidence ("The agreement is remarkable." [THESIS paper.txt:1672], about a cosmology fit). In CMS they stand at 40 and 65, with 57 of the 65 in SCOUT, 8 in IDM and none in ETA. state-of-the-art, outperform and impressive: 0 in all six. "good agreement": 0 in all six; he writes "consistent with" (6 / 13), "compatible with" (7 / 9) and "agrees well with" (2 / 0). "meet(s)" with a requirement: 5 times in the running text of SAC (7 with captions) and in no other own-voice document as a verdict. "comfortably" occurs once in the six documents and "acceptable" once [SAC main.tex:421, 236]. Outside the list of seventeen, SAC says "good linearity" (line 379), "robust double-peak resolution" (line 451) and "is clearly visible" (line 274) of its own results; do not add such words.

- "This has acceptable timing resolution while providing sufficient light yield for the low beam energies in the experiment, at a reasonable cost." [SAC main.tex:236]
- "The PbF2 resolution was found to be 81 ps, which comfortably meets the 200 ps timing requirement for a successful SAC performance." [SAC main.tex:421]
- "Nevertheless, the agreement seen here is robust enough to inspire confidence in a proper understanding of the event selection and collisional backgrounds present in data." [THESIS paper.txt:10415]
- "These requirements remove more than 90% of the electroweak SM backgrounds without incurring a significant loss of signal efficiency." [IDM main.tex:119]

**When not to apply.** A requirement, a physical fact or another group's result may take a strong adjective. "The first" may be claimed once where it is a fact (IDM and ETA do so in the contribution sentence). Do not invent a requirement that the study never had; compare with the baseline instead.

**Before.** The detector achieves an excellent time resolution of 38 ps, significantly outperforming the requirement.

**After.** The time resolution was found to be 38 ps, which meets the 50 ps requirement. (In a polish the removal of "excellent" and "significantly outperforming" is proposed in the report, not carried out.)

### WORD-3. Round with "roughly" or "about"; leave exact values bare

**Rule.** Put "roughly" or "about" before a number that you rounded or read off a plot. Give a number quoted at its measured precision with no approximator. Do not write "approximately" outside a CMS paper.

**Why.** The word tells the reader how much weight the digits carry: "roughly 10%" is a round figure, "81 ps" is the measured value.

**Evidence.** Always; the split between own voice and house style is clean. With captions, roughly occurs 49 / 9 times and approximately 2 / 24. In running text: roughly 9.5 / 2.1 per 10,000 words (11.7 in SAC), approximately 0.5 / 5.3, "about" before a number 2.0 / 8.6 (7.8 in SAC, 24.3 in ETA). "Roughly" is in all three own-voice documents; IDM has none. In SAC the fitted values (81 ps, 174 ps, 2.05 p.e./MeV) are bare, the value read from the resolution curve is "roughly 10%", and the abstract gives all headline values bare.

- "Nevertheless, we find that with a single crystal, the energy resolution is roughly 10% at 550 MeV, which already meets PADME's SAC requirements." [SAC main.tex:408]
- "The GM and dSA resolutions are roughly 1 GeV and 4 GeV, respectively." [THESIS paper.txt:8247]
- "From the slope of the solid fit line in Fig. 14, we find a light yield of 2.05 p.e./MeV." [SAC main.tex:387]
- CMS form: "About 99% of four-muon combinations passed this selection in the signal mass window, compared to only 84% in the sideband." [ETA main.tex:198]

**When not to apply.** Do not hedge the headline values in the abstract. Use one approximator per number, never two ("roughly about", "approximately ~"). Exact settings and thresholds take none. In a polish, swap "approximately" for "roughly" where the draft already rounds; do not add or remove an approximator on your own, since it changes what the number claims. "∼" before a number is also his (SAC 6, ETA 4): leave it as it is, and never put a word hedge on top of it. "About" before a number is in both voices (12 in OWN with captions, 39 in CMS) and marks neither.

**Before.** The resolution is approximately 38.2 ps and degrades by approximately 20% near the edge of the tile.

**After.** The resolution is 38 ps at the center of the tile and degrades by roughly 20% near its edge.

### WORD-4. Put the reason inside the sentence

**Rule.** Attach the reason in the same sentence with "due to" plus a noun phrase or "since" plus a clause; in the thesis he also writes "because". Place the consequence word after the subject or after "and": "We therefore", "and hence", "is then". Do not build chains with ", so".

**Why.** The reader gets a choice and its reason in one reading and never carries an unexplained statement into the next sentence.

**Evidence.** Usual; the choice of word depends on the venue. Per 10,000 words, OWN / SAC / CMS: since in its causal uses 18.4 / 5.8 / 3.2 (19.1 / 5.8 / 6.5 with the temporal uses); due to 11.6 / 17.5 / 2.5; because 7.7 / 0 / 8.8, of which "because of" 2.5 / 0 / 6.0; therefore 11.1 / 5.8 / 4.6; hence 4.3 / 7.8 / 1.4; thus 2.7 / 5.8 / 8.1. So "since" and "due to" are his own: in SAC "due to" is three times as frequent as "since", and in the thesis the order is reversed (11.7 against 19.0). "Because of" is what the CMS papers prefer (6.0 against 2.5 per 10,000 words; 11 uses in the thesis, none in PROC and SAC, which have no "because" at all). "Thus" is in his own papers at the same rate as in the CMS pool (PROC 7.4, SAC 5.8, CMS 8.1 per 10,000 words); the low OWN figure is the thesis. "Owing to" is rare in both voices (4 in the thesis, 2 in ETA, which has no "due to"). The cause words sit inside the sentence: in OWN 22 of 84 "since", 2 of 51 "due to" and 1 of 34 "because" open a sentence. Consequence words too: 29 of 49 "therefore" are inside, 16 of 19 "hence" are "and hence", 48 of 49 "then" are inside. ", so" and "and so" occur 21 / 3 times (3 in SAC).

- "By measuring precisely the energy and impact position of the photon with the ECAL, its momentum can be determined, since it originates in a fixed target." [PROC main.tex:66]
- "The ECAL has a central hole due to the high rate of Bremsstrahlung events, which are sharply peaked at small angles." [SAC main.tex:151]
- "We therefore instrument the walls of the magnet with plastic scintillators to identify these lower-energy positrons." [PROC main.tex:102]
- CMS form: "The overall efficiency to correctly assign muon charges is greater than 97% because of the low-energy spectrum of IDM muons." [IDM main.tex:119]

**When not to apply.** When the reason needs more than one clause, give it its own sentence that starts with "This": "This is due to the smaller lever arm and lack of tracker information." [IDM main.tex:121]. In a venue with CMS-like rules change an adverbial "due to" to "because of".

**Before.** The tile is small. As a result, the light path is short. Consequently, the rise time is fast.

**After.** Since the tile is small, the light path is short and hence the rise time is fast.

### WORD-5. Open few sentences with a connector, and use the ones he uses

**Rule.** Open about one sentence in ten with a connector (7 to 11%, counted on the list of 31 in `corpus-and-measurements.md`). His frequent ones are Finally, However, Therefore, Furthermore, Nevertheless, Moreover and "Note that", with "Hence," for a closing verdict. First, Then, Thus, Consequently, "In particular,", "In this case,", "For this reason,", "For example," and "On the other hand," also open sentences in his own texts, and stay. After an admitted weakness, the sentence that says what still holds often starts with "Nevertheless,". Do not open with "In addition," or "As a result,", and do not add "Additionally," or "Notably,".

**Why.** When connectors are rare, each one marks a real turn in the argument. "Nevertheless," tells the reader that the caveat just given does not undo the result.

**Evidence.** Usual; 6 of 6 for the low rate. A connector from a list of 31 opens 7.5% of sentences in PROC, 10.7% in SAC, 8.3% in OWN and 7.4% in CMS (6.0% in IDM, 5.8% in ETA). Sentence-initial counts in OWN (2,097 sentences): Finally 32, However 24, Therefore 20, Furthermore 20, Nevertheless 15, Moreover 11, Note that 8. "Nevertheless" is his own: 5 in SAC and 15 in OWN, every one sentence-initial, against 2 in CMS (both in SCOUT, one of them inside a sentence). "In addition," opens 0 / 9 sentences, "Additionally," 2 / 7 (the two are in the thesis, as are two "Notably,"); "As a result" occurs 1 / 9 times. Three of the five "Nevertheless," in SAC follow a caveat on his own number (lines 245, 408, 447); line 211 grants a use to a rejected option and line 295 limits a conclusion. In all five the two sentences speak of the same object.

- "Nevertheless, this separation resolution already meets the PADME tagging requirements." [SAC main.tex:447]
- "Nevertheless, this provides a reasonable estimate of projected sensitivity." [THESIS paper.txt:15088]
- "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]
- "Finally, PADME also has two dedicated beam monitors: the TimePix3 detector and the active diamond target." [PROC main.tex:118]

**When not to apply.** Do not add a connector where "This" plus a noun already links two sentences. Add "Nevertheless," only when three things hold: the sentence right before states a weakness, a limit or a rejected option; the sentence itself is already in the draft; and it speaks of the same result or object and says why that result still serves, or where the conclusion just drawn stops. A result for another range, sample or quantity is not what still holds: leave it without a connector. When you are not sure, do not add the word and put the question in the report. Do not write a new claim of what still holds. A short concession stays inside the sentence with "but" (SAC lines 282 and 406; "but" occurs 74 times in OWN and 31 in CMS). In a letter with long paragraphs he uses fewer openers and makes the concession with "but" inside the sentence (7 in IDM, 4 in ETA). PROC has no "However" and no "Nevertheless": a short descriptive text needs neither.

**Before.** Additionally, the temperature of the tile was not controlled. In addition, the reference detector adds jitter. However, the resolution is good.

**After.** The temperature of the tile was not controlled, and the reference detector adds a jitter of 12 ps. Nevertheless, the measured resolution meets the requirement.

### WORD-6. Hedge an expectation with one modal verb

**Rule.** Mark an expectation or an extrapolation with one modal verb (should, could, can, would) or with "is expected to". State what was measured in the indicative. Never stack hedges.

**Why.** The verb alone then tells the reader what was measured and what is only expected.

**Evidence.** Usual; his own. can, could, may, might, would, should and must total 6.2 per 1,000 words in OWN (273 uses), 5.1 in SAC and 3.3 in CMS. should 22 / 1; could 55 / 12; might 12 / 3; may 10 / 18, with none in PROC or SAC. "is/are expected to" 5 / 7 (2 in PROC, 1 in SAC). Hedging adverbs are rare: likely 7 / 4, perhaps 1 / 1, presumably 0 / 1.

- "These steps should remove a large fraction of beam-induced backgrounds for the next run of PADME." [PROC main.tex:150]
- "The photon rate in the central crystal due to Bremsstrahlung is expected to reach several hundred MHz, depending on beam intensity." [SAC main.tex:160]
- "We do not account for effects from the PMT itself, but those should be of second order and so this procedure at least allows the relative comparison of different crystal lengths." [SAC main.tex:282]

**When not to apply.** Put no modal on a measured value or on a statement of what the method does. "Can" for ability is not a hedge and stays.

**Before.** This may possibly suggest that the resolution could potentially improve with a thicker tile.

**After.** A thicker tile should improve the resolution, since it yields more light.

### WORD-7. Give the number instead of an intensifier

**Rule.** Do not put very, significantly, highly, extremely, strongly or clearly on a statement about your result. Give the two numbers. If the margin matters, allow one mild adverb: already, slightly, sharply, only. In a polish, propose the removal of an intensifier in the report; "significantly" in front of a measured difference is a claim, so ask the authors.

**Why.** A number carries the size of an effect. An intensifier asks the reader to take the size on trust.

**Evidence.** Always; 6 of 6. The six intensifiers together: 0 uses in PROC, 4 in SAC (0.8 per 1,000 words), 45 in OWN (1.0), 56 in CMS (1.3). very 21 / 19 (2 in SAC); significantly 4 / 19 (5 in OWN with the caption at SAC line 425, "not significantly affected"); clearly 1 / 6; substantially 1 / 17, all 17 in SCOUT. Mild adverbs are more common: only 71 / 62 (16 in SAC), already 12 / 5, sharply 8 / 1, slightly 7 / 5. Where a strong word appears, it sits on a physical fact.

- "A shift and broadening of the narrow peak with increasing length is clearly visible." [SAC main.tex:274] This is the only "clearly" in OWN.
- "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost." [SAC main.tex:211]
- "Global muons offer a better performance overall, though their reconstruction efficiency sharply drops after the end of the tracker region (around z ≈ 60 cm)." [THESIS paper.txt:4843]
- "This huge η production rate is critical to the study of its rare decay channels." [ETA main.tex:146]

**When not to apply.** "Significant" in the statistical sense stays. One strong word on a physical fact, with its number or its reason in the same sentence, is acceptable.

**Before.** The time-walk correction very significantly improves the resolution, which is clearly much better than before.

**After.** The time-walk correction improves the resolution from 61 ps to 38 ps.

### WORD-8. Reuse his fixed phrases

**Rule.** Give each recurring job its fixed phrase: "as a function of" for a dependence; "Note that" for what a procedure leaves out or assumes, or where a result is valid (SAC lines 270, 346, 387; add it only in front of such a sentence that the draft already has); "is taken as" for a convention chosen by the authors; "a factor of N" and "compared to" for comparisons; "consists of" for composition; "account for" for a correction; "by means of" for an instrument; "There is" plus a number for a trend. Use "in order to" where a bare "to" would be unclear.

**Why.** A fixed phrase for a fixed job lets the reader recognize the job at once.

**Evidence.** Usual; his own unless marked.

| Phrase | SAC | OWN | CMS | Note |
|---|---:|---:|---:|---|
| as a function of | 8 | 27 | 22 | 48 / 46 with captions |
| in order to | 8 | 22 | 7 | none in PROC, IDM, ETA |
| Note that (opening a sentence) | 4 | 8 | 0 | own voice only |
| taken as | 3 | 9 | 1 | "we take" 2 / 0 |
| a factor of | 2 | 6 | 5 | 2 in PROC |
| by means of | 3 | 6 | 3 | in 5 of 6 documents |
| compared to | 3 | 25 | 44 | "compared with" 1 / 4 |
| consist(s) of | 4 | 42 | 13 | "comprise" 1 / 14 |
| account(s) for | 5 | 19 | 8 | |
| there is / there are | 9 | 69 | 14 | own voice |
| can be | 13 | 64 | 40 | "can be seen" 6 / 0 |
| it is | 2 | 58 | 15 | mostly thesis |

House style, not his: "with respect to" 1 / 18 (all in SCOUT) and "is/are required to" 4 / 29 with captions.

- "Note that we do not simulate the entire detector here, just a single crystal in the SAC." [SAC main.tex:270]
- "The location of the fit at 50% height was then taken as the reference time." [SAC main.tex:413]
- "The R13478UV PMT offers in this configuration roughly a factor of 2 better resolution." [SAC main.tex:227]
- "There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282]

**When not to apply.** Do not turn every "to" into "in order to": PROC states nine purposes with a bare infinitive. Do not line up several "There is" or "It is" sentences; the CMS papers have a fifth of his rate.

**Before.** It should be noted that the fit only utilizes the leading edge. The 20% crossing serves as the timestamp.

**After.** Note that the fit uses only the leading edge of the pulse. The crossing at 20% of the amplitude is taken as the arrival time.

### WORD-9. Describe first, name second, and keep the name

**Rule.** Describe the thing, then name it with "referred to as" or "known as", or give the full name with the acronym in parentheses. The rule is for names that the authors coin. Put a coined label in quotation marks once. Afterwards use that one name unchanged. Do not write "so-called". In a polish, turn "which we call Y" into "which we refer to as Y" when the authors coined the name, and into "referred to as Y" or "known as Y" when the name is in general use.

**Why.** The reader meets the idea before the label. A label that never changes never raises the question whether two names mean two things.

**Evidence.** Usual; his own, and it survives CMS editing. referred to as 9 / 11 (3 in IDM); known as 9 / 7; called 4 / 8; dubbed 2 / 0 (thesis). "so-called": once in the six, in the thesis ("the so-called core-cusp problem" [THESIS paper.txt:1529]). "we call": 0 in all six; for a label of his own he keeps the first person ("we label the current with “iDM”" [THESIS paper.txt:4404], "Henceforth I refer to the latter collection as displaced standalone (dSA)" [THESIS paper.txt:6649]). PROC and SAC name by the parenthesis alone (SAC has "labeled" once, for a plot label). SAC does not keep one name for its fourth headline quantity: "double-peak separation resolution" 6 times and "double-peak separation capability" 5 times; do not copy that.

- "Tracks reconstructed exclusively with muon chamber data are referred to as standalone muon tracks." [THESIS paper.txt:6609]
- "Its magnitude is referred to as pTmiss." [IDM main.tex:57]
- "To mitigate such backgrounds, a very fast Small-Angle Calorimeter (SAC) is placed behind the main ECAL, flush with the central hole." [SAC main.tex:153]

**When not to apply.** A term that every reader of the journal knows needs no introduction, or may come first with its gloss after it, as in SAC: "'dark photon', a vector mediator of a new abelian gauge force that kinetically mixes with the SM U(1)Y" [SAC main.tex:139]. Do not name a thing that is used once.

**Before.** We use the so-called CFD method. The constant-fraction approach is robust against amplitude changes, and the discriminator technique is applied offline.

**After.** The arrival time is the time at which the pulse crosses a fixed fraction of its amplitude, referred to as the constant-fraction time. The constant-fraction time does not depend on the pulse amplitude.

### WORD-10. State your own work with plain verbs of saying and finding

**Rule.** Name the document by its type ("In this paper we"). State the purpose with describe, report, present or evaluate. Report findings with "we find", "we estimate", "we conclude". Do not write "we observe", "we see", "we note" or "we believe".

**Why.** These verbs say exactly what the authors did and what they claim, and no more.

**Evidence.** Always for the purpose sentence: PROC "Here we describe", SAC "In this paper we evaluate", IDM "In this Letter, we present", ETA "In this Letter, we report", SCOUT "In this report, we describe". "this paper" 3 times in SAC; "this work" appears in running text only in IDM (1) and ETA (1, in the abstract; once more in a caption). we find / we found 7 / 0 (3 in SAC); we estimate 3 / 2; we conclude 1 / 1. "we observe", "we see", "we believe": 0 in all six; "we note": once, in SCOUT. demonstrate 4 / 13, once in the purpose statement of SAC.

- "Here we describe PADME's design, status of the experiment, and future plans." [PROC main.tex:34]
- "From these considerations, we conclude the larger Hamamatsu R13478UV PMT, coupled to PbF2 crystals, is the best solution for PADME's requirements." [SAC main.tex:236]
- "Overall, we estimate the total systematic uncertainty in the branching ratio measurement to be 14%, adding all contributions in quadrature." [ETA main.tex:278]

**When not to apply.** Do not multiply "we find": SAC has three. For a procedure the passive or the object as subject is the normal form.

**Before.** In this work, we observe that our novel readout scheme provides state-of-the-art timing.

**After.** In this paper we evaluate the time resolution of a scintillator tile read out by two silicon photomultipliers. We find a resolution of 38 ps for 4 GeV electrons.

### WORD-11. Spelling and mechanics

**Rule.** Use American spelling. Spell out "Table". Write "standard model" in lower case, define "SM" once, then use "SM". Treat "data" as plural. Hyphenate a compound modifier before its noun. Define "Monte Carlo (MC)" once; "MC simulation" is then his, and a bare "MC" becomes "simulation". Write "selection" or "requirement" for a condition on events or objects and "threshold" for a value that a signal or a score must pass, where the draft's "cut" is not a defined term; a "cut" that the draft defines and uses throughout stays, and the change is proposed for the whole paper in the report. Follow the venue for "Fig." or "Figure", "Sec." or "Section", and "data set" or "dataset".

**Why.** Uniform mechanics are invisible. A switch from "dataset" to "data set" makes the reader stop on the form.

**Evidence.**

| Item | Finding (running text and captions) | Whose |
|---|---|---|
| -ize, not -ise | 137 against 1 in OWN, 129 against 0 in CMS; center 41 / 14, centre 0; behavior 14 / 4 | his, 6 of 6 |
| Section, Table | "Section" 45 / 88, in SAC, THESIS and SCOUT (PROC, IDM and ETA refer to no section); "Sec." 0; "Table" 32 / 27, "Tab." 0; "Ref." 11 / 44 | his, in the three documents that have it |
| standard model | lower case in SAC, IDM, ETA, SCOUT and THESIS (13 uses); capitalized once, in PROC (2019); "SM" 118 / 55 | lower case in five of the six |
| Fig. or Figure | PROC and SAC: "Fig." everywhere, 12 times at a sentence start; thesis: "Figure" 174 of 174; CMS: "Figure" at the start (35), "Fig." inside (57) | venue |
| data set | "data set" 70 and "dataset" 0 in CMS; thesis 8 and 12; neither in PROC, SAC | house |
| data, plural | plural verb 6, singular 1 in OWN | his |
| compound modifiers | data-driven 17, long-lived 13 / 20, single-crystal, double-peak | his, 6 of 6 |
| prefixes | non-X hyphenated 27, closed 2 in OWN; 2 and 16 in CMS | own hyphen, house closed |
| i.e., e.g. | no comma after them in OWN (27, 12); comma in CMS (15, 15); "i.e." opens a parenthesis in 19 of 21 uses in OWN | venue |
| simulation, selection | thesis: simulat- 138, "MC" 12; "selection" 98, "cut" 13. SAC says "MC" 12 times and "a cut was imposed" twice (lines 413, 431); PROC says "MC" 6 times. His thesis reprint kept "MC simulation" 8 times and both "cut", and changed a bare "MC" to "simulation" ("in simulation" [THESIS paper.txt:16814]). For a value on a signal he writes "threshold" [SAC main.tex:354] | his later choice; "MC simulation" and "cut" are no errors |
| percent | "38%" with no space: 55 / 128, never with a space | all |

- "Despite the recent discovery of the Higgs boson at the LHC, solidifying our understanding of the standard model (SM) of particle physics, many lingering questions remain that the SM cannot yet explain." [SAC main.tex:136]
- "Such a strategy is adopted in this analysis and described in Section 8.1.5." [THESIS paper.txt:6640]
- "The data are being used for detector commissioning work as well as preliminary data analysis." [PROC main.tex:134]
- "Figure 6 shows the total efficiencies vs. pT, split by rapidity range." [ETA main.tex:236]

**When not to apply.** A journal rule wins over his habit. For a Physical Review paper write "Figure" at the start of a sentence and "Fig." inside, as his two PRL papers do, and close the prefixes (nonzero, subdetector). Write "Section" in full, as he does in the three documents that refer to a section (SAC, SCOUT, THESIS; "Sec." occurs in none of the six); if the draft, the authors or the journal's guide have "Sec.", keep it and say so in the report. Where a citation is a noun, write "Ref. [N]" (THESIS 11, IDM 4, ETA 2), as in "This procedure is adapted from Ref. [57]." [THESIS paper.txt:14662-14663]; the bare number as a noun in SAC (line 295) is an early form.

**Before.** The centre of the tile is aligned with the beam axis (Sec. 3), and the dataset is analysed with the timing cuts of Tab. 2.

**After.** The center of the tile is aligned with the beam axis, as described in Section 3, and the data set is analyzed with the timing selection listed in Table 2.

## Three word lists

Counts are OWN / CMS in running text.

**Prefer.**

| Words | OWN / CMS |
|---|---|
| show; provide; allow | 123 / 89; 70 / 73; 34 / 28 |
| consist of; account for; lead to; mitigate | 42 / 13; 19 / 8; 24 / 21; 14 / 10 |
| find or found; estimate; determine; measure | 30 / 27; 40 / 22; 23 / 32; 52 / 57 |
| sufficient; reasonable; negligible; conservative | 7 / 20; 6 / 2; 10 / 6; 5 / 1 |
| roughly; "about" before a number | 42 / 9; 9 / 37 |
| since; due to; therefore; hence | 84 / 28; 51 / 11; 49 / 20; 19 / 6 |
| thus (as ", thus ...ing" and "and thus") | 12 / 35; SAC 3 and PROC 1, the CMS rate |
| Nevertheless; However; Furthermore; Finally | 15 / 2; 32 / 12; 21 / 9; 34 / 23 |
| also; then; only (inside the sentence) | 121 / 65; 49 / 28; 71 / 62 |
| main; several | 43 / 19; 57 / 43 |

**Use sparingly.**

| Words | OWN / CMS | Limit |
|---|---|---|
| very; significantly; clearly | 21 / 19; 4 / 19; 1 / 6 | not on your own result |
| highly; extremely | 5 / 7; 12 / 1 | on a physical fact only |
| novel; excellent; robust; unique | 3 / 14; 3 / 9; 11 / 5; 5 / 11 | "novel" at most once, of the experiment or the technique (SAC line 147); "robust" is his word for a verdict: keep it where the draft has it |
| crucial; key; important; interesting | 7 / 7; 8 / 12; 7 / 8; 12 / 18 | with the reason in the same sentence |
| demonstrate; enable; employ; exploit | 4 / 13; 10 / 38; 16 / 28; 7 / 24 | prefer show, allow, use |
| obtain; perform; achieve | 13 / 50; 18 / 48; 7 / 30 | prefer find, do, reach |
| approximately; respectively | 2 / 23; 24 / 44 | "approximately" is the CMS word; "respectively" is his at half the CMS rate |
| notably | 2 / 8 | thesis only in OWN; do not add |
| a dash as punctuation | 17 / 3 | one construction in SAC, a pair in PROC, ten in THESIS; never add one |
| Moreover; Additionally | 11 / 9; 5 / 8 | "Furthermore" is twice as frequent |
| may; might; likely | 10 / 18; 12 / 3; 7 / 4 | expectations only |
| ", so" and "and so" | 21 / 3 | not twice in a paragraph |
| the fact that; in this case | 9 / 1; 16 / 3 | own-voice filler |
| i.e.; e.g. | 21 / 15; 11 / 15 | inside parentheses |

**Avoid.**

| Words | OWN / CMS | Note |
|---|---|---|
| utilize; leverage; facilitate | 0 / 10; 1 / 6; 0 / 3 | CMS uses all in SCOUT |
| outperform; state-of-the-art; impressive | 0 / 0 each | absent from all six |
| superior; groundbreaking; pioneering | 0 / 3; 0 / 2; 0 / 3 | SCOUT and one in IDM |
| substantially; crucially | 1 / 17; 0 / 5 | SCOUT; one "substantially" in THESIS |
| good agreement; excellent agreement | 0 / 0; 0 / 1 | write "agrees with" or "consistent with" |
| it should be noted; the tag "as can be seen" | 0 / 0 each | write "Note that"; make the figure the subject. "X can be seen in Fig. N" is his (6 / 0) and stays |
| we observe; we see; we believe; we call | 0 / 0 each | write "we find"; "we refer to" for a coined name |
| so-called; etc.; in other words; to this end | 1 / 0 (THESIS); the others 0 / 0 | |
| In conclusion; Lastly; nonetheless; obviously | 0 / 0 each | |
| "In addition," as opener; As a result | 0 / 9; 1 / 9 | |
| with respect to | 1 / 18 | write "compared to" |
| Tab. | 0 / 0 | "Sec." is also 0 / 0, but follows the journal |

Most Avoid entries are absent from all six documents, so the evidence for them is absence in both voices, not a contrast with the CMS papers. "Showcase" occurs once in his thesis and once in SCOUT; write "show". "Significantly" is under Use sparingly, since he uses it in his own voice.

## Measured targets

Rates per 10,000 words of running text unless marked. "Aim for" applies to a short methods paper by a few authors in a Physical Review journal. The full set of targets is Table B of `voice-and-transfer.md`.

| Measure | OWN | SAC | CMS | Aim for | Reason |
|---|---:|---:|---:|---|---|
| Sentences that open with a connector (%) | 8.3 | 10.7 | 7.4 | 7 to 11 | stable across the six |
| roughly | 9.5 | 11.7 | 2.1 | 5 to 12 (0.5 to 1.2 per 1,000 words) | his approximator |
| approximately | 0.5 | 1.9 | 5.3 | 0 to 2 (0 to 0.2 per 1,000 words) | CMS word |
| "about" before a number | 2.0 | 7.8 | 8.6 | 2 to 8 (0.2 to 0.8 per 1,000 words) | used in both registers |
| Modals, can to must (per 1,000 words) | 6.2 | 5.1 | 3.3 | 4 to 6 | a paper has fewer prospects than a thesis |
| Six intensifiers (per 1,000 words) | 1.0 | 0.8 | 1.3 | below 1 | SAC is the model |
| Twelve sufficiency words | 10.5 | 27.2 | 9.3 | 10 to 25 | results are set against needs |
| Seventeen praise words | 6.4 | 3.9 | 15.0 | 0 to 4 | none on own results |
| since, causal uses | 18.4 | 5.8 | 3.2 | in use, up to 20 | his causal word |
| due to | 11.6 | 17.5 | 2.5 | in use, up to 20 | his causal word in papers |
| because, with "because of" | 7.7 | 0.0 | 8.8 | up to 20 | allowed, not needed |
| therefore | 11.1 | 5.8 | 4.6 | up to 20 | half of them inside the sentence |
| hence | 4.3 | 7.8 | 1.4 | up to 20 | mostly "and hence" |
| thus | 2.7 | 5.8 | 8.1 | up to 20 | his papers have it at the CMS rate (PROC 7.4) |
| "so" as a conjunction (", so", "and so", "so that") | 4.8 | 5.8 | 0.7 | at most 6 | rare in the papers |
| Causal words in use, of since, due to, because, therefore, hence, thus and "so" (count) | 7 | 6 | 7 | four or more | variety is the habit |
| Nevertheless | 3.4 | 9.7 | 0.5 | 3 to 10 | one per admitted weakness |
| However | 7.3 | 5.8 | 2.8 | 3 to 7 | sentence-initial |
| in order to | 5.0 | 15.6 | 1.6 | 3 to 10 | absent from PROC, IDM, ETA |
| Note that | 2.0 | 9.7 | 0.5 | 2 to 8 | one per limit of validity |
| there is, there are | 15.7 | 17.5 | 3.2 | 8 to 17 | with a number |
| show, all forms | 28.0 | 37.0 | 20.6 | 25 to 40 | his verb for figures and results |
| allow against enable (counts) | 34 : 10 | 8 : 2 | 28 : 38 | 3 : 1 or more | "enable" is the review's word |
| utilize, leverage, facilitate, outperform (counts) | 1 | 0 | 19 | 0 | absent from his own papers |

## Do not copy

- **Slips of unedited text.** SAC: "comprised of 5x5 crystals" (line 408), "10x more radiation-hard" (line 177), "10k events" (line 330), "was fit" beside "were fitted", "this data" beside "The data were", one photomultiplier model spelled three ways. PROC: "flushed with its central square hole" (line 104), "two different number of" (line 173), "Monte-Carlo" beside "Monte Carlo". THESIS: "which consist of" (line 9986), "associated to" (5 uses; the CMS papers have "associated with" 18 times), an adverb in -ly hyphenated to its participle ("feebly-interacting").
- **Restrictive "which".** In OWN "which" follows neither a comma nor a preposition about 35 times, in CMS twice. Editors change it. Write "that" for a restrictive clause and ", which" for a comment.
- **CMS boilerplate and house words.** "A search for ... is presented", "No significant excess ... is observed", "corresponding to an integrated luminosity of", "is required to", "with respect to", "approximately", the comma after "i.e." and "e.g.". They belong to collaboration papers.
- **The ornate register of the review.** utilize, leverage, delve, pivotal, groundbreaking, "kinematical" (0 / 17), "Crucially,". These sit in parts of SCOUT written by other hands. ("paramount" and "Notably," also occur in THESIS, once and twice.)
- **The promotional sentences of the PRL contribution paragraph.** "novel" (2), "pioneering" (1) and "powerful" (1) in IDM occur in one or two paragraphs written for a broad readership. Do not carry them into a methods paper.
- **Thesis-only habits.** "I"; colloquial words ("a bit", "wrinkle", "glean", "plethora", "hopefully", "of course"); evaluative adjectives about the field (exciting, remarkable, striking); "dataset" as one word; "statistics" for sample size (10 uses); "Figure" and "Equation" spelled out inside a sentence; the higher modal rate (could 53 times).
- **Proceedings-only habits.** "will" to narrate a mechanism (5 of the 8 uses in PROC) and "Fig." at the start of a sentence.

## Checklist

1. Is every utilize, leverage, facilitate and showcase replaced by use, allow or show?
2. Does each result sentence name the need or the baseline it is set against, with no praise word on your own result?
3. Does every rounded number carry "roughly" or "about", and every exact measured value none?
4. Is "approximately" gone, or kept at most once?
5. Does each design choice have its reason in the same sentence, with since, due to or because?
6. Do consequence words sit inside the sentence ("We therefore", "and hence", "is then") at least as often as at its start?
7. Do 7 to 11% of sentences open with a connector, with no "In addition," or "As a result,"?
8. Was "Nevertheless," added only in front of a sentence that the draft already has, that follows a stated weakness and speaks of the same result?
9. Are modal verbs confined to expectations and extrapolations, one per statement?
10. Are very, significantly, clearly, highly and extremely absent from statements about your results?
11. Is each new term described before it is named, and is the name unchanged afterwards?
12. Does the purpose sentence read "In this paper we" plus describe, report, present or evaluate, and are findings given with "we find", "we estimate" or "we conclude"?
13. Is the spelling American, with "Table" in full, lower-case "standard model" and plural "data"?
14. Do "Fig." or "Figure", "Sec." or "Section" and "data set" or "dataset" follow the journal, and are compound modifiers hyphenated?
15. Is the text free of "it should be noted", the tag "as can be seen", "so-called", "etc." and "In conclusion"?
