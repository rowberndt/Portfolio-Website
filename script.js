'use strict';

// Deterministic 2 -> 3 -> 3 forward pass with illustrative weights.
// This is not a trained classifier or a project performance claim.
function forwardPass(x1, x2) {
  const hidden = [Math.max(0, x1 * 1.2 + x2 * -0.4 + 0.2), Math.max(0, x1 * -0.6 + x2 * 1.1 + 0.3), Math.max(0, x1 * 0.7 + x2 * 0.8 + 0.1)];
  const logits = [hidden[0] * 1.1 - hidden[1] * 0.3 + hidden[2] * 0.2, -hidden[0] * 0.4 + hidden[1] * 1.3 + hidden[2] * 0.1, hidden[0] * 0.2 + hidden[1] * 0.1 + hidden[2] * 1.2];
  const max = Math.max(...logits);
  const exp = logits.map(value => Math.exp(value - max));
  const sum = exp.reduce((total, value) => total + value, 0);
  return { hidden, probabilities: exp.map(value => value / sum) };
}

const inputs = [document.querySelector('#input-one'), document.querySelector('#input-two')];
if (inputs.every(Boolean)) {
  const letters = ['a', 'b', 'c'];
  const outputs = [document.querySelector('#value-one'), document.querySelector('#value-two')];
  const circles = document.querySelectorAll('.output-nodes circle');
  const hiddenCircles = document.querySelectorAll('.hidden-nodes circle');
  function updateModel(announce = false) {
    const values = inputs.map(input => Number(input.value));
    values.forEach((value, index) => { outputs[index].value = value.toFixed(2); });
    const { hidden, probabilities } = forwardPass(...values);
    const winner = probabilities.indexOf(Math.max(...probabilities));
    letters.forEach((letter, index) => {
      const percent = (probabilities[index] * 100).toFixed(1);
      document.querySelector(`#prob-${letter}`).value = `${percent}%`;
      document.querySelector(`#bar-${letter}`).style.width = `${percent}%`;
      circles[index].classList.toggle('winner', index === winner);
      hiddenCircles[index].style.fillOpacity = String(0.35 + 0.65 * Math.min(hidden[index] / 2, 1));
    });
    if (announce) document.querySelector('#model-announcement').textContent = probabilities.map((value, index) => `Class ${letters[index].toUpperCase()}: ${(value * 100).toFixed(1)} percent`).join('. ');
  }
  document.querySelector('.demo-controls').hidden = false;
  inputs.forEach(input => {
    input.addEventListener('input', () => updateModel());
    input.addEventListener('change', () => updateModel(true));
  });
  updateModel();
}

const copyButton = document.querySelector('.copy-email');
if (copyButton && navigator.clipboard && window.isSecureContext) {
  copyButton.hidden = false;
  let resetTimer;
  copyButton.addEventListener('click', async () => {
    const status = document.querySelector('.copy-status');
    clearTimeout(resetTimer);
    try {
      await navigator.clipboard.writeText('row.berndt@gmail.com');
      status.textContent = 'Email copied';
    } catch {
      status.textContent = 'Select the email address to copy it.';
    }
    resetTimer = setTimeout(() => { status.textContent = ''; }, 4500);
  });
}
document.querySelectorAll('#year').forEach(element => { element.textContent = String(new Date().getFullYear()); });
