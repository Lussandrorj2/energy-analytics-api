async function carregarRanking(){

    try{

        const response = await fetch("/api/v1/analytics/top-consumers/");

        if(!response.ok){
            throw new Error("Erro ao carregar ranking");
        }

        const data = await response.json();

        const container = document.getElementById("ranking");

        if(!container) return;

        // limpa antes de adicionar
        container.innerHTML = "";

        const medalhas = ["🥇","🥈","🥉"];

        if(data.length === 0){

            container.innerHTML = "<p>Nenhum consumo registrado.</p>";
            return;

        }

        data.forEach((cliente,index)=>{

            const medalha = medalhas[index] || `#${index+1}`;

            const card = document.createElement("div");
            card.className="card";

            card.innerHTML = `
                <div class="rank">${medalha} ${cliente.cliente__nome}</div>
                <div class="consumo">${Number(cliente.consumo_total).toFixed(2)} kWh</div>
            `;

            container.appendChild(card);

        });

    }catch(error){

        console.error("Erro ao carregar ranking:", error);

    }

}

document.addEventListener("DOMContentLoaded", carregarRanking);