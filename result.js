const topDomainEl = document.getElementById('top-domain');
const topScoreEl = document.getElementById('top-score');
const textEl = document.getElementById('result-text');
const resultsEl = document.getElementById('intelligence-results');
const restartBtn = document.getElementById('restart-btn');

const profile = JSON.parse(localStorage.getItem('brightIQProfile') || 'null') || {name: 'Player', group: '18+'};
document.getElementById('profile-name').textContent = profile.name;
const questionOrder = JSON.parse(localStorage.getItem('iqQuestionOrder') || 'null') || Array.from({length: 40}, (_, index) => index);
const questionBank = QUESTION_BANKS[profile.group] || QUESTION_BANKS['18+'];
const questions = questionOrder.map((questionIndex) => questionBank[questionIndex]);
const raw = localStorage.getItem('iqQuizAnswers');
const answers = raw ? JSON.parse(raw) : Array(40).fill(null);

const domainScores = new Map(intelligenceDomains.map((domain) => [domain, {total: 0, answered: 0}]));
answers.forEach((answer, index) => {
  if (answer === null || !questions[index]) return;
  const score = domainScores.get(questions[index].category);
  if (!score) return;
  score.total += answer;
  score.answered += 1;
});

const rankedDomains = intelligenceDomains
  .map((domain) => {
    const score = domainScores.get(domain);
    const percentage = score.answered ? Math.round((score.total / (score.answered * 3)) * 100) : 0;
    return {domain, percentage, answered: score.answered};
  })
  .sort((left, right) => right.percentage - left.percentage);

const answeredDomains = rankedDomains.filter(({answered}) => answered > 0);
const topPercentage = answeredDomains.length ? answeredDomains[0].percentage : 0;
const strongestDomains = answeredDomains.filter(({percentage}) => percentage === topPercentage);

if (strongestDomains.length) {
  const domainNames = strongestDomains.map(({domain}) => domain);
  topDomainEl.textContent = domainNames.join(', ');
  topScoreEl.textContent = `${topPercentage}% interest match`;
  textEl.textContent = strongestDomains.length === 1
    ? `Based on your answers, your strongest intelligence type is ${domainNames[0]}.`
    : `Based on your answers, your strongest intelligence types are ${domainNames.join(' and ')}.`;
} else {
  topDomainEl.textContent = 'No responses yet';
  topScoreEl.textContent = 'Answer some questions to see your profile.';
  textEl.textContent = 'Your answers will show which types of intelligence match your interests and preferred ways of learning.';
}

rankedDomains.forEach(({domain, percentage, answered}) => {
  const row = document.createElement('div');
  row.className = 'domain-result';
  const label = document.createElement('span');
  label.textContent = domain;
  const bar = document.createElement('div');
  bar.className = 'domain-bar';
  bar.setAttribute('role', 'progressbar');
  bar.setAttribute('aria-label', `${domain} interest match`);
  bar.setAttribute('aria-valuemin', '0');
  bar.setAttribute('aria-valuemax', '100');
  bar.setAttribute('aria-valuenow', String(percentage));
  const fill = document.createElement('span');
  fill.style.width = `${percentage}%`;
  bar.appendChild(fill);
  const value = document.createElement('span');
  value.className = 'domain-score';
  value.textContent = answered ? `${percentage}%` : '—';
  row.append(label, bar, value);
  resultsEl.appendChild(row);
});

restartBtn.addEventListener('click', () => {
  localStorage.setItem('iqQuizAnswers', JSON.stringify(Array(40).fill(null)));
  window.location.href = 'index.html';
});
