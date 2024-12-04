// static/js/validators.js

let isSaveAction = false;

// Valida el formulario al enviar y cambia los colores de los campos
function validateFormOnSubmit(event) {
	const form = event.target;
	let formIsValid = true;
	const inputs = form.querySelectorAll('input, select, textarea');

	inputs.forEach(input => {
		// Evitar la validación en botones o campos ocultos
		if (input.type === 'submit' || input.type === 'button' || input.hidden || input.disabled) {
			return;
		}

		// Resetear estilos anteriores
		resetFieldValidation(input);

		// Validar campos vacíos
		if (!input.value || input.value.trim() === '') {
			setFieldInvalid(input, 'Este campo es obligatorio');
			// Si es una acción de guardar, permitimos que continúe, pero mostramos el borde rojo
			if (!isSaveAction) {
				formIsValid = false;
			}
		} else {
			setFieldValid(input, '¡Se ve bien!');
		}
	});

	// Si no es una acción de guardar y el formulario no es válido, prevenir el envío
	if (!formIsValid && !isSaveAction) {
		event.preventDefault();
	}

	return formIsValid;
}

function setFieldInvalid(field, message) {
	field.classList.add('border-red-500', 'text-red-500');
	field.classList.remove('border-green-500', 'text-green-500');
	showValidationMessage(field, message, 'text-red-500');
}

function setFieldValid(field, message) {
	field.classList.add('border-green-500', 'text-green-500');
	field.classList.remove('border-red-500', 'text-red-500');
	showValidationMessage(field, message, 'text-green-500');
}

function resetFieldValidation(field) {
	field.classList.remove('border-red-500', 'text-red-500', 'border-green-500', 'text-green-500');
	hideValidationMessage(field);
}

function showValidationMessage(field, message, colorClass) {
	let messageElement = field.nextElementSibling;

	if (!messageElement || !messageElement.classList.contains('validation-message')) {
		messageElement = document.createElement('p');
		messageElement.classList.add('validation-message', 'text-sm', 'mt-1');
		field.parentNode.appendChild(messageElement);
	}

	messageElement.textContent = message;
	messageElement.classList.remove('text-red-500', 'text-green-500');
	messageElement.classList.add(colorClass);
}

function hideValidationMessage(field) {
	const messageElement = field.nextElementSibling;
	if (messageElement && messageElement.classList.contains('validation-message')) {
		messageElement.textContent = '';
	}
}

// Acción para el botón de guardar sin redirigir
document.getElementById('form_button_save').addEventListener('click', function (event) {
	event.preventDefault();
	isSaveAction = true;
	const form = document.getElementById('form');

	// Validar el formulario pero permitir el envío aunque haya campos vacíos
	validateFormOnSubmit({ target: form });

	const formData = new FormData(form);
	fetch('/editar_respuestas', {
		method: 'POST',
		body: formData
	})
		.then(response => response.json())
		.then(data => {
			console.log('Formulario guardado correctamente', data);
			alert('Guardado correctamente sin redirección');
		})
		.catch(error => {
			console.error('Error al guardar el formulario', error);
		});
});

// Inicializa la validación del formulario
function initializeFormValidation() {
	const form = document.getElementById('form');
	form.addEventListener('submit', function (event) {
		isSaveAction = false;
		validateFormOnSubmit(event);
	});
}

document.addEventListener('DOMContentLoaded', initializeFormValidation);
