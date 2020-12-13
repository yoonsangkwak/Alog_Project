const menuBtn = document.querySelector('.menu-button');
const menu = document.querySelector('.menu');
const section = document.getElementById('section');
const clientRect = section.getBoundingClientRect(); // DomRect 구하기 (각종 좌표값이 들어있는 객체)
const relativeTop = clientRect.top; // Viewport의 시작지점을 기준으로한 상대좌표 Y 값.
const absoluteTop = window.pageYOffset + relativeTop; // 절대좌표

menuBtn.addEventListener("click", () => {
    menu.classList.toggle('on');
});

window.addEventListener("scroll", () => {
    if (pageYOffset >= absoluteTop) {
        menu.classList.remove('on');
    }
});