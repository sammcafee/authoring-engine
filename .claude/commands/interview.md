---
description: Interview the author to build a non-fiction book's brief, chapter map, and Stage 1 raw material, starting from nothing
---

# /interview: from the author's head to Stage 1

`/draft` long-form starts at `01-raw-statements.md`, which assumes there is
existing material to pull claims from. Most new books have none. This
command fills that gap: it interviews you, and turns what you say into the
same voiceless Stage 1 files `/draft` already expects. Everything after
Stage 1 (clusters, skeleton, draft, gate, `/learn`) is unchanged.

It is built for non-fiction: books that argue something, teach something,
or pass on hard-won experience. You are the author and the source. The
session is the interviewer and the scribe. It asks good questions and
keeps the books; it never decides what you think.

Two modes:

- **Greenfield.** No manuscript. Run all four modules in order.
- **Gap-fill.** A manuscript exists but some sections are thin or missing
  (a section the draft promises but never delivers, a bridge with no
  material behind it). Tag everything you capture so it merges cleanly
  with the statements already pulled from the manuscript. Before skipping
  ahead, check that the book-level frame is still current: read the
  existing plan or outline back to the author in two or three lines and ask
  whether the thesis, reader, and scope still hold. If any has moved, run a
  fast module 1 (and module 2, if the structure moved) before module 3.
  Thin sections are often thin because the book's direction changed.

## Ground rules

- **One question at a time** by default. A short cluster (two or three) is
  fine only for quick factual items. Assume the author may be on a phone.
- **Accept any input style.** If the author dumps a long answer or a voice
  memo transcript, extract everything from it, show what you captured, and
  ask only about the gaps. Never make them repeat themselves.
- **"I don't know" gets options.** Offer two or three concrete options that
  fit what they've already said, plus "something else". Their pick is
  theirs; unpicked options are discarded, not saved.
- **Never invent material silently.** Anything you propose is tagged
  `[PROPOSED]` until the author accepts it. Anything they hand you outright
  ("you decide") is tagged `[DELEGATED]`, so the drafting stage and the
  author's later edit know to weigh it more heavily.
- **Capture words, not summaries.** The author's actual phrasing is the
  raw material for their voice later. Record it verbatim in the interview
  notes. Clean spoken disfluencies ("um", "like", false starts, obvious
  transcription errors); never change word choice or intensifiers.
- **No generic pushback.** When you test a claim, either name something
  concrete and checkable the author would actually have to weigh (a
  specific study, a named source, a counter-example from their own
  answers), or don't push back at all. A pattern-matched "some would say
  otherwise" is noise, and it trains the author to hedge. Ask "when doesn't
  this hold?" instead: that gets the boundary from the person who knows it.
- **Reflect back** at the end of each module, and each chapter in module 3:
  a compact summary, then ask for corrections before moving on.
- **Let the author steer depth.** Offer a fast track at the start of each
  module ("I'll take reasonable defaults for the rest of this").
- **Track progress visibly**: which module, which chapter, roughly how many
  are left.
- **The files are the state.** If the interview spans sessions, read the
  files and resume from the first incomplete section. Never re-ask what is
  already answered there.
- **Leave a `RESUME.md` at every pause.** "The files are the state" needs
  one file that says which state: where the interview stopped, the exact
  next question or prompt list, open gaps not to press on, and how to
  restart ("paste the transcript and say: resume the interview"). Commit it
  with everything else.
- **Research pauses are supported.** The author may stop mid-interview and
  ask you to look something up. Do it, record every finding in an evidence
  file with its source and a status of `verify`, summarize it briefly, then
  return to the exact question you paused on. Research informs the author's
  choices; it never writes a raw statement on their behalf. A finding only
  becomes a claim when the author says it in their own words.
- **Numbering is continuous.** Turn numbers (`T1`, `T2`, ...) run across the
  whole interview, so a tag like `[SPOKEN: T12]` is unique in the book.
  Modules 1 and 2 record their turns in `book/00-interview-notes.md`;
  module 3 records each chapter's turns in that chapter's notes file.

## Module 1: Frame → `book/BOOK-BRIEF.md`

Questions (skip any already answered):

- What's the book, in a sentence or two? What is it arguing, not just
  covering?
- Who is the reader, specifically? What do they already know, and what are
  they stuck on?
- What should be different for them by the last page? (Something they'll
  believe, do, or stop doing.)
- Why you? What have you seen, done, or built that the reader can't get
  elsewhere?
