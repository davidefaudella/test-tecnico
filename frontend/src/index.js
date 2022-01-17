function resetStatus() {
  document.getElementById("title").innerText = "INSERT INPUT";
  document.getElementById("receipt").style.display = "none";
  document.getElementById("input-area").value = "";
  document.getElementById("input-area").style.display = "block";
  document.getElementById("print-button").style.display = "block";
  document.getElementById("print-button").textContent = "PRINT RECEIPT";
}

function receiptStatus() {
  document.getElementById("title").innerText = "RECEIPT DETAILS";
  document.getElementById("receipt").style.display = "block";
  document.getElementById("input-area").style.display = "none";
  document.getElementById("print-button").textContent = "CANCEL";
}

function getInput(button) {
  let array_inputs = Array(
    "2 book at 12.49" +
      "\n" +
      "1 music CD at 14.99" +
      "\n" +
      "1 chocolate bar at 0.85",
    "1 imported box of chocolates at 10.00" +
      "\n" +
      "1 imported bottle of perfume at 47.50",
    "1 imported bottle of perfume at 27.99" +
      "\n" +
      "1 bottle of perfume at 18.99" +
      "\n" +
      "1 packet of headache pills at 9.75" +
      "\n" +
      "3 box of imported chocolates at 11.25"
  );
  resetStatus();
  document.getElementById("input-area").value =
    array_inputs[button.textContent.split(" ")[1] - 1];
}

function printReceipt(button) {
  let input_data = document.getElementById("input-area").value;
  if (button.textContent.includes("CANCEL")) {
    resetStatus();
    return;
  }
  fetch("http://127.0.0.1:5000/api/v1/receipts", {
    method: "POST",
    headers: {
      Accept: "text/plain",
      "Content-Type": "text/plain",
    },
    body: input_data,
  })
    .then((res) => res.text())
    .then((res) => {
      document.getElementById("receipt").innerText = res;
      receiptStatus();
    });
}

document.addEventListener("DOMContentLoaded", (event) => {
  resetStatus();
});
