document.getElementById("fetch-discounts").addEventListener("click", () => {
    fetch("/api/scraper")
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = ""; // Limpiar resultados anteriores

            data.forEach(product => {
                const productDiv = document.createElement("div");
                productDiv.classList.add("product");

                productDiv.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Precio: ${product.price}</p>
                    <a href="${product.url}" target="_blank">Ver producto</a>
                `;

                resultsDiv.appendChild(productDiv);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});
