# TEST MODULE

## Descrizione
Modulo di test sviluppato per verificare il corretto caricamento di addons personalizzati in Odoo 17.
Questa versione estende sia il modello project.task che hr.employee, aggiungendo campi personalizzati e un'integrazione tra i due moduli.

Il modulo include anche una cartella `tests/` contenente casi di test automatici, eseguiti tramite il framework nativo di Odoo e integrati nella pipeline CI/CD di GitHub Actions.

## Funzionalità
* Estende il modello `project.task`:
    * Aggiunge il campo `x_custom_note`: campo testuale per note personalizzate.
    * Nasconde il campo nativo `user_ids`, mantenendolo **sincronizzato automaticamnte** con gli utenti corrispondenti ai dipendenti assegnati.
    * Aggiunge la relazione **many2many** `employee_ids`, che consente di assegnare uno o più dipendenti (`hr.employee`) ad un task/progetto.
    * Sincronizza automaticamente l’assegnazione e la rimozione dei task anche sugli utenti (`res.users`) collegati ai dipendenti.
* Estende il modello `hr.employee`:
    * Aggiunge il campo `x_custom_note`: campo testuale per note personalizzate.
    * Modifica la vista form di hr.employee per mostrare il campo.
    * Mostra i task/progetti assegnati al dipendente (collegamento con Project)

## Test automatici
La cartella `tests/` contiene casi di test basati su `TrasactionCase`, che permettono di:
* Verificare la creazione di record (`employee`,`task`).
* Testare la relazione tra `project.task` e `hr.employee`.

## Dipendenze
* `project` (modulo ufficiale Odoo)
* `hr` (modulo ufficiale Odoo) 