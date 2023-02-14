prfImg.addEventListener("click", ()=>{
    box.classList.toggle("active");
})

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

