from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #ejecutar por consola: pip install webdriver-manager
import json
import time


correo = "danny.marmol@iudigital.edu.co"
contrasena = "IUD1040511943"
curso = '9344'
url = "https://iudigital.instructure.com/"

#url = "https://extensioniudigital.instructure.com/"

chrome_options = Options()#con esta linea de código daremos unas configuraciones al navegador 
#chrome_options.add_argument("--headless")#con esta instrucción se ejecta sin abrir ventana, si lo quiere con ventana sólo se tiene que borrar o ponerlo como comentarlo
#chrome_options.add_argument("--window-size=%s" % "1920,1080") #cpon esta opción le damos tamaño a la ventana
chrome_options.add_argument("start-maximized")#con esta opcion maximizamos la ventana del navegador


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=chrome_options)#mandamos por parametros la dirección del chromedrive que será descargado automaticamante por un servicio y las opciones para el navegador

driver.get(''+url+'courses/'+curso+'/files/folder/iconos')

# Login
user = driver.find_element(By.ID, "pseudonym_session_unique_id")
user.send_keys(correo)


password = driver.find_element(By.ID, "pseudonym_session_password")
password.send_keys(contrasena)


# Click login
login_button = driver.find_element(By.CLASS_NAME, "Button--login")


login_button.click()    
driver.implicitly_wait(20) # seconds

#video
#icon_video = driver.find_element(By.LINK_TEXT, "Bot_Video.svg")
icon_video = driver.find_element(By.XPATH, "//span[text()='Bot_Video_peq.svg']")
driver.implicitly_wait(1000) # seconds
print(icon_video.is_enabled())
icon_video.click()
#icon_video.click()
code_video = driver.current_url.split("=")[1]
driver.implicitly_wait(100) # seconds
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#ten_presente
icon_ten_presente = driver.find_element(By.LINK_TEXT, "Bot_TenPresente.svg")
icon_ten_presente.click()
code_ten_presente = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#Importante
icon_Importante = driver.find_element(By.LINK_TEXT, "Bot_Alerta-Importante.svg")
icon_Importante.click()
code_Importante = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#pdf
icon_pdf = driver.find_element(By.LINK_TEXT, "Bot_PDF.svg")
icon_pdf.click()
code_pdf = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#lectura
icon_lectura = driver.find_element(By.LINK_TEXT, "Bot_Lectura.svg")
icon_lectura.click()
code_lectura = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#objetivo
icon_objetivo = driver.find_element(By.LINK_TEXT, "Bot_Objetivo.svg")
icon_objetivo.click()
code_objetivo = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#instrucciones
icon_instrucciones = driver.find_element(By.LINK_TEXT, "Bot_Instrucciones.svg")
icon_instrucciones.click()
code_instrucciones = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#url
icon_url = driver.find_element(By.LINK_TEXT, "Bot_URL.svg")
icon_url.click()
code_url = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#profe
icon_profe = driver.find_element(By.LINK_TEXT, "Bot_Profe.svg")
icon_profe.click()
code_profe = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()
#preg
icon_preg = driver.find_element(By.LINK_TEXT, "Bot_Pregunta.svg")
icon_preg.click()
code_preg = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()


#audio
icon_audio = driver.find_element(By.LINK_TEXT, "Bot_Audio.svg")
icon_audio.click()
code_audio = driver.current_url.split("=")[1]
cerrar = driver.find_element(By.CLASS_NAME, "ef-file-preview-header-close").click()


