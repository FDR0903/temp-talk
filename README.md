# The Economics of Regulating Tokenized Securities

Slidev presentation with 25 main slides and 25 unnumbered backup slides for Q&A.
The main slides use a white background, Computer Modern sans-serif typography,
and colored outlines. Slide 2 includes the RWA.xyz tokenization-growth chart.

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

The main talk ends at 25/25. The backup slides follow the conclusion and reproduce
the Equity Tokenization primer as vector SVGs, including its original dark
appearance. Their printed page numbers have been removed, and
`layouts/primer-backup.vue` adds no counter. The backup assets are in
`images/equity-tokenization-primer/`.

During a local preview, open `http://localhost:3030/primer` to jump directly to
the backups. They begin at deck position 26 and have descriptive titles in the
slide overview.
