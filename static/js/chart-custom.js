var userchart = {
    chart: {
        height: 500,
        type: "bar",
        fontFamily: "Inter, sans-serif",
        zoom: {
            enabled: false,
        },
        toolbar: {
            show: false,
        },
    },
    plotOptions: {
        bar: {
            horizontal: false,
            endingShape: "rounded",
            columnWidth: "50%",
            borderRadius: 5,
        },
    },
    stroke: {
        show: true,
        width: 4,
        colors: ["transparent"],
    },
    colors: ["rgba(123, 106, 254, .4)", "#7B6AFE"],
    series: [
        {
            name: "Actual",
            data: calificacion_js.map(item => item.calificacion).map(num => Number(num.toFixed(2))),
        },
    ],
    dataLabels: {
        enabled: false,
    },
    legend: {
        show: false,
    },
    labels: calificacion_js.map(item => item.nombre_formulario),
    xaxis: {
        axisBorder: {
            show: false,
        },
        axisTicks: {
            show: false,
        },
        crosshairs: {
            show: true,
        },
        labels: {
            style: {
                fontSize: "12px",
                fontWeight: "600",
                colors: "#7780A1",
                cssClass: "apexcharts-xaxis-title",
            },
        },
        minHeight: 100,
    },
    yaxis: {
        show: true, // Enable the y-axis labels
        min: 0,     // Set the minimum value of the y-axis to 0
        max: maxCalificacion,    // Set the maximum value of the y-axis to 10
        tickAmount: 10, // Ensure there are 10 intervals (0-10)
        labels: {
            formatter: function (val) {
                return Math.round(val); // Format the labels to show integers
            },
            style: {
                fontSize: "12px",
                fontWeight: "600",
                colors: "#7780A1",
            },
        },
    },
    fill: { opacity: 1 },
    grid: {
        borderColor: "#e0e6ed",
        strokeDashArray: 7,
        padding: {
            bottom: 150, // Increase space between the chart and x-axis labels
        },
    },
    tooltip: {
        y: {
            formatter: function (e) {
                return "" + e;
            },
        },
    },
};

var chart = new ApexCharts(
    document.querySelector("#cal_actual_anterior"),
    userchart
);
chart.render();
