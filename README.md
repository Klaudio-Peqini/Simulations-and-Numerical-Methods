# Simulim dhe Metoda Numerike — Leksione të rishikuara

Kjo paketë përmban versionin e rishikuar pedagogjikisht të leksioneve për
lëndën **Simulim dhe Metoda Numerike**. Përmbajtja e zgjeruar dhe derivimet e
dorëshkrimit origjinal janë ruajtur; hyrja në çdo kapitull është riorganizuar
që studenti të kalojë nga intuita te formalizmi në hapa të kontrollueshëm.

## Përmbajtja

- `Simulim_dhe_Metoda_Numerike_Leksione_Rishikuar.tex` — burimi i plotë LaTeX;
- `Simulim_dhe_Metoda_Numerike_Leksione_Rishikuar.pdf` — dokumenti i kompiluar;
- `figures/` — 25 figurat origjinale të përdorura nga dorëshkrimi;
- `REVISION_LOG.md` — përmbledhja e ndërhyrjeve pedagogjike dhe teknike.

## Struktura pedagogjike

Të 12 kapitujt ndjekin të njëjtën vijë:

1. pyetja udhëzuese dhe ideja kryesore;
2. shembulli minimal dhe llogaritja me dorë;
3. derivimi dhe algoritmi;
4. kompleksiteti në kohë dhe kujtesë;
5. qëndrueshmëria, gabimi ose kontrolli statistik;
6. lidhja me kodin dhe laboratorin;
7. interpretimi fizik dhe kufijtë e vlefshmërisë.

Kapitulli 2 është rishkruar më thellë. Ai nis me një makinë dhjetore me tri
shifra domethënëse dhe kalon gradualisht te IEEE 754, epsiloni i makinës,
anulimi, numërimi i veprimeve, shënimet asimptotike, Horner-i, kushtëzimi dhe
qëndrueshmëria.

## Kompilimi

Nga dosja e paketës ekzekutoni dy herë:

```bash
pdflatex -interaction=nonstopmode -halt-on-error \
  Simulim_dhe_Metoda_Numerike_Leksione_Rishikuar.tex
```

Dokumenti përdor klasën standarde `book` dhe paketa të zakonshme të TeX Live.
Figurat kërkohen në dosjen `figures/`.

## Kontrolli teknik

Versioni i dorëzuar është kompiluar me pdfTeX nga TeX Live 2023. PDF-ja ka
109 faqe A4. Janë kontrolluar faqet hyrëse, hyrjet e kapitujve, Kapitulli 2,
tabelat, listimet e kodit, figurat, bibliografia dhe faqja përfundimtare.

