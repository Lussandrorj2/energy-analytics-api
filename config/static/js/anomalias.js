async function carregarAnomalias() {

    try {

        const response = await fetch("/api/v1/analytics/anomalias/");

        if (!response.ok) {
            throw new Error("Erro ao carregar anomalias");
        }

        const data = await response.json();

        const container = document.getElementById("anomalias");

        if (!container) return;

        container.innerHTML = "";

        if (!data || data.length === 0) {

            container.innerHTML = "<p>Nenhuma anomalia detectada.</p>";
            return;

        }

        data.forEach(item => {

            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
                <div class="cliente">${item.cliente}</div>
                <div class="alerta">⚠ ${item.tipo}</div>
                <div class="consumo">${Number(item.consumo_kwh).toFixed(2)} kWh</div>
            `;

            container.appendChild(card);

        });

    } catch (error) {

        console.error("Erro ao carregar anomalias:", error);

        const container = document.getElementById("anomalias");

        if (container) {
            container.innerHTML = "<p>Erro ao carregar anomalias.</p>";
        }

    }

}

document.addEventListener("DOMContentLoaded", carregarAnomalias);