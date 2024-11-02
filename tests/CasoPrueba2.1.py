#TODO: Caso de Prueba TC2.1 - Editar fecha de vencimiento a una fecha futura válida

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración de opciones para Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Usar webdriver_manager para gestionar el driver automáticamente
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    # Abre la aplicación
    driver.get("http://localhost:8000")
    driver.maximize_window()
    time.sleep(2)

    # Primero, agregar una tarea para asegurar que existe
    task_name = driver.find_element(By.ID, "task-name")
    task_desc = driver.find_element(By.ID, "task-desc")
    task_due_date = driver.find_element(By.ID, "task-due-date")
    add_button = driver.find_element(By.XPATH, "//button[text()='Agregar tarea']")

    # Datos de la tarea inicial
    test_name = "Estudiar para el examen"
    test_desc = "Revisar todos los capítulos del libro"
    initial_date = "2024-11-01"

    # Agregar la tarea inicial
    task_name.send_keys(test_name)
    task_desc.send_keys(test_desc)
    task_due_date.send_keys(initial_date)
    add_button.click()
    time.sleep(2)

    # Buscar la tarea en la lista
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    target_task = None

    for task in tasks:
        if test_name in task.text:
            target_task = task
            break

    assert target_task is not None, "No se encontró la tarea para editar"

    # Encontrar y hacer clic en el botón de editar
    edit_buttons = target_task.find_elements(By.TAG_NAME, "button")
    edit_button = None
    for button in edit_buttons:
        if "Editar" in button.text:
            edit_button = button
            break

    assert edit_button is not None, "No se encontró el botón de editar"
    edit_button.click()
    time.sleep(1)

    # Manejar el prompt de edición
    # Aceptar el primer prompt (nombre) sin cambios
    alert = driver.switch_to.alert
    alert.send_keys(test_name)
    alert.accept()
    time.sleep(1)

    # Aceptar el segundo prompt (descripción) sin cambios
    alert = driver.switch_to.alert
    alert.send_keys(test_desc)
    alert.accept()
    time.sleep(1)

    # Ingresar la nueva fecha en el tercer prompt
    new_date = "2024-12-15"
    alert = driver.switch_to.alert
    alert.send_keys(new_date)
    alert.accept()
    time.sleep(2)

    # Verificar que la tarea se actualizó correctamente
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    task_updated = False
    
    for task in tasks:
        if test_name in task.text and new_date in task.text:
            task_updated = True
            break

    assert task_updated, "La fecha de la tarea no se actualizó correctamente"

    print("Caso de Prueba TC2.1: PASADO ✅")
    print("✅ La tarea se encontró correctamente")
    print("✅ Se pudo editar la fecha de vencimiento")
    print("✅ La nueva fecha se muestra correctamente en la lista")

except AssertionError as ae:
    print(f"Caso de Prueba TC2.1: FALLADO ❌")
    print(f"Error: {str(ae)}")

except NoSuchElementException as nse:
    print(f"Caso de Prueba TC2.1: FALLADO ❌")
    print(f"Error: Elemento no encontrado - {str(nse)}")

except Exception as e:
    print(f"Caso de Prueba TC2.1: FALLADO ❌")
    print(f"Error inesperado: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()
