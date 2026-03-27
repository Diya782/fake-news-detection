async function checkNews() {
    const text = document.getElementById("newsText").value.trim();
    const result = document.getElementById("result");
    const note = document.getElementById("note");
    const card = document.getElementById("resultCard");
    const bar = document.getElementById("confidenceBar");

    if (!text) {
        alert("Please enter some news text!");
        return;
    }

    result.innerText = "Analyzing... ⏳";
    note.innerText = "";
    card.classList.remove("hidden");
    bar.style.width = "0%";

    try {
        const response = await fetch("http://127.0.0.1:8001/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        result.innerText = data.prediction;
        note.innerText = data.note;

        // Extract confidence %
        const match = data.prediction.match(/\((.*?)%\)/);
        let confidence = match ? parseFloat(match[1]) : 0;

        bar.style.width = confidence + "%";

        if (data.prediction.includes("Fake")) {
            result.style.color = "#ef4444";
            bar.style.background = "linear-gradient(90deg, #ef4444, #f87171)";
        } else {
            result.style.color = "#22c55e";
            bar.style.background = "linear-gradient(90deg, #22c55e, #4ade80)";
        }

    } catch (error) {
        result.innerText = "⚠️ Server error";
        result.style.color = "#facc15";
    }
}