# Laboratorët 01–12 — Simulim dhe Metoda Numerike

Kjo dosje përmban variantet e instruktorit të dymbëdhjetë laboratorëve të lëndës **Simulim dhe Metoda Numerike**. Notebook-ët janë ndërtuar si seanca të plota 120-minutëshe dhe ndjekin rendin e kapitujve të leksioneve.

Çdo laborator përdor të njëjtën logjikë pedagogjike:

1. pyetja fizike ose numerike;
2. shembulli minimal që llogaritet me dorë;
3. derivimi matematikor;
4. formulimi i algoritmit;
5. zbatimi i ndarë në qeliza të vogla Python;
6. analiza e kompleksitetit me formulë;
7. matja eksperimentale e kompleksitetit;
8. kushtëzimi dhe qëndrueshmëria;
9. shembulli i plotë i zgjidhur;
10. punishtja ku ndryshohen parametrat;
11. fragmentet thelbësore GNU Octave;
12. ekzekutimi i programit jashtë notebook-ut.

## Përmbajtja

| Nr. | Laboratori | Tema qendrore |
|---:|---|---|
| 01 | Hyrje në simulimet fizike | Modeli, algoritmi, kodi, verifikimi, vleftësimi dhe rënia me rezistencë lineare |
| 02 | Aritmetika kompjuterike | Rrumbullakimi, anulimi, kompleksiteti, kushtëzimi dhe qëndrueshmëria |
| 03 | Ekuacionet dhe algjebra lineare | Përgjysmimi, Njutoni, eliminimi me pivotim dhe metoda fuqi |
| 04 | Interpolimi dhe regresi | Lagranzhi, Njutoni, Runge, Çebishevi, mbetjet dhe katrorët më të vegjël |
| 05 | Diferencimi dhe integrimi | Taylor-i, hapi optimal, trapezi, Simpson-i dhe Richardson-i |
| 06 | Ekuacionet diferenciale | Euler-i, RK4, stabiliteti absolut, ngurtësia dhe energjia |
| 07 | Diferencat e fundme dhe valët | Skema valore, CFL-ja, dispersimi dhe energjia diskrete |
| 08 | Probabiliteti dhe pacaktueshmëria | LLN, CLT, kovarianca, përhapja dhe algoritmi i Welford-it |
| 09 | Numrat pseudorastësorë | LCG, testet, transformimi i anasjelltë, Box–Muller dhe refuzimi |
| 10 | Integrimi Monte Carlo | Gabimi $N^{-1/2}$, $\pi$, intervalet dhe reduktimi i variancës |
| 11 | Bredhjet dhe Markov-i | Difuzioni, koha e parë e kalimit, stacionariteti dhe autokorrelacioni |
| 12 | Metropolis–Hastings dhe Ising | Log-pranimi, $N_{eff}$, $\Delta E$, sweep-et dhe termalizimi |

## Ritmi i rekomanduar i një seance

- **0–15 min:** pyetja, supozimet dhe llogaritja me dorë;
- **15–40 min:** derivimi dhe pseudokodi;
- **40–65 min:** qelizat kryesore Python;
- **65–82 min:** kompleksiteti teorik dhe kohëmatja;
- **82–100 min:** qëndrueshmëria dhe diagnostika;
- **100–112 min:** shembulli i plotë dhe një eksperiment i punishtes;
- **112–120 min:** Octave, ekzekutimi lokal dhe përfundimi.

Nuk rekomandohet përdorimi i komandës “Run All” në fillim. Studentët duhet të japin një parashikim, të ekzekutojnë një qelizë, të lexojnë daljen dhe të shkruajnë interpretimin përpara se të vazhdojnë.

## Instalimi

Krijoni një mjedis virtual dhe instaloni paketat:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Në Windows PowerShell, aktivizimi kryhet me:

```powershell
.venv\Scripts\Activate.ps1
```

Nisni Jupyter-in:

```bash
jupyter lab
```

## Python dhe GNU Octave

Pjesa e parë e çdo notebook-u përdor kernelin Python. Pjesa e dytë paraqet kodin Octave në blloqe të dallueshme `octave`, që kopjohen në editorin e GNU Octave ose në një skedar `.m`.

Python-i është trajtimi kryesor dhe përmban derivimet e kontrolluara, figurat, eksperimentet dinamike dhe matjet e kompleksitetit. Octave jep bërthamën e së njëjtës metodë dhe kontrollet numerike kryesore; ai nuk përsërit mekanikisht çdo figurë.

## Ekzekutimi lokal

Kur ekzekutohet notebook-u, qeliza përkatëse krijon një program në dosjen `scripts_local/`. Në këtë paketë janë përfshirë paraprakisht edhe dymbëdhjetë skriptet Python të verifikuara.

Shembull:

```bash
python3 scripts_local/laboratori_05_diferencimi_integrimi.py
```

Studenti duhet të ndryshojë një parametër, ta ekzekutojë përsëri programin dhe të shpjegojë ndryshimin e daljes.

## Kërkesat e raportit

Raporti i çdo laboratori duhet të përmbajë:

- pyetjen dhe madhësinë që kërkohet;
- supozimet, parametrat dhe njësitë;
- derivimin kryesor me dorë;
- formulën $T(n)$ dhe klasën asimptotike;
- matjen kompjuterike të kohës;
- provën e qëndrueshmërisë ose diagnostikën përkatëse;
- të paktën një figurë me boshte, njësi dhe legjendë;
- një ndryshim të kontrolluar në punishte;
- komandën e ekzekutimit lokal;
- një përfundim shkencor, jo vetëm pohimin “kodi punoi”.

## Riprodhueshmëria

Notebook-ët përdorin fara të deklaruara për eksperimentet stokastike. Në raport duhen ruajtur fara, madhësia e mostrës, toleranca, hapi, versionet e paketave dhe çdo ndryshim i parametrave. Rezultatet dinamike mund të varen nga ritmi i vizatimit, por madhësitë numerike duhet të mbeten të riprodhueshme.

## Kontrolli teknik

Të gjitha qelizat Python të dymbëdhjetë notebook-ëve janë ekzekutuar nga lart-poshtë. Të dymbëdhjetë skriptet lokale janë ekzekutuar veçmas. Janë kontrolluar formulat Markdown, termat shkencorë shqip, renditja Python–Octave dhe mungesa e sintaksës së ndaluar `\[...\]` ose `\(...\)`.

