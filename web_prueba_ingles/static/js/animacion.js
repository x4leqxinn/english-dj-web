window.onload = function () {
  var imagen = document.getElementById("imagenReparacion");
  var imagen2 = document.getElementById("imagenMantenimiento");
  var imagen3 = document.getElementById("imagenAsistencia");
  imagen.style.top = "0";
  imagen2.style.top = "0";
  imagen3.style.top = "0";

};
// Función para agregar la clase de animación a los cards
function animateCards() {
  const cards = document.querySelectorAll('.card');
  cards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.2}s`;
    card.classList.add('fade-in');
  });
}

//Funcion para validar que 2 contrasenias sean iguales
  const form = document.querySelector('form');
  const passwordInput = document.getElementById('password');
  const confirmPasswordInput = document.getElementById('confirm-password');

  form.addEventListener('submit', function(event) {
    if (passwordInput.value !== confirmPasswordInput.value) {
      event.preventDefault();
      alert('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.');
    }
  });

  function password_show_hide() {
    var x = document.getElementById("password");
    var show_eye = document.getElementById("show_eye");
    var hide_eye = document.getElementById("hide_eye");
    hide_eye.classList.remove("d-none");
    if (x.type === "password") {
        x.type = "text";
        show_eye.style.display = "none";
        hide_eye.style.display = "block";
    } else {
        x.type = "password";
        show_eye.style.display = "block";
        hide_eye.style.display = "none";
    }
}

//mensaje de alerta creacion con exito 
function mostrarMensajeExito() {
  var mensajeExito = document.getElementById("mensaje-exito");
  mensajeExito.style.display = "block";  // Muestra el mensaje de éxito
}

  







