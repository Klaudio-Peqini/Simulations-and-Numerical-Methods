# Laboratorët 02–12 — Simulim dhe Metoda Numerike           

## 1. Qëllimi i paketës

Kjo paketë përmban materialet laboratorike për vazhdimin e kursit **Simulim dhe Metoda Numerike**, i zhvilluar për studentët Bachelor në Fizikë dhe Shkenca Kompjuterike. Laboratorët ndjekin drejtpërdrejt rendin, terminologjinë, modelet matematikore dhe algoritmet e leksioneve të shkruara të kursit.

Qëllimi nuk është vetëm ekzekutimi i kodit. Çdo laborator e udhëheq studentin në ciklin e plotë të punës shkencore:

1. formulimi i pyetjes fizike;
2. zgjedhja e modelit matematik;
3. ndërtimi i algoritmit numerik ose stokastik;
4. zbatimi në kod;
5. verifikimi i zbatimit;
6. analiza e gabimit dhe e pacaktueshmërisë;
7. interpretimi fizik i rezultateve;
8. organizimi i funksioneve për ripërdorim të mëvonshëm.

Paketa fillon me **Laboratorin 02**. Laboratori 01, i përgatitur më parë për programimin shkencor bazë, nuk përfshihet dhe nuk është ndryshuar.

## 2. Çfarë përmban paketa

Paketa përmban gjithsej **22 notebook-e**:

- 11 versione të zgjidhura në dosjen `Instruktori/`;
- 11 versione të udhëzuara në dosjen `Studenti/`.

Skedarët plotësues janë:

- `README.md` — dokumenti kryesor i përdorimit të paketës;
- `Udhezuesi_i_Instruktorit.md` — organizimi pedagogjik dhe vlerësimi i seancave;
- `RAPORT_VALIDIMI.md` — kontrollet teknike dhe shkencore të kryera;
- `MANIFEST.txt` — lista e plotë e notebook-eve;
- `requirements.txt` — bibliotekat minimale për pjesën Python.

Struktura e dosjeve është:

```text
Laboratoret_02_12_Simulim_dhe_Metoda_Numerike/
├── Instruktori/
│   ├── Laboratori_02_..._Instruktori.ipynb
│   ├── ...
│   └── Laboratori_12_..._Instruktori.ipynb
├── Studenti/
│   ├── Laboratori_02_..._Studenti.ipynb
│   ├── ...
│   └── Laboratori_12_..._Studenti.ipynb
├── README.md
├── Udhezuesi_i_Instruktorit.md
├── RAPORT_VALIDIMI.md
├── MANIFEST.txt
└── requirements.txt
```

## 3. Lidhja me leksionet

| Laboratori | Tema | Kapitulli i leksioneve | Përmbajtja kryesore |
|---:|---|---|---|
| 02 | Aritmetika kompjuterike dhe analiza e gabimeve | Kapitulli 2 | Presja lëvizëse, epsiloni i makinës, anulimi, shuma e Kahan-it, kushtëzimi, gabimi i përparmë dhe mbetja |
| 03 | Ekuacionet, sistemet dhe vlerat vetjake | Kapitulli 3 | Përgjysmimi, Njutoni, sistemet jolineare, zgjidhja lineare, metoda fuqi dhe modet normale |
| 04 | Interpolimi dhe regresi | Kapitulli 4 | Lagranzhi, nyjet Chebyshev, fenomeni Runge, katrorët më të vegjël, mbetjet dhe bootstrap-i |
| 05 | Diferencimi dhe integrimi numerik | Kapitulli 5 | Diferencat e fundme, gabimi i këputjes, hapi optimal, trapezi, Simpsoni dhe Gauss--Legendre |
| 06 | Ekuacionet diferenciale dhe dinamika | Kapitulli 6 | Euleri, RK4, rënia në ajër, lavjerrësi jolinear, ruajtja e energjisë dhe velocity-Verlet |
| 07 | Diferencat e fundme dhe valët | Kapitulli 7 | Ekuacioni valor, rrjeta hapësirë--kohë, kushti CFL, reflektimi, energjia diskrete dhe dispersimi numerik |
| 08 | Probabiliteti dhe pacaktueshmëria | Kapitulli 8 | Bernoulli, ligji i numrave të mëdhenj, teorema qendrore kufitare dhe përhapja Monte Carlo |
| 09 | Numrat pseudorastësorë dhe kampionimi | Kapitulli 9 | Fara, testet grafike, transformimi i anasjelltë, Box--Muller dhe kampionimi me refuzim |
| 10 | Integrimi Monte Carlo | Kapitulli 10 | Integrali si pritje, gabimi $N^{-1/2}$, variablat antitetike dhe variablat kontrolluese |
| 11 | Bredhjet dhe zinxhirët Markov | Kapitulli 11 | Bredhja e rastit, difuzioni, koha e parë e kalimit, shpërndarja stacionare dhe autokorrelacioni |
| 12 | Metropolis--Hastings dhe modeli Ising | Kapitulli 12 | Balanca e detajuar, termalizimi, modeli Ising 2D, observablat dhe analiza me blloqe |

