# andre_style_check.py

`andre_style_check.py` measures the surface style of a draft and prints it next to the ranges of Andre Frankenthal's writing. It then lists the sentences that are worth a second look, with file and line.

The script is a smoke detector. It counts surface features of the text. It cannot judge meaning, and no flag is an order. A value outside a range tells you where to read again. It does not tell you that the text is wrong. The ranges describe his practice. They are not quotas: never add a connector, a "This" or a passive only to move a number.

The script is one file. It needs only the Python 3 standard library, uses no network and gives the same output for the same input.

## Run it

```
python3 scripts/andre_style_check.py draft.tex [more.tex ...] [--json]
        [--targets short-paper|cms-letter|thesis] [--max-flags N] [--dump]
```

| Option | Meaning |
|---|---|
| `--targets` | the profile of ranges: `short-paper` (default), `cms-letter` or `thesis` |
| `--max-flags N` | list at most N sentences per group (default 10) |
| `--json` | print the same data as JSON: the notice, the counts, one object per row of the table, one object per group of flags |
| `--dump` | print every sentence and caption as the script read it, with file, line, kind and word count, then stop |

Several files are read as one draft. Give the section files of a paper in their order. The script stops with an error if a file is missing or if it finds no sentence.

## What it reads

**LaTeX (`.tex`).** Comments, the preamble, the title, author lists, acknowledgments and the bibliography are dropped. Inline and display math become the word `MATH`. `\cite` becomes `CITE`, `\ref` becomes `REF`, and any other macro in the text becomes `SYM`. Simple text macros and unit macros are written out (`\GeV`, `\SI{5}{\ns}`, a `\newcommand` whose body is plain text). The abstract, the body, list items and footnotes form the running text. Captions of `figure` and `table` environments are read apart. Tables, `tikzpicture`, verbatim blocks and `\todo{...}` notes are dropped. Headings end a paragraph and are not counted as text. `\input` and `\include` are not followed: give those files on the command line. Macro definitions are taken from every file given, in any order, so give the file with the preamble too.

**Markdown (`.md`).** Headings, code blocks, table rows and front matter are dropped. List items, links, emphasis, `$...$` math and pandoc citations are handled. The text of an image (`![caption](file)`) and a paragraph that starts with "Figure 2:" or "Table 1." are read as captions.

**Plain text (`.txt`, or any other extension).** Blank lines separate paragraphs. Paragraphs that start with "Figure 2:", "Fig. 2." or "FIG. 2." are captions. `[12]` becomes `CITE`.

In Markdown and plain text, a paragraph of one sentence that does not end in a full stop, a question mark or a colon is taken as a heading and dropped, and the abstract counts as a body paragraph. Reading stops at a heading named References or Bibliography, or named Acknowledgments in the second half of the file.

**Line numbers.** A sentence is reported with the line of the source file on which it starts. A caption is reported with the line on which its text starts. If a paragraph is one long line, all its sentences carry that line.

**Words.** A word is a token between spaces that holds a letter or a digit. `MATH`, `SYM` and `REF` count as one word each. `CITE` counts as none. These are the rules of the measurement behind `references/corpus-and-measurements.md`, so a value printed by the script can be set beside the numbers in the reference files.

## The table

Each row gives a metric, the value of the draft, his range for the chosen profile, and a mark where the draft is outside the range:

```
metric                                                                        draft  his range    mark
  words per sentence, median                                                      9  19 to 22     below
  sentences containing "we", %                                            75.0 (27)  at most 20   above
  "see Fig. N" outside parentheses, count                                         1  0            above
  "Section" in full, count                                                        0  -
```

The number in parentheses is the count behind a share or a rate. A row with the range `-` is shown for information.

The marks are not a score. The ranges describe a whole paper, and they are not quotas. Never choose between two wordings by the number of marked rows: an edit that the skill asks for (a pointer, a split semicolon, a "Hence," verdict) can move a length feature out of its range, and is kept. For a text of fewer than 100 sentences the script does not print the number of marked rows; use its list of sentences instead. In [SAC] itself the median of 44 consecutive sentences runs from 18 to 23.5 words.

A marked row tells you which reference file to open:

| Marked rows | Read |
|---|---|
| Sentences, voice, openers, punctuation | `references/sentences-and-voice.md` |
| Paragraphs | `references/paragraphs-and-flow.md` |
| Connectors, causal words, approximators, intensifiers, praise, abbreviations | `references/words-and-phrases.md` |
| Captions, references to figures and tables | `references/figures-and-captions.md` |
| Any row, to tell his own voice from CMS house style | `references/voice-and-transfer.md` |

**When a row is marked.** A count is marked as soon as it is outside the range. So is a median, in a text of 100 sentences or more; in a shorter text a median must be at least 1.5 units (words, sentences) outside the range. A share or a rate is marked only when the draft is at least 1.5 items outside the range, where an item is a sentence, a paragraph, a caption or an occurrence. So one sentence cannot produce a mark in a short text: with 30 sentences, 3 sentences that open with "We" (10%) are not marked against the range "at most 8%", and 4 are. The row "causal words in use" is marked only for a text of 1500 words or more.

### How each row is counted

