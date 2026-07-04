# Location Tracker - Kurzlink mit Standorterfassung

Webanwendung zum Erstellen von Kurzlinks und Erfassen von GPS-Standorten der Benutzer, wenn sie auf den Link klicken.

## 🌟 Funktionen

- ✅ Einfache Kurzlink-Erstellung
- 📍 Präzise GPS-Standorterfassung
- 🗺️ Standortanzeige auf Google Maps
- 📊 Dashboard zur Link-Verwaltung und Statistik
- 📱 Responsive Design, mobil kompatibel
- 🔒 Datensicherheit

## 🚀 Installation und lokale Ausführung

### Voraussetzungen
- Python 3.8+
- Google Maps API Key

### Installation

1. Repository klonen:
```bash
git clone <your-repo-url>
cd location-tracker
```

2. Virtuelle Umgebung erstellen:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. .env-Datei aus env_example.txt erstellen:
```bash
copy env_example.txt .env  # Windows
# cp env_example.txt .env  # Linux/Mac
```

5. .env-Datei bearbeiten:
```env
GOOGLE_MAPS_API_KEY=your_actual_api_key_here
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///location_tracker.db
PORT=5000
```

6. Anwendung starten:
```bash
python app.py
```

Aufruf: http://localhost:5000

## 🌐 Deployment auf Railway

### Schritt 1: Vorbereitung
1. Konto bei [railway.app](https://railway.app) erstellen
2. Railway CLI installieren oder GitHub-Integration nutzen

### Schritt 2: Deploy
1. Code auf GitHub Repository pushen
2. Railway mit GitHub-Repo verbinden
3. Neues Projekt auf Railway erstellen
4. Umgebungsvariablen hinzufügen:
   - `GOOGLE_MAPS_API_KEY`: Google Maps API-Schlüssel
   - `SECRET_KEY`: Geheimer Schlüssel für Flask
   - `DATABASE_URL`: Railway erstellt automatisch PostgreSQL

### Schritt 3: Google Maps API-Schlüssel besorgen
1. [Google Cloud Console](https://console.cloud.google.com/) aufrufen
2. Neues Projekt erstellen oder vorhandenes auswählen
3. Google Maps JavaScript API aktivieren
4. API-Schlüssel erstellen und Domain-Einschränkungen hinzufügen
5. API-Schlüssel in Railway-Umgebungsvariablen kopieren

## 📖 Verwendung

### 1. Kurzlink erstellen
- Startseite aufrufen
- Titel, Ziel-URL und Beschreibung eingeben
- Auf "Kurzlink erstellen" klicken
- Erstellten Link kopieren

### 2. Link teilen
- Kurzlink an andere senden über:
  - SMS
  - E-Mail
  - Social Media
  - QR-Code

### 3. Standort verfolgen
- Wenn jemand auf den Link klickt:
  - Der Browser fragt nach Standortberechtigung
  - Die App erfasst die GPS-Koordinaten
  - Der Benutzer wird zur Ziel-URL weitergeleitet
- Statistiken im Dashboard ansehen

### 4. Berichte ansehen
- Dashboard aufrufen für:
  - Liste aller erstellten Links
  - Klick-Anzahl pro Link
  - Standortdetails auf der Karte
  - Zeit und GPS-Genauigkeit

## 🔧 API-Endpunkte

- `GET /` - Startseite
- `GET /dashboard` - Dashboard
- `POST /create` - Neuen Link erstellen
- `GET /l/<short_code>` - Weiterleitung und Standorterfassung
- `POST /api/location` - Standortdaten speichern
- `GET /link/<id>` - Link-Details und Karte

## ⚠️ Wichtige Hinweise

### Rechtlich
- Nur für legale Zwecke verwenden
- Benutzer klar über Standorterfassung informieren
- GDPR und Datenschutzbestimmungen einhalten

### Sicherheit
- Keine sensiblen Daten in der Datenbank speichern
- HTTPS in der Produktion verwenden
- Datenbankzugriff einschränken

### Ethische Nutzung
- Standort nur mit Zustimmung des Benutzers erfassen
- Klare Datenschutzrichtlinien haben
- Opt-Out-Möglichkeit anbieten

## 🛠️ Verwendete Technologien

- **Backend**: Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, jQuery, HTML5 Geolocation
- **Datenbank**: SQLite (lokal), PostgreSQL (Produktion)
- **Karten**: Google Maps JavaScript API
- **Deployment**: Railway

## 📄 Lizenz

MIT License - Siehe LICENSE-Datei für Details.

## 🤝 Beitragen

Beiträge sind willkommen! So geht's:
1. Fork das Projekt
2. Feature-Branch erstellen
3. Changes commiten
4. Branch pushen
5. Pull Request erstellen

## 📞 Support

Bei Problemen ein Issue auf GitHub erstellen oder per E-Mail kontaktieren.

---

⭐ **Wenn dir das Projekt gefällt, gib einen Stern!** ⭐
