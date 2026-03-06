async function carregarRanking(){

    const response = await fetch("/api/v1/analytics/top-consumers/?limit=10");
    const data = await response.json();

    const container = document.getElementById("ranking");

    const medalhas = ["🥇","🥈","🥉"];

    data.forEach((cliente,index)=>{

        const medalha = medalhas[index] || `#${index+1}`;

        const card = document.createElement("div");
        card.className="card";

        card.innerHTML = `
        <div class="rank">${medalha} ${cliente.cliente__nome}</div>
        <div class="consumo">${cliente.consumo_total} kWh</div>
        `;

        container.appendChild(card);

    });

}

document.addEventListener("DOMContentLoaded", carregarRanking);