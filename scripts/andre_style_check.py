#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""andre_style_check.py - compare the surface of a draft with Andre Frankenthal's papers.

This script is a smoke detector. It counts surface features of the text. It cannot judge
meaning, and no flag is an order.

Usage
    python3 scripts/andre_style_check.py draft.tex [more.tex ...] [--json]
            [--targets short-paper|cms-letter|thesis] [--max-flags N] [--dump]

Input: .tex, .md or .txt. Several files are read as one draft. \\input is not followed.

What it prints
  1. A table: each metric, the draft's value, his range for the chosen profile, and a mark
     ("above" or "below") where the draft is outside the range.
  2. Sentences to look at, with file, line and a short reason, grouped by reason.
  --json prints the same data as JSON. --dump prints the sentences as the script read them.

Metrics
  sentence length (median; share of 12 words or fewer, above 30, above 40); paragraph length
  (median sentences and words; one-sentence paragraphs; paragraphs of 8 or more sentences);
  sentences containing "we" and opening with "We"; sentences with a passive; sentence openers
  (The/This/These/A/An/Each/All, "This" + verb, fronted phrase, connector); connectors at the
  start one by one; causal words; approximators; intensifiers, praise and sufficiency words;
  semicolons, colons, dashes, parentheses; captions (words, sentences, opening, verb in the
  first sentence); references to figures and tables (float as subject, "is shown in",
  "as shown in", in parentheses, "see Fig."); "Sec." against "Section"; "Fig." against
  "Figure" at the start of a sentence.

Where the ranges come from
  short-paper (default): a methods paper by a few authors. The "Aim for" values of Table B
      in references/voice-and-transfer.md; a row that Table B does not have comes from the
      target table of another reference file (see the comments in SPEC).
  cms-letter: the values of the two CMS letters whose writing he led (IDM, ETA), bracketed
      and widened by the precision of the measurement.
  thesis: the values of his PhD thesis, widened in the same way.
  The counting rules are those of the measurement behind the references, so a value
  printed here can be set beside the numbers quoted there.