Laboratorët 03, 06 dhe 12 përmbajnë më shumë se një eksperiment madhor dhe mund të ndahen në dy seanca, në varësi të ritmit të grupit.

## 4. Dy versionet e çdo notebook-u

### 4.1 Versioni i instruktorit

Notebook-et në `Instruktori/` përmbajnë zgjidhjet e plota. Ato janë menduar për:

- përgatitjen e seancës nga pedagogu ose instruktori;
- demonstrimin hap pas hapi të algoritmit;
- kontrollin e vlerave numerike që duhet të marrin studentët;
- diskutimin e figurave, mbetjeve, ligjeve të ruajtjes dhe intervaleve;
- identifikimin e gabimeve tipike gjatë laboratorit.

Pjesët Python të këtyre notebook-eve janë ekzekutuar në rend dhe janë kontrolluar për gabime.

### 4.2 Versioni i studentit

Notebook-et në `Studenti/` ruajnë shpjegimin, strukturën e eksperimentit, parametrat bazë dhe pjesë të kodit, por blloqet thelbësore të algoritmit janë shënuar me `TODO`. Këto notebook-e nuk duhet të trajtohen si formularë mekanikë. Studenti duhet:

- të plotësojë algoritmin;
- të arsyetojë kriterin e ndalimit ose të stabilitetit;
- të kryejë kontrollin e verifikimit;
- të ndryshojë të paktën një parametër;
- të komentojë rezultatet numerike dhe fizike;
- të ruajë funksionet e veta për paketën përfundimtare të kursit.

Një bllok `TODO` mund të përmbajë qëllimisht `NotImplementedError` në Python ose `error(...)` në MATLAB/Octave. Ky ndalim nuk është defekt; ai tregon pjesën që studenti duhet të plotësojë.

## 5. Organizimi dygjuhësh i notebook-eve

Çdo notebook ndahet në dy gjysma:

1. **Pjesa I — Python**;
2. **Pjesa II — MATLAB/Octave**.

Dy pjesët trajtojnë të njëjtin model, të njëjtin algoritëm dhe të njëjtat kritere shkencore. Studenti mund të zgjedhë njërën gjuhë, përveç rasteve kur instruktori kërkon krahasim të drejtpërdrejtë.

Një notebook Jupyter përdor zakonisht vetëm një kernel. Për këtë arsye:

- kodi Python ruhet në qeliza kodi dhe ekzekutohet me kernelin `Python 3`;
- kodi MATLAB/Octave ruhet në qeliza `raw`, që notebook-u të hapet dhe të ekzekutojë pjesën Python pa gabime sintaksore;
- për MATLAB/Octave, kodi kopjohet në një skedar `.m`, ekzekutohet në Command Window ose shndërrohet në qelizë kodi kur përdoret një kernel MATLAB/Octave.

Qelizat `raw` nuk ekzekutohen automatikisht nga kerneli Python.

## 6. Instalimi i mjedisit Python

Kërkohet Python 3.10 ose më i ri. Rekomandohet përdorimi i një mjedisi virtual.

