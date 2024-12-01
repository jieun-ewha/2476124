// 상품 상세페이지 - 상품 상태 글씨 색 제어 함수
document.addEventListener("DOMContentLoaded", function () {
    const statusElement = document.querySelector("#item-status span");
    const statusValue = statusElement.textContent.trim();

    if (statusValue === "매우 좋음") {
        statusElement.classList.add("green");
    } else if (statusValue == "좋음") {
        statusElement.classList.add("lightGreen")
    } else if (statusValue === "양호") {
        statusElement.classList.add("yellow");
    } else if (statusValue === "조금 별로") {
        statusElement.classList.add("orange");
    } else if (statusValue === "별로") {
        statusElement.classList.add("red");
    }
});
