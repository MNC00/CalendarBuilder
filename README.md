
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
1. Modifica `InputFile.yaml` inserendo i tuoi eventi seguendo la struttura d'esempio.
2. Esegui lo script principale:

```bash
python main.py
```

3. Troverai il file `.ics` generato nella cartella `output/`.

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
