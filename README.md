binary-patch
=========

Binary patch repository for ForgedAlliance.exe and SupremeCommander.exe


Operation
---------
1. FAForever copies the **bin** directory from the detected / chosen SupCom and ForgedAlliance installs into %ProgramData%/FAForever/bin *(may change into bin/sc and bin/fa in milestone FAReborn, pending research)*
2. FAForever check the md5 sum of lua.scd as a version comparison. *(there are three md5 sums stored in the client to detect they are correct. the plan is to move this functionality into the binary patch directory so we can match multiple files)*
3. FAForever pulls the binary-patch repository into %ProgramData%/FAForever/repos and checks out the latest annotated tag on master.
    * **DEPRECATED:** FAForever sends the md5 of ForgedAlliance.exe to the server and gets a list of files and patches.
4. FAForever walks through all the files and checks if a directory with the same name exists in the repo. It then calculates the md5 for that file and checks if a bsdiff4 file with that name exists.
    * if so, it applies the bsdiff4 to the file *(in place, may operate with backups later)*
    * then it compares the resulting file's md5 to goal.md5 to verify successful patch


Needed
------
* sample binaries (updated to supcom_fa_patch_1.5.3596_to_1.5.3599.exe, 3601 (?) beta)
* refresher - what was the state of the last patches in FA, i.e what was the official one and what was the beta one?