- Why now? What changed that makes this book needed?
- What's deliberately out of scope?
- Two or three books a reader might compare it to, and how this one differs.
- Format and rough length (a short guide, a full-length trade book, a
  workbook).
- What evidence do you already have? Your own client or field experience,
  research you lean on, interviews you've done with other people, data,
  prior talks or posts. Inventory it; don't collect it yet.
- Assertion stance: does a claim from your own experience need a citation
  every time, or does your experience stand on its own? Is this a
  footnoted book? (This decides how hard module 4 tests claims and how
  evidence is handled for the whole book. Always ask it explicitly, even on
  the fast track; never fill it with a default or carry one over from the
  author's previous book.)

Format:

```
# Book Brief: <working title>

## Argument
- Thesis:
- Promise to the reader:
- Reader transformation (believe / do / stop doing):

## Reader
- Who:
- What they already know:
- Where they're stuck:

## Author
- Why you:
- Why now:

## Scope
- In:
- Out:
- Comparable books:
- Format and target length:

## Evidence inventory
- Field experience:
- Research relied on:
- Interviews with others:
- Other (data, talks, posts):

## Rules
- Assertion stance:
- Quotes: verbatim, attributed, never rewritten into the author's voice
- Never invent: (people, clients, numbers, studies, anything else off limits)
- Confidentiality: (categories never to name; real names stay in private config)
```

## Module 2: Spine → `book/CHAPTER-MAP.md`

- What are the big parts of the argument? Get the author's own list first,
  in their own words, before offering any structure.
- For each chapter: its one-line claim (a claim, not a topic), and why it
  sits where it does.
- What does the reader need to believe before each chapter lands?
- Is there a thread that should recur across chapters (a framework, a
  question, a story told in installments)?

Then propose a chapter order with a one-line reason for each position, and
ask the author to approve, reorder, merge, or cut. Default the Introduction
and Conclusion to last in drafting order: they are easiest to write once the
middle exists.

Format:

```
# Chapter Map: <working title>

Drafting order: <list>

## 01 <Title>
- Claim:
- Why here:
- Reader must already believe:
- Recurring thread touchpoint (if any):
```

## Module 3: Chapter mining → `chapters/<NN-slug>/`

The heart of the interview. One chapter at a time, in the approved drafting
order.

**Voice first.** Most authors talk through an argument far more easily than
they type it, and one-question-at-a-time Q&A that suits modules 1 and 2
(short factual answers) tends to stall here. So at the start of each
chapter, offer a riff list: six to eight prompts covering the question
families below, written for this chapter's claim. Ask the author to record
a voice memo working through them in any order, as long as they like, and
paste the transcript. Mine it (claims, stories, evidence, boundaries), show
what you captured, and ask only about the gaps. Fall back to single
questions when the author prefers, or for the gaps after a riff.

The question families, to build the riff list from and to probe with,
following energy rather than marching through them in order:

| Family | Example question | Becomes |
|---|---|---|
| Claim | "What does almost everyone get wrong about this?" | raw statement |
| Story | "Tell me about a time you saw that happen. Who was there? What changed?" | `stories.md` |
| Mechanism | "Why does that happen? What's actually going on underneath?" | raw statement |
| Practice | "If a reader could do one thing on Monday, what is it?" | raw statement |
| Boundary | "When doesn't this hold? Where have you seen it fail?" | raw statement, plus a steelman candidate |
| Cost | "What does it cost a reader who ignores this?" | raw statement |
| Evidence | "Where did you first see this? Whose work backs it up?" | `evidence.md` |
| Counter-position | "What's the strongest case against you here, from someone who knows the field?" | steelman beat |

Push for specifics the way a good editor would: "Which client?" (record the
category, not the name, unless the author says the name may appear),
"Roughly when?", "What did they actually say?". A claim with a real story
behind it is worth five without.

Outputs per chapter (create the folder if it doesn't exist):

- **`00-interview-notes.md`**: the author's answers, verbatim (lightly
  cleaned as above), each under the question that prompted it, with a
  turn number. This is the record every raw statement traces back to.
  It is also spoken-register material for `/bootstrap-voice`: useful for
  stance, never as a sentence-level written exemplar.
- **`01-raw-statements.md`**: atomic claims, neutral and voiceless, the
  same shape `/draft` long-form produces from a manuscript. One claim per
  line, each tagged with where it came from:
  - `[SPOKEN: T12]`: the author said it, at turn 12 of the notes
  - `[SOURCE: path]`: pulled from existing material (gap-fill mode)
  - `[PROPOSED]`: your suggestion, not yet accepted (none may remain at
    handoff)
  - `[ACCEPTED: T14]`: a proposal the author accepted at turn 14; treat as
    theirs
  - `[DELEGATED]`: the author handed this to you; flag for heavier review
- **`stories.md`**: each anecdote with who (or what kind of person), when,
  the situation, what happened, what changed, and which claim it supports.
  Note what may and may not be named.
- **`evidence.md`**: every citation, study, statistic, or third-party
  quote, each with its source as the author gave it and a status of
  `verify` until someone checks it. Third-party quotes are evidence, not
  voice: verbatim, attributed, never rewritten to sound like the author.
  Before adding a quote, check `evidence.md` in every other chapter so the
  same quote or interview moment isn't used twice.

Book-level, alongside the per-chapter files:

- **`book/CASE-BANK.md`**: other organizations' stories (a company that
  did the thing, or failed to), kept once for use case by case in any
  chapter. One row per case: what it shows, how it might be used (lead
  example, cautionary contrast, adjacent model), and links to the evidence
  rows behind it. These are not the author's stories (`stories.md`) and not
  bare facts (`evidence.md`).

