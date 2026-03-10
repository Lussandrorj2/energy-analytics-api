const container = document.getElementById("anomalias");

fetch("/api/v1/analytics/anomalias/")
    .then(res => res.json())
    .then(data => {
        // Limpa o container antes de inserir (evita duplicatas se a função rodar de novo)
        container.innerHTML = "";

        if (!data || data.length === 0) {
            container.innerHTML = "<p>Nenhuma anomalia detectada.</p>";
            return;
        }

        data.forEach(item => {
            const row = document.createElement("div");

            // Estilização da linha
            row.style.display = "flex";
            row.style.justifyContent = "space-between";
            row.style.padding = "12px 0";
            row.style.borderBottom = "1px solid rgba(255,255,255,0.1)";

            // Inserção dos dados baseados nos seus Models
            row.innerHTML = `
                <span>${item.cliente_nome || 'Cliente #' + item.cliente}</span>
                <span>${item.mes ? new Date(item.mes + "T00:00:00").toLocaleDateString('pt-BR', {month: 'long', year: 'numeric'}) : 'Sem data'}</span>
                <span>${item.consumo_kwh} kWh</span>
                <span style="color: #ff4d4d;">${item.tipo || 'Consumo Anormal'}</span>
            `;

            container.appendChild(row);
        });
    })
    .catch(err => {
        console.error("Erro ao buscar anomalias:", err);
        container.innerHTML = "<p>Erro ao carregar dados.</p>";
    });