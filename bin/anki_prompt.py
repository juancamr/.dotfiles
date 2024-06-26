import sys
import pyperclip

chatgpt_prompt = """Tu deber es convertir los apuntes que te daré a un tipo de nota básico
(adelante/atras) flashcards de anki. Necesito que priorices la información mas
importante, asegurate de que las preguntas y respuestas (adelante/atras) no
sean muy extensas y que se entiendan.
Ignora la seccion de resumen, preguntas de active recall, metadadatos y tags, solamente el contenido de Apuntes principales

Criterio de formato:

- Construye una línea con tres elementos: "Front", “Back”, "Tag".
- Cada fila de "front" column debe contener una pregunta.
- El "Back" column debe contener la respuesta.
- El "Tag" column debe contener el tag que te proporcionare para todas las filas.
- Debe haber <count> flashcards.
- No agregues las palabras Front, Back y Tag estos son solo para referencia, 
unicamente necesito el contenido de las flashcards.

Ejemplo:

Que es el ciclo de desarrollo de Software?;Las fases para que un producto de software sea entregado;Software
Que se realiza en la etapa de requerimientos?;Solicitar al cliente los requerimientos para su software.;Software

Apuntes: "<apuntes>"
Tag: <tag>"""

try:
    questions = sys.argv[1]
    tag = sys.argv[2]
    apuntes = pyperclip.paste()

    chatgpt_prompt = chatgpt_prompt.replace("<tag>", tag)
    chatgpt_prompt = chatgpt_prompt.replace("<apuntes>", apuntes)
    chatgpt_prompt = chatgpt_prompt.replace("<count>", questions)
    pyperclip.copy(chatgpt_prompt)

except:
    print("No tag or count of questions provided")