Granularity check before a chapter is done: any raw statement that bundles
two claims gets split. Any claim with no story, mechanism, or evidence
behind it gets one more question, or gets marked `[ASSERTION]` if the
author's assertion stance says their experience stands on its own.

**When the author declines a story.** Sometimes the answer is "I can't
give that here," for confidentiality or because of where they are. Don't
re-ask. Mark the claim `[STORY GAP]`, name where a case could come from
instead (recorded interviews, the case bank, research), mark it
`[ASSERTION]` if the brief's stance allows, note in `RESUME.md` that the
gap is not to be pressed, and move on.

## Module 4: Controversy pass → `chapters/<NN-slug>/CONTROVERSY-PREP.md`

Right after a chapter's raw statements are captured, before Stage 2
clustering, read through them and record three things:

1. **Controversial claims.** For each claim a practitioner reader might
   resist, write a sharper, more confident restatement: the version to
   actually argue from, not a softened one.
2. **Experience claims.** For each claim that rests on the author's own
   field experience, note what concrete example would strengthen it, if one
   came up in the interview or comes to mind. Never required, never
   invented. If the brief's assertion stance says experience stands on its
   own, say so and move on.
3. **Currency angles.** Which sections touch something fast-moving (a
   technology shift, a market condition, a regulatory change) that the
   chapter should address directly, and which claims might read as dated to
   someone reading a year or two after publication.

This file is a working reference: not part of the four-stage pipeline, not
voiced, not gated, and never a source of prose to lift directly.

## Completeness checklist (per chapter, before handoff)

- [ ] The chapter's one-line claim from `CHAPTER-MAP.md` is supported by
      its raw statements, or the map has been updated to match what the
      author actually said.
- [ ] At least one story the author owns, or an open `[STORY GAP]` with a
      named alternative source.
- [ ] At least one concrete practice a reader can act on.
- [ ] At least one boundary or counter-position, for the steelman beat.
- [ ] Every raw statement is atomic and tagged; no `[PROPOSED]` remains.
- [ ] Every `evidence.md` entry has a source and a status.
- [ ] Nothing in any file names a person, client, or organization the brief
      says must not be named.
- [ ] `CONTROVERSY-PREP.md` exists.

## Handoff

Tell the author, in two or three sentences, which chapters are ready, what
is marked `[DELEGATED]` or `[ASSERTION]`, and how many evidence items still
need verifying. Then:

- If `voice/profile/` doesn't exist yet, run `/bootstrap-voice` before
  drafting. With no written corpus at all, the interview notes can seed a
  provisional profile; see that command.
- Run `/draft` long-form for each ready chapter, starting at Stage 2
  (`02-clusters.md`). Stage 1 is already done.

## Interviewer craft notes

- Ask about concrete moments, not abstractions. "What did the room look
  like when that meeting went sideways?" beats "Describe the challenge."
- Follow energy. If the author lights up about a detail, ask one more
  question there. It's often the chapter's real point.
- Don't teach the author book structure. Use structure to choose your
  questions, not as content.
- Keep your own commentary minimal: a short acknowledgment, then the next
  question.
- If a story is painful or sensitive, let the author set the pace and the
  level of detail, and never push for specifics they skip past.