| Rows | Rule |
|---|---|
| Sentences | Words per sentence in the running text. Shares of sentences with 12 words or fewer, with more than 30 and with more than 40. |
| Paragraphs | Body paragraphs only: the abstract, list items and footnotes are left out. A display equation, `\noindent` or a lower-case start continues the paragraph before. |
| "we" | A sentence that holds "we". A sentence whose first word is "We" or "Our". |
| Passive | A form of "be" followed within three words by a past participle (a word in -ed, or one of a list of irregular forms). The search stops at a determiner, a preposition or a comma. A reduced passive ("data collected in 2018") is not counted. An adjectival participle ("is expected") is. |
| Openers | Each sentence goes into the first class that fits, in this order: connector (the list of 31 below); other connector or sentence adverb; The, This, These, A, An, Each, All; We, Our; fronted phrase (In, For, To, At, After, Before, Since, While, Because, As, When, If, With, By, From, Due to, Given, Using, Although). So "For example," is a connector and not a "For". "This" + verb: the second word is one of about 60 verb forms (is, leads, allows, ensures, makes, ...). |
| Connectors one by one | His seven are always shown. Any other connector that opens a sentence is added. |
| Causal words | "since" is counted when it gives a reason ("since 2018", "since then" and "ever since" are not). "because" includes "because of". "so" is counted as a conjunction: after a comma or a semicolon, after "and", before "that", or as the first word. "so far", "so-called", "or so" and "do so" are not counted. |
| Approximators | approximately, roughly, nearly, almost, and "about" or "around" before a number. "about" + number: "about" followed by a digit, `MATH`, a number word or "a factor". |
| Intensifiers, praise, sufficiency | The six intensifiers: very, significantly, highly, extremely, strongly, clearly. The seventeen praise words: novel, excellent, powerful, unprecedented, remarkable, outstanding, innovative, exciting, compelling, pivotal, paramount, unique, groundbreaking, pioneering, superior, state-of-the-art, impressive. The twelve sufficiency words with their adverbs: moderate, acceptable, sufficient, reasonable, negligible, manageable, satisfactory, safe, comfortably, adequate, modest, conservative. |
| Punctuation | Semicolons. Colons that are not followed by a digit. Dashes as punctuation: an em dash, an en dash between spaces, a hyphen between spaces. Parenthesis pairs: opening parentheses. |
| Captions | Words and sentences per caption. A caption opens with a noun phrase without article unless its first word is The, A or An, a panel word (Left, Right, Top, ...), a preposition, or This, These, Each, All, We or Shown. A leading label such as "(a)" is skipped, and a symbol counts as a noun phrase. The first sentence has no finite verb when it holds none of a list of about 50 verbs (is, are, shows, compares, ...). |
| References | A reference is "Fig.", "Figs.", "Figure", "Table" or "Tab." before a number or a `\ref`. Float as subject: the float is followed by a verb such as shows, lists, summarizes, illustrates or compares. "is shown in": one of 25 phrases (shown in, seen in, listed in, summarized in, plotted in, reported in, ..., and the forms with "as") stands before the float. "as shown in" is counted in that row and again in its own row. |
| Abbreviations | "Sec." and "Section" in the running text and the captions. "Fig." and "Figure" at the start of a sentence and inside it, in the running text. |

The 31 connectors of the row "connector": However, Therefore, Thus, Hence, Moreover, Furthermore, In addition, Additionally, Finally, Consequently, Nevertheless, Similarly, Indeed, For example, For instance, In particular, Specifically, Note that, Also, Then, Next, First, Second, Lastly, On the other hand, In contrast, As a result, In this way, Overall, In summary, In conclusion.

## The three profiles

**short-paper** (default) is for a methods paper by a few authors. Its ranges are the "Aim for" values of Table B in `references/voice-and-transfer.md`, which is the reference for every range of this skill. Where the target table of another reference file gave a different range for the same feature when the script was written, the value of Table B was taken. A row that Table B does not have comes from the target table of another file: punctuation from `sentences-and-voice.md`; "about" + number, intensifiers, praise and sufficiency words from `words-and-phrases.md`; references per 1000 words from `figures-and-captions.md`. Two rows are coded by the script: "about half" of the "This" openers is read as 40% to 60%, and the share of captions without a finite verb in the first sentence is set to 90% or more (his three own-voice documents have 95% to 100%, and the verb list makes errors).

**cms-letter** is for a letter under CMS style rules. Each end of a range is the lower or the higher value of the two letters [IDM] and [ETA], moved outward by about three percentage points for a share of sentences and by one unit for a median, then rounded. Rows that rest on few items (17 paragraphs, 6 or 7 captions, 8 references in each letter) span the two values with a rounded margin. The causal words keep the form of Table B.

**thesis** follows [THESIS] in the same way.

The "Fig." and "Figure" rows hold the form of his two Physical Review Letters: "Figure" at the start of a sentence and "Fig." inside. His thesis writes "Figure" everywhere. If the journal has another rule, follow the journal and ignore these rows.

