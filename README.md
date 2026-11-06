# The Economics of Regulating Tokenized Securities

Slidev presentation with 25 main slides and 27 unnumbered backup slides for Q&A.
The main slides use a white background, Computer Modern sans-serif typography,
and colored outlines. Slide 2 includes the RWA.xyz tokenization-growth chart.
Slides 2–4 include incremental reveals; slide 20 includes a mathematical
definition of optimal admission and the Milgrom–Shannon set-order argument.

View the slides at <https://fdr0903.github.io/temp-talk/>.

## Run locally

Use Node.js 24, then run:

```sh
npm ci
npm run dev
```

## Build and publish

```sh
npm run build -- --base /temp-talk/
```

The GitHub Actions workflow publishes pushes to `main` using GitHub Pages. It retains the `/temp-talk/` base path so routes and image assets work on the project website. `vercel.json` preserves the alternative Vercel deployment configuration.

`slides.md` contains the presentation and click reveals. The main-slide layout
and typography are in `layouts/seminar.vue` and `seminar.css`, with additional
shared styles in `style.css`. The bundled fonts and their license are in `fonts/`.
The dependency lockfile pins the versions used by the presentation.

The main talk ends at 25/25, after the Ethereum/Arbitrum comparison and conclusion.
The BUIDL example immediately precedes the early Main Result and has no pause.
Two unnumbered **Optimal Regulation** slides follow, reproducing the old deck's
regulatory-regime charts and four friction panels. The first credits Campello,
Cong and Dietrich (2024), *Regulatory uncertainty and fintech innovation*.
`layouts/seminar-backup.vue` displays these slides without a counter.

The remaining 25 backups reproduce the Equity Tokenization primer as vector
SVGs, including its original dark appearance. Their printed page numbers have
been removed; the primer cover omits the author, affiliation, and guest-lecture
details. `layouts/primer-backup.vue` adds no counter. The backup assets are in
`images/equity-tokenization-primer/`.

During a local preview, use `/optimal-regulation` and
`/optimal-regulation-frictions` to jump to the two optimal-regulation backups
(deck positions 26–27). Open `http://localhost:3030/primer` to jump to the primer,
which begins at position 28. The backup slides have descriptive overview titles.
