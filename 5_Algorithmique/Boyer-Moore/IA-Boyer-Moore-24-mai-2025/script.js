function badCharHeuristic(str, size) {
  const badChar = new Array(256).fill(-1);
  for (let i = 0; i < size; i++) {
    badChar[str.charCodeAt(i)] = i;
  }
  return badChar;
}

let animationData = [];
let currentStep = 0;
let text = '';
let pattern = '';

function prepareAnimation(text, pattern) {
  const m = pattern.length;
  const n = text.length;
  const badChar = badCharHeuristic(pattern, m);
  let s = 0;
  const steps = [];

  while (s <= (n - m)) {
    let j = m - 1;
    let comparisons = [];

    while (j >= 0 && pattern[j] === text[s + j]) {
      comparisons.unshift({ pos: s + j, char: text[s + j], match: true });
      j--;
    }

    if (j >= 0) {
      comparisons.unshift({ pos: s + j, char: text[s + j], match: false });
    }

    steps.push({
      shift: s,
      comparisons: comparisons,
      match: j < 0
    });

    if (j < 0) {
      s += (s + m < n) ? m - badChar[text.charCodeAt(s + m)] || 1 : 1;
    } else {
      s += Math.max(1, j - badChar[text.charCodeAt(s + j)] || 1);
    }
  }

  return steps;
}

function showStep(stepIndex) {
  const visual = document.getElementById("visual");
  const log = document.getElementById("log");
  const step = animationData[stepIndex];

  let line1 = '';
  let line2 = '';
  let line3 = '';

  for (let i = 0; i < text.length; i++) {
    // Ligne 1 : texte de base
    line1 += `<span class="char">${text[i]}</span>`;

    // Ligne 2 : motif aligné ou vide
    if (i >= step.shift && i < step.shift + pattern.length) {
      line2 += `<span class="char pattern">${pattern[i - step.shift]}</span>`;
    } else {
      line2 += `<span class="char"> </span>`;
    }

    // Ligne 3 : correspondances et erreurs
    const cmp = step.comparisons.find(c => c.pos === i);
    if (cmp) {
      if (cmp.match) {
        line3 += `<span class="char match">^</span>`;
      } else {
        line3 += `<span class="char mismatch">x</span>`;
      }
    } else {
      line3 += `<span class="char"> </span>`;
    }
  }

  visual.innerHTML = `${line1}<br>${line2}<br>${line3}`;
  log.innerHTML = `<b>Étape ${stepIndex + 1} / ${animationData.length}</b><br>` +
    (step.match ? `✔ Motif trouvé à la position ${step.shift}` : `✘ Pas de correspondance, décalage`);
}

function initManual() {
  text = document.getElementById("text").value;
  pattern = document.getElementById("pattern").value;

  if (!text || !pattern) {
    alert("Veuillez saisir un texte et un motif.");
    return;
  }

  animationData = prepareAnimation(text, pattern);
  currentStep = 0;
  showStep(currentStep);
}

function nextStep() {
  if (animationData.length === 0) return;
  if (currentStep < animationData.length - 1) {
    currentStep++;
    showStep(currentStep);
  }
}

function prevStep() {
  if (animationData.length === 0) return;
  if (currentStep > 0) {
    currentStep--;
    showStep(currentStep);
  }
}