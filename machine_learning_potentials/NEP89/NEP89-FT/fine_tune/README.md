## fine_tune:

> Input data descriptions for the `nep89_20250409.txt` potential file can be found [here](https://arxiv.org/pdf/2504.21286) and [here](https://github.com/brucefan1983/GPUMD/tree/master/potentials/nep/nep89_20250409).

> Input data descriptions for the `train.xyz` and `test.xyz` file can be found [here](https://gitlab.com/brucefan1983/nep-data/-/tree/main/2024_Dong_Si/NEP-iteration-2/predict-2?ref_type=heads).

> Running `nohup /GPUMD/src/nep &` requires [GPUMD](https://gpumd.org/) to be installed.

- Execute `nohup /GPUMD/src/nep &` to finetune the NEP89 potential for thermal transport applications of silicon.

- Install [GPUMD](https://gpumd.org/) as follow:

```console
git clone https://github.com/brucefan1983/GPUMD.git
cd /GPUMD/src/
make -j 8
```

- Proceed finetuning based on protocol specific in `nep.in`, follow instructions [here](https://gpumd.org/nep/input_files/nep_in.html) for specific parameters:

```console
nohup /GPUMD/src/nep &
disown
```

- After finetuning, rename txt file for later thermal conductivity computations:

```console
cat nep.txt > nep89_finetuned_on_Si.txt
``` 
