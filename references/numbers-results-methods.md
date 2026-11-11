# Numbers, results and the description of methods

> **When to read this file.** Read it when you write or check a sentence that carries a number, a comparison, a verdict, a caveat or an uncertainty, or a passage that describes a procedure, a component, a simulation or a cross-check.
> It holds fifteen habits (NUM-1 to NUM-15) with their evidence, quotes, limits and before/after pairs, then the measured targets, the things not to copy and a checklist.
> It changes how a number is framed and never the number: every value, unit, uncertainty and hedge of the authors stays as it is.

**Conventions.** Tags name the six documents: PROC (proceedings, 2019), SAC (detector paper, 2018), IDM and ETA (CMS letters, 2023), SCOUT (CMS review, 2024) and THESIS (PhD thesis, 2020); `corpus-and-measurements.md` gives titles and sizes. OWN pools PROC, SAC and THESIS, his own voice. The thesis dominates that pool, so the SAC value is the better guide for a paper. CMS pools IDM, ETA and SCOUT, which passed collaboration style rules. Strength is given as always, usual or occasional, and "k of 6" counts documents. Running text means abstract and body without captions. A float is a figure or a table; a pointer is the sentence that introduces a float; a signpost is a sentence that says what comes next in the text. A quote from the corpus is verbatim and carries its tag and locator, a file and line such as [SAC main.tex:421]; a macro or a math expression appears in its printed form, and citation commands are dropped. A tag followed by "line" and a number points to the same source file without quoting it. Habits are cited across files by their labels (STRUCT, PARA, SENT, WORD, FIG, NUM, VOICE).

**Invented examples.** Every sentence after **Before.**, **After.**, **Wrong.** or **Not.** is invented, with or without quotation marks. All of them follow one made-up study with made-up numbers: a test-beam measurement of the time resolution of a small scintillator tile read out by two silicon photomultipliers (SiPMs), with 4 GeV electrons, a requirement of 50 ps and a result of 38 ps. None of its numbers is a real result. Never carry them into a user's text. The After sentences show the target form and assume that the authors supplied every fact in them. In a polish, a change of that kind to a number, a hedge or a claim is a question for the authors, not an edit.

Counts are from the source files, captions included, unless the measurement tables are named.

**Contents.**

- NUM-1. Give every number its condition in the same sentence
- NUM-2. Put the target, baseline or expectation next to the number
- NUM-3. Define each metric before its first value
- NUM-4. Report a measured value exactly and the same everywhere; hedge only rounded numbers
- NUM-5. Word a gain as a factor or a percentage in a named quantity, with its price
- NUM-6. Give sober verdicts
- NUM-7. State a caveat where it arises, then weigh it
- NUM-8. Explain every trend, outlier and curve shape by its cause
- NUM-9. Describe each uncertainty with one template
- NUM-10. Compare with the baseline under the same conditions, and credit the weaker option
- NUM-11. Describe a procedure as counted steps with exact settings
- NUM-12. Describe a component or a sample in a fixed order
- NUM-13. Report a cross-check as purpose, test, verdict, consequence
- NUM-14. Keep units, rounding, ranges and number words uniform
- NUM-15. Wrap each equation in a sentence
- Measured targets; Do not copy; Checklist

**Summary.**

1. A number never stands alone. It carries its condition in the same sentence, and its target, baseline or expectation in the same or the next sentence.
2. A measured headline value is exact and identical in the abstract, the results and the conclusions. A rounded working number takes "roughly" or "about". A setting is exact.
3. A metric is defined before its first value. A gain is a factor or a percentage in a named quantity, against a named reference, with its price.
4. Verdicts are sober ("meets", "sufficient", "negligible", "agrees with"). A caveat is stated where it arises and then weighed, in his own voice with "Nevertheless,".
5. Methods follow fixed orders of information: fair baseline, counted steps, component description, simulation chain, purpose-led check, one template per uncertainty.

## Habits

### NUM-1. Give every number its condition in the same sentence

**Rule.** In the sentence that carries a number, name the sample, energy, range or working point for which it holds.

**Why.** The reader can lift the sentence out of the paper and still use the number. Without its condition a number cannot be compared with any other.

**Evidence.** 6 of 6; always in his own voice, usual in CMS; his own. SAC results carry "at 550 MeV", "with a single crystal", "with 1.8 ns separation". Its one headline value without a condition, 81 ps, gets a caption sentence saying that it does not depend on beam energy [SAC main.tex:425]; the sentence that reports it (line 421) names no beam energy, and the gain assumed for the 2.05 p.e./MeV is only in a caption (line 379). Where a draft has the condition elsewhere, ask the authors whether it belongs in the sentence. SCOUT quotes trigger rates with the instantaneous luminosity (18 values). The condition usually closes the sentence ("at", "for", "with"). An assumption opens it ("Assuming", "Given").

