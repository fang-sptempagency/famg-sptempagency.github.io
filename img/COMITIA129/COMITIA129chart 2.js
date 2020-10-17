    new Chart(document.getElementById("myChart"), {
    type: "bar",
    data: {
        labels: ['11時', '12時', '13時', '14時', '15時'],
        datasets: [{
            data: [5, 7, 3, 4, 1],
            backgroundColor: "rgb(250,128,0)",
            borderColor:"rgb(250,128,0)",
            borderWidth:1
        }]
    },
    options: {
        responsive: true,
        legend: {
            display: false
        },
        title: {
            display: false
        },
        scales: {
            yAxes: [{
                display: true,
                scaleLabel:{
                    display: true,
                    labelString: '来場者数',
                    fontSize:14,
                    fontColor:"black"
                },
                ticks: {
                    min: 0,
                    max: 10,
                    stepSize:2,
                    fontColor:"black"
                }
            }],
            xAxes: [{
                display: true,
                scaleLabel:{
                    display: true,
                    labelString: '時間帯',
                    fontSize:14,
                    fontColor:"black"
                },
                gridLines:{                   display:true},
                ticks:{
                    fontColor:"black"
                }
            }]
        }
    }
});