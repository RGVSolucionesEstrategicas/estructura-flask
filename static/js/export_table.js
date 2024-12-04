function exportTableToCSV(table) {
    alert('¡Se ha iniciado la descarga!');
    const csv = [];
    const rows = document.querySelectorAll("#"+table+ " tr");

    for (const row of rows) {
        const cols = row.querySelectorAll("td, th");
        const csvRow = [];
        for (const col of cols) {
            let colText = col.textContent.trim();
            // Escape any double quotes and wrap the content in double quotes if it contains a comma or double quote
            if (colText.includes(",") || colText.includes("\"")) {
                colText = `"${colText.replace(/"/g, '""')}"`;
            }
            csvRow.push(colText);
        }
        csv.push(csvRow.join(","));
    }

    // Create a Blob with UTF-8 encoding
    const blob = new Blob([`\ufeff${csv.join("\n")}`], {
        type: "text/csv;charset=utf-8;"
    });

    // Create a link element to trigger the download
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", table+'.csv');
    link.style.visibility = "hidden";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
