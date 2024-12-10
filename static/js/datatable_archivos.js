window.dataTable = function () {
	return {
		items: [],
		searchInput: "",
		sorted: {
			field: "filename",
			rule: "asc",
		},
		initData() {
			this.items = data.sort(this.compareOnKey("filename", "asc"));
		},
		compareOnKey(key, rule) {
			return function (a, b) {
				if (key === "filename" || key === "uploaded_at") {
					let comparison = 0;
					const fieldA = a[key].toUpperCase();
					const fieldB = b[key].toUpperCase();
					if (rule === "asc") {
						if (fieldA > fieldB) {
							comparison = 1;
						} else if (fieldA < fieldB) {
							comparison = -1;
						}
					} else {
						if (fieldA < fieldB) {
							comparison = 1;
						} else if (fieldA > fieldB) {
							comparison = -1;
						}
					}
					return comparison;
				}
			};
		},
		search(value) {
			if (value.length > 1) {
				const options = {
					shouldSort: true,
					keys: ["filename"],
					threshold: 0,
				};
				const fuse = new Fuse(data, options);
				this.items = fuse.search(value).map((elem) => elem.item);
			} else {
				this.items = data;
			}
		},
		sort(field, rule) {
			this.items = this.items.sort(this.compareOnKey(field, rule));
			this.sorted.field = field;
			this.sorted.rule = rule;
		},
	};
};
