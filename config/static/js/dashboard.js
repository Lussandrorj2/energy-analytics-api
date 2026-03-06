let grafico = null;

document.addEventListener("DOMContentLoaded", function () {

    // 🔹 MÉTRICAS
    fetch("/api/v1/analytics/resumo-geral/")
        .then(res => {
            if (!res.ok) throw new Error("Erro ao carregar resumo");
            return res.json();
        })
        .then(data => {
            const totalClientes = document.getElementById("totalClientes");
            const totalConsumo = document.getElementById("totalConsumo");
            const mediaGeral = document.getElementById("mediaGeral");

            if (totalClientes) totalClientes.innerText = data.total_clientes;

            if (totalConsumo)
                totalConsumo.innerText = Number(data.total_consumo_geral).toFixed(2) + " kWh";

            if (mediaGeral)
                mediaGeral.innerText =
                    (data.media_geral ? Number(data.media_geral).toFixed(2) : "0.00") + " kWh";
        })
        .catch(err => console.error(err));

});

// 🔹 Carregar clientes no select
carregarClientes();

// 🔹 Top consumidores
carregarTopConsumers();

// 🔹 Top consumidores
carregarGraficoClientes();

// 🔹 Evento select cliente
const select = document.getElementById("clienteSelect");

select.addEventListener("change", function () {

    const clienteId = this.value;

    if (clienteId === "geral") {
        carregarResumo("geral");
        carregarGrafico("geral");
        carregarCrescimento("geral");
    } else {
        carregarResumo(Number(clienteId));
        carregarGrafico(Number(clienteId));
        carregarCrescimento(Number(clienteId));
    }

});

let graficoClientes = null;

async function carregarGraficoClientes() {

    const response = await fetch("/api/v1/analytics/consumo-clientes/");
    const data = await response.json();

    const labels = data.map(item => item.cliente__nome);
    const valores = data.map(item => item.total);

    const ctx = document
        .getElementById("graficoClientes")
        .getContext("2d");

    if (graficoClientes) graficoClientes.destroy();

    graficoClientes = new Chart(ctx, {

        type: "bar",

        data: {
            labels: labels,
            datasets: [{
                label: "Consumo total (kWh)",
                data: valores,
                backgroundColor: "#38bdf8"
            }]
        },

        options: {
            responsive: true
        }

    });

}

async function carregarResumo(clienteId = "geral") {

    const response = await fetch(`/api/v1/analytics/resumo-geral/?cliente=${clienteId}`);
    const data = await response.json();

    document.getElementById("totalClientes").innerText = data.total_clientes;
    document.getElementById("totalConsumo").innerText = data.total_consumo_geral.toFixed(2) + " kWh";
    document.getElementById("mediaGeral").innerText =
        (data.media_geral ? data.media_geral.toFixed(2) : "0.00") + " kWh";

}

/* ===============================
   📈 CRESCIMENTO PERCENTUAL
================================ */
async function carregarCrescimento(clienteId) {

    try {
        const response = await fetch(`/api/v1/analytics/crescimento-percentual/?cliente_id=${clienteId}`);

        const elemento = document.getElementById("crescimentoPercentual");

        if (!response.ok) {
            if (elemento) elemento.innerText = "Sem dados";
            return;
        }

        const data = await response.json();

        if (elemento && data.crescimento_percentual !== undefined) {
            elemento.innerText = data.crescimento_percentual + " %";
        } else if (elemento) {
            elemento.innerText = "Sem dados";
        }

    } catch (error) {
        console.error("Erro ao carregar crescimento:", error);
        const elemento = document.getElementById("crescimentoPercentual");
        if (elemento) elemento.innerText = "Erro";
    }

}



/* ===============================
   🏆 TOP CONSUMIDORES
================================ */
async function carregarTopConsumers() {

    try {
        const response = await fetch("/api/v1/analytics/top-consumers/");
        const data = await response.json();

        const lista = document.getElementById("topConsumers");

        if (!lista) return;

        lista.innerHTML = "";

        data.forEach(item => {

            const li = document.createElement("li");

            li.innerText = `${item.cliente__nome} — ${item.consumo_total} kWh`;

            lista.appendChild(li);

        });

    } catch (error) {
        console.error("Erro ao carregar top consumidores:", error);
    }

}



/* ===============================
   👥 CARREGAR CLIENTES
================================ */
async function carregarClientes() {

    try {
        const response = await fetch("/api/v1/clientes/");

        if (!response.ok) throw new Error("Erro ao carregar clientes");

        const clientes = await response.json();

        const select = document.getElementById("clienteSelect");

        if (!select) return;

        clientes.forEach(cliente => {

            const option = document.createElement("option");

            option.value = cliente.id;
            option.textContent = cliente.nome;

            select.appendChild(option);

        });

    } catch (error) {
        console.error("Erro ao carregar clientes:", error);
    }

}



/* ===============================
   📊 GRÁFICO DE CONSUMO
================================ */
async function carregarGrafico(clienteId) {

    try {

        const response = await fetch(`/api/v1/analytics/crescimento/?cliente_id=${clienteId}`);

        if (!response.ok) throw new Error("Erro ao carregar gráfico");

        const data = await response.json();

        const labels = data.map(item => item.mes);
        const valores = data.map(item => parseFloat(item.consumo));

        const canvas = document.getElementById("graficoConsumo");

        if (!canvas) return;

        const ctx = canvas.getContext("2d");

        if (grafico) grafico.destroy();

        grafico = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Consumo (kWh)",
                    data: valores,
                    borderColor: "#38bdf8",
                    backgroundColor: "rgba(56,189,248,0.2)",
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });

    } catch (error) {
        console.error("Erro ao carregar gráfico:", error);
    }

}