| Row | short-paper | cms-letter | thesis |
|---|---|---|---|
| **Sentences** | | | |
| words per sentence, median | 19 to 22 | 21 to 24 | 19 to 21 |
| sentences of 12 words or fewer, % | 13 to 18 | 6 to 13 | 14 to 20 |
| sentences above 30 words, % | 13 to 18 | 17 to 29 | 12 to 18 |
| sentences above 40 words, % | 2 to 5 | 4 to 13 | 1 to 6 |
| **Paragraphs** | | | |
| sentences per paragraph, median | 3 to 5 | 5 to 9 | 3 to 5 |
| words per paragraph, median | 60 to 110 | 140 to 190 | 60 to 110 |
| paragraphs of one sentence, % | at most 6.7 | at most 4 | at most 12 |
| paragraphs of 8 or more sentences, % | at most 5 | 25 to 58 | at most 9 |
| **Voice** | | | |
| sentences containing "we", % | at most 20 | 2 to 9 | 3 to 9 |
| sentences opening with "We" or "Our", % | at most 8 | at most 5 | at most 5 |
| sentences with a passive, % | 35 to 45 | 50 to 59 | 35 to 45 |
| **Sentence openers, % of sentences** | | | |
| The, This, These, A, An, Each, All | 45 to 55 | 48 to 62 | 42 to 52 |
| "This" | 6 to 10 | 3 to 11 | 7 to 13 |
| "This" + verb, % of the "This" openers | 40 to 60 | 20 to 50 | 40 to 60 |
| fronted phrase (In, For, To, Since, With, ...) | 11 to 16 | 8 to 17 | 9 to 15 |
| "For" | at most 3 | at most 3 | at most 3 |
| "With" | at most 1 | at most 1 | at most 1.5 |
| "To" | 2 to 4 | 1 to 8 | at most 4 |
| connector (list of 31) | 7 to 11 | 3 to 9 | 6 to 11 |
| **Connectors at the start, one by one, % of sentences** | | | |
| each connector | at most 2 | at most 2 | at most 2 |
| a connector of the avoid list (In addition, Additionally, As a result, Notably, ...) | 0 | 0 | at most 0.2 |
| **Causal words, per 10,000 words** | | | |
| since (causal) | at most 20 | at most 20 | at most 25 |
| due to | at most 20 | at most 20 | at most 25 |
| therefore | at most 20 | at most 20 | at most 25 |
| because (with "because of") | at most 20 | at most 20 | at most 25 |
| hence | at most 20 | at most 20 | at most 25 |
| thus | at most 20 | at most 20 | at most 25 |
| "so" as a conjunction (", so", "and so", "so that") | at most 6 | at most 3 | at most 7 |
| causal words in use, of these seven | at least 4 | at least 4 | at least 4 |
| **Approximators, per 1000 words** | | | |
| all (approximately, roughly, about/around + number, nearly, almost) | 1.5 to 2.5 | 1.3 to 4.3 | 1 to 2.2 |
| roughly | 0.5 to 1.2 | at most 0.5 | 0.5 to 1.5 |
| about + number | 0.2 to 0.8 | 0.7 to 3 | at most 0.6 |
| approximately | at most 0.2 | 0.2 to 1 | at most 0.2 |
| **Intensifiers, praise and sufficiency** | | | |
| six intensifiers (very, significantly, highly, ...), per 1000 words | at most 1 | at most 2 | at most 1.5 |
| praise words (list of 17), per 10,000 words | at most 4 | at most 25 | at most 8 |
| sufficiency words (list of 12), per 10,000 words | 10 to 25 | 5 to 20 | 5 to 15 |
| **Punctuation, per 1000 words** | | | |
| semicolons | at most 1 | at most 1.5 | at most 1.2 |
| colons | 2 to 4 | 0.5 to 2.5 | 3 to 5.5 |
| dashes as punctuation | at most 0.2 | 0 | at most 0.8 |
| parenthesis pairs | 9 to 13 | 7 to 17 | 8 to 13 |
| **Captions** | | | |
| words per caption, median | 25 to 50 | 35 to 75 | 25 to 50 |
| longest caption, words | at most 100 | at most 100 | no range |
| sentences per caption, median | 1 to 3 | 2 to 4 | 1 to 3 |
| captions of 4 or more sentences, % | at most 25 | at most 55 | at most 20 |
| captions that open with a noun phrase without article, % | 100 | 85 to 100 | 95 to 100 |
| captions whose first sentence has no finite verb, % | 90 to 100 | 80 to 100 | 90 to 100 |
| **References to figures and tables** | | | |
| references per 1000 words | 3 to 6 | 1.8 to 3.3 | 3.5 to 6 |
| float as subject ("Figure N shows"), % of references | 30 to 50 | 10 to 55 | 40 to 55 |
| "is shown in Fig. N" and its variants, % of references | 35 to 45 | 45 to 80 | 30 to 42 |
| "as shown in Fig. N", count | at most 1 | at most 1 | at most 2 |
| "(Fig. N)" or "(see Fig. N)", count | at most 1 | at most 1 | at most 1 |
| "see Fig. N" outside parentheses, count | 0 | 0 | 0 |
| **Abbreviations** | | | |
| "Sec." or "Secs.", count | no range | no range | 0 |
| "Section" in full, count | no range | no range | no range |
| sentences that start with "Fig.", count | 0 | 0 | 0 |
| sentences that start with "Figure", count | no range | no range | no range |
| "Figure" in full inside a sentence, count | 0 | 0 | no range |

## Sentences to look at

The second part of the output lists sentences in ten groups. Each entry has the file, the line, a short reason and the start of the sentence. `--max-flags` caps each group.

| Group | A sentence is listed when |
|---|---|
| Runs of "We" | three or more sentences in a row, in one paragraph, start with "We". One entry per run. |
| "so" as the causal join | it holds "so" as a conjunction (", so", "and so", "so that", or "So" as the first word). |
| Float in parentheses or with "see" | it holds "(Fig. N)", "(see Fig. N)", "(e.g. Fig. N)" or "see Fig. N", for a figure or a table. |
| Captions | the caption opens with an article; or does not open with what is plotted (a preposition, This, We, a panel word); or its first sentence has a verb from a short list of verbs that are not also nouns (is, are, shows, compares, ...); or it has more words or more sentences than the upper end of the range for the median (50 words and 3 sentences in `short-paper`); or it holds "we". |
| Avoid list | it holds an entry of the avoid list of `references/words-and-phrases.md`: utilize, leverage, facilitate, showcase, outperform, state-of-the-art, impressive, superior, groundbreaking, pioneering, substantially, crucially, good agreement, excellent agreement, it should be noted, as can be seen, we observe, we see, we believe, we note, we call, so-called, etc., in other words, to this end, in conclusion, lastly, nonetheless, obviously, as a result, with respect to. A dash used as punctuation is listed here too (he has one dash construction in a paper at most). The plain form is printed after the colon. "as can be seen" is the tag only: "X can be seen in Fig. N" is his and is not listed. A term that the draft defines and uses throughout stays. |
| Intensifiers and praise | it holds one of the six intensifiers or one of the praise words that are not already in the avoid list. |
| Long sentences | it has more than 45 words and is not a list. A list has a colon, a semicolon, two enumerators such as (a) and (b), or three short items in a row between commas. |
| Connectors that his own texts do not open with | it starts with a connector or a sentence adverb that is not in the list below. |
| "Sec." and "Tab." | it holds "Sec.", "Secs.", "Tab." or "Tabs.", in the text or in a caption. "Sec." occurs in none of the six documents, but the journal decides: where it prints "Sec.", keep the draft's form and name it in the report. |
| "approximately" before a number | information only. His own voice rounds with "roughly" or "about". CMS style prefers "approximately", so keep it where the paper follows CMS rules. The group is not printed with `--targets cms-letter`. |

