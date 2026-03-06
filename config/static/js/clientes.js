let clienteEditando = null;

const token = localStorage.getItem("access_token");

const form = document.getElementById("clienteForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const nome = document.getElementById("nome").value;
    const documento = document.getElementById("documento").value;

    // 🔹 EDITAR CLIENTE
    if (clienteEditando) {

        const response = await fetch(`/api/v1/clientes/${clienteEditando}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token
            },
            body: JSON.stringify({ nome, documento })
        });

        if (response.ok) {
            alert("Cliente atualizado!");
            clienteEditando = null;
            form.reset();
            carregarClientes();
        } else {
            alert("Erro ao atualizar cliente");
        }

    }

    // 🔹 CRIAR CLIENTE
    else {

        const response = await fetch("/api/v1/clientes/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token
            },
            body: JSON.stringify({ nome, documento })
        });

        if (response.ok) {
            alert("Cliente cadastrado!");
            form.reset();
            carregarClientes();
        } else {
            alert("Erro ao cadastrar cliente");
        }

    }

});

async function carregarClientes() {

    const response = await fetch("/api/v1/clientes/", {
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    const data = await response.json();

    const container = document.getElementById("clientes-container");

    container.innerHTML = "";

    data.forEach(cliente => {

        const div = document.createElement("div");
        div.className = "cliente-card";

        div.innerHTML = `
            <strong>${cliente.nome}</strong><br>
            Documento: ${cliente.documento}<br>
            ID: ${cliente.id}
            <br><br>

            <button onclick="editarCliente(${cliente.id}, '${cliente.nome}', '${cliente.documento}')">
                ✏️ Editar
            </button>

            <button onclick="deletarCliente(${cliente.id})">
                🗑 Deletar
            </button>
        `;

        container.appendChild(div);

    });

}

function editarCliente(id, nome, documento) {

    document.getElementById("nome").value = nome;
    document.getElementById("documento").value = documento;

    clienteEditando = id;

}

async function deletarCliente(clienteId) {

    const confirmar = confirm("Deseja realmente deletar este cliente?");

    if (!confirmar) return;

    const response = await fetch(`/api/v1/clientes/${clienteId}/`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    if (response.ok) {
        alert("Cliente deletado");
        carregarClientes();
    } else {
        alert("Erro ao deletar cliente");
    }

}

carregarClientes();

async function buscarClientes() {

    const nome = document.getElementById("buscarCliente").value;

    const response = await fetch(`/api/clientes/?nome=${nome}`);

    const data = await response.json();

    const container = document.getElementById("lista-clientes");

    container.innerHTML = "";

    data.forEach(cliente => {

        const card = document.createElement("div");
        card.className = "cliente-card";

        card.innerHTML = `
            <strong>${cliente.nome}</strong>
            <p>Documento: ${cliente.documento}</p>
            <p>ID: ${cliente.id}</p>
        `;

        container.appendChild(card);

    });

}