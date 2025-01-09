document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('modal');
    const openModalBtn = document.getElementById('openModal');
    const closeModalBtn = document.getElementById('closeModal');

    // Abrir o modal
    openModalBtn.addEventListener('click', function () {
        modal.style.display = 'flex';
    });

    // Fechar o modal
    closeModalBtn.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // Fechar o modal ao clicar fora dele
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
