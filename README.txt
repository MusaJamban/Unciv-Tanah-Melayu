TANAH MELAYU PATCH 3

This patch removes the warnings shown for legacy building uniques and fixes victory milestones that pointed to buildings absent from this mod.

APPLY THESE FILES
1. Extract this ZIP.
2. Copy the files inside the "jsons" folder into the "jsons" folder at the ROOT of your GitHub repository.
3. Replace existing files when prompted:
   - Buildings.json
   - VictoryTypes.json
4. Open jsons/Units.json and replace this exact text:
   "Can build improvements on tiles"
   with:
   "Can build [Land] improvements on tiles"
5. Save. In GitHub Desktop, commit the changes and push them to GitHub.
6. Fully close Unciv, reopen it, and load the mod again.

TRADE-OFF
To remove unsupported-unique warnings, this patch moves ordinary building yields into supported direct fields. Some special bonuses from the old Barracks, Walls, Castle, Courthouse and Arsenal uniques are removed for now rather than leaving invalid uniques.
This is a data-level repair based on the screenshot and current repository files. It has not been runtime-tested inside your exact Unciv app, so send the next screenshot if any messages remain.
