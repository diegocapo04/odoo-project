# Odoo Project

## Descrizione
Ambiente di sviluppo **Odoo 17** con **PostgreSQL 15**, gestito tramite **Docker Compose**.  
Il progetto utilizza la cartella `addons/` locale dove vengono salvati i moduli personalizzati.  

In questa versione, è stato creato un modulo di test test_module che estende e integra i moduli predefiniti project e hr, aggiungendo campi personalizzati e relazioni tra task e dipendenti.
È stato inoltre configurato un workflow di CI/CD con GitHub Actions per testare automaticamente il modulo all’avvio dell’ambiente.

## Servizi
- **web**: Odoo 17 (porta esposta `8069`)
- **db**: PostgreSQL 15

## Avvio del progetto
1. Avviare i container:
   ```bash
   docker compose up -d
2. Aprire il browser su: http://localhost:8069

## Aggiungere un modulo personalizzato
1. Creare una nuova cartella dentro addons/.
2. Inserire al suo interno i file del modulo.
3. Riavviare Odoo:
   ```bash
    docker compose restart web
4. Da interfaccia Odoo, andare su App → Aggiorna elenco app.
5. Cercare e installare il modulo.

## Test automatici con GitHub Actions
- Ogni push sul branch `main` attiva il workflow CI/CD configurato.
- Il workflow avvia temporaneamente i container con docker-compose, installa il modulo `test_module` e verfica che Odoo si avii correttamente.