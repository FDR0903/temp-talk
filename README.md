# Who Survives AI?

Slides by Fayçal Drissi (University of Oxford) and Fahad Saleh (University of Florida).

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

The site is generated in `dist/`. The GitHub Actions workflow deploys pushes to `main` at <https://www.faycaldrissi.com/temp-talk/>. In the repository's **Settings → Pages**, set **Source** to **GitHub Actions** so Pages publishes the built slides. `vercel.json` also configures deployment and slide routing on Vercel.

## Export to PDF

```sh
npm run export
```

PDF export requires a Playwright Chromium browser installation. If Slidev reports that the browser is missing, run `npx playwright install chromium` and retry.

The slides contain text and equations; no local image assets are required.
