# The Economics of Regulating Tokenized Securities

Slidev presentation for a 25-minute talk plus questions, using the Frankfurt theme and slate palette.

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

`slides.md` contains the presentation and click reveals. `style.css` contains its layout and typography. `images/` contains only images referenced by this deck. The dependency lockfile pins the versions used by the current presentation.