fileName = "snippets.jsonc"
jsonString = {
	"base": {
		"prefix": "base",
		"body": [
			"<div class='IUD_container_azul_2019'>",
			"    <div class='IUD_banner_2022'>",
			"        <h1>$1</h1>",
			"    </div>",
			"    <div class='IUD_container'>",
			"        <div class='grid-row'>",
			"",
			"        </div>",
			"        <div>&nbsp;</div>",
			"        <div class='grid-row'>",
			"            <div class='col-md-12 col-xs-12 col-sm-12 col-lg-12'>",
			"                <div class='alert_2019 alert-info_2019'>",
			"                    <p style='text-align: center;  color: #7e8c8d;'>",
			"                        <em>",
			"                             Haz clic en <strong>Siguiente</strong> para continuar.",
			"                        </em>",
			"                    </p>",
			"                </div>",
			"            </div>",
			"        </div>",
			"    </div>",
			"    <div>&nbsp;</div>",
			"</div>",
		]
	},
	"pestañas": {
		"prefix": "pesta",
		"body": [
			"<div class='enhanceable_content tabs IUD_tabs_azul_2020 '>",
			"    <ul>",
			"        <li><a href='#tabs-1'>$1</a></li>",
			"        <li><a href='#tabs-2'>$2</a></li>",
			"        <li><a href='#tabs-3'>$3</a></li>",
			"    </ul>",
			"    <div id='tabs-1'>",
			"$4",
			"    </div>",
			"    <div id='tabs-2'>",
			"$5",
			"    </div>",
			"    <div id='tabs-3'>",
			"$6",
			"    </div>",
			"<hr>",
			"</div>",
		]
	},
	"imagen": {
		"prefix": "imagen",
		"body": [
			"<div class='col-md-$1' style='margin: auto auto auto 0;'>",
			"    <p>",
			"        <img class='img_100' src='"+url+"courses/${2:"+curso+"}/files/$3/download'",
			"            data-api-endpoint='"+url+"api/v1/courses/${2:"+curso+"}/files/$3' ",
			"            data-api-returntype='File'>",
			"    </p>",
			"</div>",
		]
	},
	"imagen-center": {
		"prefix": "imagen-center",
		"body": [
			"<div class='col-md-$1' style=' margin: auto ;'>",
			"    <p style='text-align: center;'>",
			"        <img class='img_100' src='"+url+"courses/${2:"+curso+"}/files/$3/download'",
			"            data-api-endpoint='"+url+"api/v1/courses/${2:"+curso+"}/files/$3' ",
			"            data-api-returntype='File'><br><p>$4</p>",
			"    </p>",
			"</div>",
		]
	},
	"alert-azul": {
		"prefix": "alert-azul",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/$2/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/$2' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-$3_2019'>",
			"            <p>$4</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"salto": {
		"prefix": "salto",
		"body": "<div>&nbsp;</div>"
	},
	"instruccion": {
		"prefix": "instruc",
		"body": [
			"<p style='color: #999; text-align: center;'>",
			"<em>",
			"$1",
			"</em>",
			"</p>",
		]
	},
	"btn-iud": {
		"prefix": "btn-iud",
		"body": [
			"<p>",
			"    <a class='btn btn-primary'>",
			"",
			"    </a>",
			"</p>",
		]
	},



	"alert-video": {
		"prefix": "alert-video",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_video+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_video+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:info}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-ten-presente": {
		"prefix": "alert-ten-presente",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_ten_presente+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_ten_presente+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:warning}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-important": {
		"prefix": "alert-important",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_Importante+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_Importante+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:warning}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-pdf": {
		"prefix": "alert-pdf",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_pdf+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_pdf+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:warning}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-lectura": {
		"prefix": "alert-lectura",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_lectura+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_lectura+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:warning}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-objetivo": {
		"prefix": "alert-objetivo",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_objetivo+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_objetivo+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			  "            <p>xxcs</p>",
			"    </div>",
			"</div>",
		]
	},
	"alert-instrucciones": {
		"prefix": "alert-instrucciones",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_instrucciones+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_instrucciones+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			  "            <p>xxcs</p>",
			"    </div>",
			"</div>",
		]
	},
	"alert-url": {
		"prefix": "alert-url",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px; margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_url+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_url+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:info}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-profe": {
		"prefix": "alert-profe",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px;  margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_profe+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_profe+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:success}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-preg": {
		"prefix": "alert-preg",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-4 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px;  margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_preg+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_preg+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:success}_2019'>",
			  "            <p>xxcs</p>",
			"        </div>",
			"    </div>",
			"</div>",
		]
	},
	"alert-audio": {
		"prefix": "alert-audio",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-3 col-sm-12 col-xs-12 col-lg-2' style='min-width: 110px; max-width: 110px;  margin: auto;'><img class='img_100' src='"+url+"courses/${1:"+curso+"}/files/${2:"+code_audio+"}/preview' alt='' data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/${2:"+code_audio+"}' data-api-returntype='File' style='max-width: 86px;'></div>",
			"    <div class='col-md-9 col-sm-8 col-xs-12 col-lg-10'>",
			"        <div class='alert_2019 alert-${3:info}_2019'>",
			"            <p> <i><a class='element_toggler' aria-controls='modal_uno'>xx</a></i></p>",
			"        </div>",
	
			"    </div>",
			"</div>",
		]
	},




	
	"alert-code": {
		"prefix": "alert-code",
		"body": [
			"<div class='grid-row'>",
			"            <div class='col-md-8' style='margin: auto;'>",
			"                <pre style='font-size: 1.5rem;'>",
			"$1",
			"            </pre>",
			"            </div>",
			"        </div>"
		]
	},
	"img-text-left": {
		"prefix": "img-text-left",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-12'>",
			"        <div class='IUD_img_float_container'><img id='1784474' class='img_100 img_left'",
			"                src='"+url+"courses/${1:"+curso+"}/files/$2/preview'",
			"                alt='Slide_45_Graf_01.jpg'",
			"                data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/$2'",
			"                data-api-returntype='File' />",
			"            <p>$3</p>",
			"        </div>",
			"    </div>",
			"</div>"
		]
	},
	"img-text-right": {
		"prefix": "img-text-right",
		"body": [
			"<div class='grid-row'>",
			"    <div class='col-md-12'>",
			"        <div class='IUD_img_float_container'><img id='1784474' class='img_100 img_right'",
			"                src='"+url+"courses/${1:"+curso+"}/files/$2/preview'",
			"                alt='Slide_45_Graf_01.jpg'",
			"                data-api-endpoint='"+url+"api/v1/courses/${1:"+curso+"}/files/$2'",
			"                data-api-returntype='File' />",
			"            <p>$3</p>",
			"        </div>",
			"    </div>",
			"</div>"
		]
	},
}


out_file = open("D:/Documentos/código_iudigital-20220621T133342Z-001/código_iudigital/auto_snippet_iconos_python/myfile.jsonc", "w")
json.dump(jsonString, out_file, indent = 6)
print("FIN")
out_file.close()
driver.quit()