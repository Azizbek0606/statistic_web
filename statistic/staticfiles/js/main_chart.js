// document.addEventListener('DOMContentLoaded', function () {
//     var ctx = document.getElementById('second_chart').getContext('2d');
//     var myChart = new Chart(ctx, {
//         type: 'line',
//         data: {
//             labels: ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr'],
//             datasets: [{
//                 label: 'Har Kunlik Amal',
//                 data: [12, 20, 3, 7, 2, 20, 30],
//                 backgroundColor: 'rgba(0, 99, 132, 0.2)',
//                 borderColor: 'rgba(0, 99, 132, 1)',
//                 borderWidth: 1
//             }]
//         },
//         options: {
//             scales: {
//                 y: {
//                     beginAtZero: true
//                 }
//             }
//         }
//     });
// });
month_list = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
const url = "http://127.0.0.1:8000/api/daily/work"
fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const dateString = data[0].day_work;
        const date = new Date(dateString);
        const month = date.getMonth() + 1;
        const day = date.getDate();
        console.log(`Oy: ${month_list[month - 1]}, Kun: ${day}`);

    })
    .catch(error => {
        console.error('Sorry we have some problem with: ', error);
    });