- "Assuming a minimum separation capability of r < 0.95, then roughly 90% of peaks with 1.8 ns separation can be distinguished." [SAC main.tex:439]
- "There is roughly a 16% increase when going from 14 cm to 18 cm." [SAC main.tex:282]
- "It has an energy resolution of 1-2%/√E for positrons below a GeV." [PROC main.tex:86]

**When not to apply.** A block of numbers shares one condition. State it once, in the sentence that opens the block: "Results are shown for 2018 conditions, though conclusions remain the same for other years." [THESIS paper.txt:6655]

**Before.** The time resolution is 38 ps.

**After.** The time resolution is 38 ps for 4 GeV electrons at the center of the tile, at an overvoltage of 5 V.

### NUM-2. Put the target, baseline or expectation next to the number

**Rule.** Give the reference value in the same sentence or in the next one. Close with a short verdict clause: ", which meets ...", ", compared to ...". The value of a standard method may follow the result in a sentence of its own; SCOUT opens that sentence with "In comparison,", which opens no sentence in his own texts, where the form is "Compared to" ("Compared to the R98880U-110, it has a similar rise time" [SAC main.tex:213]).

**Why.** A number is informative only against something. If the reference sits two pages away, the reader must search for it, and most readers will not.

**Evidence.** 5 of 6 (PROC gives its baseline only in a caption); usual; his own, and it survives CMS editing. SAC lists six requirements as numbers at the end of the introduction [SAC main.tex:155] and "meet(s)" then occurs seven times: once in the purpose statement and six times to close a result (4 in the text, 2 in captions). "meets" with a requirement is a SAC form; PROC has none, and the two in the thesis outside the reprint are not verdicts. ETA sets its trigger rate, its selection check and its branching fraction against their references. In the first half of SCOUT, a hand count finds 27 of 131 quantity sentences with the reference in the same sentence; the others get it within two sentences.

- "The PbF2 resolution was found to be 81 ps, which comfortably meets the 200 ps timing requirement for a successful SAC performance." [SAC main.tex:421]
- "About 99% of four-muon combinations passed this selection in the signal mass window, compared to only 84% in the sideband." [ETA main.tex:198]
- "The efficiency to select AK4 and AK8 scouting jets is about 100% for pT > 300 GeV. In comparison, the standard trigger is fully efficient only from around 700–800 GeV." [SCOUT main.tex:1174]

**When not to apply.** The reference was obtained under other conditions. Say so before comparing: "We note that the comparison between the two data sets has some limitations." [SCOUT main.tex:725] A setting needs a reason, not a baseline.

**Before.** With the two-SiPM readout we obtain a time resolution of 38 ps, a clear improvement.

**After.** The time resolution with the two-SiPM readout is 38 ps, which meets the 50 ps requirement. The single-SiPM readout reaches 54 ps under the same conditions.

### NUM-3. Define each metric before its first value

**Rule.** Say in one sentence how the quantity is computed: numerator and denominator, or the fit and the parameter. For a new quantity, add how to read a high and a low value. Then give the number.

**Why.** Efficiency, resolution and purity have several definitions in use. The reader cannot judge a value before knowing which one is meant.

**Evidence.** 4 of 6 (SAC, ETA, SCOUT, THESIS); usual; his own. SAC defines all four of its performance quantities before their values. IDM defines its variables with "defined as" four times but quotes one identification efficiency without a definition. PROC has no metric.

- "The energy resolution was calculated as the fitted sigma over mean of single-electron peaks in the charge distributions (e.g. Fig. 13)." [SAC main.tex:391]
- "A value closer to 1, for example, implies the two peaks are very close together and distinguishing them is more challenging." [SAC main.tex:431]
- "The efficiency is defined as the ratio of the number of events where an offline reconstructed PF jet is selected by the data scouting or standard triggers, relative to the total number of events with an offline reconstructed PF jet." [SCOUT main.tex:1172]

**When not to apply.** The quantity has one accepted definition and a reference. Cite it and move on.

**Before.** The tile efficiency is 99.6%.

**After.** The efficiency is defined as the fraction of beam triggers with a tile signal above 0.5 MIP within 2 ns of the reference time. It is 99.6% at the center of the tile.

### NUM-4. Report a measured value exactly and the same everywhere; hedge only rounded numbers

**Rule.** Give a headline result with its measured digits. Repeat the same digits and the same condition in the abstract, the results and the conclusions. Put "roughly" or "about" before a number that is rounded, read off a plot or extrapolated. Write a threshold or a setting exactly, in symbols.

**Why.** The approximator tells the reader which digits to trust. Identical headline numbers let the reader check that the three places report the same result.

