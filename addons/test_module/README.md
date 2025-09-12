# TEST MODULE

## Descrizione
Modulo di test sviluppato per verificare il corretto caricamento di addons personalizzati in Odoo 17.
Questa versione estende sia il modello project.task che hr.employee, aggiungendo campi personalizzati e un'integrazione tra i due moduli.

## Funzionalità
* Estende il modello `project.task`:
    * Aggiunge il campo `x_custom_note`: campo testuale per note personalizzate.
    * Modifica la vista form di project.task per mostrare il nuovo campo.
    * Consente l'assegnazione di un dipendente, `hr.employee`, ad un task/progetto.
* Estende il modello `hr.employee`:
    * Aggiunge il campo `x_custom_note`: campo testuale per note personalizzate.
    * Modifica la vista form di hr.employee per mostrare il campo.
    * Mostra i task/progetti assegnati al dipendente (collegamento con Project)

## Dipendenze
* `project` (modulo ufficiale Odoo)
* `hr` (modulo ufficiale Odoo) 

## Note
Questa versione completa il ciclo di integrazione tra **Project** e **HR**, consentendo la gestione delle assegnazioni progetto-dipendente in un unico flusso.