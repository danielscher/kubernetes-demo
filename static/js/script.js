// retrieve new advice from the server every 3 seconds.
function getAdvice() {
    document.getElementById("text").classList.remove("fade-out");
    document.getElementById("text").style.opacity = 0;
    fetch("/get_advice")
    .then(response => response.json())
    .then(data => {
        document.getElementById("advice").innerText = data.advice;
        document.getElementById("rand_id").innerText = "Tip #" + data.number;
        document.getElementById("text").classList.add("fade-in");

        setTimeout(function (){
            document.getElementById("text").classList.remove("fade-in");
            document.getElementById("text").style.opacity = 1;
            document.getElementById("text").classList.add("fade-out");
        },7600);
    });
}

getAdvice();
setInterval(getAdvice, 10000);