**Evidence.** 5 of 6; usual; his own. "roughly" is his word and "approximately" is the CMS word (per 10,000 words: 9.5 and 0.5 in OWN, 2.1 and 5.3 in CMS). SAC gives 81 ps, 2.05 p.e./MeV and 1.8 ns in the abstract, the results and the conclusions, and "roughly 80 ps" only in a caption. Its energy resolution, extrapolated to 550 MeV from data at 100 to 400 MeV, takes "roughly" in the results (line 408 and the caption at line 395) and stands bare as 10% in the abstract and the conclusions; the digits agree and the hedge does not. Do not copy these two slips. "∼" before a number is also his (SAC 6, ETA 4). ETA prints the same branching-fraction expression three times [ETA main.tex:34, 287, 297]. IDM puts what was achieved in words ("about 90%", "greater than 97%") and what was imposed in symbols (pT > 80 GeV). His frame for a result is evidence, verb, value: "From the slope of the solid fit line in Fig. 14, we find a light yield of 2.05 p.e./MeV." [SAC main.tex:387]

- "The SAC timing resolution of roughly 80 ps meets PADME's requirements." [SAC main.tex:425]
- "The efficiency for the algorithm to reconstruct a vertex is roughly 70%." [THESIS paper.txt:8354]
- "The peak boundaries were set via a simple threshold (|ADC − pedestal|/4096 > 0.005)." [SAC main.tex:354]

**When not to apply.** Do not hedge a result quoted with its uncertainty, a count or a setting. Do not stack hedges ("roughly ∼40"). In a polish, do not add, remove or round on your own: ask the authors which digits are measured.

**Before.** The resolution is approximately 38.2 ps and gets worse (∼46 ps) near the edge. The trigger threshold was about 30 mV.

**After.** The time resolution is 38 ps at the center of the tile and roughly 46 ps at 2 mm from the edge. The trigger threshold is 30 mV.

### NUM-5. Word a gain as a factor or a percentage in a named quantity, with its price

**Rule.** Write "a factor of N", "N times", or a percentage with both end points. Name the quantity that gains and the reference. Use "compared to". Where the option has a cost, state it in the same sentence, with "while" or "but".

**Why.** "Improves" and "better" do not say in what or against what. A gain without its price reads as advocacy.

**Evidence.** 5 of 6 (IDM quotes no numerical gain); usual; his own. "a factor of": PROC 2, SAC 2, SCOUT 5, THESIS 3 outside the reprinted chapter. ETA has "more than 60 times the rate of the standard muon triggers". "compared to" against "compared with": SAC 4 to 1, IDM 4 to 0, ETA 6 to 0, SCOUT 40 to 5, THESIS 26 to 1. Gain and cost share a sentence in SAC, IDM, ETA, SCOUT and THESIS (in SAC in 2 of its gain statements, lines 211 and 215; the others state no cost). "only" marks a small fraction or a small loss.

- "Another possibility is moving the detector to Jefferson Lab, where a 12 GeV positron beam would increase the mass reach by a factor of 20." [PROC main.tex:190]
- "The new inclusive trigger provides a factor of 12 increase in the signal yield per fb^-1 with respect to the standard dimuon triggers available in Run 2." [SCOUT main.tex:1796]
- "Even coupling two of them provides only 11% of geometric acceptance, while doubling the cost." [SAC main.tex:211]

**When not to apply.** The change is small. Below a factor of about 1.5, use a percentage with both end points, as in the second quote of NUM-1.

**Before.** The two-SiPM readout significantly improves the timing performance.

**After.** The two-SiPM readout improves the time resolution by roughly 30%, from 54 ps to 38 ps, while doubling the number of readout channels.

### NUM-6. Give sober verdicts

**Rule.** Judge a result by whether it is enough: "meets", "sufficient", "acceptable", "reasonable", "negligible", "safe", "the preferred solution". Allow one mild adverb ("already"; "comfortably" occurs once in the six documents). Word agreement as "agrees with", "is consistent with" or "is in agreement with", and put the reference value beside it.

**Why.** The reader trusts a verdict that claims no more than the number shows. Praise makes a referee look for the weak point.

**Evidence.** PROC, SAC, THESIS, IDM and ETA (5 of 6); always there; his own. SAC has "meet(s)" 7 times and "negligible" 3 times. "outperform", "state-of-the-art", "impressive" and "good agreement" occur 0 times in all six. "agrees well" occurs once in SAC. "consistent with": IDM 1, ETA 2, SCOUT 11, THESIS 5. "agrees well with" occurs twice in OWN and "in agreement with" twice in the thesis; "consistent with" is absent from SAC and PROC. SCOUT is the exception: it has "significantly" 18 times, mostly before a verb of gain ("significantly reduce", "significantly enhanced"), "excellent" 9 times, and closers such as "remarkable capabilities" [SCOUT main.tex:783]. It is a review with many contributors.

