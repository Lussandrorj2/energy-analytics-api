const container = document.getElementById("anomalias");

fetch("/api/v1/analytics/anomalias/")
    .then(res => res.json())
    .then(data => {

        if (data.length === 0) {
            container.innerHTML = "<p>Nenhuma anomalia detectada.</p>";
            return;
        }

        data.forEach(item => {

            const row = document.createElement("div");

            row.style.display = "flex";
            row.style.justifyContent = "space-between";
            row.style.padding = "12px 0";
            row.style.borderBottom = "1px solid rgba(255,255,255,0.1)";

            row.innerHTML = `
<span>${item.cliente}</span>
<span>${item.mes}</span>
<span>${item.consumo_kwh} kWh</span>
<span>${item.tipo}</span>
`;

            container.appendChild(row);

        });

    });