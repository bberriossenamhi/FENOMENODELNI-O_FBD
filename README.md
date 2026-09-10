# El Pacífico en movimiento

Maqueta educativa 3D de El Niño, La Niña y las condiciones normales. Conserva los controles de cámara, el movimiento del agua y la lluvia, y las explicaciones de la versión preparada en Codex.

## Qué contiene

- `index.html`: la página completa, con sus estilos y programación.
- `abrir_maqueta.py`: servidor local opcional para probar la página con Python.
- `.nojekyll`: indica a GitHub Pages que publique los archivos directamente.
- `README.md`: esta guía.

La interactividad funciona con JavaScript y Three.js en el navegador. No requiere un servidor Python al publicarse. Necesita conexión a Internet para cargar las bibliotecas externas y un navegador con WebGL. Los archivos no incluyen claves ni requieren una cuenta de Codex para visitar la maqueta.

## Probar en VS Code

1. Extrae el ZIP, si usas el paquete descargado.
2. En VS Code elige Archivo > Abrir carpeta y selecciona la carpeta que contiene `index.html`.
3. Abre Terminal > Nueva terminal.
4. En Windows ejecuta `py abrir_maqueta.py`. Si tu instalación utiliza el comando `python`, ejecuta `python abrir_maqueta.py`.
5. Se abrirá el navegador. Si no ocurre, copia la dirección que imprime la terminal.
6. Mantén la terminal abierta mientras presentas. Usa Ctrl+C para detener el servidor.

También puedes abrir `abrir_maqueta.py` en VS Code y ejecutarlo con tu intérprete de Python seleccionado.

## Publicar en GitHub Pages, sin usar comandos de Git

1. Inicia sesión en https://github.com y crea un repositorio nuevo llamado `pacifico-3d`.
2. Selecciona Public para usar GitHub Pages con una cuenta gratuita. El sitio y el código serán públicos.
3. Activa Add a README para que exista una rama inicial; crea el repositorio.
4. En Code, elige Add file > Upload files.
5. Sube `index.html` y `.nojekyll` directamente en la raíz del repositorio. No subas el ZIP cerrado ni pongas el HTML dentro de otra carpeta. El servidor Python es solo para tu computadora y no hace falta subirlo.
6. Confirma con Commit changes.
7. Entra en Settings > Pages.
8. En Build and deployment, selecciona Source: Deploy from a branch.
9. Selecciona la rama que contiene los archivos (normalmente `main`) y la carpeta `/(root)`; pulsa Save.
10. Espera a que termine la publicación. La página Settings > Pages mostrará el enlace del sitio, normalmente `https://TU-USUARIO.github.io/pacifico-3d/`.
11. Abre ese enlace para comprobar la maqueta y compártelo con tu público. No compartas solo el enlace del repositorio.

Para actualizarla, vuelve a subir el `index.html` modificado y confirma los cambios. GitHub Pages volverá a publicar la página.

## Presentar

- Arrastra la escena para girarla y usa la rueda para acercar o alejar.
- Cambia entre Condición normal, El Niño y La Niña.
- Activa Ver movimiento para una demostración de 15 segundos.
- Usa las vistas Perspectiva, Corte del océano, Desde arriba y Costa sudamericana.
- Sigue los botones 1. Viento, 2. Océano, 3. Lluvias y 4. Perú.
- Pulsa Ampliar para aumentar la escena. F11 permite usar pantalla completa en navegadores de escritorio de Windows.

## Si algo no aparece

- Error 404 en GitHub Pages: comprueba que `index.html` está en la raíz y que Pages usa la rama correcta y `/(root)`; revisa el estado de publicación en Actions.
- Se ve la página, pero no el 3D: comprueba Internet, WebGL y que la red permita cdn.jsdelivr.net.
- `python` no se reconoce: en Windows prueba `py abrir_maqueta.py`, o selecciona tu intérprete en VS Code.
- La página compartida muestra código: estás compartiendo el repositorio; usa la dirección `github.io` que aparece en Settings > Pages.

## Fuentes

La maqueta muestra patrones generales y volúmenes sin escala; no es un pronóstico ni un mapa geográfico. Los colores distinguen temperaturas, no el color real del océano.

- NOAA: https://oceanservice.noaa.gov/facts/ninonina.html
- NOAA PMEL: https://www.pmel.noaa.gov/elnino/what-is-el-nino
- MINAM: https://www.minam.gob.pe/fenomenodelnino/el-nino-en-el-peru-y-sus-caracteristicas/
- Guía de GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Acerca de GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

Versión preparada: 10 de septiembre de 2026. El paquete está listo para publicar; no se ha publicado automáticamente.