- "This has acceptable timing resolution while providing sufficient light yield for the low beam energies in the experiment, at a reasonable cost." [SAC main.tex:236]
- "Hence, PbF2 is the preferred solution for PADME's requirements." [SAC main.tex:178]
- "The sum of the predicted signal and background contributions agrees with the observation." [ETA main.tex:193]
- "The ensemble of control tests shows no statistically significant deviation between prediction and observation." [IDM main.tex:134]

**When not to apply.** A strong word may stand on a physical fact, once, with the number beside it: "This huge η production rate is critical to the study of its rare decay channels." [ETA main.tex:146]

**Before.** The measurement is in excellent agreement with simulation and significantly outperforms the requirement.

**After.** The measured resolution of 38 ps agrees with the simulated value of 37 ps within the uncertainty, and meets the 50 ps requirement.

### NUM-7. State a caveat where it arises, then weigh it

**Rule.** Put the limitation in the paragraph of the number it affects, in one flat sentence ("is not accurate", "can only correct for", "Note that"). Say which way the number errs. Then say in one sentence why the result still serves; in his own voice that sentence often opens with "Nevertheless,". Take that sentence from the authors; do not supply it. Keep the plain adjective with which the authors name an approximation, and report a setback as a finding.

**Why.** A reader who meets the caveat beside the number can size it at once. A limitations section at the end forces every earlier number to be read again.

**Evidence.** The caveat in place: 6 of 6, always; none of the six has a limitations section. "Nevertheless": SAC 5, THESIS 10 outside the reprinted chapter, SCOUT 2, PROC, IDM and ETA 0. The word belongs to his own voice. The CMS letters make the same move inside the sentence, with "but" [IDM main.tex:54] or a participle ("neglecting reconstruction inefficiencies" [ETA main.tex:146]). "Note that": SAC 6 (4 open a sentence of the running text, 1 is in a footnote, 1 in a caption) and none as a sentence opener in CMS. Direction words: "only an upper limit" [SAC main.tex:346], "This overestimates" [SAC main.tex:387], and "conservative" in PROC, SAC, ETA and THESIS. Three of the five "Nevertheless," in SAC follow a caveat on his own number (lines 245, 408, 447); a short concession stays inside the sentence with "but" (lines 282 and 406).

He names an approximation by a plain adjective on the noun: "a simple threshold" [SAC main.tex:354], "the empirical function" [SAC main.tex:338], "an order-of-magnitude estimate" [SAC main.tex:245], "simplified Monte Carlo (MC) simulations" [ETA main.tex:211]. Where a choice has no physical basis he says so once, flatly: "The choice of a Landau fit was empirically driven and not based on underlying physical processes." [SAC main.tex:282] Never add such a label yourself; if a fit function or a setting has no stated basis, ask the authors.

He reports a setback or a surprise as a finding, in the order what was seen, its cause, what is being done: "From this original set of data, a new source of backgrounds not previously accounted for was identified: beam-induced backgrounds." [PROC main.tex:134] An odd entry of a table is explained where it stands: "The jet uncertainties are larger in 2017 because of noise issues with the ECAL endcap." [IDM main.tex:161] The five papers never say "unfortunately".

- "The assumption of uniformity is not accurate, as most of the energy deposits happen early on during the shower development inside a crystal. Nevertheless, we are only interested in an order-of-magnitude estimate of radiation dose, to show that radiation damage on the crystals will be negligible throughout the experiment and that we can safely mitigate concerns about transparency losses." [SAC main.tex:245]
- "Therefore the energy resolution quoted here is only an upper limit to the actual one achievable by PADME, and should be interpreted as a single-crystal SAC energy resolution." [SAC main.tex:346]

**When not to apply.** The caveat undoes the claim. Then weaken the claim. Use "Nevertheless," once per caveat. In a polish, add "Nevertheless," only when the sentence right before states a weakness, a limit or a rejected option, the sentence itself is already in the draft, and it speaks of the same result or object. A result for another range, sample or quantity is not what still holds: leave it without a connector, and when you are not sure, put the question in the report.

**Before** (in a closing "Limitations" section). The reference detector was not recalibrated, which may affect our results.

**After** (in the results paragraph). The resolution of the reference detector, 12 ps, is taken from an earlier campaign and was not remeasured. Nevertheless, it enters in quadrature, and a change of 2 ps moves the tile resolution by less than 1 ps.

### NUM-8. Explain every trend, outlier and curve shape by its cause

**Rule.** When a value rises, falls, saturates or stands out, give the physical or procedural cause in the same sentence or the next ("due to", "because of", "since").

**Why.** An unexplained feature makes the reader ask whether it is a mistake. One clause of cause answers the question.

