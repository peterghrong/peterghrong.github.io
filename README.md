# peterrong.github.io

Personal site and writing log. Built with Jekyll, deployed via GitHub Pages.

## Add a post

Drop a file in `_posts/` named `YYYY-MM-DD-slug.md` with this front matter:

```yaml
---
layout: post
title: Your title
---
```

Then write below it. The post appears on the home page and at `/writing/<slug>/`.

## Run locally

```
bundle install
bundle exec jekyll serve
```

Open http://127.0.0.1:4000.

## Deploy

Push to `main`. The repo is named `peterrong.github.io`, so Pages serves from the root.

## Writing style

All writing on this site, and any prose an agent drafts for it, must follow these rules.

1. **Be concise.** Cut anything that is not pulling weight. Short is good.
2. **No em dashes.** Use a period, comma, colon, or parentheses instead. Never `—`.
3. **Keep sentences natural.** Write the way a person would say it. Avoid inverted or contrived phrasings.
4. **Use plain words.** Skip big or archaic vocabulary when a common word works. "Use" not "utilize." "Help" not "facilitate." "About" not "regarding."
5. **Easy to digest.** Short sentences are fine. Read it aloud before publishing. If it feels stiff out loud, rewrite it.
6. **No "it's X, not Y" constructions.** Avoid the AI-flavored contrast pattern ("This is not a bug, it's a feature," "Black-Scholes is not a pricing formula, it's a hedging recipe"). Just say what it is. Drop the foil.
7. **No corny narrator moves.** No "Here is the trick," "That is what clicked for me," "Wait, is that X?" section hooks, no winking asides to the reader, no folksy performance of insight. State the thing. Trust the reader to find it interesting.

These rules apply to posts, page copy, and anything else written under my name on this site.
