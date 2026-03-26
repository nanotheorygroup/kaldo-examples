# `aluminum_EMT_parallel_third`

Demonstrates kALDo's **parallel third-order force constant calculator** on Al FCC
using ASE's built-in EMT potential. No external files or compiled codes are required.

The example shows that the serial and parallel implementations produce numerically
identical force constants and thermal conductivities, and places the results in
context of an Ab Initio literature value (~5.8 W/m/K at 300 K, Wang, Lu, & Ruan JAP 2016).

## Scripts

### `1_force_constants.py`
1. Builds Al FCC (4-atom conventional cubic cell, `a = 4.05 Å`).
2. Creates two `ForceConstants` objects with 3×3×3 supercells — one for each path.
3. Computes 2nd-order IFCs (same method for both).
4. Computes 3rd-order IFCs **serially** (`n_threads=1`, EMT instance) into `fc_al_serial/`.
5. Computes 3rd-order IFCs **in parallel** (`n_threads=None` for all CPUs, EMT class as factory) into `fc_al_parallel/`.
6. Prints the max absolute and relative difference between the two values.

**Key API difference:**

| Mode     | `calculator` argument | `n_threads`  |
|----------|-----------------------|-------------|
| Serial   | `EMT()` — instance    | `1`          |
| Parallel | `EMT` — class/factory | `None` or N  |

For file-based calculators (e.g. LAMMPS), use a lambda factory so each worker
gets a unique scratch directory:
```python
calculator=lambda: LAMMPS(tmp_dir=f'/tmp/kaldo_{os.getpid()}')
```

### `2_conductivity.py`
1. Loads `ForceConstants` from both `fc_al_serial/` and `fc_al_parallel/`.
2. Creates `Phonons` objects with a 7×7×7 k-point mesh at 300 K.
3. Computes thermal conductivity via RTA and exact-inverse BTE methods.
4. Prints a side-by-side comparison table and notes the experimental reference.
5. Saves `kappa_serial.npy` and `kappa_parallel.npy` for the plotting script.

### `3_plot_comparison.py`
1. Plots a grouped bar chart of thermal conductivity (serial vs parallel) for
   both BTE methods, with an literature reference line.
2. Plots the absolute difference between serial and parallel results.
3. Saves `conductivity_comparison.png` and `conductivity_difference.png`.

---

## Running the example

```bash
cd examples/aluminum_EMT_parallel_third
python 1_force_constants.py
python 2_conductivity.py
python 3_plot_comparison.py
```

Outputs:
- `fc_al_serial/` — second and serial third-order IFCs
- `fc_al_parallel/` — second and parallel third-order IFCs
- `ALD_al_serial/`, `ALD_al_parallel/` — phonon properties
- `conductivity_comparison.png`, `conductivity_difference.png` — figures
