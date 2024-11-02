#TODO: Caso de Prueba TC1.2 - Validar campos incompletos al agregar una tarea

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
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

    # Localiza los campos de entrada
    task_name = driver.find_element(By.ID, "task-name")
    task_desc = driver.find_element(By.ID, "task-desc")
    task_due_date = driver.find_element(By.ID, "task-due-date")
    add_button = driver.find_element(By.XPATH, "//button[text()='Agregar tarea']")

    # Dejar el nombre vacío e ingresar los otros campos
    test_desc = "Comprar materiales de oficina"
    test_date = "2024-11-15"

    # No ingresamos nada en el campo nombre (dejarlo vacío)
    task_desc.send_keys(test_desc)
    task_due_date.send_keys(test_date)

    # Hace clic en "Agregar tarea"
    add_button.click()
    time.sleep(2)

    # Verifica el mensaje de error
    confirmation = driver.find_element(By.ID, "add-confirmation").text
    assert confirmation == "Por favor, completa todos los campos.", "El mensaje de error no se mostró correctamente"

    # Verifica que la tarea NO aparezca en la lista
    task_list = driver.find_element(By.ID, "task-list")
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    
    # Busca si la tarea se agregó (no debería encontrarla)
    task_found = False
    for task in tasks:
        if test_desc in task.text:
            task_found = True
            break

    # Verifica que la tarea NO se haya agregado
    assert not task_found, "La tarea se agregó a pesar de tener campos incompletos"

    print("Caso de Prueba TC1.2: PASADO ✅")
    print("✅ La tarea no se agregó (correcto)")
    print("✅ Se mostró el mensaje de error apropiado")
    print("✅ Se validaron correctamente los campos incompletos")

except AssertionError as ae:
    print(f"Caso de Prueba TC1.2: FALLADO ❌")
    print(f"Error: {str(ae)}")

except NoSuchElementException as nse:
    print(f"Caso de Prueba TC1.2: FALLADO ❌")
    print(f"Error: Elemento no encontrado - {str(nse)}")

except Exception as e:
    print(f"Caso de Prueba TC1.2: FALLADO ❌")
    print(f"Error inesperado: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()
