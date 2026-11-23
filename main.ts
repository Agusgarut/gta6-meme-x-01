// Entry point for the gta6-meme-x-01 entry.
//
// The house judges the X post itself; this program's only job is to
// hand the post's address over. It copies POST.json (which holds the
// post URL) from the bot directory into the output directory, creating
// that directory first when it does not exist yet. On success it prints
// nothing and exits 0.

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const sourceDir = process.env.MAKEFUN_BOT_DIR ?? ".";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });
copyFileSync(join(sourceDir, "POST.json"), join(outputDir, "POST.json"));
