// chartjs start

var ctx = document.getElementById('lineChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jun', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Foyda in $',
            data: [4500,3486,1546,4900,2020,3210,4022,4500,3486,1546,4900,2020],
            backgroundColor: [
                '#1788EF'
            ],
            borderColor: [
                '#1788EF'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});

var ctx2 = document.getElementById('doughnut').getContext('2d');
var myChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Offline Users', 'Online Users', 'Offline Admins', 'Online Admins'],
        datasets: [{
            label: 'Users',
            data: [42,54,5,4],
            backgroundColor: [
                'rgba(41,155,99,1)',
                '#1788EF',
                'rgba(255,206,86,1)',
                'rgba(120,46,139,1)'
            ],
            borderColor: [
                'rgba(41,155,99,1)',
                '#1788EF',
                'rgba(255,206,86,1)',
                'rgba(120,46,139,1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});

// chartjs end