**The connectors that open his sentences.** The seven frequent ones that the references name: Finally, However, Therefore, Furthermore, Nevertheless, Moreover, Note that. Also those that open a sentence in at least two of his three own-voice texts: Hence, Thus, First, Then, Consequently, In particular, For example, On the other hand, Here, Instead, In this case, At the same time; and Overall, which opens sentences in [THESIS] and [ETA]. `cms-letter` adds what else opens a sentence in the two letters: In summary, Specifically, In contrast, Subsequently. `thesis` adds what opens at least 0.1% of the thesis sentences: Similarly, Next, In contrast, In general, In fact, As mentioned, As discussed, As such, Conversely. It leaves out "And", "But", "Additionally" and "Notably", which the references list as slips or as words to avoid. The script looks for the 31 connectors above and for about 45 further connectors and sentence adverbs (Importantly, Interestingly, Notably, Meanwhile, In other words, And, But, So, ...). Adverbs of time and frequency (Now, Recently, Currently, Typically, ...) are not listed.

## Tests

The four papers were read from the LaTeX sources posted on arXiv: [PROC] arXiv:1910.00764, [SAC] arXiv:1809.10840, [IDM] arXiv:2305.11649 and [ETA] arXiv:2305.04904 (`main.tex`, here in folders named after the tags). The sources are not part of this repository.

### (a) His own texts with the default profile, and (b) a CMS letter with `--targets cms-letter`

```
python3 -I scripts/andre_style_check.py PROC/main.tex
python3 -I scripts/andre_style_check.py SAC/main.tex
python3 -I scripts/andre_style_check.py IDM/main.tex --targets cms-letter
python3 -I scripts/andre_style_check.py ETA/main.tex --targets cms-letter
```

| | [PROC] | [SAC] | [IDM] | [ETA] |
|---|---|---|---|---|
| Profile | short-paper | short-paper | cms-letter | cms-letter |
| Words | 1349 | 5138 | 3398 | 2880 |
| Sentences | 67 | 234 | 135 | 122 |
| Paragraphs | 14 | 61 | 17 | 17 |
| Captions | 7 | 20 | 6 | 7 |
| Rows that have a range | 63 | 68 | 62 | 65 |
| Rows marked | 3 | 2 | 0 | 0 |
| Sentences and captions listed | 2 | 20 | 20 | 10 |