**Evidence.** 5 of 6 (PROC reads no figure); usual; his own. SAC explains the fall of light yield with length, and why the timing resolution does not depend on beam energy. ETA explains the plateau, the low end and the high end of its efficiency curve in three consecutive sentences [ETA main.tex:237-241]. IDM explains two outliers of its uncertainty table in the caption [IDM main.tex:161]. The causal word is "due to" in his own voice and more often "because of" in CMS.

- "The light yield decreases with increasing length due to a higher chance of Cherenkov photons getting lost (absorbed or escaping) while traveling towards the PMT." [SAC main.tex:284]
- "In two-muon decays, A2μ^i,j is limited by the trigger efficiency, reaching a plateau of about 70%." [ETA main.tex:237]
- "The higher uncertainties in the 2 GM-dSA match category are due to limited statistical power compared to the other categories." [THESIS paper.txt:14815]

**When not to apply.** The cause is not established. Mark it with one hedge ("is understood to be" [ETA main.tex:238-239]) or say that it was not studied. Do not guess.

**Before.** The resolution is worse near the edge of the tile.

**After.** The time resolution degrades from 38 ps at the center to roughly 46 ps at 2 mm from the edge, due to the lower light collection near the tile boundary.

### NUM-9. Describe each uncertainty with one template

**Rule.** For each source write, in this order: where it comes from; what is varied and by how much; what is compared with the nominal; what "is taken as" the uncertainty; how it is correlated or combined; the table. Put the largest first and call it "dominant". Give the total with its combination rule. Quote the result with each term labeled.

**Why.** The same order for every source lets the reader find the size and the method of any one of them without reading the others.

**Evidence.** 4 of 6 (THESIS, ETA, IDM, SCOUT); always where a budget exists. The template is CMS practice, and he follows it unprompted in his thesis: the six sections of chapter 11 use it, with "taken as" four times. ETA gives cause ("are caused by"), procedure ("are estimated by varying"), value, and the total, "adding all contributions in quadrature" [ETA main.tex:279]. IDM gives three sentences and a table with a correlation column. SAC has no budget and ranks its sources in words [SAC main.tex:408]. IDM and SCOUT write "uncertainty in"; ETA has both ("in" 5 times, "on" 3 times); THESIS has "uncertainty on" 12 times against 4. Use "in".

- "We estimate the uncertainty on the trigger weight by varying the data and simulation measurements independently based on their statistical uncertainties (up and down by 1σ) and recalculating the weights. These new weights are then fed into the analysis workflow and the new signal yields are compared to the nominal ones. The envelope of the percent discrepancy (i.e. the maximum uncertainty across all signal samples) is conservatively taken as the scale factor uncertainty." [THESIS paper.txt:14656]
- "With B(η → 2μ) = (5.8 ± 0.8) × 10^-6, the branching fraction of the newly observed four-muon decay channel is measured to be B(η → 4μ) = [5.0 ± 0.8 (stat) ± 0.7 (syst) ± 0.7 (B2μ)] × 10^-9, where the last term reflects the uncertainty in B(η → 2μ)." [ETA main.tex:285]

**When not to apply.** An effect is shown to be negligible. Then one clause is enough: "but it is negligible compared to the other uncertainties" [ETA main.tex:263].

**Before.** Systematic effects were studied and found to be small.

**After.** The dominant systematic uncertainty arises from the resolution of the reference detector. It is estimated by varying this resolution by ±2 ps. The resulting change of 0.7 ps is taken as the uncertainty. Adding all contributions in quadrature, the time resolution is 38.0 ± 0.4 (stat) ± 0.9 (syst) ps.

### NUM-10. Compare with the baseline under the same conditions, and credit the weaker option

**Rule.** Name both options. Say what they share, and on which sample and settings both are measured. Give the weaker one its number and the case where it would be the better choice. Close with a short verdict tied to the requirement.

**Why.** A comparison convinces only if the reader sees that the baseline had a fair run. A point conceded to the rejected option shows that it was examined.

**Evidence.** 5 of 6 (not PROC); usual; his own. SAC section 3 has two materials and two photomultipliers, what both share, the disadvantage with a number, a table, the verdict, and the use case of the rejected option. IDM and THESIS compare the displaced and the standard muon reconstruction on "a representative signal sample" and put strength and weakness in one sentence. ETA describes the standard triggers and their rate before the new ones. A comparison at a matched working point occurs only in SCOUT [SCOUT main.tex:1572], in a contributor's part.

- "Both materials are suitable Cherenkov radiators due to their high refractive index, allowing for good timing resolution. However, SF57 has two (related) main disadvantages compared to PbF2." [SAC main.tex:168]
- "The DSA muons have higher reconstruction efficiencies but degraded momentum resolution and impact parameter resolution compared to muons reconstructed with the standard algorithm." [IDM main.tex:121]
- "Nevertheless, for higher energy applications, the two-PMT setup could be an interesting solution to explore." [SAC main.tex:211]