### Linux dhe macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install jupyterlab
jupyter lab
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install jupyterlab
jupyter lab
```

Bibliotekat bazë janë:

- NumPy për vargjet, algjebrën lineare dhe gjenerimin pseudorastësor;
- Matplotlib për figurat;
- SciPy për integratorët dhe disa funksione numerike ndihmëse.

Notebook-u duhet të hapet gjithmonë nga rrënja e paketës ose nga dosja ku ndodhet vetë notebook-u.

## 7. Përdorimi në MATLAB

Kodi është shkruar për MATLAB modern. Për ta përdorur:

1. hapni notebook-un dhe gjeni seksionin `Pjesa II — MATLAB/Octave`;
2. kopjoni blloqet sipas radhës në një Live Script ose skedar `.m`;
3. ekzekutoni fillimisht bllokun e parametrave dhe pastaj funksionet;
4. kontrolloni që figurat dhe vlerat përputhen me kriteret e notebook-ut;
5. ruani skriptin dhe figurat bashkë me raportin.

Funksionet lokale duhet të vendosen në fund të skriptit kur versioni i MATLAB-it e kërkon këtë organizim.

## 8. Përdorimi në GNU Octave

Shumica e kodeve përdorin sintaksë të përbashkët MATLAB/Octave. Në Octave rekomandohet:

```octave
pkg list
pkg load statistics
```

Paketa `statistics` nevojitet veçanërisht për `mvnrnd` në Laboratorin 08. Nëse paketa mungon, instalimi mund të bëhet nga administratori ose përmes sistemit të paketave të Octave.

Paraqitja grafike mund të ndryshojë lehtë ndërmjet MATLAB-it dhe Octave-s. Ky ndryshim nuk duhet të ndryshojë rezultatin numerik, rendin e konvergjencës ose interpretimin fizik.

## 9. Rrjedha e rekomanduar e punës për studentin

Për çdo laborator ndiqet kjo procedurë:

1. Lexohet kapitulli përkatës i leksioneve.
2. Identifikohen madhësitë hyrëse, dalëse dhe njësitë.
3. Shkruhet me fjalë algoritmi para plotësimit të kodit.
4. Ekzekutohet rasti bazë.
5. Kryhet një kontroll me zgjidhje analitike, mbetje, ligj ruajtjeje ose rezultat kufitar.
6. Ndryshohet vetëm një faktor në çdo seri eksperimentesh.
7. Raportohet gabimi numerik ose pacaktueshmëria statistike.
8. Krahasohen rezultatet me parashikimin teorik.
9. Shkruhet interpretimi fizik dhe përmenden kufizimet.
10. Funksionet e përgjithshme ruhen për paketën përfundimtare.

Ekzekutimi pa interpretim nuk konsiderohet përfundim i laboratorit.

## 10. Struktura e një dorëzimi të plotë

Dorëzimi duhet të përmbajë:

- notebook-un e ekzekutuar ose skedarin MATLAB/Octave;
- kodin e plotësuar nga studenti;
- një tabelë të parametrave dhe njësive;
- të paktën një kontroll verifikimi;
- figurat me titull, emra boshtesh, njësi dhe legjendë;
- një vlerësim të gabimit ose të pacaktueshmërisë;
- interpretimin fizik të rezultateve;
- kufizimet e modelit dhe të metodës;
- përfundime të shkurtra;
- funksionet e ripërdorshme të krijuara gjatë punës.

Emrat e figurave dhe funksioneve duhet të jenë përshkrues. Nuk rekomandohen emra si `test1`, `final2` ose `figure_new`.

## 11. Kriteret e verifikimit

Në varësi të laboratorit përdoret një ose disa nga provat e mëposhtme:

- krahasimi me zgjidhje analitike;
- mbetja e ekuacionit ose e sistemit;
- studimi i konvergjencës kur zvogëlohet hapi;
- ruajtja e energjisë ose e një invarianti;
- kontrolli i kushteve kufitare;
- krahasimi me një vlerë reference;
- kontrolli i mesatares, variancës dhe kuantileve;
- përsëritja me fara të ndryshme;
- analiza e autokorrelacionit dhe e madhësisë efektive;
- krahasimi Python–MATLAB/Octave.

Një figurë e bukur nuk zëvendëson verifikimin numerik.

## 12. Konventat shkencore dhe gjuhësore

Materiali përdor terminologjinë e leksioneve:

- *gabim i këputjes* për `truncation error`;
- *gabim i rrumbullakimit* për `round-off error`;
- *bredhje e rastit* për `random walk`;
- *pacaktueshmëri* për `uncertainty`;
- *balancë e detajuar* për `detailed balance`;
- *gjenerator pseudorastësor* për `pseudorandom generator`;
- *mostër*, *kampionim*, *vlerësues* dhe *gabim standard* sipas kuptimit statistikor.

Në Markdown, matematika shkruhet vetëm me:

- `$...$` për shprehje brenda rreshtit;
- `$$...$$` për ekuacione të veçuara.

Nuk përdoren `\\(...\\)` dhe `\\[...\\]`.

## 13. Riprodhueshmëria

Kur përdoret rastësia, notebook-et vendosin një farë të dokumentuar. Në raport duhet të shënohen:

- fara ose strategjia e farave;
- madhësia e mostrës;
- numri i përsëritjeve;
- hapi kohor ose hapësinor;
- toleranca dhe numri maksimal i iteracioneve;
- versioni i gjuhës dhe bibliotekave kur rezultati është i ndjeshëm;
- çdo ndryshim nga parametrat bazë.

Fara e njëjtë ndihmon diagnostikën, por një përfundim statistikor duhet të kontrollohet edhe me fara të tjera.

## 14. Gabime të zakonshme

### Kerneli nuk gjendet

Sigurohuni që Jupyter është nisur nga mjedisi ku janë instaluar bibliotekat. Nëse duhet, regjistroni kernelin:

```bash
python -m pip install ipykernel
python -m ipykernel install --user --name simulim-numerik --display-name "Simulim Numerik"
```

### `ModuleNotFoundError`

Aktivizoni mjedisin virtual dhe ekzekutoni:

```bash
python -m pip install -r requirements.txt
```

### Qelizat MATLAB/Octave nuk ekzekutohen në Jupyter

Kjo është sjellje e pritshme me kernelin Python, sepse ato janë qeliza `raw`. Kopjojini në MATLAB/Octave ose përdorni një kernel të përshtatshëm.

### Rezultati ndryshon nga versioni i instruktorit

Kontrolloni njësitë, parametrat, farën, tolerancën, rendin e ekzekutimit dhe faktin nëse të gjitha qelizat e mëparshme janë ekzekutuar.

### Simulimi Monte Carlo është i ngadaltë

Filloni me mostër më të vogël për diagnostikë, pastaj rriteni. Mos ndryshoni njëkohësisht madhësinë e mostrës, modelin dhe parametrat fizikë.

### Skema e valës bëhet e paqëndrueshme

Kontrolloni kushtin CFL. Paqëndrueshmëria për $c\Delta t/\Delta x>1$ është rezultat teorik i rëndësishëm, jo problem grafik.

## 15. Vlerësimi i rekomanduar

Një skemë orientuese është:

- 25% zbatimi i saktë i algoritmit;
- 25% verifikimi dhe analiza e gabimit;
- 20% figurat, tabelat dhe qartësia e raportimit;
- 20% interpretimi fizik;
- 10% riprodhueshmëria dhe organizimi i kodit.

Instruktori mund ta përshtatë peshën sipas laboratorit. Për shembull, te Laboratori 12 duhet t'i jepet peshë më e madhe diagnostikës së termalizimit dhe korrelacionit.

## 16. Kalimi drejt paketës përfundimtare të studentit

Gjatë semestrit studenti duhet të mbledhë funksionet e përgjithshme në një strukturë të vetën, për shembull:

```text
paketa_studentit/
├── src/
│   ├── rrenjet.py
│   ├── ode.py
│   ├── kampionimi.py
│   └── monte_carlo.py
├── tests/
├── examples/
├── README.md
└── requirements.txt
```

Për MATLAB/Octave mund të përdoret një dosje funksionesh `.m` dhe një dosje me skriptet demonstrative. Kjo veprimtari duhet të mbikëqyret nga pedagogu, sepse kërkon zgjedhje mbi ndërfaqet, testet dhe dokumentimin.

## 17. Validimi i paketës

Para paketimit janë kryer këto kontrolle:

- u verifikua struktura JSON e të 22 notebook-eve;
- u kontrollua rendi Python pastaj MATLAB/Octave;
- u kontrolluan delimituesit matematikorë;
- u auditua terminologjia shkencore;
- u kontrollua sintaksa e qelizave Python;
- u ekzekutuan të gjitha pjesët Python të versioneve të instruktorit;
- u kontrollua që versionet e studentëve ndalen vetëm në blloqet `TODO`;
- u kontrollua integriteti i arkivit ZIP.

Kodi MATLAB/Octave është kontrolluar statikisht. Laboratori 08 kërkon Statistics Toolbox në MATLAB ose paketën `statistics` në Octave për funksionin `mvnrnd`.

## 18. Parimi përfundimtar

Rezultati i një simulimi bëhet bindës vetëm kur studenti mund të shpjegojë:

- çfarë modeli është zgjidhur;
- çfarë algoritmi është përdorur;
- pse algoritmi pritet të funksionojë;
- si është verifikuar zbatimi;
- sa është gabimi ose pacaktueshmëria;
- cili është interpretimi fizik;
- cilat janë kufizimet e përfundimit.

Notebook-u është mjeti që bashkon këto elemente; ai nuk është vetë qëllimi i laboratorit.