| Row | [PROC] | [SAC] | short-paper | [IDM] | [ETA] | cms-letter |
|---|---|---|---|---|---|---|
| **Sentences** | | | | | | |
| words per sentence, median | 19 | 20 | 19 to 22 | 23 | 22 | 21 to 24 |
| sentences of 12 words or fewer, % | 19.4 (13) | 13.7 (32) | 13 to 18 | 9.6 (13) | 9.0 (11) | 6 to 13 |
| sentences above 30 words, % | 10.4 (7) **below** | 17.5 (41) | 13 to 18 | 25.9 (35) | 19.7 (24) | 17 to 29 |
| sentences above 40 words, % | 1.5 (1) | 4.3 (10) | 2 to 5 | 9.6 (13) | 7.4 (9) | 4 to 13 |
| **Paragraphs** | | | | | | |
| sentences per paragraph, median | 4.5 | 3 | 3 to 5 | 8 | 6 | 5 to 9 |
| words per paragraph, median | 93 | 74 | 60 to 110 | 176 | 151 | 140 to 190 |
| paragraphs of one sentence, % | 0.0 (0) | 6.6 (4) | at most 6.7 | 0.0 (0) | 0.0 (0) | at most 4 |
| paragraphs of 8 or more sentences, % | 0.0 (0) | 3.3 (2) | at most 5 | 52.9 (9) | 29.4 (5) | 25 to 58 |
| **Voice** | | | | | | |
| sentences containing "we", % | 3.0 (2) | 19.2 (45) | at most 20 | 5.9 (8) | 4.9 (6) | 2 to 9 |
| sentences opening with "We" or "Our", % | 1.5 (1) | 7.7 (18) | at most 8 | 2.2 (3) | 0.8 (1) | at most 5 |
| sentences with a passive, % | 37.3 (25) | 42.7 (100) | 35 to 45 | 55.6 (75) | 52.5 (64) | 50 to 59 |
| **Sentence openers, % of sentences** | | | | | | |
| The, This, These, A, An, Each, All | 44.8 (30) | 47.0 (110) | 45 to 55 | 51.9 (70) | 58.2 (71) | 48 to 62 |
| "This" | 6.0 (4) | 6.8 (16) | 6 to 10 | 5.9 (8) | 8.2 (10) | 3 to 11 |
| "This" + verb, % of the "This" openers | 50.0 (2) | 56.2 (9) | 40 to 60 | 50.0 (4) | 20.0 (2) | 20 to 50 |
| fronted phrase (In, For, To, Since, With, ...) | 11.9 (8) | 15.4 (36) | 11 to 16 | 11.1 (15) | 13.9 (17) | 8 to 17 |
| "For" | 0.0 (0) | 3.0 (7) | at most 3 | 0.7 (1) | 1.6 (2) | at most 3 |
| "With" | 0.0 (0) | 0.8 (2) | at most 1 | 0.0 (0) | 0.8 (1) | at most 1 |
| "To" | 1.5 (1) | 2.1 (5) | 2 to 4 | 4.4 (6) | 4.1 (5) | 1 to 8 |
| connector (list of 31) | 7.5 (5) | 10.7 (25) | 7 to 11 | 5.9 (8) | 5.7 (7) | 3 to 9 |
| **Connectors at the start, one by one, % of sentences** | | | | | | |
| Finally | 1.5 (1) | 0.4 (1) | at most 2 | 2.2 (3) | 0.8 (1) | at most 2 |
| However | 0.0 (0) | 0.8 (2) | at most 2 | 0.7 (1) | 0.8 (1) | at most 2 |
| Therefore | 0.0 (0) | 0.4 (1) | at most 2 | 0.0 (0) | 0.8 (1) | at most 2 |
| Furthermore | 1.5 (1) | 1.3 (3) | at most 2 | 0.0 (0) | 0.8 (1) | at most 2 |
| Nevertheless | 0.0 (0) | 2.1 (5) | at most 2 | 0.0 (0) | 0.0 (0) | at most 2 |
| Moreover | 3.0 (2) | 0.0 (0) | at most 2 | 0.7 (1) | 0.0 (0) | at most 2 |
| Note that | 0.0 (0) | 1.7 (4) | at most 2 | 0.0 (0) | 0.0 (0) | at most 2 |
| **Causal words, per 10,000 words** | | | | | | |
| since (causal) | 7.4 (1) | 5.8 (3) | at most 20 | 5.9 (2) | 3.5 (1) | at most 20 |
| due to | 7.4 (1) | 17.5 (9) | at most 20 | 5.9 (2) | 0.0 (0) | at most 20 |
| therefore | 14.8 (2) | 5.8 (3) | at most 20 | 5.9 (2) | 3.5 (1) | at most 20 |
| because (with "because of") | 0.0 (0) | 0.0 (0) | at most 20 | 17.7 (6) | 10.4 (3) | at most 20 |
| hence | 0.0 (0) | 7.8 (4) | at most 20 | 0.0 (0) | 3.5 (1) | at most 20 |
| thus | 7.4 (1) | 5.8 (3) | at most 20 | 8.8 (3) | 0.0 (0) | at most 20 |
| "so" as a conjunction (", so", "and so", "so that") | 0.0 (0) | 5.8 (3) | at most 6 | 2.9 (1) | 0.0 (0) | at most 3 |
| causal words in use, of these seven | 4 | 6 | at least 4 | 6 | 4 | at least 4 |
| **Approximators, per 1000 words** | | | | | | |
| all (approximately, roughly, about/around + number, nearly, almost) | 0.74 (1) | 2.34 (12) | 1.5 to 2.5 | 1.77 (6) | 3.82 (11) | 1.3 to 4.3 |
| roughly | 0.74 (1) | 1.17 (6) | 0.5 to 1.2 | 0.00 (0) | 0.35 (1) | at most 0.5 |
| about + number | 0.00 (0) | 0.78 (4) | 0.2 to 0.8 | 1.18 (4) | 2.43 (7) | 0.7 to 3 |
| approximately | 0.00 (0) | 0.19 (1) | at most 0.2 | 0.59 (2) | 0.69 (2) | 0.2 to 1 |
| **Intensifiers, praise and sufficiency** | | | | | | |
| six intensifiers (very, significantly, highly, ...), per 1000 words | 0.00 (0) | 0.78 (4) | at most 1 | 1.77 (6) | 1.04 (3) | at most 2 |
| praise words (list of 17), per 10,000 words | 0.0 (0) | 3.9 (2) | at most 4 | 23.5 (8) | 0.0 (0) | at most 25 |
| sufficiency words (list of 12), per 10,000 words | 7.4 (1) | 27.2 (14) | 10 to 25 | 8.8 (3) | 17.4 (5) | 5 to 20 |
| **Punctuation, per 1000 words** | | | | | | |
| semicolons | 0.00 (0) | 0.97 (5) | at most 1 | 0.59 (2) | 1.04 (3) | at most 1.5 |
| colons | 4.45 (6) | 2.53 (13) | 2 to 4 | 1.77 (6) | 1.04 (3) | 0.5 to 2.5 |
| dashes as punctuation | 1.48 (2) **above** | 0.19 (1) | at most 0.2 | 0.00 (0) | 0.00 (0) | 0 |
| parenthesis pairs | 11.86 (16) | 12.85 (66) | 9 to 13 | 15.60 (53) | 9.03 (26) | 7 to 17 |
| **Captions** | | | | | | |
| words per caption, median | 24 | 42 | 25 to 50 | 69.5 | 38 | 35 to 75 |
| longest caption, words | 53 | 97 | at most 100 | 92 | 87 | at most 100 |
| sentences per caption, median | 1 | 2 | 1 to 3 | 3.5 | 2 | 2 to 4 |
| captions of 4 or more sentences, % | 0.0 (0) | 25.0 (5) | at most 25 | 50.0 (3) | 28.6 (2) | at most 55 |
| captions that open with a noun phrase without article, % | 100.0 (7) | 100.0 (20) | 100 | 100.0 (6) | 85.7 (6) | 85 to 100 |
| captions whose first sentence has no finite verb, % | 100.0 (7) | 95.0 (19) | 90 to 100 | 83.3 (5) | 100.0 (7) | 80 to 100 |
| **References to figures and tables** | | | | | | |
| references per 1000 words | 5.19 (7) | 5.64 (29) | 3 to 6 | 2.35 (8) | 2.78 (8) | 1.8 to 3.3 |
| float as subject ("Figure N shows"), % of references | 57.1 (4) | 31.0 (9) | 30 to 50 | 12.5 (1) | 50.0 (4) | 10 to 55 |
| "is shown in Fig. N" and its variants, % of references | 42.9 (3) | 41.4 (12) | 35 to 45 | 75.0 (6) | 50.0 (4) | 45 to 80 |
| "as shown in Fig. N", count | 0 | 0 | at most 1 | 0 | 1 | at most 1 |
| "(Fig. N)" or "(see Fig. N)", count | 0 | 2 **above** | at most 1 | 0 | 0 | at most 1 |
| "see Fig. N" outside parentheses, count | 0 | 0 | 0 | 0 | 0 | 0 |
| **Abbreviations** | | | | | | |
| "Sec." or "Secs.", count | 0 | 0 | - | 0 | 0 | - |
| "Section" in full, count | 0 | 2 | - | 0 | 0 | - |
| sentences that start with "Fig.", count | 4 **above** | 8 **above** | 0 | 0 | 0 | 0 |
| sentences that start with "Figure", count | 0 | 0 | - | 1 | 4 | - |
| "Figure" in full inside a sentence, count | 0 | 0 | 0 | 0 | 0 | 0 |

