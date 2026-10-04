# Simulim dhe Metoda Numerike

Leksione të shkruara për programin Bachelor në Fizikë dhe Shkenca Kompjuterike. Versioni i kompiluar ka 100 faqe A4 me tipografi standarde dhe të dendur. Teksti është ndërtuar si një kurs i vetëm, koherent, mbi të cilin mund të zhvillohen notebook-ët e laboratorit.

## Përmbajtja

- `Simulim_dhe_Metoda_Numerike_Leksione.tex` — dokumenti kryesor;
- `chapters/` — 12 kapitujt, zhvillimet matematikore, shtesat algoritmike me kod Python dhe shtojca terminologjike;
- `figures/` — 25 figurat origjinale në format PDF;
- `generate_figures.py` — kodi që rigjeneron figurat;
- `Simulim_dhe_Metoda_Numerike_Leksione.pdf` — versioni i kompiluar.

## Kompilimi

```bash
python generate_figures.py
pdflatex Simulim_dhe_Metoda_Numerike_Leksione.tex
pdflatex Simulim_dhe_Metoda_Numerike_Leksione.tex
```

Dokumenti përdor Latin Modern, variantin vektorial standard të Computer Modern të LaTeX-it, me kodim T1.

## Parimet redaktuese

- çdo kapitull shpjegon algoritmet kryesore dhe përfshin fragmente të ekzekutueshme në Python;
- derivimet zhvillohen nga modeli ose identiteti bazë deri te gabimi, qëndrueshmëria, kostoja dhe kontrolli numerik;
- faqosja shmang kutitë me ngjyra, titujt ornamentalë dhe ndërprerjet manuale brenda kapitujve;
- hierarkia përdor pak seksione kryesore dhe bashkon zhvillimet e lidhura në nënseksione më të gjata;
- terminologjia përdor në mënyrë të njëtrajtshme format *bredhje*, *statistike* dhe *pacaktueshmëri*;
- nuk trajtohen nënhapësirat e Krilovit;
- bibliografia përfshin literaturë universitare në shqip për analizën numerike, probabilitetin, të dhënat dhe metodat Monte Carlo, të plotësuar me burime ndërkombëtare standarde;
- shtojca jep fjalorthin shqip--anglisht, standardin e notebook-ut dhe lidhjen kapitull--laborator.

## Mjedisi Python për figurat

Kërkohen Python 3, NumPy dhe Matplotlib. Të gjitha figurat prodhohen lokalisht nga skripti dhe nuk varen nga skedarë të jashtëm.
