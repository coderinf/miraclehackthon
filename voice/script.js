const voiceButton = document.getElementById('voiceButton');
const stopButton = document.getElementById('stopButton');
const waveIndicator = document.getElementById('waveIndicator');
const textOutput = document.getElementById('textOutput');

// Check if the browser supports Speech Recognition
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.continuous = true;  // Keep recording until manually stopped
    recognition.interimResults = true;  // Show results as they are being spoken

    voiceButton.addEventListener('click', () => {
        // Start recording when voice button is clicked
        recognition.start();
        voiceButton.classList.add('hidden');
        stopButton.classList.remove('hidden');
        waveIndicator.classList.remove('hidden');
    });

    stopButton.addEventListener('click', () => {
        // Stop recording when stop button is clicked
        recognition.stop();
        voiceButton.classList.remove('hidden');
        stopButton.classList.add('hidden');
        waveIndicator.classList.add('hidden');
    });

    // Capture speech as text
    recognition.onresult = function(event) {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
            transcript += event.results[i][0].transcript;
        }
        textOutput.textContent = transcript;
    };

    // Handle the end of recognition
    recognition.onend = function() {
        voiceButton.classList.remove('hidden');
        stopButton.classList.add('hidden');
        waveIndicator.classList.add('hidden');
    };

    // Handle errors
    recognition.onerror = function(event) {
        console.error('Speech recognition error', event.error);
        voiceButton.classList.remove('hidden');
        stopButton.classList.add('hidden');
        waveIndicator.classList.add('hidden');
    };
} else {
    alert("Your browser doesn't support Speech Recognition API.");
}
