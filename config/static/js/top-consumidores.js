const container = document.getElementById("ranking");

fetch("/api/v1/analytics/top-consumidores/")
    .then(res => res.json())
    .then(data => {

        data.forEach((cliente, index) => {

            const item = document.createElement("div");

            item.style.display = "flex";
            item.style.justifyContent = "space-between";
            item.style.padding = "12px 0";
            item.style.borderBottom = "1px solid rgba(255,255,255,0.1)";

            item.innerHTML = `
<span>${index + 1}º ${cliente.nome}</span>
<span>${cliente.consumo} kWh</span>
`;

            container.appendChild(item);

        });

    });