**When not to apply.** The baseline is a published number obtained elsewhere. Quote it with its own conditions and state the difference.

**Before.** Our two-SiPM readout is far superior to the conventional single-SiPM readout.

**After.** Both readout schemes are measured with the same tile, in the same beam, at the same overvoltage. The single-SiPM readout needs half the channels but reaches only 54 ps. Hence, the two-SiPM readout is the preferred solution for the 50 ps requirement.

### NUM-11. Describe a procedure as counted steps with exact settings

**Rule.** Announce the number of steps. Give them in the order the data pass through them ("First", "then", "Finally"), each with its exact setting in symbols or in parentheses. Give the reason for the one setting that is not obvious. Close a block of requirements with what it achieves and what it costs.

**Why.** The count tells the reader when the description is complete. Exact settings make the step repeatable. The closing sentence turns a list of settings into a result.

**Evidence.** 5 of 6; usual; his own. SAC has "in three steps", then "First", "After" and "Finally" [SAC main.tex:352-364], thresholds in parentheses, and a separate short paragraph for the reason of the threshold. In IDM, a hand count finds 7 of 12 requirements with a stated purpose; two blocks close on a percentage and its cost. ETA says what is deliberately not done ("no additional selection is applied" [ETA main.tex:138]). The tense is past passive for a laboratory procedure done once (SAC) and present passive for a selection (CMS). SAC and THESIS say "cut"; IDM and ETA say "selection" or "requirement".

- "The total energy deposited in the crystal was reconstructed in three steps." [SAC main.tex:352]
- "The choice of threshold was made to mitigate the after-pulse ringing which can be seen in the figure." [SAC main.tex:362]
- "These requirements remove more than 90% of the electroweak SM backgrounds without incurring a significant loss of signal efficiency." [IDM main.tex:119]

**When not to apply.** Do not narrate the order in which settings were tried. His papers give the final procedure only.

**Before.** Pulses are selected with several quality cuts, which were tuned for good performance.

**After.** The arrival time is extracted in three steps. First the baseline is computed from the 50 samples before the pulse. Then the rising edge is fit to a straight line between 10% and 90% of the amplitude. Finally the time at which the fit crosses 20% of the amplitude is taken as the arrival time.

### NUM-12. Describe a component or a sample in a fixed order

**Rule.** For a piece of apparatus: its role; "consists of" with count, material and dimensions; what follows from the geometry; one performance number with its condition; the figure. For a simulation: purpose and tool with citation; what it contains; inputs and sample size in one short sentence; what is left out or assumed, named as such.

**Why.** A reader who knows the order can find a given number in any component paragraph. Naming what is left out stops the reader from assuming it is there.

**Evidence.** Apparatus: PROC, SAC, THESIS; always; his own. "consist(s) of": PROC 2, SAC 3, THESIS 35. The CMS detector paragraph is shared boilerplate ("superconducting solenoid of 6 m internal diameter" is in IDM, ETA and SCOUT) and is not his. Simulation: SAC describes three simulations in this order, with the sample size in a short clause ("we generated 400 million events" [SAC main.tex:243]). The CMS papers and THESIS give the chain in processing order, one tool per sentence with version and citation. IDM, ETA and SCOUT contain no hyperparameter, loss function or training schedule.

- "The ECAL consists of 616 BGO scintillating crystals (from the old L3 experiment at LEP) with dimensions 21x21x230 mm^3 each, arranged in a cylindrical orientation." [PROC main.tex:86]
- "The ECAL is placed roughly 3 m downstream from the target, and thus has an angular acceptance between 20 and 95 mrad." [PROC main.tex:86]
- "Note that we do not simulate the entire detector here, just a single crystal in the SAC." [SAC main.tex:270]

**When not to apply.** The component or the sample is standard. Cite it in one sentence and describe only what differs.

**Before.** We simulated the detector with Geant4 using a large sample.

**After.** The response of the tile is simulated with Geant4. The simulation contains the tile, its wrapping and the two SiPMs. We generate 100,000 electrons of 4 GeV at normal incidence. Note that the readout electronics are not simulated.

### NUM-13. Report a cross-check as purpose, test, verdict, consequence

**Rule.** Open with the question the check answers ("To check whether ...", "To validate ..."). Name the sample and what was done, in the past tense. Give the outcome in one short sentence. Say what follows from it.

**Why.** The reader learns which doubt the check removes, and can move on once the verdict is given.

**Evidence.** Checks are reported in 5 of 6 (not PROC); usual; his own. A fronted purpose opens checks in IDM (1), ETA (2) and THESIS (4). SAC and SCOUT fold a routine check into a clause ("confirmed with", "which agrees with the estimate obtained from simulation"). The consequence follows at once: "this indicates" and "Based on these studies, we conclude" in ETA. In IDM, 31 closure tests lead to the decision to apply no systematic uncertainty to the background [IDM main.tex:134].

