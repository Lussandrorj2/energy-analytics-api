let grafico = null;
let graficoClientes = null;

document.addEventListener("DOMContentLoaded", function () {

    carregarClientes();
    carregarTopConsumers();
    carregarGraficoClientes();

    carregarResumo("geral");
    carregarGrafico("geral");
    carregarCrescimento("geral");

    /* ===============================
       EVENTO SELECT CLIENTE
    =============================== */
    const clienteSelect = document.getElementById("clienteSelect");

    if (clienteSelect) {

        clienteSelect.addEventListener("change", function () {

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

    }

    /* ===============================
       EVENTO SELECT PERÍODO
    =============================== */

    const periodoSelect = document.getElementById("periodoSelect");

    if (periodoSelect) {

        periodoSelect.addEventListener("change", function () {

            const clienteId = document.getElementById("clienteSelect").value;

            if (clienteId === "geral") {
                carregarGrafico("geral");
            } else {
                carregarGrafico(Number(clienteId));
            }

        });

    }

});


/* ===============================
   📊 MÉTRICAS
================================ */
async function carregarResumo(clienteId = "geral") {

    const response = await fetch(`/api/v1/analytics/resumo-geral/?cliente=${clienteId}`);
    const data = await response.json();

    document.getElementById("totalClientes").innerText = data.total_clientes;

    document.getElementById("totalConsumo").innerText =
        Number(data.total_consumo_geral).toFixed(2) + " kWh";

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
            elemento.innerText = "Sem dados";
            return;
        }

        const data = await response.json();

        if (data.crescimento_percentual !== undefined) {
            elemento.innerText = data.crescimento_percentual + " %";
        } else {
            elemento.innerText = "Sem dados";
        }

    } catch (error) {
        console.error(error);
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
        console.error(error);
    }

}


/* ===============================
   👥 CARREGAR CLIENTES
================================ */
async function carregarClientes() {

    try {

        const response = await fetch("/api/v1/clientes/");

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
        console.error(error);
    }

}


/* ===============================
   📊 GRÁFICO TOTAL POR CLIENTE
================================ */
async function carregarGraficoClientes() {

    const response = await fetch("/api/v1/analytics/consumo-clientes/");
    const data = await response.json();

    const labels = data.map(item => item.cliente__nome);
    const valores = data.map(item => item.total);

    const ctx = document.getElementById("graficoClientes").getContext("2d");

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


/* ===============================
   📈 GRÁFICO CONSUMO
================================ */
async function carregarGrafico(clienteId) {

    try {

        const periodoSelect = document.getElementById("periodoSelect");

        let periodo = periodoSelect ? periodoSelect.value : "todos";

        if (periodo === "todos") {
            periodo = "";
        }

        const response = await fetch(
            `/api/v1/analytics/crescimento/?cliente_id=${clienteId}&periodo=${periodo}`
        );

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
        console.error(error);
    }

}