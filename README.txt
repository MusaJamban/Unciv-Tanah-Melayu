TANAH MELAYU - PATCH 2

This patch fixes the remaining errors visible in the latest screenshot:
1. Victory milestones referenced buildings not present in the mod (Apollo Program, Utopia Project, United Nations).
2. Worker uses an obsolete unique.

HOW TO APPLY
1. Extract this ZIP.
2. Open the extracted folder named "jsons".
3. Copy VictoryTypes.json and Units.json into your repository's "jsons" folder.
4. Choose Replace/Overwrite when asked.
5. Commit and push the two changed files in GitHub Desktop.
6. Fully close and reopen Unciv, then load the mod again.

IMPORTANT
This patch targets the errors shown in the screenshot. It does not yet repair the many Building unique warnings, nor does it prove the full ruleset is playable. Send the next error screenshot after applying it.

UNITS.JSON MANUAL EDIT
Open jsons/Units.json and find this exact line:
  "Can build improvements on tiles"
Replace it with:
  "Can build [Land] improvements on tiles"
Save the file, then commit and push it too.
