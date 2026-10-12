# AI Platforms — LSESU Maths Society

Slides by Fayçal Drissi (University of Oxford), presenting joint research with Fahad Saleh and Andrea Barbon.

The talk covers AI providers and firms, followed by financial markets, AI use, and cognitive capital.

## Run locally

```sh
npm ci
npm run dev
```

## Build

```sh
npm run build
```

The GitHub Actions workflow publishes pushes to `main` using GitHub Pages. `vercel.json` contains the alternative Vercel configuration.

The `images/` directory contains only assets used in the slides. The `scripts/` directory contains the two figure generators. Research papers are kept locally and excluded from Git.