Other connectors found at the start of a sentence: [PROC] For example 1, Here 1, In this case 1, Instead 1; [SAC] And 1, At the same time 1, Consequently 1, First 3, Hence 1, In particular 1, On the other hand 1, Then 1, Thus 1; [IDM] Here 2, In summary 1, Specifically 2; [ETA] Here 1, In contrast 1, In summary 1, In this case 1, Overall 1, Subsequently 1.

**[PROC], 3 marked rows.** Each is a known property of this six-page status report. The text has 67 sentences, so the script prints no total of marked rows for it.

- Sentences above 30 words: 7 of 67. The text describes an experiment in short sentences and gives few reasons at length.
- Dashes: one pair. "Moreover, two additional sub-detectors – the Positron Veto and Small-Angle Calorimeter (SAC) – help in the mitigation of Bremsstrahlung events." [PROC main.tex:102] The range allows the one dash construction of [SAC] (0.2 per 1000 words); in a text of 1349 words a pair counts 1.48.
- "Fig." at the start of 4 sentences. This is the form of the venue. The references list it under "do not copy" for a Physical Review paper.
- Not marked: sentences containing "we" (2 of 67; the range is "at most 20%", since the rate follows the genre) and the median of 24 words per caption (one word below the range, inside the margin of 1.5 that a median has in a text of fewer than 100 sentences).

**[SAC], 2 marked rows.**

- Sentences containing "we" (19.2%) and opening with "We" (7.7%) are inside the ranges "at most 20%" and "at most 8%": [SAC] is the model for a paper by a few authors, and the upper end of his practice.
- Floats cited in parentheses: 2, at [SAC main.tex:217] and [SAC main.tex:391]. Table B allows one.
- "Fig." at the start of 8 sentences: the form of the venue, as in [PROC].

**Sentences listed.** [PROC]: 2 entries (captions 1; avoid list and dashes 1). They are a caption of 53 words and the sentence with the pair of dashes. [SAC]: 20 entries ("so" 3; float in parentheses 2; captions 6; avoid list and dashes 1; intensifiers and praise 6; above 45 words 1; connectors 1). Most of them are habits or slips that the reference files also record:

- The three "so" joins, for example "The spectrum of Bremsstrahlung radiation is highly peaked at small angles, so the SAC receives most of the radiation." [SAC main.tex:243]
- The two floats cited in parentheses.
- Six captions with more than 50 words or more than three sentences. Table B allows a quarter of the captions to have four sentences or more, and [SAC] has 5 of 20.
- One dash, at [SAC main.tex:136].
- Four intensifiers and two praise words, the ones that `references/words-and-phrases.md` counts for [SAC].
- One sentence of 46 words, in the abstract.
- One connector that the list does not hold, "And": "And in the third, we simulate electrons striking a single crystal in order to match accurately the electron test beam results." [SAC main.tex:241]

**[IDM] and [ETA] with `--targets cms-letter`: no marked row.** This is by construction, since the profile brackets these two letters. The same texts against the other profile show how far CMS house style is from his own voice: [IDM] has 17 marked rows of 62 with `short-paper` (longer sentences, paragraphs of eight sentences, 56% passives, captions of 70 words), and [SAC] has 16 marked rows of 68 with `cms-letter`. Sentences listed for [IDM]: 20 entries ("so" 1; captions 3; avoid list and dashes 1; intensifiers and praise 13; above 45 words 2). For [ETA]: 10 entries (captions 3; intensifiers and praise 3; above 45 words 4). The avoid-list entry of [IDM] is "pioneering" [IDM main.tex:54], which the references list under "do not copy".

**`--targets thesis`.** The thesis exists only as PDF text, which this script does not clean well (see Limits). The profile was therefore checked on the thesis text as it was cleaned for the measurement: 2008 sentences, 184 captions, no marked row. (This check was made before the last revision of the script, which changed no range of the `thesis` profile.)

### (c) A text in another style

`scripts/example_draft.tex` is an invented passage of 407 words in a style that is not his: short sentences, "We" at the start of most of them, ", so" as the causal join, long captions and "see Fig.". The study is invented (a test-beam measurement of the time resolution of a small scintillator timing detector), and every number in it is made up.

```
python3 -I scripts/andre_style_check.py scripts/example_draft.tex --max-flags 2
```

17 of the 63 rows that have a range are marked, and 33 sentences and captions are listed. All ten groups of flags fire. The text has 36 sentences, so the script prints no total of marked rows. The complete output:

