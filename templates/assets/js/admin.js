const arrow = document.querySelectorAll(".arrow");
const sidebar = document.querySelector(".sidebar");
const mainWidth = document.querySelector(".main");
const sidebarBtn = document.querySelector(".bx-menu");


for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
        arrowParent.classList.toggle("showMenu");
    });
}
sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    mainWidth.classList.toggle('main-width');
    mainWidth.classList.toggle('main-show');
});

// chartjs start

var ctx = document.getElementById('lineChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jun', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Earnings in $',
            data: [4500,3486,1546,4900,2020,3210,4022,4500,3486,1546,4900,2020],
            backgroundColor: [
                'rgba(54,162,235,1)'
            ],
            borderColor: [
                'rgba(54,162,235,1)'
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
                'rgba(54,162,235,1)',
                'rgba(255,206,86,1)',
                'rgba(120,46,139,1)'
            ],
            borderColor: [
                'rgba(41,155,99,1)',
                'rgba(54,162,235,1)',
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