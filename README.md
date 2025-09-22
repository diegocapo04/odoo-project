# Odoo Project

![Odoo CI](https://github.com/diegocapo04/odoo-project/actions/workflows/odoo-pipeline.yaml/badge.svg?branch=main)

## Descrizione
Ambiente di sviluppo **Odoo 17** con **PostgreSQL 15**, gestito tramite **Docker Compose**.  
Il progetto utilizza la cartella `addons/` locale dove vengono salvati i moduli personalizzati.  

In questa versione:
- E' stato creato un modulo di test test_module che estende e integra i moduli predefiniti project e hr, aggiungendo:
   - campi personalizzati 
   - una relazione **many2many** tra `project.task` e `hr.employee`
   - sincronizzazione automatica con il campo `user_ids` per mantenere la compatibilità con Odoo
- E' stato configurato un workflow di CI/CD con GitHub Actions per testare automaticamente il modulo all’avvio dell’ambiente.
- E' stato creato un Dockerfile per costruire l'immagine `odoo-custom` con i moduli integrati.


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
- Il workflow esegue i seguenti step:
   1. Build dell'immagine **odoo-custom**
   2. Avvio dei container con **docker-compose** 
   3. Installazione del modulo `test_module`
   4. Esecuzione dei **test Python**
   5. Arresto e pulizia dei container