```
Smoke detector: this script counts surface features of the text. It cannot judge meaning, and no flag is an order. The ranges describe his practice; they are not quotas.

files: example_draft.tex
profile: short-paper    words: 407    sentences: 36    paragraphs: 5    captions: 2
note: fewer than 50 sentences: the shares are rough, read the counts in parentheses.

metric                                                                        draft  his range    mark
--------------------------------------------------------------------------------------------------------
SENTENCES
  words per sentence, median                                                      9  19 to 22     below
  sentences of 12 words or fewer, %                                       72.2 (26)  13 to 18     above
  sentences above 30 words, %                                               2.8 (1)  13 to 18     below
  sentences above 40 words, %                                               2.8 (1)  2 to 5
PARAGRAPHS
  sentences per paragraph, median                                                 7  3 to 5       above
  words per paragraph, median                                                    82  60 to 110
  paragraphs of one sentence, %                                             0.0 (0)  at most 6.7
  paragraphs of 8 or more sentences, %                                     20.0 (1)  at most 5
VOICE
  sentences containing "we", %                                            75.0 (27)  at most 20   above
  sentences opening with "We" or "Our", %                                 55.6 (20)  at most 8    above
  sentences with a passive, %                                               2.8 (1)  35 to 45     below
SENTENCE OPENERS, % OF SENTENCES
  The, This, These, A, An, Each, All                                       19.4 (7)  45 to 55     below
  "This"                                                                    0.0 (0)  6 to 10      below
  "This" + verb, % of the "This" openers                                          -  40 to 60
  fronted phrase (In, For, To, Since, With, ...)                            8.3 (3)  11 to 16
  "For"                                                                     5.6 (2)  at most 3
  "With"                                                                    2.8 (1)  at most 1
  "To"                                                                      0.0 (0)  2 to 4
  connector (list of 31)                                                    8.3 (3)  7 to 11
CONNECTORS AT THE START, ONE BY ONE, % OF SENTENCES
  Finally                                                                   0.0 (0)  at most 2
  However                                                                   0.0 (0)  at most 2
  Therefore                                                                 0.0 (0)  at most 2
  Furthermore                                                               0.0 (0)  at most 2
  Nevertheless                                                              0.0 (0)  at most 2
  Moreover                                                                  0.0 (0)  at most 2
  Note that                                                                 0.0 (0)  at most 2
  Additionally                                                              2.8 (1)  0
  As a result                                                               2.8 (1)  0
  Importantly                                                               2.8 (1)  at most 2
  In addition                                                               2.8 (1)  0
CAUSAL WORDS, PER 10,000 WORDS
  since (causal)                                                            0.0 (0)  at most 20
  due to                                                                    0.0 (0)  at most 20
  therefore                                                                 0.0 (0)  at most 20
  because (with "because of")                                               0.0 (0)  at most 20
  hence                                                                     0.0 (0)  at most 20
  thus                                                                      0.0 (0)  at most 20
  "so" as a conjunction (", so", "and so", "so that")                     122.8 (5)  at most 6    above
  causal words in use, of these seven                                             1  at least 4
APPROXIMATORS, PER 1000 WORDS
  all (approximately, roughly, about/around + number, nearly, almost)      4.91 (2)  1.5 to 2.5
  roughly                                                                  0.00 (0)  0.5 to 1.2
  about + number                                                           0.00 (0)  0.2 to 0.8
  approximately                                                            4.91 (2)  at most 0.2  above
INTENSIFIERS, PRAISE AND SUFFICIENCY
  six intensifiers (very, significantly, highly, ...), per 1000 words      4.91 (2)  at most 1    above
  praise words (list of 17), per 10,000 words                              24.6 (1)  at most 4
  sufficiency words (list of 12), per 10,000 words                          0.0 (0)  10 to 25
PUNCTUATION, PER 1000 WORDS
  semicolons                                                               2.46 (1)  at most 1
  colons                                                                   0.00 (0)  2 to 4
  dashes as punctuation                                                    0.00 (0)  at most 0.2
  parenthesis pairs                                                        2.46 (1)  9 to 13      below
CAPTIONS
  words per caption, median                                                      49  25 to 50
  longest caption, words                                                         52  at most 100
  sentences per caption, median                                                 4.5  1 to 3       above
  captions of 4 or more sentences, %                                      100.0 (2)  at most 25   above
  captions that open with a noun phrase without article, %                  0.0 (0)  100          below
  captions whose first sentence has no finite verb, %                      50.0 (1)  90 to 100
REFERENCES TO FIGURES AND TABLES
  references per 1000 words                                                4.91 (2)  3 to 6
  float as subject ("Figure N shows"), % of references                      0.0 (0)  30 to 50
  "is shown in Fig. N" and its variants, % of references                    0.0 (0)  35 to 45
  "as shown in Fig. N", count                                                     0  at most 1
  "(Fig. N)" or "(see Fig. N)", count                                             1  at most 1
  "see Fig. N" outside parentheses, count                                         1  0            above
ABBREVIATIONS
  "Sec." or "Secs.", count                                                        1  -
  "Section" in full, count                                                        0  -
  sentences that start with "Fig.", count                                         0  0
  sentences that start with "Figure", count                                       0  -
  "Figure" in full inside a sentence, count                                       0  0
--------------------------------------------------------------------------------------------------------
Fewer than 100 sentences: the ranges describe a whole paper. Use the sentences listed below, not the marks. In parentheses: the count behind a share or a rate.
A share, a rate or a median is marked only when it is at least 1.5 items (for a median: units) outside the range.
The marks are not a score: never choose between two wordings by the number of marked rows.

SENTENCES TO LOOK AT (at most 2 per group)

Three or more sentences in a row that open with "We": 4
  "We" should mark where the authors chose, tested, ran or concluded something. Give an operation on
  recorded data the thing as its subject; a study or a simulation run of the authors keeps "we".
  example_draft.tex:10  4 sentences, lines 10 to 13
      We test a small scintillator tile in a 120 GeV pion beam.
  example_draft.tex:22  3 sentences, lines 22 to 24
      We check the baseline before each pulse.
  ... and 2 more

"so" as the causal join: 5
  One join used again and again makes every step read alike. He writes it about once in 2000 words,
  so one may stay. For the others: under about 25 words keep one sentence, with a fronted "Since",
  "due to" plus a noun phrase, or a tail (", making X a Y", ", thus ...ing", ", which" plus a verb);
  split off a "This" + verb sentence only after a first clause of about 15 words or more.
  example_draft.tex:15  ", so"
      The beam spot is wider than the tile, so we select tracks that point to its central region.
  example_draft.tex:38  ", so"
      We average the times of the two sensors, so the result does not depend on the impact point.
  ... and 3 more

Figure or table cited in parentheses or with "see": 2
  The reader should learn what is plotted before the result. Introduce the float by a sentence with
  the float or the plotted thing as subject: "Figure N shows X." or "X is shown in Fig. N." A figure
  that illustrates one statement carries it in a clause: "Figure N shows X, in which ...".
  example_draft.tex:18  "see Fig. N"
      We utilize a constant-fraction threshold to extract the arrival time; see Fig. REF.
  example_draft.tex:42  "(Fig. N)"
      In addition, we repeat the fit at five bias voltages (Fig. REF).

Captions that open with an article or a full sentence, or run beyond the range: 2
  A caption says what is plotted and how to read it. Open with a noun phrase without article and
  without verb. Range of the median: 25 to 50 words, 1 to 3 sentences. Move out only what explains
  or argues (a derivation, the physical reason, a second finding). A limit of what the plot shows,
  the definition of a plotted element and how a point was obtained stay in the caption. If it is
  still long, leave it and report its length.
  example_draft.tex:28  opens with an article; 52 words; 5 sentences; has "we"
      The pulse shape of the tile for 120 GeV pions. We fit the leading edge with a straight line. The fit is ver...
  example_draft.tex:58  does not open with what is plotted; first sentence is a full sentence ("shows"); 4 sentences
      This figure shows the time resolution for different bias voltages. The resolution improves with the voltage...

Words and phrases from the avoid list, and dashes: 10
  A rare word makes the reader ask whether a special meaning is intended. These are absent or nearly
  absent from the texts he wrote alone. The plain form follows the colon. A term that the draft
  defines and uses throughout stays; propose the change for the whole paper.
  example_draft.tex:18  "utilize": write "use"
      We utilize a constant-fraction threshold to extract the arrival time; see Fig. REF.
  example_draft.tex:21  "It should be noted that": write "Note that"
      It should be noted that we do not correct for the residual walk.
  ... and 8 more

Intensifiers and praise words: 2
  A number carries the size of an effect; an intensifier asks for trust. Give the number or the
  requirement. "Significant" in the statistical sense stays. In a polish, propose the removal in the
  report; "significantly" before a measured difference is a claim, so ask the authors.
  example_draft.tex:20  "very"
      With this choice, the time walk is very small.
  example_draft.tex:52  "significantly"
      We note that the resolution that we obtain after this restriction is significantly better than the one that...

Sentences above 45 words that are not a list: 1
  He passes 40 words mostly for a list or a definition. Split, or give the reason a "This" + verb
  sentence.
  example_draft.tex:52  48 words
      We note that the resolution that we obtain after this restriction is significantly better than the one that...

Sentence-initial connectors that his own texts do not open with: 4
  A connector should tell the reader whether the sentence adds, turns or concludes. His own texts
  open sentences with: Finally, However, Therefore, Furthermore, Nevertheless, Moreover, Note that,
  Hence, Thus, First, Then, Consequently, In particular, For example, On the other hand, Overall,
  Here, Instead, In this case, At the same time.
  example_draft.tex:42  "In addition"
      In addition, we repeat the fit at five bias voltages (Fig. REF).
  example_draft.tex:43  "Additionally"
      Additionally, we leverage the track position to study the edges of the tile, as described in Sec. REF.
  ... and 2 more

"Sec." and "Tab.": 1
  He writes "Table" in full in all six documents, and "Section" in full in the three that refer to a
  section; "Sec." is in none of the six. The journal decides: where it prints "Sec.", keep the
  draft's "Sec." and name it in the report.
  example_draft.tex:43  "Sec."
      Additionally, we leverage the track position to study the edges of the tile, as described in Sec. REF.

"approximately" before a number (information only): 2
  His own voice rounds with "roughly" or "about". CMS style prefers "approximately": keep it where
  the paper follows CMS rules.
  example_draft.tex:16  "approximately 50,000"
      For each run, we record approximately 50,000 events.
  example_draft.tex:40  "approximately 40"
      We observe a width of approximately 40 ps.
```

