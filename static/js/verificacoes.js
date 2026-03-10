// var nome = prompt("Como você chama?")
//
// if (nome === '') {
//     alert("Recarregue a página")
// } else {
//     let correto = confirm("Você se chama " + nome + "?")
//
//     if (correto) {
//         alert(` ${nome} Bem vindo ao site de cursos`)
//     } else {
//         alert("Recarregue a página")
//     }
// }

function limpaInputsLogin() {
    const inputCpf = document.getElementById('input-cpf')
    const inputSenha = document.getElementById('input-senha')

    inputCpf.value = ''
    inputSenha.value = ''
}

document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')

    formLogin.addEventListener("submit", function (event) {
        // Pegar os dois inputs do formulário
        const inputCpf = document.getElementById('input-cpf')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false

        // Verificar se os inputs estão vazios
        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o formulário
            event.preventDefault()
            alert("Preencha todos os campos!")
        }
    })

    const formCadastro = document.getElementById('form-cadastro')

    formCadastro.addEventListener("submit", function (event) {
        const inputNome = document.getElementById('input-nome')
        const inputNascimento = document.getElementById('input-nascimento')
        const inputCpf2 = document.getElementById('input-cpf2')
        const inputEmail = document.getElementById('input-email')
        const inputSenha2 = document.getElementById('input-senha2')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false

        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (inputNascimento.value === '') {
            inputNascimento.classList.add('is-invalid')
            temErro = true
        } else {
            inputNascimento.classList.remove('is-invalid')
        }

        if (inputCpf2.value === '') {
            inputCpf2.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf2.classList.remove('is-invalid')
        }

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (inputSenha2.value === '') {
            inputSenha2.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha2.classList.remove('is-invalid')
        }

        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o formulário
            event.preventDefault()
            alert("Preencha todos os campos!")
        }
    })

    const formFuncionarios = document.getElementById('form-funcionarios')

    formFuncionarios.addEventListener("submit", function (event) {
        const inputNome2 = document.getElementById('input-nome2')
        const inputNascimento2 = document.getElementById('input-nascimento2')
        const inputCpf3 = document.getElementById('input-cpf3')
        const inputEmail2 = document.getElementById('input-email2')
        const inputSenha3 = document.getElementById('input-senha3')
        const inputCargo2 = document.getElementById('input-cargo2')
        const inputSalario2 = document.getElementById('input-salario2')

        let temErro = false

        if (inputNome2.value === '') {
            inputNome2.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome2.classList.remove('is-invalid')
        }

        if (inputNascimento2.value === '') {
            inputNascimento2.classList.add('is-invalid')
            temErro = true
        } else {
            inputNascimento2.classList.remove('is-invalid')
        }

        if (inputCpf3.value === '') {
            inputCpf3.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf3.classList.remove('is-invalid')
        }

        if (inputEmail2.value === '') {
            inputEmail2.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail2.classList.remove('is-invalid')
        }

        if (inputSenha3.value === '') {
            inputSenha3.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha3.classList.remove('is-invalid')
        }

        if (inputCargo2.value === '') {
            inputCargo2.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo2.classList.remove('is-invalid')
        }

        if (inputSalario2.value === '') {
            inputSalario2.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario2.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o formulário
            event.preventDefault()
            alert("Preencha todos os campos!")
        }
    })
})



