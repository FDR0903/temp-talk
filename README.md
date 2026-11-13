# Economics of proof of stake

A 33-slide talk covering issuance taxes, staking incentives, and Layer 1 / Layer 2 interactions.

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

Pushes to `main` trigger the existing GitHub Pages workflow. The `/temp-talk/` base path keeps slide routes and image assets working on the project website. `vercel.json` also supports the existing Vercel deployment configuration.

`slides.md` contains the talk and its click reveals. `style.css` contains the Frankfurt/slate presentation styles. `images/` contains only the eight assets needed by this talk. The dependency lockfile records the tested package versions.
