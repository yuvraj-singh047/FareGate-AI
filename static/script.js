// FareGate - Client Side Interactions

const sourceEl = document.getElementById("source");
const destEl = document.getElementById("destination");
const depEl = document.getElementById("dep_time");
const arrEl = document.getElementById("arr_time");

const stubFrom = document.getElementById("stubFrom");
const stubTo = document.getElementById("stubTo");
const stubDuration = document.querySelector(".stub-duration");

const form = document.getElementById("boardingPassForm");
const predictBtn = document.querySelector(".predict-btn");

// ----------------------------
// Update Route Preview
// ----------------------------
function updateRoute() {
    stubFrom.textContent = sourceEl.value || "--";
    stubTo.textContent = destEl.value || "--";
}

sourceEl.addEventListener("change", updateRoute);
destEl.addEventListener("change", updateRoute);

// ----------------------------
// Calculate Flight Duration
// ----------------------------
function updateDuration() {

    if (!depEl.value || !arrEl.value) {
        stubDuration.innerHTML = "Duration —";
        return;
    }

    let [dh, dm] = depEl.value.split(":").map(Number);
    let [ah, am] = arrEl.value.split(":").map(Number);

    let departure = dh * 60 + dm;
    let arrival = ah * 60 + am;

    // Next day arrival
    if (arrival < departure) {
        arrival += 24 * 60;
    }

    const total = arrival - departure;

    const hours = Math.floor(total / 60);
    const minutes = total % 60;

    stubDuration.innerHTML = `Duration ${hours}h ${minutes}m`;
}

depEl.addEventListener("change", updateDuration);
arrEl.addEventListener("change", updateDuration);

// ----------------------------
// Form Validation
// ----------------------------
form.addEventListener("submit", function (e) {

    if (sourceEl.value === destEl.value) {
        e.preventDefault();
        alert("Source and Destination cannot be the same.");
        return;
    }

    predictBtn.disabled = true;

    predictBtn.innerHTML = `
        <span class="btn-label">PREDICTING...</span>
    `;
});

// Initial Preview
updateRoute();
updateDuration();