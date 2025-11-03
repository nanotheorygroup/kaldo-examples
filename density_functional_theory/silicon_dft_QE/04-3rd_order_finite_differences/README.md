# Compute 3rd order force constants (FCs) using [thridorder.py](https://bitbucket.org/sousaw/thirdorder/src/master/) 

> Installation instruction of `thirdorder.py` can be found [here](https://bitbucket.org/sousaw/thirdorder/src/master/)

1. Generate displaced structures using `thirdorder_espresso.py` to obtain 3rd order FCs with **3-by-3-by-3** supercells up to 4 nearest neighbors. 

```console
thirdorder_espresso.py scf.in sow 3 3 3 -4 scf_sc.in
```

2. Run bash script to compute forces for each displaced structures iteratively

```console
./run.sh
```

3. After all the jobs have finished successfully, compute 3rd force constants by finite difference method

```console
find . -name 'DISP.scf_sc.out.*' | sort -n | thirdorder_espresso.py scf.in reap 3 3 3 -4
```
