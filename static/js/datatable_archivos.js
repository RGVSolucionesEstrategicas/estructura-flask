window.dataTable = function () {
	return {
		items: [],
		initData() {
			this.fetchData();
		},
		fetchData() {
			fetch("/files/data")
				.then((response) => response.json())
				.then((data) => {
					if (data.error) {
						console.error("Error:", data.error);
					} else {
						this.items = data.sort(this.compareOnKey("uploaded_at", "desc"));
					}
				})
				.catch((error) => {
					console.error("Error al obtener los datos:", error);
				});
		},
		compareOnKey(key, rule) {
			return function (a, b) {
				let comparison = 0;
				const fieldA = a[key].toLowerCase();
				const fieldB = b[key].toLowerCase();
				if (rule === "asc") {
					comparison = fieldA > fieldB ? 1 : fieldA < fieldB ? -1 : 0;
				} else {
					comparison = fieldA < fieldB ? 1 : fieldA > fieldB ? -1 : 0;
				}
				return comparison;
			};
		},
	};
};
