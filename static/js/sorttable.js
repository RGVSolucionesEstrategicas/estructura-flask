function sortTable(id,n) {
    const table = document.getElementById(id);
    const tbody = table.getElementsByTagName("tbody")[0];
    const rows = Array.from(tbody.rows);
    const isAscending = table.getAttribute('data-sort-order') !== 'asc';
    rows.sort((a, b) => {
        const aText = a.cells[n].innerText;
        const bText = b.cells[n].innerText;
        if (!isNaN(aText) && !isNaN(bText)) {
            return isAscending ? aText - bText : bText - aText;
        }
        return isAscending ? aText.localeCompare(bText) : bText.localeCompare(aText);
    });
    rows.forEach(row => tbody.appendChild(row));
    table.setAttribute('data-sort-order', isAscending ? 'asc' : 'desc');
}