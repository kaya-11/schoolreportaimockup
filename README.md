# School Report AI Mockup

**Ein Flask-basiertes Web-Tool zur Generierung von Schulzeugnis-Bemerkungen mit KI-Unterstützung (Ollama).**

---

## Überblick
Dieses Projekt nutzt **Flask** als Backend und **Ollama (llama3)** zur automatisierten Erstellung von **individuellen, wertschätzenden Bemerkungstexten** für Grundschulzeugnisse.
Die KI wandelt Stichworte (z. B. *"Mathe: gut"*) in ausführliche, positive Texte um – direkt an die Schüler:innen gerichtet.

---

## Technologien
- **Backend**: Python (Flask)
- **KI-Integration**: [Ollama](https://ollama.ai/) (llama3)
- **Frontend**: HTML/CSS (Jinja2-Templates)
- **Struktur**:
  - `app.py`: Flask-Routen für Zeugnisansicht und API
  - `ollama_module.py`: KI-Logik für Fach- und Softskill-Bewertungen
  - `templates/`: HTML-Vorlagen (z. B. `zeugnis.html`)
  - `static/`: CSS/JS-Ressourcen

---

## Schnellstart
1. **Voraussetzungen**:
   - Python 3.10+
   - Ollama (lokal installiert, [Anleitung](https://ollama.ai/))
   - Abhängigkeiten: `pip install flask ollama`

2. **Starten**:
   ```bash
   python app.py
   ```
   → Web-App läuft unter `http://localhost:5000`.

3. **Nutzung**:
   - Zeugnis-ID auswählen (z. B. `/zeugnis?id=1` für Max Mustermann).
   - Über die API (`/api/data`) können Stichworte an die KI gesendet werden.

---
## Beispiel-API-Aufruf
```json
POST /api/data
{
  "content": "aktiv",
  "fach": "Mathematik",
  "name": "Max"
}
```
→ **Antwort**: Ausformulierter Bemerkungstext (z. B. *"Im Mathematikunterricht bist du sehr aktiv und beteiligst dich gerne am Unterrichtsgeschehen."*).

---

## Features
✅ **Fächer & Softskills**: Automatische Erkennung von Schulfächern (Mathe, Deutsch, etc.) und sozialen Kompetenzen (hilfsbereit, teamfähig).
✅ **Individuelle Texte**: Anpassung an Schüler:innen-Namen und Fachkontext.
✅ **Positive Sprache**: Wertschätzender, motivierender Ton.

---

## Projektstruktur
```
schoolreportaimockup/
├── app.py                # Flask-App
├── ollama_module.py      # KI-Logik
├── templates/            # HTML-Vorlagen
│   ├── home.html
│   ├── zeugnis.html
│   └── ...
└── static/               # CSS/JS
```

---

** Hinweis**: Ollama muss lokal laufen (`ollama pull llama3`).

---

**Fragen?** Öffne ein Issue oder kontaktiere [@kaya-11](https://github.com/kaya-11).
