import frappe
from frappe import _
from datetime import datetime
 #Ricontrollo file
@frappe.whitelist()
def get_customer_info(customer_code):
    """
    Estrae tutte le informazioni relative al cliente e ai suoi dipendenti
    
    Args:
        customer_code (str): Codice del cliente
        
    Returns:
        dict: Dizionario contenente le informazioni del cliente e dei dipendenti
    """
    try:
        # Ottieni i dati del cliente
        customer = frappe.get_doc("Ecopan Customer", customer_code)
        
        # Prepara il dizionario di risposta
        response = {
            "customer_info": {
                "name": customer.name,
                "customer_name": customer.customer_name,
                "tax_id": customer.tax_id,
                "vat_number": customer.vat_number,
                "address": customer.address,
                "city": customer.city,
                "province": customer.province,
                "postal_code": customer.postal_code,
                "country": customer.country
            },
            "branches": [],
            "employees": []
        }
        
        # Ottieni le sedi del cliente
        branches = frappe.get_all(
            "Ecopan Branch",
            filters={"parent": customer_code},
            fields=["branch_name", "address", "city", "province", "postal_code"]
        )
        response["branches"] = branches
        
        # Ottieni i dipendenti del cliente con i loro dettagli
        employees = frappe.get_all(
            "Ecopan Employee",
            filters={"parent": customer_code},
            fields=[
                "name", "first_name", "last_name", "fiscal_code", 
                "birth_date", "employment_status", "current_job_title",
                "branch", "employment_start_date", "employment_end_date"
            ]
        )
        response["employees"] = employees
        
        return response
        
    except Exception as e:
        frappe.log_error(f"Errore nell'estrazione dei dati del cliente: {str(e)}")
        return {"error": str(e)}

@frappe.whitelist()
def get_training_info(customer_code):
    """
    Estrae tutte le informazioni relative alla formazione dei dipendenti
    
    Args:
        customer_code (str): Codice del cliente
        
    Returns:
        dict: Dizionario contenente le informazioni sulla formazione
    """
    try:
        # Ottieni tutti i dipendenti del cliente
        employees = frappe.get_all(
            "Ecopan Employee",
            filters={"parent": customer_code},
            fields=["name", "first_name", "last_name", "current_job_title"]
        )
        
        response = {
            "customer_code": customer_code,
            "employees_training": []
        }
        
        for employee in employees:
            employee_training = {
                "employee_info": employee,
                "training_courses": [],
                "medical_visits": []
            }
            
            # Ottieni i corsi di formazione per il dipendente
            training_courses = frappe.get_all(
                "Ecopan Training Record",
                filters={"employee": employee.name},
                fields=[
                    "corso_formazione", "formazione_ecopan",
                    "data_formazione", "data_scadenza",
                    "descrizione"
                ]
            )
            employee_training["training_courses"] = training_courses
            
            # Ottieni le visite mediche per il dipendente
            medical_visits = frappe.get_all(
                "Ecopan Medical Visit",
                filters={"employee": employee.name},
                fields=[
                    "data_visita", "data_scadenza",
                    "annotazioni_visita"
                ]
            )
            employee_training["medical_visits"] = medical_visits
            
            response["employees_training"].append(employee_training)
            
        return response
        
    except Exception as e:
        frappe.log_error(f"Errore nell'estrazione dei dati di formazione: {str(e)}")
        return {"error": str(e)}

@frappe.whitelist()
def get_documents_info(customer_code):
    """
    Estrae tutte le informazioni relative ai documenti (DVR, HACCP) del cliente
    
    Args:
        customer_code (str): Codice del cliente
        
    Returns:
        dict: Dizionario contenente le informazioni sui documenti
    """
    try:
        response = {
            "customer_code": customer_code,
            "dvr_documents": [],
            "haccp_documents": [],
            "ssp_documents": []
        }
        
        # Ottieni i documenti DVR
        dvr_docs = frappe.get_all(
            "Ecopan DVR",
            filters={"client": customer_code},
            fields=[
                "name", "branch", "creation_date", "expiry_date",
                "status", "modified", "modified_by"
            ]
        )
        response["dvr_documents"] = dvr_docs
        
        # Ottieni i documenti HACCP
        haccp_docs = frappe.get_all(
            "Ecopan HACCP",
            filters={"client": customer_code},
            fields=[
                "name", "branch", "creation_date", "expiry_date",
                "status", "modified", "modified_by"
            ]
        )
        
        # Aggiungi le nomine HACCP per ogni documento
        for haccp in haccp_docs:
            haccp["responsabili"] = frappe.get_all(
                "Ecopan Employee",
                filters={
                    "parent": customer_code,
                    "data_responsabile_haccp": ["is", "set"]
                },
                fields=[
                    "first_name", "last_name", "current_job_title",
                    "data_responsabile_haccp"
                ]
            )
            
            haccp["delegati"] = frappe.get_all(
                "Ecopan Employee",
                filters={
                    "parent": customer_code,
                    "data_delega_haccp": ["is", "set"]
                },
                fields=[
                    "first_name", "last_name", "current_job_title",
                    "data_delega_haccp"
                ]
            )
            
        response["haccp_documents"] = haccp_docs
        
        # Ottieni i documenti SSP
        ssp_docs = frappe.get_all(
            "Ecopan SSP",
            filters={"client": customer_code},
            fields=[
                "name", "branch", "creation_date", "expiry_date",
                "status", "modified", "modified_by"
            ]
        )
        response["ssp_documents"] = ssp_docs
        
        return response
        
    except Exception as e:
        frappe.log_error(f"Errore nell'estrazione dei documenti: {str(e)}")
        return {"error": str(e)} 