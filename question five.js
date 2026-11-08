const questionNumber = 5;
const totalQuestions = 40;
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options');
const nextBtn = document.getElementById('next-btn');
const prevBtn = document.getElementById('prev-btn');
const progressCount = document.getElementById('progress-count');
const answerStatus = document.getElementById('answer-status');

const profile = JSON.parse(localStorage.getItem('brightIQProfile') || 'null') || {name: 'Player', group: '18+'};
document.getElementById('profile-name').textContent = profile.name;
const questionOrder = JSON.parse(localStorage.getItem('iqQuestionOrder') || 'null') || Array.from({length: totalQuestions}, (_, questionIndex) => questionIndex);
const questionBank = QUESTION_BANKS[profile.group] || QUESTION_BANKS['18+'];
const question = questionBank[questionOrder[questionNumber - 1]];

const storageKey = 'iqQuizAnswers';
const storedAnswers = JSON.parse(localStorage.getItem(storageKey) || '[]');
const answers = Array(totalQuestions).fill(null);
for (let i = 0; i < answers.length; i++) {
  answers[i] = storedAnswers[i] ?? null;
}

const previousPageName = 'four';
const nextPageName = 'six';
progressCount.textContent = answers.filter((answer) => answer !== null).length + ' answered';
if (answers[questionNumber - 1] !== null) answerStatus.textContent = 'Answer saved. You can change it before moving on.';

questionText.textContent = question.category + ": " + question.prompt;
question.options.forEach((option, index) => {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'option-btn';
  button.dataset.letter = String.fromCharCode(65 + index);
  button.textContent = option;
  button.setAttribute('aria-pressed', answers[questionNumber - 1] === index ? 'true' : 'false');
  if (answers[questionNumber - 1] === index) button.classList.add('selected');
  button.addEventListener('click', () => {
    answers[questionNumber - 1] = index;
    localStorage.setItem(storageKey, JSON.stringify(answers));
    document.querySelectorAll('.option-btn').forEach((btn) => {
      btn.classList.remove('selected');
      btn.setAttribute('aria-pressed', 'false');
    });
    button.classList.add('selected');
    button.setAttribute('aria-pressed', 'true');
    progressCount.textContent = answers.filter((answer) => answer !== null).length + ' answered';
    answerStatus.textContent = 'Answer saved. You can change it before moving on.';
  });
  optionsContainer.appendChild(button);
});

prevBtn.style.visibility = questionNumber === 1 ? 'hidden' : 'visible';
nextBtn.textContent = questionNumber === totalQuestions ? 'See Result' : 'Next';

prevBtn.addEventListener('click', () => {
  if (questionNumber > 1) {
    window.location.href = 'question ' + previousPageName + '.html';
  }
});

nextBtn.addEventListener('click', () => {
  if (questionNumber < totalQuestions) {
    window.location.href = 'question ' + nextPageName + '.html';
  } else {
    window.location.href = 'result.html';
  }
});
