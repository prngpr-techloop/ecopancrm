# API Documentation EcopanCRM

## Panoramica
Questo documento descrive le API disponibili per l'estrazione dei dati dal sistema EcopanCRM. 
Tutte le API sono accessibili tramite chiamate HTTP e richiedono l'autenticazione Frappe.

## Endpoint Disponibili

### 1. get_customer_info(customer_code)
Estrae tutte le informazioni relative al cliente e ai suoi dipendenti.

**Endpoint:** `ecopancrm.ecopancrm.api.get_customer_info`

**Parametri:**
- customer_code (str): Codice identificativo del cliente

**Risposta:**
```json
{
  "customer_info": {
    "name": "string",
    "customer_name": "string",
    "tax_id": "string",
    "vat_number": "string",
    "address": "string",
    "city": "string",
    "province": "string",
    "postal_code": "string",
    "country": "string"
  },
  "branches": [
    {
      "branch_name": "string",
      "address": "string",
      "city": "string",
      "province": "string",
      "postal_code": "string"
    }
  ],
  "employees": [
    {
      "name": "string",
      "first_name": "string",
      "last_name": "string",
      "fiscal_code": "string",
      "birth_date": "date",
      "employment_status": "string",
      "current_job_title": "string",
      "branch": "string",
      "employment_start_date": "date",
      "employment_end_date": "date"
    }
  ]
}
```

### 2. get_training_info(customer_code)
Estrae tutte le informazioni relative alla formazione dei dipendenti.

**Endpoint:** `ecopancrm.ecopancrm.api.get_training_info`

**Parametri:**
- customer_code (str): Codice identificativo del cliente

**Risposta:**
```json
{
  "customer_code": "string",
  "employees_training": [
    {
      "employee_info": {
        "name": "string",
        "first_name": "string",
        "last_name": "string",
        "current_job_title": "string"
      },
      "training_courses": [
        {
          "corso_formazione": "string",
          "formazione_ecopan": "boolean",
          "data_formazione": "date",
          "data_scadenza": "date",
          "descrizione": "string"
        }
      ],
      "medical_visits": [
        {
          "data_visita": "date",
          "data_scadenza": "date",
          "annotazioni_visita": "string"
        }
      ]
    }
  ]
}
```

### 3. get_documents_info(customer_code)
Estrae tutte le informazioni relative ai documenti (DVR, HACCP, SSP) del cliente.

**Endpoint:** `ecopancrm.ecopancrm.api.get_documents_info`

**Parametri:**
- customer_code (str): Codice identificativo del cliente

**Risposta:**
```json
{
  "customer_code": "string",
  "dvr_documents": [
    {
      "name": "string",
      "branch": "string",
      "creation_date": "date",
      "expiry_date": "date",
      "status": "string",
      "modified": "datetime",
      "modified_by": "string"
    }
  ],
  "haccp_documents": [
    {
      "name": "string",
      "branch": "string",
      "creation_date": "date",
      "expiry_date": "date",
      "status": "string",
      "modified": "datetime",
      "modified_by": "string",
      "responsabili": [
        {
          "first_name": "string",
          "last_name": "string",
          "current_job_title": "string",
          "data_responsabile_haccp": "date"
        }
      ],
      "delegati": [
        {
          "first_name": "string",
          "last_name": "string",
          "current_job_title": "string",
          "data_delega_haccp": "date"
        }
      ]
    }
  ],
  "ssp_documents": [
    {
      "name": "string",
      "branch": "string",
      "creation_date": "date",
      "expiry_date": "date",
      "status": "string",
      "modified": "datetime",
      "modified_by": "string"
    }
  ]
}
```

## Esempi di Utilizzo

### Python
```python
import frappe

# Esempio 1: Ottenere informazioni cliente
customer_info = frappe.call('ecopancrm.ecopancrm.api.get_customer_info', 
                           customer_code='CLIENTE001')

# Esempio 2: Ottenere informazioni formazione
training_info = frappe.call('ecopancrm.ecopancrm.api.get_training_info',
                           customer_code='CLIENTE001')

# Esempio 3: Ottenere informazioni documenti
documents_info = frappe.call('ecopancrm.ecopancrm.api.get_documents_info',
                            customer_code='CLIENTE001')
```

### JavaScript
```javascript
// Esempio 1: Ottenere informazioni cliente
frappe.call({
    method: 'ecopancrm.ecopancrm.api.get_customer_info',
    args: {
        customer_code: 'CLIENTE001'
    }
}).then(r => {
    console.log(r.message);
});

// Esempio 2: Ottenere informazioni formazione
frappe.call({
    method: 'ecopancrm.ecopancrm.api.get_training_info',
    args: {
        customer_code: 'CLIENTE001'
    }
}).then(r => {
    console.log(r.message);
});

// Esempio 3: Ottenere informazioni documenti
frappe.call({
    method: 'ecopancrm.ecopancrm.api.get_documents_info',
    args: {
        customer_code: 'CLIENTE001'
    }
}).then(r => {
    console.log(r.message);
});
```

## Gestione degli Errori
Tutte le API restituiscono un oggetto di errore in caso di problemi:

```json
{
  "error": "Descrizione dell'errore"
}
```

Gli errori vengono anche registrati nei log di sistema di Frappe per il debugging.

## Note
- Tutte le API richiedono autenticazione
- Le date sono in formato ISO 8601
- I campi datetime includono il timestamp
- Le API sono ottimizzate per minimizzare il numero di query al database
- Tutti i dati sensibili sono gestiti secondo le normative sulla privacy 