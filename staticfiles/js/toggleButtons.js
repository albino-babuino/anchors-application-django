document.addEventListener('DOMContentLoaded', () => {
	const toggleCheckbox = document.querySelector('.toggle-edit-delete');

	// Función para mostrar u ocultar botones
	const toggleButtons = () => {
		const deleteButtons = document.querySelectorAll('.delete-btn');
		const updateButtons = document.querySelectorAll('.update-btn');

		// Muestra u oculta los botones dependiendo del estado del checkbox
		const isChecked = toggleCheckbox.checked; // Estado del checkbox
		deleteButtons.forEach(
			(button) => (button.style.display = isChecked ? 'inline' : 'none')
		);
		updateButtons.forEach(
			(button) => (button.style.display = isChecked ? 'inline' : 'none')
		);
	};

	// Inicializar estado de los botones
	toggleButtons(); // Inicializa los botones en base al estado del checkbox

	// Añadir evento de cambio al checkbox
	toggleCheckbox.addEventListener('change', toggleButtons);

	// Event listener para restablecer el checkbox al salir de la página
	window.addEventListener('beforeunload', () => {
		toggleCheckbox.checked = false; // Restablecer el checkbox a su estado inicial
	});
});
