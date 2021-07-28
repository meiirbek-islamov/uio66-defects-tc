

install mofun via github code
requires click

usage:
```
# convert cml files to UFF-parameterized lmpdat files
python cml2lmpdat_wparams.py ./uio66-linker* -o ./

# replace linkers with defective linkers
python uio66-replace-linkers-workflow.py

```





UIO66 (no topology) replicated to NxNxN

Option A:
- find / replace metal center with UFF parameterized metal center
- find / replace ligand with UFF parameterized defective ligand (based on %)
- find / replace ligand with UFF parameterized ligand
- (make sure that where patterns overlap, the terms are correct)

Option B:
- define topology of UIO-66 across boundary conditions at desired replication
- parameterize the whole UIO-66
- find / replace ligand with UFF parameterized defective ligand (based on %)







UIO-66 w/ range % defects