### Agreement with the measurement behind the references

The counting code was written again for this script, so it was compared with the measurement that produced the tables of `references/corpus-and-measurements.md`.

- [PROC] and [SAC]: the sentences are the same, one by one (67 and 234), the paragraphs and the captions are the same, and every row that the measurement also has agrees to two decimals.
- [IDM], [ETA] and [SCOUT]: one difference each. This script ends a sentence after a number and a one-letter unit ("a magnetic field of 3.8 T."), which the measurement read as an initial. It therefore finds 135, 122 and 1480 sentences where the reference tables give 134, 121 and 1479, and its shares differ from those tables by at most one percentage point.
- Line numbers were checked on a LaTeX file with wrapped lines, comment lines, a figure and a table inside a paragraph, a footnote, a display equation and a list: every sentence and caption is reported on the line where it starts.

## Limits

- The script reads words and punctuation. It has no parser and no dictionary. It cannot tell whether a "we" states a decision, whether a passive hides who decided, whether a caption states a finding, or whether a number has its condition and its baseline. Those checks need a reader.
- It does not check structure: the abstract, the purpose sentence, the order of sections, titles, or what a paragraph opens and closes on.
- The ranges come from six documents. [PROC] has 67 sentences and each letter about 130, so `cms-letter` rests on two short texts. Read a mark as a place to look, and use the reference files to decide.
- A short draft gives rough shares. The script therefore marks a share only when it is 1.5 items outside the range, and it prints the counts.
- Run it on the source. Text taken from a PDF has no blank lines between paragraphs and mixes captions, page numbers and figure labels into the text. For [SAC] taken from the PDF, the median sentence length is 19 words against 20 from the source, and the share of sentences with a passive is 40% against 43%. Paragraph and caption rows are then not usable.
- LaTeX: `\input` is not followed, and a macro defined in a file that is not given becomes `SYM`. A sentence full of symbols is counted shorter than it reads. Every `\caption` inside a float counts as a caption, so the captions of subfigures are counted too. Unbalanced braces can hide the text that follows them.
- Sentence splitting protects "Fig.", "Eq.", "Ref.", "Sec.", "e.g.", "i.e.", "et al.", "vs." and initials. A sentence that ends in one of these abbreviations, or that starts in lower case, merges with its neighbour. Use `--dump` to see the split.
- The passive test, the causal "since", "so" as a conjunction, the list test for long sentences and the verb test for captions are keyword rules. Expect some wrong calls in both directions.
