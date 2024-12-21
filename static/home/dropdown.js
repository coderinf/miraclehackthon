// Get the dropdown buttons and contents
var dropdownButtons = document.querySelectorAll(".dropdown-button");
var dropdownContents = document.querySelectorAll(".dropdown-content");

// Loop through the dropdown buttons
dropdownButtons.forEach(function(button, index) {
    // Add event listener to the dropdown button
    button.addEventListener("click", function() {
        // Hide all dropdown contents
        dropdownContents.forEach(function(content) {
            content.classList.remove("show");
        });

        // Show the corresponding dropdown content
        dropdownContents[index].classList.toggle("show");
    });
});

// Add event listener to the window to close the dropdown content when clicking outside
window.addEventListener("click", function(event) {
    if (!event.target.matches(".dropdown-button")) {
        dropdownContents.forEach(function(content) {
            if (content.classList.contains("show")) {
                content.classList.remove("show");
            }
        });
    }
});
const candleChartContainer = document.querySelector('.candle-chart-container');
const candleChartCanvas = document.getElementById('candle-chart-canvas');
const ctx = candleChartCanvas.getContext('2d');

let candles = [];
let candleWidth = 10;
let candleSpacing = 2;
let chartWidth = candleChartCanvas.width;
let chartHeight = candleChartCanvas.height;
let animationSpeed = 2;

function initCandles() {
  for (let i = 0; i < 6; i++) { // Decreased number of candles
    let candleX = Math.random() * chartWidth;
    let candleY = Math.random() * chartHeight;
    let candleHeight = Math.random() * 50 + 20;
    let candleColor = Math.random() < 0.5 ? 'red' : 'green';
    let wickHeight = Math.random() * 20 + 10;
    candles.push({ x: candleX, y: candleY, height: candleHeight, color: candleColor, wickHeight: wickHeight });
  }
}

function drawCandles() {
  ctx.clearRect(0, 0, chartWidth, chartHeight);
  for (let i = 0; i < candles.length; i++) {
    ctx.fillStyle = candles[i].color;
    ctx.fillRect(candles[i].x, candles[i].y, candleWidth, candles[i].height);
    ctx.fillStyle = 'black';
    ctx.fillRect(candles[i].x + candleWidth / 2, candles[i].y - candles[i].wickHeight, 2, candles[i].wickHeight);
  }
}

function animateCandles() {
  for (let i = 0; i < candles.length; i++) {
    candles[i].y += 1;
    if (candles[i].y > chartHeight) {
      candles[i].y = -candles[i].height;
      candles[i].x = Math.random() * chartWidth;
    }
  }
  drawCandles();
  requestAnimationFrame(animateCandles);
}

initCandles();
animateCandles();

// Animate the candle chart container
let containerY = -candleChartContainer.offsetHeight;
function animateContainer() {
  containerY += 2;
  candleChartContainer.style.top = `${containerY}px`;
  if (containerY > window.innerHeight) {
    containerY = -candleChartContainer.offsetHeight;
  }
  requestAnimationFrame(animateContainer);
}
animateContainer();