Python 3 standard library only. Deterministic. No network.
"""
import argparse
import json
import os
import re
import sys
import textwrap

NOTICE = ('Smoke detector: this script counts surface features of the text. It cannot judge '
          'meaning, and no flag is an order. The ranges describe his practice; they are not quotas.')

# ----------------------------------------------------------------------------------------
# Ranges.  One row per metric: key, label, then (low, high) for the profiles short-paper,
# cms-letter and thesis.  None in place of a pair: no range, the value is shown for
# information.  None as high: no upper end.  A bare string opens a group of rows.
#
# short-paper: the "Aim for" values of Table B in references/voice-and-transfer.md, the
#   reference for every range of this skill.  Where the target table of another file
#   gave a different range for the same feature when this script was written (shares of
#   short and long sentences, paragraph length, "we", connectors, captions of four or more
#   sentences, float as subject), the value of Table B was taken.  A row that Table B does
#   not have names the reference file it comes from.  "we": no document of his lies between
#   6 % (thesis) and 19 % (SAC), so the short-paper range is "up to 20 %" and "up to 8 %".
# cms-letter: each end is the lower or the higher value of the two letters (IDM, ETA),
#   moved outward by about three percentage points for a share of sentences and one unit
#   for a median, then rounded.  Rows that rest on few items (paragraphs, captions,
#   references, "This" openers) span the two values with a rounded margin.
# thesis: the thesis value, widened in the same way.
# ----------------------------------------------------------------------------------------
SPEC = [
    'Sentences',                                                                    # Table B
    ('sent_median', 'words per sentence, median', (19, 22), (21, 24), (19, 21)),
    ('sent_le12', 'sentences of 12 words or fewer, %', (13, 18), (6, 13), (14, 20)),
    ('sent_gt30', 'sentences above 30 words, %', (13, 18), (17, 29), (12, 18)),
    ('sent_gt40', 'sentences above 40 words, %', (2, 5), (4, 13), (1, 6)),
    'Paragraphs',                                                                   # Table B
    ('par_median', 'sentences per paragraph, median', (3, 5), (5, 9), (3, 5)),
    ('par_words', 'words per paragraph, median', (60, 110), (140, 190), (60, 110)),
    ('par_one', 'paragraphs of one sentence, %', (0, 6.7), (0, 4), (0, 12)),         # 1 in 15
    ('par_ge8', 'paragraphs of 8 or more sentences, %', (0, 5), (25, 58), (0, 9)),
    'Voice',                                                                        # Table B
    ('we_any', 'sentences containing "we", %', (0, 20), (2, 9), (3, 9)),
    ('we_open', 'sentences opening with "We" or "Our", %', (0, 8), (0, 5), (0, 5)),
    ('passive', 'sentences with a passive, %', (35, 45), (50, 59), (35, 45)),
    'Sentence openers, % of sentences',                                             # Table B
    ('open_thing', 'The, This, These, A, An, Each, All', (45, 55), (48, 62), (42, 52)),
    ('open_this', '"This"', (6, 10), (3, 11), (7, 13)),
    # "about half" of the "This" openers is coded as 40 to 60 %
    ('this_verb', '"This" + verb, % of the "This" openers', (40, 60), (20, 50), (40, 60)),
    ('open_fronted', 'fronted phrase (In, For, To, Since, With, ...)', (11, 16), (8, 17), (9, 15)),
    ('open_for', '"For"', (0, 3), (0, 3), (0, 3)),
    ('open_with', '"With"', (0, 1), (0, 1), (0, 1.5)),
    ('open_to', '"To"', (2, 4), (1, 8), (0, 4)),
    ('open_conn', 'connector (list of 31)', (7, 11), (3, 9), (6, 11)),
    # Table B: each connector at most about 2 %.  The rows are made at run time: his seven,
    # then any other connector found.  A connector of the avoid list has the range 0.
    'Connectors at the start, one by one, % of sentences',
    'CONNECTORS',
    # Table B: four or more in use, none above 20, "so" at most 6.
    'Causal words, per 10,000 words',
    ('c_since', 'since (causal)', (0, 20), (0, 20), (0, 25)),
    ('c_due', 'due to', (0, 20), (0, 20), (0, 25)),
    ('c_therefore', 'therefore', (0, 20), (0, 20), (0, 25)),
    ('c_because', 'because (with "because of")', (0, 20), (0, 20), (0, 25)),
    ('c_hence', 'hence', (0, 20), (0, 20), (0, 25)),
    ('c_thus', 'thus', (0, 20), (0, 20), (0, 25)),
    ('c_so', '"so" as a conjunction (", so", "and so", "so that")', (0, 6), (0, 3), (0, 7)),
    ('c_used', 'causal words in use, of these seven', (4, None), (4, None), (4, None)),
    # Table B; "about" + number: words-and-phrases.md.
    'Approximators, per 1000 words',
    ('ap_all', 'all (approximately, roughly, about/around + number, nearly, almost)',
     (1.5, 2.5), (1.3, 4.3), (1.0, 2.2)),
    ('ap_roughly', 'roughly', (0.5, 1.2), (0, 0.5), (0.5, 1.5)),
    ('ap_about', 'about + number', (0.2, 0.8), (0.7, 3.0), (0, 0.6)),
    ('ap_approx', 'approximately', (0, 0.2), (0.2, 1.0), (0, 0.2)),
    # words-and-phrases.md: six intensifiers below 1 per 1000 words; seventeen praise
    # words 0 to 4 and twelve sufficiency words 10 to 25 per 10,000 words.
    'Intensifiers, praise and sufficiency',
    ('int_six', 'six intensifiers (very, significantly, highly, ...), per 1000 words',
     (0, 1), (0, 2), (0, 1.5)),
    ('praise', 'praise words (list of 17), per 10,000 words', (0, 4), (0, 25), (0, 8)),
    ('suffice', 'sufficiency words (list of 12), per 10,000 words', (10, 25), (5, 20), (5, 15)),
    'Punctuation, per 1000 words',                                    # sentences-and-voice.md
    ('p_semi', 'semicolons', (0, 1), (0, 1.5), (0, 1.2)),
    ('p_colon', 'colons', (2, 4), (0.5, 2.5), (3, 5.5)),
    # one dash construction in SAC (0.2 per 1000 words), a pair in PROC, none in IDM and ETA
    ('p_dash', 'dashes as punctuation', (0, 0.2), (0, 0), (0, 0.8)),
    ('p_paren', 'parenthesis pairs', (9, 13), (7, 17), (8, 13)),
    # Table B: median 25 to 50 words, none above 100; 1 to 3 sentences; at most a quarter
    # with four or more; all open with a noun phrase without article.  The share without a
    # finite verb has no "Aim for" cell: his three own-voice documents have 95 to 100 %,
    # and 90 % allows for the errors of the verb list.
    'Captions',
    ('cap_words', 'words per caption, median', (25, 50), (35, 75), (25, 50)),
    ('cap_max', 'longest caption, words', (0, 100), (0, 100), None),
    ('cap_sents', 'sentences per caption, median', (1, 3), (2, 4), (1, 3)),
    ('cap_ge4', 'captions of 4 or more sentences, %', (0, 25), (0, 55), (0, 20)),
    ('cap_bare', 'captions that open with a noun phrase without article, %', (100, 100), (85, 100), (95, 100)),
    ('cap_frag', 'captions whose first sentence has no finite verb, %', (90, 100), (80, 100), (90, 100)),
    # Table B: float as subject 30 to 50 %, "is shown in" 35 to 45 %, "see Fig. N" 0,
    # "(see Fig. N)" at most 1, "as shown in" at most 1.  References per 1000 words:
    # figures-and-captions.md.
    'References to figures and tables',
    ('ref_rate', 'references per 1000 words', (3, 6), (1.8, 3.3), (3.5, 6)),
    ('ref_subj', 'float as subject ("Figure N shows"), % of references', (30, 50), (10, 55), (40, 55)),
    ('ref_in', '"is shown in Fig. N" and its variants, % of references', (35, 45), (45, 80), (30, 42)),
    ('ref_as', '"as shown in Fig. N", count', (0, 1), (0, 1), (0, 2)),
    ('ref_paren', '"(Fig. N)" or "(see Fig. N)", count', (0, 1), (0, 1), (0, 1)),
    ('ref_see', '"see Fig. N" outside parentheses, count', (0, 0), (0, 0), (0, 0)),
    # words-and-phrases.md and figures-and-captions.md: he writes "Section" in full in the
    # three documents that refer to a section (SAC, SCOUT, THESIS); "Sec." is in none of the
    # six, and the journal decides, so the count has a range for the thesis profile only.
    # "Figure" at the start of a sentence and "Fig." inside is the form of his two PRL
    # papers; the thesis writes "Figure" everywhere.  The journal's rule wins.
    'Abbreviations',
    ('sec_abbr', '"Sec." or "Secs.", count', None, None, (0, 0)),
    ('sec_full', '"Section" in full, count', None, None, None),
    ('fig_start', 'sentences that start with "Fig.", count', (0, 0), (0, 0), (0, 0)),
    ('figure_start', 'sentences that start with "Figure", count', None, None, None),
    ('figure_in', '"Figure" in full inside a sentence, count', (0, 0), (0, 0), None),
]
PROFILES = ('short-paper', 'cms-letter', 'thesis')
RANGE = {p: {r[0]: r[2 + i] for r in SPEC if not isinstance(r, str)} for i, p in enumerate(PROFILES)}
MIN_ITEMS = 1.5           # a share or a rate is marked only if it is this many items outside
SMALL_TEXT = 100          # below this many sentences a median needs the same margin (in its
                          # own unit), and the number of marked rows is not printed
MIN_WORDS_CAUSAL = 1500   # "four causal words in use" is checked from this length on

# ----------------------------------------------------------------------------------------
# Word lists (those of the measurement, so that the numbers can be compared)
# ----------------------------------------------------------------------------------------
CONNECTORS = ['However', 'Therefore', 'Thus', 'Hence', 'Moreover', 'Furthermore', 'In addition',
              'Additionally', 'Finally', 'Consequently', 'Nevertheless', 'Similarly', 'Indeed',
              'For example', 'For instance', 'In particular', 'Specifically', 'Note that', 'Also',
              'Then', 'Next', 'First', 'Second', 'Lastly', 'On the other hand', 'In contrast',
              'As a result', 'In this way', 'Overall', 'In summary', 'In conclusion']
CONNECTORS_MORE = ['Here', 'Instead', 'Still', 'Yet', 'But', 'And', 'So', 'Nonetheless', 'Likewise',
                   'Conversely', 'Notably', 'Ultimately', 'Subsequently', 'Accordingly', 'Third',
                   'In other words', 'In fact', 'In general', 'In practice', 'In turn',
                   'In this case', 'At the same time', 'Rather', 'Otherwise', 'Meanwhile',
                   'Alternatively', 'Importantly', 'Crucially', 'Interestingly', 'Fortunately',
                   'Unfortunately', 'Together', 'Now', 'Again', 'Currently', 'Recently',
                   'Previously', 'Typically', 'Generally', 'Analogously', 'Concurrently',
                   'Naturally', 'Clearly', 'Of course', 'That is', 'To summarize', 'As such',
                   'As expected', 'As mentioned', 'As discussed', 'As shown']
HIS_SEVEN = ['Finally', 'However', 'Therefore', 'Furthermore', 'Nevertheless', 'Moreover', 'Note that']
# Also his: these open a sentence in at least two of his three own-voice texts ("Overall":
# in the thesis and in ETA).  The lists per profile hold what else opens a sentence in the
# two letters, or in at least 0.1 % of the thesis sentences.
HIS_ALSO = ['Hence', 'Thus', 'First', 'Then', 'Consequently', 'In particular', 'For example',
            'On the other hand', 'Overall', 'Here', 'Instead', 'In this case', 'At the same time']
HIS_BY_PROFILE = {'short-paper': [],
                  'cms-letter': ['In summary', 'Specifically', 'In contrast', 'Subsequently'],
                  'thesis': ['Similarly', 'Next', 'In contrast', 'In general', 'In fact', 'As mentioned',
                             'As discussed', 'As such', 'Conversely']}
AVOID_OPENERS = ['In addition', 'Additionally', 'As a result', 'Notably', 'Crucially', 'In conclusion',
                 'Lastly', 'Nonetheless', 'In other words']
NOT_CONNECTORS = ['Now', 'Again', 'Currently', 'Recently', 'Previously', 'Typically', 'Generally']
DET_OPENERS = ['The', 'This', 'These', 'A', 'An', 'Each', 'All']
FRONTED = ['In', 'For', 'To', 'At', 'After', 'Before', 'Since', 'While', 'Because', 'As', 'When', 'If',
           'With', 'By', 'From', 'Due to', 'Given', 'Using', 'Although']
LONGEST_FIRST = [(name, sorted(words, key=len, reverse=True)) for name, words in (
    ('connector', CONNECTORS), ('connector2', CONNECTORS_MORE), ('fronted', FRONTED))]
THIS_VERBS = set("""is was are leads allows means makes can will would has could should may might
results provides ensures gives corresponds requires implies suggests shows indicates enables reduces
increases happens occurs does includes represents constitutes contrasts improves yields follows
causes motivates informs overestimates underestimates removes helps avoids prevents translates
reflects confirms demonstrates explains limits applies holds becomes remains""".split())
BE_FORMS = {'is', 'are', 'was', 'were', 'be', 'been', 'being', 'am'}
IRREG_PP = set("""shown given taken found seen known made done chosen written built kept held set run
put cut led left lost met read sent spent told thought brought bought drawn driven fed grown hidden
split spread understood withdrawn broken begun sought taught undergone overcome fit hit shut bound
gotten proven laid paid said sold stuck struck swept thrown worn won dealt felt heard meant frozen
forbidden forgotten beaten bent bred cast caught dug hung lit shot spun strung swung torn woven
overridden overwritten rewritten rebuilt reset offset shed sped borne become arisen fallen risen
gone come""".split())
ED_NOT_PP = set("""need speed seed feed indeed exceed proceed succeed hundred embed red bed shed bleed
breed weed deed greed reed creed steed heed infrared""".split())
PASSIVE_BLOCK = set("""the a an this that these those its their our his her my no some any each every
one two of in on at for to by with from as and or but than which who""".split())
NUMBER_WORDS = """one two three four five six seven eight nine ten eleven twelve twenty thirty forty
fifty sixty hundred thousand million billion half twice dozen dozens several few""".split()
ABBR = set("""fig figs eq eqs ref refs sec secs tab tabs al vs cf nos dr prof mr mrs chap
phys rev lett approx resp ca viz incl excl e.g i.e et p.e d.o.f a.u w.r.t c.l stat syst reco
jr vol eds nucl instrum meth u.s ph.d sect chapt eqn eqns""".split())
SIX_INTENSIFIERS = ['very', 'significantly', 'highly', 'extremely', 'strongly', 'clearly']
PRAISE = ['novel', 'excellent', 'powerful', 'unprecedented', 'remarkable', 'outstanding', 'innovative',
          'exciting', 'compelling', 'pivotal', 'paramount', 'unique',
          'groundbreaking', 'pioneering', 'superior', 'state-of-the-art', 'impressive']
# The last five praise words are in AVOID; the others and the six intensifiers get a flag here.
LOOK_AT = re.compile(r'\b(' + '|'.join(SIX_INTENSIFIERS + PRAISE[:12]) + r')\b', re.I)
SUFFICIENCY = (r'moderate(?:ly)?|acceptabl[ey]|sufficient(?:ly)?|reasonabl[ey]|negligibl[ey]|'
               r'manageabl[ey]|satisfactor(?:y|ily)|safe(?:ly)?|comfortabl[ey]|adequate(?:ly)?|'
               r'modest(?:ly)?|conservative(?:ly)?')
# The avoid list of references/words-and-phrases.md with the plain form, and dashes used as
# punctuation.  "Sec." and the sentence-initial connectors have groups of their own.
AVOID = [(re.compile(pat, re.I), fix) for pat, fix in [
    (r'\butili[sz]\w+', 'write "use"'), (r'\bleverag\w+', 'write "use"'),
    (r'\bfacilitat\w+', 'write "allow"'), (r'\bshowcas\w+', 'write "show"'),
    (r'\boutperform\w*', 'give the two numbers'),
    (r'\bstate[- ]of[- ]the[- ]art\b', 'name the reference method and its number'),
    (r'\b(?:impressive(?:ly)?|superior|groundbreaking|pioneering)\b', 'state the need and whether the result meets it'),
    (r'\b(?:substantially|crucially)\b', 'give the number'),
    (r'\b(?:good|excellent) agreement\b', 'write "agrees with" or "consistent with" and give the reference value'),
    (r'\bit should be noted(?: that)?\b', 'write "Note that"'),
    (r'\bas can be seen\b', 'make the figure the subject'),
    (r'\bwe (?:observe|see|believe|note)\b', 'write "we find"'),
    (r'\bwe call\b', 'describe the thing first; "we refer to" for a name the authors coined, '
                     '"referred to as" for a name in general use'),
    (r'\bso-called\b', 'name the thing once with "referred to as"'),
    (r'\betc\.', 'list the items'),
    (r'\b(?:in other words|to this end)\b', 'delete it'),
    (r'\b(?:in conclusion|lastly)\b', 'write "Finally,"'),
    (r'\bnonetheless\b', 'write "Nevertheless,"'), (r'\bobviously\b', 'delete it'),
    (r'\bas a result\b', 'write "therefore", "hence" or a "This" + verb sentence'),
    (r'\bwith respect to\b', 'write "compared to"'),
    (r'—|(?<=\s)–(?=\s)|(?<=[A-Za-z)])\s-\s(?=[A-Za-z(])',
     'a dash: he has one construction in a paper at most; never add one'),
]]
# For the flag on one caption: verbs that are not also nouns ("yield", "marks", "fit").
SURE_VERBS = re.compile(r"\b(is|are|was|were|has|have|had|shows?|displays?|illustrates?|compares?|presents?|"
                        r"represents?|corresponds?|denotes?|indicates?|depicts?|summarizes?|consists?|includes?|"
                        r"contains?|agrees?)\b")
FINITE_VERBS = re.compile(r"\b(is|are|was|were|has|have|had|shows?|displays?|illustrates?|compares?|presents?|"
                          r"represents?|corresponds?|denotes?|indicates?|depicts?|gives?|lists?|summarizes?|"
                          r"can|will|may|should|must|sits|consists?|includes?|contains?|uses?|agrees?|yields?|"
                          r"shifts?|broadens?|meets?|leave|leaves|marks?|join|joins|separate|separates|differ|differs|"
                          r"record|records|removed|lies|find|finds|loses|lose|start|starts|reports?|provides?)\b")
FLOAT_W = r'(?:Figures?|Figs?\.|Tables?|Tabs?\.)'
SUBJ_VERBS = (r'shows?|lists?|summari[sz]es?|illustrates?|displays?|presents?|compares?|gives?|reports?|depicts?|'
              r'contrasts?|demonstrates?|contains?|provides?|plots?|details?|describes?|highlights?|sketches|'
              r'outlines?|collects?|includes?|indicates?|reveals?|confirms?|defines?')
LOC_PHRASES = ['as shown in', 'shown in', 'seen in', 'illustrated in', 'given in', 'listed in', 'summarized in',
               'presented in', 'displayed in', 'reported in', 'plotted in', 'described in', 'depicted in',
               'sketched in', 'provided in', 'found in', 'compared in', 'visible in', 'detailed in', 'defined in',
               'as seen in', 'as illustrated in', 'as described in', 'as listed in', 'as summarized in']
PLACEHOLDERS = ('MATH', 'SYM', 'CITE', 'REF')
EDGE = '.,;:!?()[]{}“”"‘’\'`'

# ----------------------------------------------------------------------------------------
# LaTeX tables
# ----------------------------------------------------------------------------------------
UNIT_MACROS = {
    'GeV': 'GeV', 'TeV': 'TeV', 'MeV': 'MeV', 'keV': 'keV', 'eV': 'eV', 'PeV': 'PeV',
    'GeVns': 'GeV', 'TeVns': 'TeV', 'MeVns': 'MeV', 'keVns': 'keV', 'GeVc': 'GeV/c', 'GeVcc': 'GeV/c2',
    'fbinv': 'fb-1', 'pbinv': 'pb-1', 'nbinv': 'nb-1', 'mm': 'mm', 'cm': 'cm', 'mum': 'µm',
    'micron': 'µm', 'ns': 'ns', 'mus': 'µs', 'ms': 'ms', 'ps': 'ps', 'nm': 'nm', 'um': 'µm',
    'MHz': 'MHz', 'kHz': 'kHz', 'Hz': 'Hz', 'tesla': 'T', 'invcms': 'cm-2s-1', 'gbs': 'GB/s',
    'percms': 'cm-2s-1', 'mrad': 'mrad', 'rad': 'rad', 'pb': 'pb', 'fb': 'fb', 'mb': 'mb'}
TEXT_MACROS = {
    'eg': 'e.g.', 'ie': 'i.e.', 'vs': 'vs.', 'etal': 'et al.', 'cf': 'cf.', 'etc': 'etc.',
    'CL': 'CL', 'CLs': 'CLs', 'cmsLeft': 'left', 'cmsRight': 'right', 'MGvATNLO': 'MadGraph5_aMC@NLO',
    'PYTHIA': 'PYTHIA', 'GEANTfour': 'GEANT4', 'GEANT': 'GEANT', 'POWHEG': 'POWHEG',
    'MADGRAPH': 'MADGRAPH', 'HERWIG': 'HERWIG', 'ROOT': 'ROOT', 'stat': '(stat)', 'syst': '(syst)',
    'lumi': '(lumi)', 'LaTeX': 'LaTeX', 'TeX': 'TeX', 'ldots': '...', 'dots': '...',
    'textemdash': '—', 'textendash': '–', 'NA': '—', 'ss': 'ss', 'o': 'o', 'ae': 'ae', 'aa': 'a',
    'l': 'l', 'O': 'O', 'textgreater': '>', 'textless': '<', 'textasciitilde': '~',
    'textbackslash': '', 'slash': '/', 'S': '§'}
DROP_MACROS = set("""maketitle tableofcontents newpage clearpage cleardoublepage centering linenumbers
balance bigskip medskip smallskip hline raggedright small footnotesize normalsize large Large tiny
scriptsize bf it rm sc em sf tt normalfont itshape bfseries upshape sloppy xspace Xspace protect
relax twocolumngrid onecolumngrid appendix flushleft flushright hfill vfill noalign toprule
midrule bottomrule today frenchspacing nonfrenchspacing allowbreak break nobreak null strut
ignorespaces unskip displaystyle textstyle limits nolimits nonumber notag qed indent pagebreak
linebreak nolinebreak samepage thispagestyle baselineskip columnwidth textwidth linewidth
arraystretch tabcolsep""".split())
ARG_SYM_MACROS = {1: 'phantom|vec|abs|sqrt|vphantom|hphantom|overline|bar|hat|tilde|mathcal|mathbf|mathbb|'
                     'boldsymbol|operatorname|smash',
                  2: 'frac|rule|raisebox|stackrel|binom|sci',
                  3: 'multirow|multicolumn|resizebox|HepParticle'}
ARG_DROP_MACROS = {1: 'author|Author|address|affiliation|Institution|cortext|ead|email|journal|date|'
                      'hypersetup|cmsNoteHeader|pacs|keywords|collaboration|thanks|hyphenation|'
                      'bibliographystyle|vspace|hspace|includegraphics|label|pagestyle|thispagestyle|'
                      'preprint|tnotetext|fntext|corref|fnref|tnoteref|color|graphicspath|usepackage|'
                      'bibliography|cline|enlargethispage|todo',
                   2: 'setcounter|setlength|addtolength|markboth|pdfbookmark',
                   3: 'ifthenelse|definecolor|addcontentsline'}
SI_UNITS = {'tesla': 'T', 'MeV': 'MeV', 'GeV': 'GeV', 'TeV': 'TeV', 'keV': 'keV', 'eV': 'eV',
            'mm': 'mm', 'cm': 'cm', 'ns': 'ns', 'ps': 'ps', 'um': 'µm', 'nm': 'nm', 'pe': 'p.e.',
            'V': 'V', 's': 's', 'pico': 'p', 'coulomb': 'C', 'mega': 'M', 'hertz': 'Hz', 'kilo': 'k',
            'micro': 'µ', 'milli': 'm', 'nano': 'n', 'm': 'm', 'gray': 'Gy', 'second': 's',
            'meter': 'm', 'metre': 'm', 'volt': 'V', 'percent': '%', 'degree': '°', 'giga': 'G',
            'tera': 'T', 'byte': 'B', 'bit': 'bit', 'radian': 'rad', 'femto': 'f', 'barn': 'b'}
MATH_ENVS = (r'equation\*?|align\*?|eqnarray\*?|multline\*?|gather\*?|displaymath|flalign\*?|'
             r'alignat\*?|subequations')
FLOAT_ENVS = r'figure\*?|table\*?|sidewaysfigure|sidewaystable|wrapfigure|SCfigure'
DROP_ENVS = (r'tabular\*?|scotch|ruledtabular|longtable|tabularx|array|frontmatter|keyword|keywords|'
             r'sloppypar|comment|tikzpicture|verbatim|lstlisting|algorithm|algorithmic|acknowledge?ments')
# The text ends at the bibliography, or at acknowledgments in the second half of the file.
END_PATTERNS = [r'\\begin\{thebibliography\}', r'\\bibliography\{', r'\\printbibliography',
                r'\\input\{[^}]*\.bbl\}', r'\\end\{document\}']
END_ACK = r'\\begin\{acknowledg[e]?ments\}|\\section\*?\{\s*Acknowledg|\\acknowledg[e]?ments'
HEADINGS = 'part|chapter|section|subsection|subsubsection|paragraph|subparagraph'

# Three control characters keep line numbers and paragraph breaks through the cleaning.
# All three count as white space.
SOFT = '\v'      # a line break of the source that does not end a paragraph
PARA = '\x1e'    # a paragraph break that is not a line break (a heading, \item, \par)
GONE = '\x1f'    # text was removed here (a comment, a float, a label)
BREAK = re.compile(r'(?:\n[ \t\v\x1f]*\n|\x1e)\s*')


# ----------------------------------------------------------------------------------------
# small helpers
# ----------------------------------------------------------------------------------------
def breaks(t):
    """The number of line breaks in t, soft ones included."""
    return t.count('\n') + t.count(SOFT)


def keep(old, new):
    """new, plus soft marks for the line breaks that old had and new has not."""
    lost = breaks(old) - breaks(new)
    return new + SOFT * lost if lost > 0 else new


def rsub(pat, repl, s, flags=0):
    """re.sub that keeps the line numbers of the text after each replacement."""
    return re.sub(pat, lambda m: keep(m.group(0), repl(m) if callable(repl) else m.expand(repl)),
                  s, flags=flags)


def lineno(s, pos):
    """The line of the source file on which position pos of s lies."""
    return 1 + breaks(s[:pos])


def soften(s):
    """A line that held only removed text is not a blank line: make its line break soft."""
    return re.sub(r'(?m)^([ \t\v]*\x1f[ \t\v\x1f]*)\n', lambda m: m.group(1) + SOFT, s)


def tidy(t):
    """One space between words, none before punctuation or after an opening bracket."""
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\s+([,.;:!?)\]])', r'\1', t)
    t = re.sub(r'([(\[])\s+', r'\1', t)
    t = re.sub(r'\(\s*\)', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def core_of(tok):
    """A token without the punctuation at its edges."""
    return tok.strip(EDGE)


def count_words(text):
    """Tokens with a letter or a digit; MATH, SYM and REF count as one word, CITE as none."""
    n = 0
    for tok in text.split():
        c = core_of(tok)
        if c and c != 'CITE' and re.search(r'[A-Za-z0-9]', c):
            n += 1
    return n


def pctl(vals, p):
    """The p-th percentile with linear interpolation; None for an empty list."""
    vals = sorted(vals)
    if not vals:
        return None
    k = (len(vals) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(vals) - 1)
    return vals[f] + (vals[c] - vals[f]) * (k - f)


def phrase(p, flags=re.I):
    """A pattern for the words of p as a whole phrase."""
    return re.compile(r'\b' + r'[ ]+'.join(re.escape(w) for w in p.split()) + r'\b', flags)


def clip(t, n=110):
    """t, cut to n characters."""
    return t if len(t) <= n else t[:n - 3].rstrip() + '...'


# ----------------------------------------------------------------------------------------
# LaTeX -> plain text with the placeholders MATH, SYM, CITE and REF
# ----------------------------------------------------------------------------------------
def read_group(s, i):
    """s[i] is '{'.  Return (content, index after the closing brace)."""
    depth, j, n = 0, i, len(s)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], n


def skip_ws(s, i):
    """The index of the first character at or after i that is not white space."""
    while i < len(s) and s[i] in ' \t\n\v\x1f':
        i += 1
    return i


def read_optional(s, i):
    """An optional argument [..] at s[i]: (content, index after it), or (None, i)."""
    if i < len(s) and s[i] == '[':
        depth, j = 0, i
        while j < len(s):
            c = s[j]
            if c == '\\':
                j += 2
                continue
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    return s[i + 1:j], j + 1
            elif c == '{':
                _, j = read_group(s, j)
                continue
            j += 1
    return None, i


def replace_command(s, names, nargs, fn):
    """Replace every \\name*[opt]{a1}..{an} by fn(args, where); where() is the line on which
    the last argument starts."""
    pat = re.compile(r'\\(?:' + names + r')(?![A-Za-z@])\*?')
    out, pos = [], 0
    while True:
        m = pat.search(s, pos)
        if not m:
            break
        j = m.end()
        while True:
            o, j3 = read_optional(s, skip_ws(s, j) if nargs else j)
            if o is None:
                break
            j = j3
        args = []
        for _ in range(nargs):
            j2 = skip_ws(s, j)
            if j2 < len(s) and s[j2] == '{':
                a, j = read_group(s, j2)
                args.append(a)
            else:
                break
        if len(args) < nargs:
            out.append(s[pos:m.end()])
            pos = m.end()
            continue
        out.append(s[pos:m.start()])
        out.append(keep(s[m.start():j], fn(args, lambda at=j - 1 - len(args[-1]) if args else j: lineno(s, at))))
        pos = j
    out.append(s[pos:])
    return ''.join(out)


def replace_envs(s, envs, fn):
    """Replace \\begin{env}...\\end{env} by fn(envname, inner, where); where() is the line on
    which the inner text starts."""
    pat = re.compile(r'\\begin\{(' + envs + r')\}')
    out, pos = [], 0
    while True:
        m = pat.search(s, pos)
        if not m:
            break
        endtok = '\\end{' + m.group(1) + '}'
        e = s.find(endtok, m.end())
        if e < 0:
            break
        out.append(s[pos:m.start()])
        out.append(keep(s[m.start():e + len(endtok)],
                        fn(m.group(1), s[m.end():e], lambda at=m.end(): lineno(s, at))))
        pos = e + len(endtok)
    out.append(s[pos:])
    return ''.join(out)


def strip_comments(s):
    """Remove % comments.  A line that was only a comment does not break a paragraph."""
    out = []
    for line in s.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        if m:
            head = line[:m.start()]
            line = head.rstrip() + ' ' if head.strip() else GONE
        out.append(line)
    return soften('\n'.join(out))


DEF_PAT = re.compile(r'\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand|'
                     r'DeclareMathOperator)\*?\s*\{?\s*\\([A-Za-z@]+)\s*\}?\s*(?:\[(\d)\])?'
                     r'(?:\[[^\]]*\])?\s*(?=\{)')
DEF_PAT2 = re.compile(r'\\def\s*\\([A-Za-z@]+)\s*((?:#\d)*)\s*(?=\{)')


def collect_defs(s, defs):
    """Remove macro definitions and remember what each macro stands for."""
    for pat in (DEF_PAT, DEF_PAT2):
        out, pos = [], 0
        while True:
            m = pat.search(s, pos)
            if not m:
                break
            body, j = read_group(s, m.end())
            g2 = m.group(2) or ''
            nargs = g2.count('#') if pat is DEF_PAT2 else int(g2 or 0)
            b = re.sub(r'\\[xX]space', '', body).strip()
            unit = re.fullmatch(r'\\unit\{([^{}]*)\}', b)
            if nargs:
                defs[m.group(1)] = ('sym', nargs)
            elif unit:
                defs[m.group(1)] = ('unit', unit.group(1))
            elif b and re.fullmatch(r"[A-Za-z0-9 ,.'/\-]*", b):
                defs[m.group(1)] = ('text', b)
            else:
                defs[m.group(1)] = ('sym', 0)
            out.append(s[pos:m.start()] + keep(s[m.start():j], GONE))
            pos = j
        out.append(s[pos:])
        s = ''.join(out)
    return rsub(r'\\newlength\s*\{?\\[A-Za-z@]+\}?', '', s)


def si_value(v):
    """The number of a siunitx command as plain text."""
    v = v.replace('\\sim', '~').replace('\\approx', '≈')
    return re.sub(r'\\[A-Za-z]+', '', v).replace('{', '').replace('}', '').strip()


def si_unit(u):
    """The unit of a siunitx command as plain text."""
    u = re.sub(r'\\([A-Za-z]+)', lambda m: SI_UNITS.get(m.group(1), m.group(1)), u)
    return re.sub(r'[{}\s]', '', u)


def inline_math(s):
    """$...$ -> MATH.  Math glued to a word (PbF$_2$) is dropped; a stray $ is dropped."""
    tok = re.compile(r'\\.|\$', re.S)
    close = re.compile(r'((?:\\.|[^$\\])*)\$', re.S)
    out, i, last = [], 0, ''
    while True:
        m = tok.search(s, i)
        if not m:
            out.append(s[i:])
            break
        chunk = s[i:m.start()]
        out.append(chunk)
        if chunk:
            last = chunk[-1]
        i = m.end()
        if m.group(0) != '$':
            out.append(m.group(0))
            last = m.group(0)[-1]
            continue
        c = close.match(s, i)
        if not c or re.search(r'\n[ \t\v\x1f]*\n', c.group(1)):
            continue
        rep = '' if last.isalnum() else 'MATH'
        out.append(keep(c.group(0), rep))
        last = 'H' if rep else last
        i = c.end()
    return ''.join(out)


def tex_inline(s, defs):
    """A piece of LaTeX (body, abstract, caption) -> plain text with placeholders."""
    s = s.replace('\\%', '%').replace('\\&', '&').replace('\\$', '＄').replace('\\_', '_').replace('\\#', '#')
    s = rsub(r'\\\\\*?(\[[^\]]*\])?', ' ', s)
    s = rsub(r'\\item\s*\\textbf\{[^{}]*\}\s*\.?', r'\\item ', s)
    s = replace_command(s, 'texorpdfstring', 2, lambda a, where: a[0])

    def dm(inner):                                   # display math keeps its closing punctuation
        t = re.sub(r'\\label\{[^}]*\}', '', inner)
        t = re.sub(r'(\\[,;:!]|\\quad|\\qquad|~|\s)+$', '', t)
        return ' DMATH' + (t[-1] if t and t[-1] in '.,;' else '') + ' '
    s = replace_envs(s, r'linenomath\*?', lambda n, inner, where: inner)
    s = replace_envs(s, MATH_ENVS, lambda n, inner, where: dm(inner))
    s = rsub(r'\\\[(.*?)\\\]', lambda m: dm(m.group(1)), s, re.S)
    s = rsub(r'\$\$(.*?)\$\$', lambda m: dm(m.group(1)), s, re.S)
    s = replace_command(s, 'ensuremath', 1, lambda a, where: 'MATH')
    s = inline_math(s)
    s = rsub(r'\\\((.*?)\\\)', 'MATH', s, re.S)
    # a citation takes the space before it, but not a blank line
    s = rsub(r'(?:(?<![~\s])(?:[~ \t\v\x1f]|\n(?![ \t\v\x1f]*\n))*)?\\(?:cite|citep|citet|citealp|citeauthor|'
             r'citeyear|nocite|onlinecite)\*?(?:\[[^\]]*\])*\s*\{[^}]*\}', ' CITE', s)

    def ref_fn(m):                                   # \cref prints the word; \Cref and \autoref spell it out
        cmd, key = m.group(1), re.match(r'[a-z]*', m.group(2).strip().lower()).group(0)
        if cmd in ('cref', 'Cref', 'autoref'):
            word = {'fig': 'Fig.', 'figure': 'Fig.', 'tab': 'Table', 'tbl': 'Table', 'table': 'Table',
                    'sec': 'Section', 'subsec': 'Section', 'section': 'Section', 'eq': 'Eq.', 'eqn': 'Eq.',
                    'app': 'Appendix', 'ch': 'Chapter', 'chap': 'Chapter'}.get(key, '')
            if cmd != 'cref':
                word = {'Fig.': 'Figure', 'Eq.': 'Equation'}.get(word, word)
            return (word + ' REF') if word else 'REF'
        return '(REF)' if cmd == 'eqref' else 'REF'
    s = rsub(r'\\(ref|cref|Cref|autoref|eqref|pageref|nameref|subref)\*?\s*\{([^}]*)\}', ref_fn, s)
    s = replace_command(s, 'SIrange', 3,
                        lambda a, where: si_value(a[0]) + ' to ' + si_value(a[1]) + ' ' + si_unit(a[2]))
    s = replace_command(s, 'SIlist', 2,
                        lambda a, where: ' and '.join(si_value(x) for x in a[0].split(';')) + ' ' + si_unit(a[1]))
    s = replace_command(s, 'SI', 2, lambda a, where: si_value(a[0]) + ' ' + si_unit(a[1]))
    s = replace_command(s, 'numrange', 2, lambda a, where: si_value(a[0]) + ' to ' + si_value(a[1]))
    s = replace_command(s, 'num', 1, lambda a, where: si_value(a[0]))
    s = replace_command(s, 'si', 1, lambda a, where: si_unit(a[0]))
    s = replace_command(s, 'unit', 1, lambda a, where: ' ' + si_unit(a[0]))
    s = replace_command(s, 'href', 2, lambda a, where: a[1])
    s = replace_command(s, 'url|doi', 1, lambda a, where: 'URL')
    s = replace_command(s, 'textcolor', 2, lambda a, where: a[1])
    s = rsub(r'\\(?:textbf|textit|emph|textsc|textrm|texttt|textsf|text|mbox|hbox|underline|mathrm|'
             r'textnormal|textsuperscript|textsubscript|uppercase|lowercase|textup)(?![A-Za-z@])\s*', '', s)
    for n, names in ARG_DROP_MACROS.items():
        s = replace_command(s, names, n, lambda a, where: GONE)
    for n, names in ARG_SYM_MACROS.items():
        s = replace_command(s, names, n, lambda a, where: 'SYM')
    for name, d in defs.items():
        if d[0] == 'sym' and d[1]:
            s = replace_command(s, re.escape(name), d[1], lambda a, where: 'SYM')
    s = rsub(r"\\[`'^\"~=.]\s*\{?([A-Za-z])\}?", r'\1', s)              # accents
    s = re.sub(r'\\[cvuHtdb]\{([A-Za-z])\}', r'\1', s)
    s = re.sub(r'\\i(?![A-Za-z])', 'i', s)
    s = re.sub(r'\\[ ,;:>]', ' ', s)                                    # spacing commands
    s = s.replace('\\!', '').replace('\\-', '').replace('\\/', '').replace('\\@', '')
    s = re.sub(r'\\(?:quad|qquad|enspace|thinspace)(?![A-Za-z])', ' ', s)
    s = s.replace('~', ' ')
    s = rsub(r'\\begin\{[^}]*\}(\[[^\]]*\])?', PARA, s)
    s = re.sub(r'\\end\{[^}]*\}', PARA, s)
    src = s

    def mac(m):                                      # every macro that is left
        name = m.group(1)
        prev = src[m.start() - 1] if m.start() else ' '
        d = defs.get(name)
        if name == 'noindent':
            return ' NOINDENT '
        if name == 'par':
            return PARA
        if name == 'item':
            return PARA + 'ITEMMARK '
        if name in DROP_MACROS:
            return ''
        if d and d[0] == 'text':
            return d[1]
        if d and d[0] == 'unit':
            return ' ' + d[1]
        if name in UNIT_MACROS:
            return ('' if (prev.isspace() or prev in '-/(') else ' ') + UNIT_MACROS[name]
        return TEXT_MACROS.get(name, 'SYM')
    s = re.sub(r'\\([A-Za-z@]+)\*?', mac, src)
    s = s.replace('``', '“').replace("''", '”')
    s = re.sub(r"(?<![A-Za-z0-9])`", '‘', s)
    s = s.replace('---', '—').replace('--', '–').replace('＄', '$').replace('{', '').replace('}', '')
    s = re.sub(r'(?:SYM|MATH)(?:[ \t]*(?:SYM|MATH))+', lambda m: 'MATH' if 'MATH' in m.group(0) else 'SYM', s)
    return soften(s)


def read_tex(raw, path, defs, notes):
    """-> (segments, captions): segments are (kind, first line, LaTeX text), kind in
    abstract / body / footnote; captions are (figure or table, line, LaTeX text)."""
    s = strip_comments(raw)
    ends = [m.start() for m in (re.search(p, s) for p in END_PATTERNS) if m]
    ends += [m.start() for m in re.finditer(END_ACK, s) if m.start() > len(s) / 2][:1]
    s = s[:min(ends or [len(s)])]
    s = rsub(r'\\iffalse\b.*?\\fi\b', GONE, s, re.S)
    s = collect_defs(s, defs)
    m = re.search(r'\\begin\{document\}', s)
    if m:
        s = keep(s[:m.end()], GONE) + s[m.end():]
    inputs = re.findall(r'\\(?:input|include)(?![A-Za-z])[ \t]*(?:\{([^}]*)\}|([^\s{}\\]+))', s)
    if inputs:
        notes.append('%s: \\input is not followed; give these files too: %s' % (
            os.path.basename(path), ', '.join(a or b for a, b in inputs)))
    s = rsub(r'\\(?:input|include)(?![A-Za-z])[ \t]*(?:\{[^}]*\}|[^\s{}\\]+)', GONE, s)
    segs, caps = [], []
    s = replace_command(s, 'title|Title', 1, lambda a, where: GONE)

    def grab(kind, text, where):
        segs.append((kind, where(), text))
        return GONE
    s = replace_envs(s, 'abstract', lambda n, inner, where: grab('abstract', inner, where))
    if not segs:
        s = replace_command(s, 'abstract|Abstract', 1, lambda a, where: grab('abstract', a[0], where))
    if not segs and os.path.basename(path).lower().startswith('abstract'):
        segs.append(('abstract', 1, s))
        s = ''

    def float_fn(name, inner, where):
        kind = 'table' if 'table' in name else 'figure'
        for cm in re.finditer(r'\\(?:top)?caption(?![A-Za-z])\*?', inner):
            j = skip_ws(inner, read_optional(inner, skip_ws(inner, cm.end()))[1])
            if j < len(inner) and inner[j] == '{':
                caps.append((kind, where() + breaks(inner[:j + 1]), read_group(inner, j)[0]))
        return GONE
    s = replace_envs(s, FLOAT_ENVS, float_fn)
    s = replace_envs(s, DROP_ENVS, lambda n, inner, where: GONE)
    s = replace_command(s, 'label', 1, lambda a, where: GONE)
    s = replace_command(s, 'footnote', 1, lambda a, where: grab('footnote', a[0], where))
    s = replace_command(s, HEADINGS, 1, lambda a, where: PARA)
    return [g for g in segs if g[0] == 'abstract'] + [('body', 1, s)] + [g for g in segs if g[0] == 'footnote'], caps


# ----------------------------------------------------------------------------------------
# Markdown and plain text
# ----------------------------------------------------------------------------------------
STOP_HEAD = re.compile(r'(?:\d+\.?\s+)?(references|bibliography|acknowledge?ments?)\s*$', re.I)
CAPTION_START = re.compile(r'(?:Figure|Fig\.|FIG\.|Table|TABLE|Tab\.)\s+(?:REF|\d+[a-z]?|[IVX]+)\s*[.:|]\s*')


def read_plain(raw, md):
    """Markdown or plain text -> (segments, captions).  Blank lines separate paragraphs."""
    lines = raw.replace('\f', '\n').split('\n')
    out, caps, code, front = [], [], False, False

    def last_heading(title, i):          # references, or acknowledgments in the second half
        m = STOP_HEAD.match(title)
        return m and len(title.split()) <= 3 and (m.group(1)[0] in 'RrBb' or i > len(lines) / 2)
    for i, L in enumerate(lines):
        st = L.strip()
        if md and i == 0 and st == '---':
            front = True
        elif front:
            front = st not in ('---', '...')
            L = GONE
        if md and re.match(r'```|~~~', st):
            code = not code
            L = GONE
        elif code or front:
            L = GONE
        elif md and (st.startswith('|') or st.startswith('<!--') or re.fullmatch(r'[-=*_ ]{3,}', st)):
            L = GONE
        elif md and st.startswith('#'):
            if last_heading(st.lstrip('# '), i):
                break
            L = PARA
        elif md:
            img = re.match(r'!\[(.*?)\]\([^)]*\)', st)
            if img:
                if img.group(1).strip():
                    caps.append(('figure', i + 1, img.group(1)))
                L = GONE
            L = re.sub(r'^\s*>\s?', '', L)
            L = re.sub(r'^\s*(?:[-*+]|\d+[.)])\s+', PARA + 'ITEMMARK ', L)
            L = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', L)                 # links
            L = re.sub(r'\[\^[^\]]*\]:?', '', L)                          # footnote marks
            L = re.sub(r'\[-?@[^\]]*\]', ' CITE', L)                       # pandoc citations
            L = re.sub(r'`[^`]*`', 'SYM', L)
            L = re.sub(r'(\*\*|__)(?=\S)(.+?)(?<=\S)\1', r'\2', L)
            L = re.sub(r'(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])', r'\1', L)
            L = re.sub(r'(?<![\w_])_(?=\S)(.+?)(?<=\S)_(?![\w_])', r'\1', L)
        elif last_heading(st, i):
            break
        elif re.fullmatch(r'\d{1,3}', st):                                 # a page number
            L = GONE
        out.append(L)
    s = '\n'.join(out)
    if not md:                                       # a word split at a line end; a compound keeps its hyphen
        s = re.sub(r'([a-z])-\n[ \t]*([a-z]+)', lambda m: m.group(1) + (
            '-' if re.search(r'[A-Za-z]-[A-Za-z]+$', s[max(0, m.start() - 30):m.start() + 1]) else '')
            + m.group(2) + SOFT, s)
    return [('body', 1, soften(s))], caps


def plain_inline(t, cites):
    """Float numbers ("Fig. 3" -> "Fig. REF") and, outside LaTeX, numbered citations."""
    if cites:
        t = re.sub(r'\[\d+(?:\s*[,–-]\s*\d+)*\]', 'CITE', t)
    word = r'(?:Figures?|Figs?\.|FIG\.|Tables?|Tabs?\.|TABLE|Sections?|Secs?\.|Chapters?|Equations?|Eqs?\.|Refs?\.)'
    number = r'(?:\(\d+(?:\.\d+)*[a-z]?\)|\d+(?:\.\d+)*[a-z]?)(?![\d%])'
    t = re.sub(r'\b(' + word + r')[ \t]+' + number, r'\1 REF', t)
    for _ in range(4):
        t = re.sub(r'\bREF(,| and| to| or|–|-)[ \t]*' + number, r'REF\1 REF', t)
    return t


# ----------------------------------------------------------------------------------------
# paragraphs and sentences, with line numbers
# ----------------------------------------------------------------------------------------
SPLIT_RE = re.compile(r'([.!?])([”"’\')\]]*)\s+(?=[“"‘\'(\[]*(?:[A-Z0-9]|[a-z]{1,3}[A-Z]))')
NO_WORDS = re.compile(r'\b(?:D?MATH|SYM|CITE|REF)\b')


def split_sentences(par):
    """-> [(offset, sentence)].  Fig., Eq., e.g., i.e., et al. and initials do not end one;
    a one-letter unit after a number does ("3.8 T.", "58 V.")."""
    out, start = [], 0
    for m in SPLIT_RE.finditer(par):
        if m.group(1) == '.':
            pre = par[start:m.start(1)]
            w = re.search(r'([A-Za-z][A-Za-z.]*)$', pre)
            last = w.group(1) if w else ''
            if last not in PLACEHOLDERS and last.lower() in ABBR:
                continue
            if re.fullmatch(r'[A-Z]', last) and not re.search(
                    r'(?:\d|\b(?:bin|bins|region|regions|type|class|point|sample|vitamin|plan|part|option|case))'
                    r'\s+[A-Z]$', pre):
                continue
            if re.search(r'\b(?:Nos?|Refs?|Figs?|Eqs?|Secs?)$', pre):
                continue
        out.append((start, par[start:m.end(2)]))
        start = m.end()
    out.append((start, par[start:]))
    return [(o, t.strip()) for o, t in out if re.search(r'[A-Za-z]{2,}', NO_WORDS.sub('', t))]


def paragraphs(text, first_line):
    """Cleaned text with its marks -> [(kind, [(line, sentence), ...])], kind body or item.
    Display math, \\noindent and a lower-case start continue the paragraph before."""
    spans, pos = [], 0
    for m in list(BREAK.finditer(text)) + [None]:
        a, b = pos, (m.start() if m else len(text))
        pos = m.end() if m else b
        t = tidy(text[a:b])
        kind = 'item' if t.startswith('ITEMMARK') else 'body'
        t = tidy(t.replace('ITEMMARK', ' '))
        only_math = re.fullmatch(r'(?:DMATH[.,;]?\s*)+', t) is not None
        noindent = t.startswith('NOINDENT')
        t = tidy(t.replace('NOINDENT', ' '))
        if not t:
            continue
        if spans and kind == 'body' and (only_math or noindent or re.match(r'[a-z]', t)):
            spans[-1][2] = b
        else:
            spans.append([kind, a, b])
    out, done, line = [], 0, first_line
    for kind, a, b in spans:
        line += breaks(text[done:a])
        done = b
        raw = text[a:b].replace('ITEMMARK', ' ').replace('NOINDENT', ' ')
        while re.search(r'\(\s*\)', raw):
            raw = rsub(r'\(\s*\)', '', raw)
        raw = re.sub(r'\bDMATH(?=\s+(?:[“"‘]|\(\s*)*[A-Z])', 'MATH.', raw).replace('DMATH', 'MATH')
        lines = []                                   # the line of each character that is not a space
        for ch in raw:
            if ch == '\n' or ch == SOFT:
                line += 1
            elif not ch.isspace():
                lines.append(line)
        clean = tidy(raw)
        sents = [(lines[min(o - clean.count(' ', 0, o), len(lines) - 1)], t)
                 for o, t in split_sentences(clean)]
        if sents:
            out.append((kind, sents))
    return out


TEX = ('.tex', '.ltx', '.latex')


def read_file(path):
    """The text of a file with plain line ends and without the three control characters."""
    with open(path, encoding='utf-8', errors='replace') as fh:
        raw = fh.read().replace('\r\n', '\n').replace('\r', '\n')
    return raw.replace(SOFT, ' ').replace(PARA, ' ').replace(GONE, ' ')


class Draft(object):
    """The sentences and captions of all files, with file, line, paragraph and kind."""

    def __init__(self):
        self.files = []
        self.sents = []      # dict: t text, n words, f file, l line, p paragraph, k kind
        self.caps = []       # dict: kind, f file, l line, t text, ss sentences
        self.npar = 0
        self.notes = []

    def add(self, path, name, defs):
        raw, ext = read_file(path), os.path.splitext(path)[1].lower()
        if ext in TEX:
            ext = '.tex'
            segs, caps = read_tex(raw, path, defs, self.notes)
        else:
            segs, caps = read_plain(raw, ext in ('.md', '.markdown'))
        self.files.append(name)
        for kind, line0, text in segs:
            for pkind, sents in paragraphs(plain_inline(tex_inline(text, defs), ext != '.tex'), line0):
                first = sents[0][1]
                if ext != '.tex' and CAPTION_START.match(first):          # "Figure 2: ..." paragraph
                    t = CAPTION_START.sub('', ' '.join(t for _, t in sents), 1)
                    self._caption('table' if first[0] in 'Tt' else 'figure', name, sents[0][0], t)
                    continue
                if ext != '.tex' and len(sents) == 1 and not re.search(r'[.!?:]["”’)\]]*$', first):
                    continue                                              # a heading or a stray line
                k = kind if kind != 'body' else pkind
                for line, t in sents:
                    self.sents.append({'t': t, 'n': count_words(t), 'f': name, 'l': line, 'p': self.npar, 'k': k})
                self.npar += 1
        for kind, line, text in caps:
            t = plain_inline(tex_inline(text, defs), ext != '.tex')
            t = tidy(t.replace('NOINDENT', ' ').replace('ITEMMARK', ' ')).replace('DMATH', 'MATH')
            self._caption(kind, name, line, t)

    def _caption(self, kind, name, line, t):
        if t:
            self.caps.append({'kind': kind, 'f': name, 'l': line, 't': t,
                              'ss': [x for _, x in split_sentences(t)] or [t]})


# ----------------------------------------------------------------------------------------
# measuring
# ----------------------------------------------------------------------------------------
def opener(t):
    """-> (class, word): class in connector, connector2, thing, we, fronted or ''."""
    t = re.sub(r'^[“"‘\'(\[]+', '', t)
    w1 = core_of(t.split()[0]) if t.split() else ''
    for cls, words in LONGEST_FIRST:
        if cls == 'fronted' and w1 in DET_OPENERS + ['We', 'Our']:
            return ('we' if w1 in ('We', 'Our') else 'thing'), w1
        for p in words:
            rest = t[len(p):]
            if not t.startswith(p) or (rest and (rest[0].isalnum() or rest[0] == '-')):
                continue
            if p == 'In addition' and rest.startswith(' to'):
                continue
            if p in ('First', 'Second', 'Third', 'Next') and not re.match(
                    r',| (?:of all|we|i|the|a|an|it|this|these|there|one|each|all|let)\b', rest, re.I):
                continue
            return cls, p
    return '', w1


def toks_of(s):
    """[(token, lower-cased core)]; the core of a placeholder is '<ph>'."""
    out = []
    for raw in s.split():
        c = core_of(raw)
        out.append((raw, '<ph>' if c in PLACEHOLDERS else c.lower()))
    return out


def passives(s):
    """A form of "be" followed within three words by a past participle."""
    tk, n = toks_of(s), 0
    for i, (raw, low) in enumerate(tk):
        if low not in BE_FORMS or raw[-1:] in ',;:':
            continue
        for r2, l2 in tk[i + 1:i + 4]:
            if l2 in IRREG_PP or (l2.endswith('ed') and len(l2) > 3 and l2 not in ED_NOT_PP):
                n += 1
                break
            if (l2 in PASSIVE_BLOCK or l2 in BE_FORMS or l2 == '<ph>' or r2[-1:] in ',;:' or not l2
                    or not re.fullmatch(r'[a-z\-]+', l2)):
                break
    return n


def so_joins(s):
    """"so" as a conjunction: after a comma or semicolon, after "and", before "that", or first."""
    tk, hits = toks_of(s), []
    for i, (_, low) in enumerate(tk):
        if low != 'so':
            continue
        prev_raw, prev = (tk[i - 1] if i else ('', ''))
        nxt = tk[i + 1][1] if i + 1 < len(tk) else ''
        if nxt in ('far', 'on', 'forth', 'much', 'many', 'little', 'few', 'as', 'called') or prev in (
                'or', 'do', 'doing', 'does', 'did', 'if', 'even', 'not', 'done'):
            continue
        if i == 0 or prev_raw.endswith((',', ';')) or prev == 'and' or nxt == 'that':
            hits.append('so that' if nxt == 'that' else 'and so' if prev == 'and' else 'So' if i == 0 else ', so')
    return hits


def causal_since(s):
    """The number of "since" that give a reason ("since 2018", "since then", "ever since" do not)."""
    tk, n = toks_of(s), 0
    for i, (_, low) in enumerate(tk):
        if low != 'since':
            continue
        prev = tk[i - 1][1] if i else ''
        nxt = tk[i + 1][1] if i + 1 < len(tk) else ''
        nxt2 = tk[i + 2][1] if i + 2 < len(tk) else ''
        if prev in ('ever', 'long', 'years', 'time', 'decades'):
            continue
        if re.match(r'\d', nxt) or nxt in ('then', 'run', 'early', 'late', 'mid', 'last', 'inception', 'long'):
            continue
        if nxt in ('its', 'their', 'the', 'that') and (re.match(r'\d', nxt2) or nxt2 in (
                'inception', 'beginning', 'start', 'early', 'late', 'first', 'last', 'time', 'discovery',
                'introduction', 'advent', 'end', 'initial')):
            continue
        n += 1
    return n


def caption_opening(t):
    """-> article, panel, other or bare (a noun phrase without article; a symbol counts)."""
    t = re.sub(r'^\([^()]{1,30}\)\s*', '', t)
    tk = re.sub(r'^[“"‘\'(\[]+', '', t).split()
    w1 = core_of(tk[0]) if tk else ''
    if w1 in ('The', 'A', 'An'):
        return 'article'
    if w1 in ('Left', 'Right', 'Top', 'Bottom', 'Upper', 'Lower', 'Center'):
        return 'panel'
    if w1 in FRONTED or w1 in ('Same', 'Here', 'This', 'These', 'Each', 'All', 'Two', 'Three', 'We', 'Shown',
                               'On', 'Within', 'During', 'Over', 'Among'):
        return 'other'
    return 'bare'


REF_SUBJ = re.compile(r'\b(' + FLOAT_W + r') REF(?:\s*\([^)]*\))?(?:(?:,| and| or|–) REF(?:\s*\([^)]*\))?)*\s+'
                      r'(?:also\s+|then\s+|further\s+|thus\s+)?(' + SUBJ_VERBS + r')\b')
REF_PAREN = re.compile(r'\((?:(?:see|cf\.|e\.g\.,?|i\.e\.,?)[ ]+(?:also[ ]+)?)?' + FLOAT_W + r' REF[^()]*\)', re.I)
REF_SEE = re.compile(r'(?<!\()\b[Ss]ee[ ]+(?:also[ ]+)?' + FLOAT_W + r' REF')


def ref_forms(t):
    """Counts for one sentence: mentions, float as subject, participle + in, as shown in."""
    c = {'n': len(re.findall(r'\b' + FLOAT_W + r' REF', t)), 'subj': len(REF_SUBJ.findall(t)), 'in': 0, 'as': 0}
    for p in LOC_PHRASES:
        for m in re.finditer(r'\b' + p.replace(' ', r'[ ]+') + r'[ ]+(?:the[ ]+)?(?:\w+[ ]+){0,2}?' + FLOAT_W + r' REF',
                             t, re.I):
            if not p.startswith('as ') and re.search(r'\bas[ ]+$', t[:m.start()], re.I):
                continue
            if re.search(r'\b(?:not|never)[ ]+(?:\w+[ ]+)?$', t[:m.start()], re.I):
                continue                             # "is not shown in Fig. N" introduces nothing
            c['in'] += 1
            c['as'] += p == 'as shown in'
    return c


def measure(d):
    """-> {key: (value, weight, count, digits)}.  weight turns a distance from the range
    into a number of items (sentences, captions, occurrences); see mark()."""
    S = d.sents
    ns, nw = len(S), sum(s['n'] for s in S)
    text = '\n'.join(s['t'] for s in S)
    M = {}

    def share(key, n, of):
        M[key] = (100.0 * n / of if of else None, of / 100.0, n, 1)

    def rate(key, n, per):
        M[key] = (float(n) * per / nw if nw else None, float(nw) / per, n, 2 if per == 1000 else 1)

    def count(key, n):
        M[key] = (n, 1e9, None, 0)

    def median(key, vals):
        M[key] = (pctl(vals, 50), 1.0 if ns < SMALL_TEXT else 1e9, None, 1)

    def n_of(p):
        return len(phrase(p).findall(text))

    lens = [s['n'] for s in S]
    median('sent_median', lens)
    share('sent_le12', sum(x <= 12 for x in lens), ns)
    share('sent_gt30', sum(x > 30 for x in lens), ns)
    share('sent_gt40', sum(x > 40 for x in lens), ns)

    per_s, per_w = {}, {}
    for s in S:
        if s['k'] == 'body':
            per_s[s['p']] = per_s.get(s['p'], 0) + 1
            per_w[s['p']] = per_w.get(s['p'], 0) + s['n']
    npar = len(per_s)
    median('par_median', list(per_s.values()))
    median('par_words', list(per_w.values()))
    share('par_one', sum(x == 1 for x in per_s.values()), npar)
    share('par_ge8', sum(x >= 8 for x in per_s.values()), npar)

    share('we_any', sum(1 for s in S if re.search(r'\b[Ww]e\b', s['t'])), ns)
    share('passive', sum(1 for s in S if passives(s['t'])), ns)

    cls, conn, this_verb = {}, {}, 0
    for s in S:
        c, w = opener(s['t'])
        cls[c] = cls.get(c, 0) + 1
        if c in ('connector', 'connector2'):
            conn[w] = conn.get(w, 0) + 1
        elif c:
            cls[w] = cls.get(w, 0) + 1
        tk = re.sub(r'^[“"‘\'(\[]+', '', s['t']).split()
        if c == 'thing' and w == 'This' and len(tk) > 1 and core_of(tk[1]).lower() in THIS_VERBS:
            this_verb += 1
    share('we_open', cls.get('we', 0), ns)
    share('open_thing', cls.get('thing', 0), ns)
    share('open_this', cls.get('This', 0), ns)
    share('this_verb', this_verb, cls.get('This', 0))
    share('open_fronted', cls.get('fronted', 0), ns)
    share('open_for', cls.get('For', 0), ns)
    share('open_with', cls.get('With', 0), ns)
    share('open_to', cls.get('To', 0), ns)
    share('open_conn', cls.get('connector', 0), ns)
    for w in HIS_SEVEN + sorted(k for k in conn if k not in HIS_SEVEN and k not in NOT_CONNECTORS):
        share('conn:' + w, conn.get(w, 0), ns)

    rate('c_since', sum(causal_since(s['t']) for s in S), 10000)
    rate('c_due', n_of('due to'), 10000)
    rate('c_therefore', n_of('therefore'), 10000)
    rate('c_because', n_of('because'), 10000)
    rate('c_hence', n_of('hence'), 10000)
    rate('c_thus', n_of('thus'), 10000)
    rate('c_so', sum(len(so_joins(s['t'])) for s in S), 10000)
    used = sum(1 for k in ('c_since', 'c_due', 'c_therefore', 'c_because', 'c_hence', 'c_thus', 'c_so') if M[k][2])
    M['c_used'] = (used, 1e9 if nw >= MIN_WORDS_CAUSAL else 0.0, None, 0)

    about = len(re.findall(r'\b[Aa]bout[ ]+(?:\d[\d.,]*|MATH|a factor|' + '|'.join(NUMBER_WORDS) + r')\b', text))
    around = len(re.findall(r'\b[Aa]round[ ]+(?:\d|MATH)', text))
    rate('ap_all', n_of('approximately') + n_of('roughly') + about + around + n_of('nearly') + n_of('almost'), 1000)
    rate('ap_roughly', n_of('roughly'), 1000)
    rate('ap_about', about, 1000)
    rate('ap_approx', n_of('approximately'), 1000)
    rate('int_six', sum(n_of(w) for w in SIX_INTENSIFIERS), 1000)
    rate('praise', sum(n_of(w) for w in PRAISE), 10000)
    rate('suffice', len(re.findall(r'\b(?:' + SUFFICIENCY + r')\b', text, re.I)), 10000)

    rate('p_semi', text.count(';'), 1000)
    rate('p_colon', len(re.findall(r':(?!\d)', text)), 1000)
    rate('p_dash', text.count('—') + len(re.findall(r'(?<=\s)–(?=\s)', text))
         + len(re.findall(r'(?<=[A-Za-z)])\s-\s(?=[A-Za-z(])', text)), 1000)
    rate('p_paren', text.count('('), 1000)

    C = d.caps
    words = [count_words(c['t']) for c in C]
    median('cap_words', words)
    count('cap_max', max(words) if words else None)
    median('cap_sents', [len(c['ss']) for c in C])
    share('cap_ge4', sum(len(c['ss']) >= 4 for c in C), len(C))
    share('cap_bare', sum(caption_opening(c['t']) == 'bare' for c in C), len(C))
    share('cap_frag', sum(not FINITE_VERBS.search(c['ss'][0]) for c in C), len(C))

    refs = dict.fromkeys(('n', 'subj', 'in', 'as', 'paren', 'see', 'fig_start', 'figure_start', 'figure_in'), 0)
    for s in S:
        for k, v in ref_forms(s['t']).items():
            refs[k] += v
        refs['paren'] += len(REF_PAREN.findall(s['t']))
        refs['see'] += len(REF_SEE.findall(s['t']))
        for m in re.finditer(r'\b(Figs?\.|Figures?) REF', s['t']):
            first = s['t'][:m.start()].strip(EDGE + ' ') == ''
            if m.group(1).endswith('.'):
                refs['fig_start'] += first
            else:
                refs['figure_start' if first else 'figure_in'] += 1
    rate('ref_rate', refs['n'], 1000)
    share('ref_subj', refs['subj'], refs['n'])
    share('ref_in', refs['in'], refs['n'])
    for k in ('as', 'paren', 'see'):
        count('ref_' + k, refs[k])
    everything = text + '\n' + '\n'.join(c['t'] for c in C)
    count('sec_abbr', len(re.findall(r'\bSecs?\.', everything)))
    count('sec_full', len(re.findall(r'\bSections?\b', everything)))
    for k in ('fig_start', 'figure_start', 'figure_in'):
        count(k, refs[k])
    return M, {'words': nw, 'sentences': ns, 'paragraphs': npar, 'captions': len(C)}


def mark(value, weight, rng):
    """'above', 'below' or ''.  A share or a rate must be MIN_ITEMS items outside the range;
    so must a median, in its own unit, when the text has fewer than SMALL_TEXT sentences."""
    if value is None or rng is None:
        return ''
    lo, hi = rng
    if hi is not None and value > hi and (value - hi) * weight >= MIN_ITEMS:
        return 'above'
    if lo is not None and value < lo and (lo - value) * weight >= MIN_ITEMS:
        return 'below'
    return ''


def rows(M, profile):
    """The table as a list of dicts, in the order of SPEC."""
    col = 2 + PROFILES.index(profile)
    out, group = [], ''
    for spec in SPEC:
        if spec == 'CONNECTORS':
            for key in [k for k in M if k.startswith('conn:')]:
                w = key[5:]
                avoid = (0, 0.2) if profile == 'thesis' else (0, 0)
                out.append(row(group, key, w, M[key], avoid if w in AVOID_OPENERS else (0, 2)))
        elif isinstance(spec, str):
            group = spec
        else:
            out.append(row(group, spec[0], spec[1], M[spec[0]], spec[col]))
    return out


def row(group, key, label, m, rng):
    """One row of the table as a dict."""
    value, weight, n, digits = m
    return {'group': group, 'key': key, 'label': label, 'value': None if value is None else round(value, 2),
            'count': n, 'low': rng[0] if rng else None, 'high': rng[1] if rng else None,
            'mark': mark(value, weight, rng), 'digits': digits}


# ----------------------------------------------------------------------------------------
# sentences to look at
# ----------------------------------------------------------------------------------------
def groups(profile):
    """The groups of flags in the order of the report: (key, title, what he does)."""
    words, sents = RANGE[profile]['cap_words'], RANGE[profile]['cap_sents']
    his = HIS_SEVEN + HIS_ALSO + HIS_BY_PROFILE[profile]
    return [
        ('we_run', 'Three or more sentences in a row that open with "We"',
         '"We" should mark where the authors chose, tested, ran or concluded something. Give an operation '
         'on recorded data the thing as its subject; a study or a simulation run of the authors keeps "we".'),
        ('so', '"so" as the causal join',
         'One join used again and again makes every step read alike. He writes it about once in 2000 words, '
         'so one may stay. For the others: under about 25 words keep one sentence, with a fronted "Since", '
         '"due to" plus a noun phrase, or a tail (", making X a Y", ", thus ...ing", ", which" plus a verb); '
         'split off a "This" + verb sentence only after a first clause of about 15 words or more.'),
        ('float', 'Figure or table cited in parentheses or with "see"',
         'The reader should learn what is plotted before the result. Introduce the float by a sentence with '
         'the float or the plotted thing as subject: "Figure N shows X." or "X is shown in Fig. N." A figure '
         'that illustrates one statement carries it in a clause: "Figure N shows X, in which ...".'),
        ('caption', 'Captions that open with an article or a full sentence, or run beyond the range',
         'A caption says what is plotted and how to read it. Open with a noun phrase without article and '
         'without verb. Range of the median: %d to %d words, %d to %d sentences. Move out only what explains '
         'or argues (a derivation, the physical reason, a second finding). A limit of what the plot shows, '
         'the definition of a plotted element and how a point was obtained stay in the caption. If it is '
         'still long, leave it and report its length.' % (words + sents)),
        ('avoid', 'Words and phrases from the avoid list, and dashes',
         'A rare word makes the reader ask whether a special meaning is intended. These are absent or nearly '
         'absent from the texts he wrote alone. The plain form follows the colon. A term that the draft '
         'defines and uses throughout stays; propose the change for the whole paper.'),
        ('intensifier', 'Intensifiers and praise words',
         'A number carries the size of an effect; an intensifier asks for trust. Give the number or the '
         'requirement. "Significant" in the statistical sense stays. In a polish, propose the removal in '
         'the report; "significantly" before a measured difference is a claim, so ask the authors.'),
        ('long', 'Sentences above 45 words that are not a list',
         'He passes 40 words mostly for a list or a definition. Split, or give the reason a "This" + '
         'verb sentence.'),
        ('connector', 'Sentence-initial connectors that his own texts do not open with',
         'A connector should tell the reader whether the sentence adds, turns or concludes. His own texts '
         'open sentences with: ' + ', '.join(his) + '.'),
        ('sec', '"Sec." and "Tab."',
         'He writes "Table" in full in all six documents, and "Section" in full in the three that refer to a '
         'section; "Sec." is in none of the six. The journal decides: where it prints "Sec.", keep the '
         'draft\'s "Sec." and name it in the report.'),
        ('approx', '"approximately" before a number (information only)',
         'His own voice rounds with "roughly" or "about". CMS style prefers "approximately": keep it where the '
         'paper follows CMS rules.'),
    ]


def is_list(t):
    """A colon, a semicolon, two enumerators such as (a) (b), or three short items in a row."""
    if re.search(r':(?!\d)|;', t) or len(re.findall(r'\((?:[a-z]|[ivx]{1,4}|\d)\)', t)) >= 2:
        return True
    run = 0
    for part in t.split(',')[1:]:
        run = run + 1 if 0 < len(part.split()) <= 5 else 0
        if run >= 3:
            return True
    return False


def find_flags(d, profile):
    """-> {group key: [{file, line, why, text}]}, each list in reading order."""
    F = {}

    def add(key, s, why):
        F.setdefault(key, []).append({'file': s['f'], 'line': s['l'], 'why': why, 'text': clip(s['t'])})

    def quoted(m):
        return '"%s"' % clip(m.group(0).strip().replace('REF', 'N'), 40)

    run = []
    for s in d.sents + [None]:
        we = s is not None and opener(s['t']) == ('we', 'We')
        if we and (not run or run[-1]['p'] == s['p']):
            run.append(s)
            continue
        if len(run) >= 3:
            add('we_run', run[0], '%d sentences, lines %d to %d' % (len(run), run[0]['l'], run[-1]['l']))
        run = [s] if we else []
    his = HIS_SEVEN + HIS_ALSO + HIS_BY_PROFILE[profile] + NOT_CONNECTORS
    number = r'[ ]+(?:(?:a|an|the)[ ]+)?(?:\d[\d.,]*\d|\d|MATH|factor|half|twice|' + '|'.join(NUMBER_WORDS) + r')\b'
    for s in d.sents:
        t = s['t']
        cls, word = opener(t)
        connector = cls in ('connector', 'connector2')
        for hit in so_joins(t):
            add('so', s, '"%s"' % hit)
        m = REF_SEE.search(t) or REF_PAREN.search(t)
        if m:
            add('float', s, quoted(m))
        for pat, fix in AVOID:
            m = pat.search(t)
            if m and not (connector and m.start() == 0):
                add('avoid', s, '%s: %s' % (quoted(m), fix))
        m = LOOK_AT.search(t)
        if m:
            add('intensifier', s, quoted(m))
        if s['n'] > 45 and not is_list(t):
            add('long', s, '%d words' % s['n'])
        if connector and word not in his:
            add('connector', s, '"%s"' % word)
        m = re.search(r'\b(?:Secs?|Tabs?)\.', t)
        if m:
            add('sec', s, quoted(m))
        m = re.search(r'\b[Aa]pproximately' + number, t)
        if m and profile != 'cms-letter':
            add('approx', s, quoted(m))
    max_words, max_sents = RANGE[profile]['cap_words'][1], RANGE[profile]['cap_sents'][1]
    for c in d.caps:
        why, n = [], count_words(c['t'])
        verb = SURE_VERBS.search(c['ss'][0])
        if caption_opening(c['t']) == 'article':
            why.append('opens with an article')
        elif caption_opening(c['t']) != 'bare':
            why.append('does not open with what is plotted')
        if verb:
            why.append('first sentence is a full sentence ("%s")' % verb.group(0))
        if n > max_words:
            why.append('%d words' % n)
        if len(c['ss']) > max_sents:
            why.append('%d sentences' % len(c['ss']))
        if re.search(r'\b[Ww]e\b', c['t']):
            why.append('has "we"')
        if why:
            add('caption', c, '; '.join(why))
        m = re.search(r'\b(?:Secs?|Tabs?)\.', c['t'])
        if m:
            add('sec', c, quoted(m) + ' in a caption')
    order = {f: i for i, f in enumerate(d.files)}
    for items in F.values():
        items.sort(key=lambda x: (order[x['file']], x['line']))
    return F


# ----------------------------------------------------------------------------------------
# output
# ----------------------------------------------------------------------------------------
def show_range(lo, hi):
    """A range in words: "19 to 22", "at most 5", "at least 4", "0", or "-" for none."""
    if lo is None and hi is None:
        return '-'
    if hi is None:
        return 'at least %g' % lo
    if lo == hi:
        return '%g' % lo
    return ('at most %g' % hi) if lo == 0 else '%g to %g' % (lo, hi)


def show_value(r):
    """The value of a row, with the count behind a share or a rate in parentheses."""
    if r['value'] is None:
        return '-'
    v = '%.*f' % (r['digits'], r['value'])
    if r['count'] is None:
        return v[:-2] if v.endswith('.0') else v
    return '%s (%d)' % (v, r['count'])


def report(d, table, counts, flags, profile, max_flags):
    """The plain-text report: notice, counts, table, sentences to look at."""
    out = [NOTICE, '', 'files: %s' % ', '.join(d.files),
           'profile: %s    words: %d    sentences: %d    paragraphs: %d    captions: %d' % (
               profile, counts['words'], counts['sentences'], counts['paragraphs'], counts['captions'])]
    out += ['note: ' + n for n in d.notes]
    out += ['', '%-70s %12s  %-12s %s' % ('metric', 'draft', 'his range', 'mark'), '-' * 104]
    group = None
    for r in table:
        if r['group'] != group:
            group = r['group']
            out.append(group.upper())
        out.append(('  %-68s %12s  %-12s %s' % (
            r['label'], show_value(r), show_range(r['low'], r['high']), r['mark'])).rstrip())
    ranged = [r for r in table if r['low'] is not None or r['high'] is not None]
    if counts['sentences'] < SMALL_TEXT:
        total = ('Fewer than %d sentences: the ranges describe a whole paper. Use the sentences listed below, '
                 'not the marks. In parentheses: the count behind a share or a rate.' % SMALL_TEXT)
        rule = ('A share, a rate or a median is marked only when it is at least %.1f items (for a median: '
                'units) outside the range.' % MIN_ITEMS)
    else:
        total = '%d of %d rows that have a range are marked. In parentheses: the count behind a share or a rate.' % (
            sum(1 for r in ranged if r['mark']), len(ranged))
        rule = 'A share or a rate is marked only when it is at least %.1f items outside the range.' % MIN_ITEMS
    out += ['-' * 104, total, rule,
            'The marks are not a score: never choose between two wordings by the number of marked rows.',
            '', 'SENTENCES TO LOOK AT (at most %d per group)' % max_flags]
    for key, title, hint in groups(profile):
        items = flags.get(key, [])
        if items:
            out += ['', '%s: %d' % (title, len(items)),
                    textwrap.fill(hint, 100, initial_indent='  ', subsequent_indent='  ')]
            for it in items[:max_flags]:
                out += ['  %s:%d  %s' % (it['file'], it['line'], it['why']), '      ' + it['text']]
            if len(items) > max_flags:
                out.append('  ... and %d more' % (len(items) - max_flags))
    if not flags:
        out.append('  none')
    return '\n'.join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Compare the surface style of a draft with Andre Frankenthal's papers. "
                                             "A smoke detector: no flag is an order.")
    ap.add_argument('files', nargs='+', help='.tex, .md or .txt files of one draft')
    ap.add_argument('--targets', choices=PROFILES, default='short-paper', help='range profile (default: short-paper)')
    ap.add_argument('--max-flags', type=int, default=10, metavar='N', help='sentences listed per group (default 10)')
    ap.add_argument('--json', action='store_true', help='print the same data as JSON')
    ap.add_argument('--dump', action='store_true', help='print the sentences and captions as read, then stop')
    a = ap.parse_args(argv)
    for p in a.files:
        if not os.path.isfile(p):
            ap.error('no such file: %s' % p)
    d, defs = Draft(), {}
    for p in a.files:                                # the macros of every file, before any text is read
        if os.path.splitext(p)[1].lower() in TEX:
            collect_defs(strip_comments(read_file(p)), defs)
    names = [os.path.basename(p) for p in a.files]
    for p, name in zip(a.files, names if len(set(names)) == len(names) else a.files):
        d.add(p, name, defs)
    if a.dump:
        for s in d.sents:
            print('%s:%d\t%s\t%d\t%s' % (s['f'], s['l'], s['k'], s['n'], s['t']))
        for c in d.caps:
            print('%s:%d\t%s caption\t%d\t%s' % (c['f'], c['l'], c['kind'], count_words(c['t']), c['t']))
        return 0
    if not d.sents:
        ap.error('no sentences found in the input. ' + ' '.join(d.notes))
    M, counts = measure(d)
    if counts['sentences'] < 50:
        d.notes.append('fewer than 50 sentences: the shares are rough, read the counts in parentheses.')
    elif counts['sentences'] < SMALL_TEXT:
        d.notes.append('fewer than %d sentences: the ranges describe a whole paper; use the list of sentences, '
                       'not the marks.' % SMALL_TEXT)
    table = rows(M, a.targets)
    flags = find_flags(d, a.targets)
    if a.json:
        print(json.dumps({
            'notice': NOTICE, 'files': d.files, 'profile': a.targets, 'counts': counts, 'notes': d.notes,
            'metrics': [{k: v for k, v in r.items() if k != 'digits'} for r in table],
            'flags': [{'key': k, 'title': t, 'hint': h, 'total': len(flags.get(k, [])),
                       'items': flags.get(k, [])[:a.max_flags]} for k, t, h in groups(a.targets)]},
            ensure_ascii=False, indent=1))
    else:
        print(report(d, table, counts, flags, a.targets, a.max_flags))
    return 0


if __name__ == '__main__':
    try:
        status = main()
        sys.stdout.flush()
    except BrokenPipeError:                          # the reader of a pipe (head, less) stopped early
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        status = 0
    sys.exit(status)
