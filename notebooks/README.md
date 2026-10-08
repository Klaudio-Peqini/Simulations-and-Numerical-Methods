# Notebook-et e instruktorit — Simulim dhe Metoda Numerike

Kjo paketë përmban vetëm dosjen `Instruktori/`. Dosja e studentëve është hequr sipas kërkesës. Dy notebook-et e Laboratorit 01 ruhen byte për byte pa ndryshim. Laboratorët 02–12 janë zgjeruar në seanca të plota 120-minutëshe.

Çdo notebook i zgjeruar përmban:

- planin e kohës për 120 minuta;
- kuadrin konceptual dhe zhvillimin matematikor;
- pyetje parashikuese para ekzekutimit;
- zbatim të udhëhequr në Python;
- pika kontrolli pas çdo eksperimenti;
- eksperiment parametrik ose diagnostikë shtesë;
- eksport automatik të skripteve `.py` dhe `.m`;
- udhëzime për ekzekutimin lokal nga terminali;
- zbatim të plotë ekuivalent në GNU Octave në të njëjtin notebook;
- detyra konsoliduese, raport dhe listë kontrolli.

## Ekzekutimi

Për Python:

```bash
python -m pip install numpy matplotlib scipy jupyterlab
jupyter lab
```

Për GNU Octave:

```bash
octave --version
octave --quiet scripts_local/emri_i_skedarit.m
```

Laboratori 09 mund të kërkojë paketën `statistics` të Octave për disa teste:

```octave
pkg load statistics
```

Qelizat Octave janë `raw`, në mënyrë që notebook-u të përdorë kernelin Python pa gabime. Qeliza e eksportit krijon skedarin `.m` për ekzekutim lokal.
