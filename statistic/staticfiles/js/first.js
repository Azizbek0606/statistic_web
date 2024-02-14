let choose_block = document.querySelectorAll(".x_mark");
let main_block = document.querySelector(".main_block");
let main_toggler_btn = document.querySelector('.main_toggler_btn');
for (let i = 0; i < choose_block.length; i++) {
    choose_block[i].addEventListener("click", () => {
        main_toggler_btn.classList.toggle("active_choose")
        main_block.classList.toggle("active_menu")
    })
}
document.querySelector('.date').innerHTML = new Date().toDateString()
setInterval(() => {
    document.querySelector('.time').innerHTML = new Date().toLocaleTimeString()
}, 1000);