- "To check whether the observed peak is indeed compatible with the η → 4μ decay, the signal simulation was used to predict the four-muon pT (pT^4μ) spectrum for the experimentally measured branching fraction B(η → 4μ) of 5 × 10^-9 (described later)." [ETA main.tex:187]
- "Since the sidebands presumably contain more hadrons misidentified as muons, this indicates a negligible contamination of such hadrons in the signal region." [ETA main.tex:199]
- "We found zero events surviving the event selection." [THESIS paper.txt:9988]

**When not to apply.** The check tests nothing a reader would doubt. Leave it out, or give it one clause.

**Before.** Many cross-checks were performed and all gave consistent results.

**After.** To check that the result does not depend on the reference detector, the measurement was repeated with a second reference detector. This gives 38.4 ps, which agrees with the nominal value within the uncertainty.

### NUM-14. Keep units, rounding, ranges and number words uniform

**Rule.**

- Number, space, unit ("0.5 T"). The percent sign is attached ("10%").
- Two or three significant figures for a headline value, one or two for a working number and for an uncertainty ("5.0 ± 0.8").
- A range in words in running text ("between 100 and 400 MeV in steps of 100 MeV", "from 14 cm to 18 cm"). An en dash only for a window or in a table.
- Digits with any unit, also below ten ("3 mm", "4 months"), and for tallies. Words for a small count of things discussed ("two options", "three steps").
- Parallel values in the order of their labels, closed with "respectively".

**Why.** Uniform mechanics let the reader compare numbers without decoding each one.

**Evidence.** All six. PROC and SAC have no en-dash range; IDM has about 20, ETA about 10, SCOUT over 40. The dash is CMS and the words are his. "respectively" per 1,000 words: SAC 0.20, OWN 0.55, CMS 1.02. A shared unit is written once in CMS ("17 and 8 GeV") and repeated in his own text ("roughly 1 GeV and 4 GeV"). "standard deviations" and "confidence level" are spelled out in the CMS papers.

- "We define 32 bins in pT in the range 7–70 GeV and 2 bins in |y|." [ETA main.tex:259]
- "Specifically, the measured (predicted) yields are 2 (1.2 ± 0.6), 0 (0.5 ± 0.2), and 0 (0.5 ± 0.2) in the zero-, one-, and two-match categories, respectively." [IDM main.tex:183]

**When not to apply.** The journal's style sheet rules otherwise. Follow the journal and keep one form throughout.

**Before.** The beam energy was 1-5GeV and 3 overvoltages (2, 3.5, 5V) were used, giving 46 +- 1ps, 41 +- 1ps and 38 +- 1ps.

**After.** The beam energy was varied between 1 and 5 GeV in steps of 1 GeV. Three overvoltages were used, 2.0, 3.5, and 5.0 V, for which the time resolution is 46 ± 1, 41 ± 1, and 38 ± 1 ps, respectively.

### NUM-15. Wrap each equation in a sentence

**Rule.** Define the symbols in the text before a displayed equation or in a "where" clause after it. Lead in with a clause that ends in a colon. Keep displayed equations few, and define a one-line quantity inline.

**Why.** The reader meets the equation as part of a sentence and knows each symbol before using it.

**Evidence.** His own; SAC, PROC and THESIS, and it holds in the CMS papers. All four displayed equations of SAC (after lines 217, 222, 338 and 399) and the one of PROC (line 66) follow a lead-in clause that ends in a colon. The symbols are defined before the equation or in a "where" clause after it (SAC lines 344 and 406; ETA); the thesis continues with "Here, ..." [THESIS paper.txt:15133]. Displayed equations are few: SAC 4, PROC 1, ETA 3, SCOUT 6, IDM 0. IDM defines one-line quantities inline with "≡" (4 times).

- "The plot was fit to the empirical function:" [SAC main.tex:338], then "where f(E) is the average fraction of energy deposited on the crystal." [SAC main.tex:344]
- "First we calculate the number of p.e. produced by each configuration:" [SAC main.tex:217]

**When not to apply.** A journal may drop the colon where the equation completes the verb, as in "is measured to be" [ETA main.tex:285]. Never change an equation, a symbol or its definition in a polish.

**Before.** N = L × ε × G. Here we use the light yield, the photon detection efficiency and the gain.

**After.** The number of photoelectrons is estimated from the light yield L, the photon detection efficiency ε and the gain G: N = L × ε × G, where N is the number of photoelectrons per MIP.

## Measured targets

