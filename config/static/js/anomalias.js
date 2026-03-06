async function carregarAnomalias() {

    const clienteId = 1;

    const response = await fetch(`/api/v1/analytics/anomalias/?cliente_id=${clienteId}`);
    const data = await response.json();

    const container = document.getElementById("anomalias");

    container.innerHTML = "";

    data.forEach(item => {

        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <div class="cliente">${item.cliente__nome}</div>
            <div class="alerta">⚠ Consumo anormal</div>
            <div class="consumo">${item.consumo_kwh} kWh</div>
        `;

        container.appendChild(card);

    });

}

carregarAnomalias();