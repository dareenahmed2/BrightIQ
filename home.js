const profileForm = document.getElementById('profile-form');
const nameInput = document.getElementById('player-name');
const ageInput = document.getElementById('player-age');
const ageHint = document.getElementById('age-hint');

function getAgeGroup(age) {
  if (age <= 7) return '4-7';
  if (age <= 12) return '8-12';
  if (age <= 17) return '13-17';
  return '18+';
}

function updateAgeHint() {
  const age = Number(ageInput.value);
  if (!ageInput.value || age < 4 || age > 120) {
    ageHint.textContent = 'Your age helps choose a suitable question level.';
    return;
  }
  const hints = {
    '4-7': 'Age group 4–7: simple statements about activities and interests.',
    '8-12': 'Age group 8–12: age-appropriate statements about activities and interests.',
    '13-17': 'Age group 13–17: age-appropriate statements about learning and interests.',
    '18+': 'Age group 18+: reflective statements about learning and interests.'
  };
  ageHint.textContent = hints[getAgeGroup(age)];
}

ageInput.addEventListener('input', updateAgeHint);
profileForm.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!profileForm.reportValidity()) return;

  const profile = {
    name: nameInput.value.trim(),
    age: Number(ageInput.value),
    group: getAgeGroup(Number(ageInput.value))
  };
  if (!profile.name || profile.age < 4 || profile.age > 120) return;

  const questionOrder = Array.from({length: 40}, (_, index) => index);
  for (let index = questionOrder.length - 1; index > 0; index--) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [questionOrder[index], questionOrder[swapIndex]] = [questionOrder[swapIndex], questionOrder[index]];
  }
  const previousOrder = JSON.parse(localStorage.getItem('iqQuestionOrder') || 'null');
  if (Array.isArray(previousOrder) && previousOrder.length === 40 && questionOrder.every((questionIndex, index) => questionIndex === previousOrder[index])) {
    [questionOrder[0], questionOrder[1]] = [questionOrder[1], questionOrder[0]];
  }

  localStorage.setItem('brightIQProfile', JSON.stringify(profile));
  localStorage.setItem('iqQuestionOrder', JSON.stringify(questionOrder));
  localStorage.setItem('iqQuizAnswers', JSON.stringify(Array(40).fill(null)));
  window.location.href = 'question one.html';
});
