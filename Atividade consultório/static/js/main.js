document.addEventListener('DOMContentLoaded', function () {

    const formulario = document.getElementById('form-consulta');
    const botao = document.getElementById('btn-buscar');
    const btnText = document.querySelector('.btn-text');
    const input = document.getElementById('especialidade');

    // Foco automático
    if (input) {
        input.focus();
    }

    // Loading botão
    if (formulario) {

        formulario.addEventListener('submit', function () {

            if (!input.value.trim()) return;

            botao.classList.add('loading');
            botao.disabled = true;

            btnText.textContent = 'Buscando...';

        });

    }

    // Formatação automática
    if (input) {

        input.addEventListener('blur', function () {

            this.value = this.value
                .toLowerCase()
                .replace(/\b\w/g, letra => letra.toUpperCase());

        });

    }

});

function preencherBusca(especialidade) {

    const input = document.getElementById('especialidade');

    input.value = especialidade;

    input.focus();

}