binary-patch
=========

Binary patch repository for ForgedAlliance.exe and SupremeCommander.exe


Operation
---------
1. FAForever clones/fetches the binary-patch repository into %ProgramData%/FAForever/repos and checks out origin/master (may use tags later).

2. FAForever guesses the game type (*retail* or *steam*) from the **bin** directory in the detected / chosen SupCom and ForgedAlliance installs and loads the appropriate *.json* migration file from the binary-patch repo.

3. FAForever checksums each file in %ProgramData%/FAForever/bin and compares it with the expected md5 in the migration file. It also checks whether all files in the bin directory exist in the migration dict. If there is a 100% match, the update process ends here, otherwise, it wipes the bin directory and continues to the next step.

4. FAForever copies all files in *pre_patch_copy_rename* into %ProgramData%/FAForever/bin, SupremeCommander.exe and ForgedAlliance.exe get renamed to ForgedAllianceForever.exe

5. FAForever checksums each file and checks if file in the **bsdiff4** folder exists with that name. If so, it applies the contents of the latter as a patch in place to the former.

6. FAForever iterates throuch the *post_patch_verify* dictionary and checks if all files have the expected md5 digests.

