# TEST MODULE

## Descrizione
Modulo di test sviluppato per verificare il corretto caricamento di addons personalizzati in Odoo 17.
Questa versione estende sia il modello project.task che hr.employee, aggiungendo campi personalizzati e un'integrazione tra i due moduli.

Il modulo include anche una cartella `tests/` contenente casi di test automatici, eseguiti tramite il framework nativo di Odoo e integrati nella pipeline CI/CD di GitHub Actions.

## Funzionalità
* Estende il modello `project.task`:
    * Aggiunge il campo `x_custom_note`: campo testuale per note personalizzate.
    * Modifica la vista form di project.task per mostrare il nuovo campo.
    * Consente l'assegnazione di un dipendente, `hr.employee`, ad un task/progetto.
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