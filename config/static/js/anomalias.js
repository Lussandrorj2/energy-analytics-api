async function carregarAnomalias() {

    const response = await fetch("/api/v1/analytics/anomalias/");
    const data = await response.json();

    const container = document.getElementById("anomalias");

    if (!container) return;

    container.innerHTML = "";

    if (data.length === 0) {

        container.innerHTML = "<p>Nenhuma anomalia detectada.</p>";
        return;

    }

    data.forEach(item => {

        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <div class="cliente">${item.cliente}</div>
            <div class="alerta">⚠ Consumo anormal</div>
            <div class="consumo">${item.consumo_kwh} kWh</div>
        `;

        container.appendChild(card);

    });

}

document.addEventListener("DOMContentLoaded", carregarAnomalias);