Rates are per 10,000 words of running text, from the measurement tables in `corpus-and-measurements.md`. "Aim for" applies to a short methods paper by a few authors. The full set of targets is Table B of `voice-and-transfer.md`.

| Measure | OWN | SAC | CMS | Aim for | Reason |
|---|---|---|---|---|---|
| "roughly" | 9.5 | 11.7 | 2.1 | 5 to 12 | His approximator for his own rounded numbers. |
| "approximately" | 0.5 | 1.9 | 5.3 | 0 to 2 | The CMS word. |
| "about" before a number | 2.0 | 7.8 | 8.6 | 2 to 8 | Second approximator, in both registers. |
| "only" | 16.1 | 31.1 | 14.4 | 15 to 30 | Marks a small fraction, loss or scope. |
| "significantly" | 0.9 | 0.0 | 4.4 | 0 on a result without its number | Absent from the running text of SAC (once in a caption); 5 uses in OWN. |
| "compared to" | 5.7 | 5.8 | 10.2 | 5 to 10 | His comparison marker. |
| "with respect to" | 0.2 | 0.0 | 4.2 | 0 | CMS review diction. |
| "a factor of" | 1.4 | 3.9 | 1.2 | 2 to 4 | One per gain claimed. |
| "Nevertheless" | 3.4 | 9.7 | 0.5 | 3 to 10 | One per weighed caveat. |
| "note that" | 2.0 | 9.7 | 0.5 | 2 to 8 | Scope of a number or a procedure. |
| "we find" | 0.7 | 5.8 | 0.0 | 2 to 6 | Kept for headline results. |
| Numbers in the abstract (count) | PROC 3 | 12 | IDM 4, ETA 9 | the reference value and every headline result | The abstract carries the headline values. |
| "±" expressions in the source (count) | PROC 0 | 0 | 27 | every headline result | SAC gives no uncertainty; see below. |

## Do not copy

- **No uncertainty on a headline value.** SAC quotes 81 ps and 2.05 p.e./MeV without an uncertainty. A journal measurement needs one. Take the form from ETA (NUM-9).
- **A factor mixed with a percentage.** "by a factor of roughly 30%" [SAC main.tex:215]. Write "by roughly 30%".
- **Shorthand that an editor would remove.** "10x more radiation-hard" [SAC main.tex:177], "5x5 crystals" [SAC main.tex:408], "10k events" [SAC main.tex:330], "below a GeV" [PROC main.tex:86]. Write "ten times", "5 × 5", "10,000 events", "below 1 GeV".
- **Slips.** Fit parameters named p0 and p1 in the equation and p1 and p2 in the text [SAC main.tex:401-406]. "between 10–40%" [IDM main.tex:57], which joins "between" with a dash. Hyphens in ranges ("1-2%").
- **Thesis hedges on a verdict.** "The closure does seem robust." [THESIS paper.txt:12067] In a paper, give the test and its outcome.
- **Thesis genre.** A bullet list and a figure for every requirement, a subsection for rejected attempts, "statistics" for sample size, "uncertainty on".
- **CMS boilerplate.** The detector paragraph, "corresponding to an integrated luminosity of", "Upper limits are set on". Also the paired form "about 2-3% (1%) at low (high) displacements" [IDM main.tex:119], which saves space and is slow to read.
- **Review and letter register.** "These results confirm the good performance of" [SCOUT main.tex:682], "showing excellent agreement" [SCOUT main.tex:1269], "thus significantly extending" [SCOUT main.tex:658], "The pioneering sensitivity" [IDM main.tex:54]. SAC and PROC have nothing of this kind.
- **Figures without a reading.** PROC points to seven figures and never reads a number off one. Always read one number.

## Checklist

1. Does every number have its condition (sample, energy, range, working point) in the same sentence?
2. Does every performance number have its target, baseline or expectation in the same or the next sentence?
3. Is every metric defined before its first value?
4. Are the headline values identical, with the same condition, in the abstract, the results and the conclusions?
5. Does every headline value carry an uncertainty with labeled terms? If the draft gives none, ask the authors; do not invent one.
6. Is every rounded, read-off or extrapolated number marked "roughly" or "about", and is no exact result or setting hedged?
7. Is every gain a factor or a percentage in a named quantity, against a named reference, with its cost in the same sentence where it has one?
8. Are the verdicts free of praise ("excellent", "significantly better", "outperforms", "superior")?
9. Does each statement of agreement have the reference value beside it?
10. Is each caveat in the paragraph of the number it affects, followed by one sentence that weighs it?
11. Does every trend, outlier and curve feature have its cause in the same or the next sentence?
12. Does each uncertainty follow the template: source, variation, comparison, "is taken as", combination, table?
13. Are the method and the baseline compared on the same sample and settings, with the baseline's strength stated?
14. Are steps counted, settings exact, and units, ranges and number words uniform?
