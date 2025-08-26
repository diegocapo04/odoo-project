# Odoo Project

## Descrizione
Ambiente di sviluppo **Odoo 17** con **PostgreSQL 15**, gestito tramite **Docker Compose**.  
Il progetto utilizza la cartella `addons/` locale dove vengono salvati i moduli personalizzati.  

---

## Servizi
- **web**: Odoo 17 (porta esposta `8069`)
- **db**: PostgreSQL 15

---

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