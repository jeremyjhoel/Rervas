// main.js
document.addEventListener("DOMContentLoaded", function () {
  // Obtén una referencia al enlace y al div de contenido dinámico
  const cargarContenidoLink = document.getElementById("cargarContenidoLink");
  const contenidoDinamico = document.getElementById("contenidoDinamico");

  // Asocia un evento de clic al enlace
  cargarContenidoLink.addEventListener("click", function (event) {
    event.preventDefault(); // Evita el comportamiento predeterminado del enlace
    
    // Realiza una solicitud GET para cargar el contenido del archivo de plantilla
    fetch("/formBus/")
      .then(response => response.text())
      .then(html => {
        // Asigna el HTML cargado al div de contenido dinámico
        contenidoDinamico.innerHTML = html;
      })
      .catch(error => {
        console.error("Error al cargar el archivo de plantilla:", error);
      });
  });
});


