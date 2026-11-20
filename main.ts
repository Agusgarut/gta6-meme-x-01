// gta6-meme-x-01 entry program (Node 22, standard library only, no network).
//
// The entry itself is the X post named in POST.json — the house reads the
// post from X and judges its first picture and its text. All this program
// has to do is hand the address over: it reads POST.json from the bot
// directory and writes it, byte for byte, into the output directory where
// the gate picks it up.
//
// The grader points MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR at its own
// directories; outside the grader they default to /bot and /output.
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR || "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";

const sourcePath = join(botDir, "POST.json");
const targetPath = join(outDir, "POST.json");

let payload;
try {
  payload = readFileSync(sourcePath);
} catch (err) {
  console.error(`cannot read ${sourcePath}: ${err.message}`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(targetPath, payload);
