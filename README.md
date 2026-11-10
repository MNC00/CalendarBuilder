
# CalendarBuilder

CalendarBuilder è uno strumento Python che genera file calendario `.ics` a partire da un file YAML di eventi, pensato per facilitare l'importazione di calendari sportivi (es. CSI Roma) su dispositivi digitali (Google Calendar, Outlook, ecc.).

## Caratteristiche
- Input semplice tramite file YAML
- Output in formato `.ics` compatibile con la maggior parte dei calendari
- Personalizzazione eventi (titolo, descrizione, data/ora, durata, luogo)

## Struttura del progetto

```
CalendarBuilder/
├── InputFile.yaml           # File di input con gli eventi
├── main.py                  # Script principale per generare il calendario
├── requirements.txt         # Dipendenze Python
├── output/                  # Cartella di output per i file .ics generati
├── src/
│   └── utilities.py         # Funzioni di utilità per parsing e generazione eventi
└── .gitignore               # File di esclusione per git
```

## Requisiti
- Python 3.8+
- [PyYAML](https://pyyaml.org/) (`pip install pyyaml`)

Installa le dipendenze con:

```bash
pip install -r requirements.txt
```

## Utilizzo
1. Modifica `InputFile_UNIeTRINI.yaml` inserendo i tuoi eventi seguendo la struttura d'esempio. Per usare un altro file, cambia `INPUT_PATH` in `main.py`.
2. Esegui lo script principale:

```bash
python main.py
```

3. Troverai `output/CalendarioUNIeTRINI.ics` (nome configurabile con `OUTPUT_FILE` in `main.py`).

Su Windows, se `python` non trova `yaml`, usa l'ambiente virtuale del progetto:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

| Tipo di evento | Campi YAML | Significato |
| --- | --- | --- |
| Con orario | `start: "12/11/2026 21:00"`, `duration: 120` | Durata in minuti |
| Giornaliero o di piu giorni | `start: "04/12/2026"`, `end: "08/12/2026"` | Entrambe le date sono incluse; non serve `duration` |

Per un solo giorno, usa la stessa data in `start` ed `end`. `location` e facoltativo.

## Esempio di input (`InputFile.yaml`)
```yaml
events:
	- title: "(Casa) Squadra A vs Squadra B"
		description: "Campionato CSI Roma"
		start: "27/02/2026 21:00"
		duration: 120
		location: "Via Esempio 1, Roma"
```

## Contribuire
Contributi, segnalazioni di bug e suggerimenti sono benvenuti! Apri una issue o una pull request.

## Licenza
Questo progetto è distribuito sotto licenza MIT.
