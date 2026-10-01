# Who survives AI?

Slides by Fayçal Drissi (University of Oxford), based on joint work with Fahad Saleh (University of Florida).

The deck covers AI providers, firms’ use of models, and the incentives for providers to enter their customers’ markets.

## Run locally

```sh
npm ci
npm run dev
```

Open <http://localhost:3030>.

## Build

```sh
npm run build
```

The site is generated in `dist/`. The GitHub Actions workflow deploys pushes to GitHub Pages at <https://fdr0903.github.io/temp-talk/>. `vercel.json` also configures deployment and slide routing on Vercel.

## Export to PDF

```sh
npm run export
```

PDF export requires a Playwright Chromium browser installation. If Slidev reports that the browser is missing, run `npx playwright install chromium` and retry.

The slides contain text and equations; no local image assets are required.
