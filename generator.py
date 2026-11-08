import json
import os
from math import gcd

root = r"c:\Users\DAREEN\isef"
os.chdir(root)

questions = [
    {"prompt": "What number completes the sequence: 2, 4, 8, 16, ?", "options": ["24", "28", "32", "64"], "correct": 3},
    {"prompt": "Which word does not belong?", "options": ["Pencil", "Book", "Library", "Eraser"], "correct": 2},
    {"prompt": "If each square equals 3 and each circle equals 2, what is square + circle?", "options": ["5", "6", "7", "8"], "correct": 0},
    {"prompt": "Which number completes the pattern: 5, 10, 20, 40, ?", "options": ["60", "70", "80", "90"], "correct": 2},
    {"prompt": "Which animal does not belong?", "options": ["Tiger", "Lion", "Wolf", "Whale"], "correct": 3},
    {"prompt": "If the time is 3:15, what is the angle between the hour and minute hands?", "options": ["30°", "45°", "52.5°", "67.5°"], "correct": 2},
    {"prompt": "Choose the word closest in meaning to 'conclusion'.", "options": ["Guess", "Inference", "Result", "Lock"], "correct": 1},
    {"prompt": "Bird : Wing :: Fish : ?", "options": ["Tail", "Fin", "Muzzle", "Shark"], "correct": 1},
    {"prompt": "What number completes the sequence: 9, 7, 10, 8, 11, ?", "options": ["9", "10", "12", "13"], "correct": 2},
    {"prompt": "What is the opposite of 'fast'?", "options": ["Slow", "Strong", "Bright", "Silent"], "correct": 0},
    {"prompt": "If each letter equals its alphabet position, what is B + A?", "options": ["3", "4", "5", "6"], "correct": 2},
    {"prompt": "Which number does not fit: 1, 4, 9, 16, 25, 27?", "options": ["9", "16", "25", "27"], "correct": 3},
    {"prompt": "Which word means 'optimistic'?", "options": ["Sad", "Hopeful", "Anxious", "Depressed"], "correct": 1},
    {"prompt": "If 3 × 4 = 12 and 4 × 5 = 20, what is 5 × 6?", "options": ["25", "30", "35", "40"], "correct": 1},
    {"prompt": "Choose the logically correct sentence:", "options": ["All birds swim", "All fish fly", "The dog is an animal", "The house runs"], "correct": 2},
    {"prompt": "Which item belongs to the group?", "options": ["Bottle", "Lamp", "Piano", "Wall"], "correct": 2},
    {"prompt": "How many letters are in the word 'intelligence'?", "options": ["11", "12", "13", "14"], "correct": 2},
    {"prompt": "Which letter comes immediately after A?", "options": ["B", "C", "D", "E"], "correct": 0},
    {"prompt": "If Ahmed is taller than Sami and Sami is taller than Fahd, who is tallest?", "options": ["Sami", "Fahd", "Ahmed", "Unknown"], "correct": 2},
    {"prompt": "What is 12 ÷ 3 + 4?", "options": ["6", "8", "10", "12"], "correct": 1},
    {"prompt": "What comes next in the sequence: 1, 3, 6, 10, 15, ?", "options": ["18", "20", "21", "22"], "correct": 2},
    {"prompt": "Choose the word closest in meaning to 'careful'.", "options": ["Reckless", "Alert", "Forgiven", "Stable"], "correct": 1},
    {"prompt": "If 2 + 2 = 5, what is 4 + 4?", "options": ["8", "10", "12", "16"], "correct": 1},
    {"prompt": "Which number breaks the pattern: 3, 6, 9, 12, 14?", "options": ["3", "9", "12", "14"], "correct": 3},
    {"prompt": "What comes next: Sun, Moon, Star, ?", "options": ["Sky", "Tree", "Cloud", "Earth"], "correct": 2},
    {"prompt": "Which word means 'knowledge'?", "options": ["Clarity", "Science", "Speed", "Strength"], "correct": 1},
    {"prompt": "If each apple equals 2 and each orange equals 3, what is apple + orange?", "options": ["4", "5", "6", "7"], "correct": 1},
    {"prompt": "Which idea does not belong to logical thinking?", "options": ["Analysis", "Comparison", "Guessing", "Production"], "correct": 3},
    {"prompt": "How are 'friend' and 'enemy' related?", "options": ["Opposites", "Similar", "Equal", "Same"], "correct": 0},
    {"prompt": "Which number follows 64 in the pattern: 1, 4, 9, 16, 25, 36, 49, 64, ?", "options": ["72", "81", "90", "100"], "correct": 1},
    {"prompt": "Which word is the opposite of 'bright'?", "options": ["Dark", "Clear", "Lively", "Fast"], "correct": 0},
    {"prompt": "If the sequence is 8, 10, 12, 14, what comes next?", "options": ["15", "16", "18", "20"], "correct": 1},
    {"prompt": "What is 7 + 8 × 2?", "options": ["15", "23", "30", "32"], "correct": 1},
    {"prompt": "Which word does not belong to colors?", "options": ["Blue", "Green", "Banana", "Red"], "correct": 2},
    {"prompt": "What is the relationship between 'text' and 'readable'?", "options": ["Cause and effect", "Part and whole", "Opposite", "Comparison"], "correct": 1},
    {"prompt": "What is 10% of 150?", "options": ["10", "15", "20", "25"], "correct": 1},
    {"prompt": "Which word means 'insight'?", "options": ["Foolishness", "Perception", "Weakness", "Speed"], "correct": 1},
    {"prompt": "If each letter in 'wisdom' has a number based on its alphabet position, what is the total?", "options": ["15", "16", "17", "18"], "correct": 2},
    {"prompt": "Choose the correct next term: 8, 13, 21, 34, ?", "options": ["44", "55", "65", "75"], "correct": 1},
    {"prompt": "Which choice reflects quick reasoning?", "options": ["Indecision", "Logical thinking", "Distraction", "Haste"], "correct": 1},
    {"prompt": "If every car has wheels and every wheel rotates, do all cars rotate?", "options": ["Yes", "No", "Sometimes", "Unknown"], "correct": 0},
    {"prompt": "What is the average of 12 and 20?", "options": ["14", "15", "16", "17"], "correct": 2},
]

def make_question(prompt, answer, distractors, salt):
  answer_text = str(answer)
  options = []
  for distractor in distractors:
    distractor_text = str(distractor)
    if distractor_text != answer_text and distractor_text not in options:
      options.append(distractor_text)
  filler_index = 1
  while len(options) < 3:
    try:
      filler = str(int(answer_text) + filler_index)
    except ValueError:
      filler = f"Other choice {filler_index}"
    filler_index += 1
    if filler != answer_text and filler not in options:
      options.append(filler)
  options = options[:3]
  correct_index = salt % 4
  options.insert(correct_index, answer_text)
  return {"prompt": prompt, "options": options, "correct": correct_index}


age_question_banks = {"4-7": [], "8-12": [], "13-17": [], "18+": []}
stars = ["⭐", "🌟", "✨", "💫", "🌠"]
odd_groups = [
    ("apple", "pear", "carrot", "peach"),
    ("bus", "train", "bicycle", "grape"),
    ("shirt", "socks", "hat", "spoon"),
    ("piano", "guitar", "drum", "window"),
    ("rose", "tulip", "daisy", "sandwich"),
    ("January", "March", "Friday", "October"),
    ("square", "triangle", "circle", "pencil"),
    ("copper", "iron", "silver", "cotton"),
    ("meter", "centimeter", "kilometer", "minute"),
    ("novel", "poem", "story", "ladder"),
    ("doctor", "nurse", "surgeon", "watermelon"),
    ("violin", "trumpet", "flute", "pillow"),
    ("eagle", "sparrow", "robin", "shovel"),
    ("river", "lake", "ocean", "backpack"),
    ("kilogram", "gram", "tonne", "hour"),
    ("whisper", "murmur", "mumble", "bright"),
    ("hexagon", "pentagon", "octagon", "cucumber"),
    ("oxygen", "nitrogen", "helium", "granite"),
    ("fiction", "mystery", "fantasy", "thermometer"),
    ("compass", "map", "atlas", "teacup"),
    ("oak", "maple", "birch", "candle"),
    ("February", "April", "September", "Tuesday"),
    ("keyboard", "mouse", "monitor", "cushion"),
    ("kilometer", "mile", "meter", "liter"),
    ("evaporation", "condensation", "freezing", "rectangle"),
]

for question_index in range(100):
    round_index = question_index // 4
    mode = question_index % 4

    if mode == 0:
      count = round_index % 5 + 1
      picture = " ".join(stars[:count])
      age_question_banks["4-7"].append(make_question(
        f"Count the stars in group {round_index // 5 + 1}: {picture}", count,
        [count + 1, max(0, count - 1), count + 2], question_index
      ))
    elif mode == 1:
      start = round_index + 1
      answer = start + 4
      age_question_banks["4-7"].append(make_question(
        f"What number comes next? {start}, {start + 1}, {start + 2}, {start + 3}, ?",
        answer, [answer - 1, answer + 1, answer + 2], question_index
      ))
    elif mode == 2:
      smallest = round_index + 1
      answer = smallest + 3
      age_question_banks["4-7"].append(make_question(
        f"Which number is biggest: {smallest}, {smallest + 1}, {answer}, or {smallest + 2}?", answer,
        [smallest, smallest + 1, smallest + 2], question_index
      ))
    else:
      first = round_index % 10 + 1
      second = round_index // 10 + 1
      answer = first + second
      age_question_banks["4-7"].append(make_question(
        f"How many apples are there? {'🍎 ' * first}+ {'🍎 ' * second}",
        answer, [answer - 1, answer + 1, answer + 2], question_index
      ))

    if mode == 0:
      start = round_index + 2
      step = round_index % 4 + 2
      answer = start + step * 4
      age_question_banks["8-12"].append(make_question(
        f"Find the next number: {start}, {start + step}, {start + 2 * step}, {start + 3 * step}, ?",
        answer, [answer - step, answer + 1, answer + step], question_index
      ))
    elif mode == 1:
      first = round_index % 10 + 2
      second = round_index // 10 + 2
      answer = first * second
      age_question_banks["8-12"].append(make_question(
        f"What is {first} × {second}?", answer,
        [answer - first, answer + first, answer + 2], question_index
      ))
    elif mode == 2:
      group = odd_groups[round_index % len(odd_groups)]
      odd_word = group[2]
      age_question_banks["8-12"].append(make_question(
        f"Which word does not belong: {', '.join(group)}?", odd_word,
        [group[0], group[1], group[3]], question_index
      ))
    else:
      value = round_index + 3
      answer = value * 3 + 4
      age_question_banks["8-12"].append(make_question(
        f"A number is multiplied by 3, then 4 is added. The number is {value}. What is the result?",
        answer, [answer - 3, answer + 3, answer + 4], question_index
      ))

    if mode == 0:
      value = round_index + 2
      total = 3 * value + round_index % 5 + 1
      offset = round_index % 5 + 1
      age_question_banks["13-17"].append(make_question(
        f"Solve for x: 3x + {offset} = {total}", value,
        [value - 1, value + 1, value + 2], question_index
      ))
    elif mode == 1:
      start = round_index + 3
      step = round_index % 6 + 3
      answer = start + step * 4
      age_question_banks["13-17"].append(make_question(
        f"What is the next term? {start}, {start + step}, {start + 2 * step}, {start + 3 * step}, ?",
        answer, [answer - 2, answer + 2, answer + step], question_index
      ))
    elif mode == 2:
      percent = (round_index % 4 + 1) * 10
      amount = 100 + round_index * 50
      answer = amount * percent // 100
      age_question_banks["13-17"].append(make_question(
        f"What is {percent}% of {amount}?", answer,
        [answer - 5, answer + 5, answer + 10], question_index
      ))
    else:
      red_count = round_index % 5 + 1
      blue_count = round_index % 7 + 2
      total_count = red_count + blue_count
      divisor = gcd(red_count, total_count)
      answer = f"{red_count // divisor}/{total_count // divisor}"
      age_question_banks["13-17"].append(make_question(
        f"A bag has {red_count} red counters and {blue_count} blue counters. What is the chance of picking red?",
        answer, [f"{red_count}/{total_count + 1}", f"{red_count + 1}/{total_count}", f"{blue_count}/{total_count}"], question_index
      ))

    if mode == 0:
      start = round_index + 2
      answer = (start + 3) * (start + 4)
      age_question_banks["18+"].append(make_question(
        f"Find the next term: {start * (start + 1)}, {(start + 1) * (start + 2)}, {(start + 2) * (start + 3)}, ?",
        answer, [answer - 2, answer + 2, answer + 6], question_index
      ))
    elif mode == 1:
      value = round_index + 4
      answer = value
      total = 7 * value - 8
      age_question_banks["18+"].append(make_question(
        f"Solve for x: 4(x - 2) + 3x = {total}", answer,
        [answer - 1, answer + 1, answer + 2], question_index
      ))
    elif mode == 2:
      group = odd_groups[round_index % len(odd_groups)]
      odd_word = group[2]
      age_question_banks["18+"].append(make_question(
        f"Which item breaks the category pattern: {', '.join(group)}?", odd_word,
        [group[0], group[1], group[3]], question_index
      ))
    else:
      first = round_index % 6 + 2
      second = round_index // 6 + 3
      age_question_banks["18+"].append(make_question(
        f"A recipe uses {first} parts of A for every {second} parts of B. If A is {first * 4}, how much B is needed?",
        second * 4, [second * 3, second * 5, second * 4 + first], question_index
      ))

question_data_js = 'const QUESTION_BANKS = ' + json.dumps(age_question_banks, ensure_ascii=False) + ';\n'

home_html = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BrightIQ | IQ Challenge</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
    <link rel="stylesheet" href="home.css" />
  </head>
  <body>
    <div class="page-shell">
      <div class="brand-row">
        <img class="brand-mark" src="favicon.svg" alt="" />
        <div class="brand-name">BrightIQ</div>
      </div>

      <div class="card">
        <p class="eyebrow">SMART MIND TEST</p>
        <h1>Discover Your IQ</h1>
        <p class="subtitle">Take a fun 40-question challenge designed to test logic, reasoning, problem-solving, and mental speed. Answer at your own pace and see your final percentage at the end.</p>
        <form id="profile-form" class="profile-form">
          <div class="form-row">
            <label for="player-name">Your name
              <input id="player-name" name="name" type="text" maxlength="24" autocomplete="nickname" placeholder="Enter your name" required />
            </label>
            <label for="player-age">Your age
              <input id="player-age" name="age" type="number" min="4" max="120" inputmode="numeric" placeholder="Age 4 or older" required />
            </label>
          </div>
          <p id="age-hint" class="age-hint" aria-live="polite">Your age helps choose a suitable question level.</p>
          <button id="start-btn" class="primary-btn" type="submit">Start Test <span aria-hidden="true">→</span></button>
        </form>
        <div class="stat-row">
          <div class="stat-box"><span class="stat-number">40</span><span class="stat-label">Questions</span></div>
          <div class="stat-box"><span class="stat-number">4</span><span class="stat-label">Choices each</span></div>
          <div class="stat-box"><span class="stat-number">100%</span><span class="stat-label">Focus</span></div>
        </div>
        <p class="privacy-note">Your name and age stay in this browser and are not sent to a server.</p>
      </div>
    </div>
    <footer class="site-footer">
      <span class="footer-spark" aria-hidden="true">✦</span>
      <span>Made by <strong>Darin Ahmed @</strong></span>
      <span class="footer-separator" aria-hidden="true"></span>
      <span>2026</span>
    </footer>
    <script src="home.js"></script>
  </body>
</html>
'''

home_css = '''* { box-sizing: border-box; }
:root { --ink: #2d3f63; --muted: #536d95; --pink: #f28fb3; --aqua: #73d5d0; }
body { margin: 0; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px; padding: 36px 0 18px; font-family: "Segoe UI", Arial, sans-serif; background: radial-gradient(circle at 8% 12%, #fff4bd 0, transparent 30%), radial-gradient(circle at 88% 82%, #f8d9ef 0, transparent 34%), linear-gradient(135deg, #e4f8fa, #fff8e6 52%, #f5eaff); color: var(--ink); }
.page-shell { width: min(760px, 92vw); display: grid; gap: 20px; }
.brand-row { display: inline-flex; align-items: center; justify-content: center; gap: 11px; justify-self: center; padding: 10px 18px; border: 1px solid rgba(255,255,255,0.75); border-radius: 999px; background: rgba(255,255,255,0.62); box-shadow: 0 10px 28px rgba(90, 112, 160, 0.12); }
.brand-mark { width: 40px; height: 40px; display: block; border-radius: 50%; box-shadow: 0 5px 13px rgba(100, 91, 135, 0.14); }
.brand-name { font-size: 1.35rem; font-weight: 850; letter-spacing: 0.04em; }
.card { padding: 42px 30px; text-align: center; background: rgba(255,255,255,0.74); border: 1px solid rgba(255,255,255,0.82); border-radius: 26px; box-shadow: 0 22px 50px rgba(115, 135, 190, 0.15); }
.eyebrow { margin: 0 0 14px; letter-spacing: 0.17em; font-size: 0.72rem; color: #d66e9b; font-weight: 800; }
h1 { margin: 0 0 16px; font-size: clamp(2.4rem, 5vw, 4rem); line-height: 1.12; }
.subtitle { margin: 0 auto 25px; max-width: 590px; line-height: 1.75; color: var(--muted); font-size: 1.04rem; }
.profile-form { max-width: 540px; margin: 0 auto 24px; }
.form-row { display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 12px; text-align: left; }
.profile-form label { display: grid; gap: 7px; color: #536d95; font-size: 0.82rem; font-weight: 750; }
.profile-form input { width: 100%; min-height: 48px; padding: 0 13px; border: 1px solid #e8d8e6; border-radius: 12px; background: rgba(255,255,255,0.82); color: var(--ink); font: inherit; outline: none; }
.profile-form input:focus { border-color: #e58daf; box-shadow: 0 0 0 3px rgba(242,143,179,0.18); }
.age-hint { min-height: 21px; margin: 9px 0 13px; color: #72859c; text-align: left; font-size: 0.78rem; }
.privacy-note { margin: -13px 0 0; color: #75839a; font-size: 0.74rem; }
.site-footer { width: min(760px, 92vw); display: flex; align-items: center; justify-content: center; gap: 8px; padding: 13px 12px 0; border-top: 1px solid rgba(139, 125, 163, 0.18); color: #718095; font-size: 0.78rem; letter-spacing: 0.02em; }
.site-footer strong { color: #a9527b; font-weight: 800; }
.footer-spark { color: #e783aa; font-size: 1rem; }
.footer-separator { color: #d184a2; }
.stat-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 500px; margin: 0 auto 26px; }
.stat-box { padding: 13px 10px; border: 1px solid #f0e9f4; border-radius: 14px; background: rgba(255,255,255,0.72); }
.stat-number { display: block; color: #d66e9b; font-weight: 850; font-size: 1.35rem; }
.stat-label { display: block; margin-top: 4px; color: var(--muted); font-size: 0.7rem; letter-spacing: 0.08em; text-transform: uppercase; }
.primary-btn { border: 0; min-height: 54px; padding: 0 28px; border-radius: 14px; font-size: 1rem; font-weight: 800; cursor: pointer; background: linear-gradient(135deg, #f28fb3, #ffb5c8); color: #4a2d49; box-shadow: 0 12px 25px rgba(230, 125, 165, 0.27); transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease; }
.primary-btn:hover { transform: translateY(-2px); filter: saturate(1.08); box-shadow: 0 16px 30px rgba(230, 125, 165, 0.36); }
.primary-btn:focus-visible { outline: 3px solid var(--aqua); outline-offset: 4px; }
.primary-btn span { margin-left: 9px; }
@media (max-width: 520px) {
  body { justify-content: center; padding: 22px 0 14px; gap: 14px; }
  .page-shell { width: 94vw; gap: 15px; }
  .site-footer { width: 94vw; font-size: 0.72rem; }
  .card { padding: 34px 20px; }
  h1 { font-size: clamp(2rem, 9vw, 3rem); }
  .subtitle { font-size: 0.96rem; }
  .stat-row { gap: 8px; }
  .stat-label { font-size: 0.62rem; }
  .form-row { grid-template-columns: 1fr; gap: 10px; }
  .age-hint { margin-bottom: 12px; }
  .primary-btn { width: min(100%, 300px); }
}
'''

home_js = '''const profileForm = document.getElementById('profile-form');
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
    '4-7': 'Age group 4–7: picture counting and simple number patterns.',
    '8-12': 'Age group 8–12: number patterns, multiplication, and word puzzles.',
    '13-17': 'Age group 13–17: algebra, sequences, percentages, and probability.',
    '18+': 'Age group 18+: advanced patterns, algebra, logic, and proportional reasoning.'
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
  if (Array.isArray(previousOrder) && previousOrder.length === 40 && questionOrder.every((questionIndex) => previousOrder.includes(questionIndex))) {
    let replacementIndex;
    do {
      replacementIndex = Math.floor(Math.random() * 100);
    } while (previousOrder.includes(replacementIndex));
    questionOrder[0] = replacementIndex;
  }

  localStorage.setItem('brightIQProfile', JSON.stringify(profile));
  localStorage.setItem('iqQuestionOrder', JSON.stringify(questionOrder));
  localStorage.setItem('iqQuizAnswers', JSON.stringify(Array(40).fill(null)));
  window.location.href = 'question one.html';
});
'''

result_html = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BrightIQ | Result</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
    <link rel="stylesheet" href="result.css" />
  </head>
  <body>
    <div class="page-shell">
      <div class="brand-row">
        <img class="brand-mark" src="favicon.svg" alt="" />
        <div class="brand-name">BrightIQ</div>
      </div>

      <div id="profile-name" class="profile-pill">Player</div>
      <div class="card">
        <p class="eyebrow">FINAL RESULT</p>
        <h1>Your IQ Percent</h1>
        <div id="iq-score">0%</div>
        <p id="result-text">Thank you for taking the test.</p>
        <button id="restart-btn" class="primary-btn">Restart Test</button>
      </div>
    </div>
    <footer class="site-footer">
      <span class="footer-spark" aria-hidden="true">✦</span>
      <span>Made by <strong>Darin Ahmed</strong></span>
      <span class="footer-separator" aria-hidden="true">·</span>
      <span>2026</span>
    </footer>
    <script src="question-data.js"></script>
    <script src="result.js"></script>
  </body>
</html>
'''

result_css = '''* { box-sizing: border-box; }
:root {
  --bg-top: #fff7d6;
  --bg-mid: #dff9ff;
  --bg-bottom: #f7e7ff;
  --card: rgba(255,255,255,0.72);
  --text: #2d3f63;
  --muted: #536d95;
  --shadow: 0 24px 60px rgba(124, 126, 248, 0.16);
}
html, body {
  margin: 0;
  min-height: 100vh;
}
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 28px 0 16px;
  place-items: center;
  font-family: "Segoe UI", Arial, sans-serif;
  background: radial-gradient(circle at top left, #fff9c4 0%, var(--bg-mid) 28%, var(--bg-top) 50%, var(--bg-bottom) 100%);
  color: var(--text);
}
.page-shell {
  width: min(760px, 92vw);
  display: grid;
  gap: 22px;
}
.site-footer {
  width: min(760px, 92vw);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 13px 12px 0;
  border-top: 1px solid rgba(139, 125, 163, 0.18);
  color: #718095;
  font-size: 0.78rem;
}
.site-footer strong { color: #a9527b; font-weight: 800; }
.footer-spark { color: #e783aa; font-size: 1rem; }
.footer-separator { color: #d184a2; }
.profile-pill {
  justify-self: center;
  max-width: 80%;
  overflow: hidden;
  padding: 8px 16px;
  border: 1px solid rgba(255,255,255,0.7);
  border-radius: 999px;
  background: #e6f5eb;
  color: #355f4b;
  font-weight: 700;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.brand-row {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  align-self: center;
  padding: 12px 20px;
  border-radius: 999px;
  background: rgba(255,255,255,0.5);
  box-shadow: 0 10px 30px rgba(102, 119, 255, 0.15);
}
.brand-mark {
  width: 42px;
  height: 42px;
  display: block;
  border-radius: 50%;
  box-shadow: 0 5px 13px rgba(100, 91, 135, 0.14);
}
.brand-name {
  font-size: clamp(1.4rem, 2vw, 2rem);
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--text);
}
.card {
  padding: 42px 26px;
  text-align: center;
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.5);
  border-radius: 30px;
  box-shadow: var(--shadow);
}
.eyebrow {
  margin: 0 0 16px;
  letter-spacing: 0.18em;
  font-size: 0.74rem;
  color: #7d8dff;
  font-weight: 700;
}
h1 {
  margin: 0 0 14px;
  font-size: clamp(2.1rem, 4vw, 3.2rem);
}
#iq-score {
  font-size: clamp(3rem, 7vw, 5.5rem);
  font-weight: 900;
  color: #ff8fab;
  margin: 14px 0 10px;
}
#result-text {
  color: var(--muted);
  line-height: 1.9;
  margin: 0 auto 28px;
  max-width: 540px;
  font-size: 1.05rem;
}
.primary-btn {
  border: none;
  padding: 18px 30px;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 800;
  cursor: pointer;
  background: linear-gradient(135deg, #7c7ef8, #4cc9f0, #f9a8d4);
  color: white;
  box-shadow: 0 16px 30px rgba(124, 126, 248, 0.24);
}
@media (max-width: 560px) {
  body { gap: 12px; padding: 20px 0 12px; }
  .page-shell { width: 94vw; gap: 16px; }
  .site-footer { width: 94vw; font-size: 0.72rem; }
  .card { padding: 34px 20px; }
  .brand-row { padding: 9px 15px; }
  .brand-mark { width: 38px; height: 38px; }
  h1 { font-size: clamp(1.9rem, 9vw, 2.7rem); }
  #iq-score { font-size: clamp(3.2rem, 18vw, 4.5rem); }
  #result-text { font-size: 0.96rem; }
  .primary-btn { width: min(100%, 300px); }
}
'''

result_js = '''const scoreEl = document.getElementById('iq-score');
const textEl = document.getElementById('result-text');
const restartBtn = document.getElementById('restart-btn');

const defaultQuestions = [
    {"correct": 3}, {"correct": 2}, {"correct": 0}, {"correct": 2}, {"correct": 3}, {"correct": 2}, {"correct": 1}, {"correct": 1}, {"correct": 2}, {"correct": 0}, {"correct": 2}, {"correct": 3}, {"correct": 1}, {"correct": 1}, {"correct": 2}, {"correct": 2}, {"correct": 2}, {"correct": 0}, {"correct": 2}, {"correct": 1}, {"correct": 2}, {"correct": 1}, {"correct": 1}, {"correct": 3}, {"correct": 2}, {"correct": 1}, {"correct": 1}, {"correct": 1}, {"correct": 0}, {"correct": 1}, {"correct": 1}, {"correct": 1}, {"correct": 2}, {"correct": 1}, {"correct": 1}, {"correct": 2}, {"correct": 1}, {"correct": 1}, {"correct": 0}, {"correct": 2}
];
const profile = JSON.parse(localStorage.getItem('brightIQProfile') || 'null') || {name: 'Player', group: '18+'};
document.getElementById('profile-name').textContent = profile.name;
const questionOrder = JSON.parse(localStorage.getItem('iqQuestionOrder') || 'null') || Array.from({length: 40}, (_, index) => index);
const questionBank = QUESTION_BANKS[profile.group] || QUESTION_BANKS['18+'];
const questions = questionOrder.map((questionIndex) => questionBank[questionIndex]);
const raw = localStorage.getItem('iqQuizAnswers');
const answers = raw ? JSON.parse(raw) : Array(40).fill(null);
let correct = 0;
answers.forEach((answer, index) => {
  if (answer !== null && answer === questions[index].correct) correct += 1;
});
const percentage = (correct / questions.length) * 100;
const percentText = `${Math.round(percentage)}%`;
scoreEl.textContent = percentText;

if (percentage >= 80) {
  textEl.textContent = 'Excellent! Your logic and reasoning are highly advanced.';
} else if (percentage >= 60) {
  textEl.textContent = 'Great result! You have strong analytical thinking and problem-solving skills.';
} else if (percentage >= 40) {
  textEl.textContent = 'Good work! Your thinking is solid, and there is room to improve further.';
} else if (percentage >= 20) {
  textEl.textContent = 'Nice effort! Practice more and your reasoning skills will grow quickly.';
} else {
  textEl.textContent = 'Every challenge helps. Keep practicing and your IQ score will improve over time.';
}

restartBtn.addEventListener('click', () => {
  localStorage.setItem('iqQuizAnswers', JSON.stringify(Array(40).fill(null)));
  window.location.href = 'index.html';
});
'''

number_names = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
    'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'thirty',
    'thirty one', 'thirty two', 'thirty three', 'thirty four', 'thirty five', 'thirty six', 'thirty seven', 'thirty eight', 'thirty nine', 'forty'
]

pastel_palette = [
    '#ffb4a2', '#ffd6a5', '#caffbf', '#bde0fe', '#fbc4ab', '#a0c4ff', '#ffc8dd', '#d8f3dc',
    '#ffafcc', '#98f5e1', '#cdb4db', '#ffd6a5', '#90dbf4', '#f7d6e0', '#b8f2e6', '#e7c6ff',
    '#f7d9c4', '#cce3de', '#f9c74f', '#90be6d', '#adb5bd', '#ffcf99', '#b892ff', '#ff9f1c',
    '#7bdff2', '#f4acb7', '#9ad1d4', '#f1c0e8', '#e9d8a6', '#aaf683', '#d4a373', '#bde0fe',
    '#ffd166', '#9ae6b4', '#c5d86d', '#f7a072', '#b5e48c', '#ff7eb6', '#7dd3fc', '#c0caff'
]

with open('index.html', 'w', encoding='utf-8') as f:
  f.write(home_html)
with open('home.css', 'w', encoding='utf-8') as f:
    f.write(home_css)
with open('home.js', 'w', encoding='utf-8') as f:
    f.write(home_js)
with open('result.html', 'w', encoding='utf-8') as f:
    f.write(result_html)
with open('result.css', 'w', encoding='utf-8') as f:
    f.write(result_css)
with open('result.js', 'w', encoding='utf-8') as f:
    f.write(result_js)
with open('question-data.js', 'w', encoding='utf-8') as f:
  f.write(question_data_js)

for index in range(1, 41):
    q = questions[index - 1]
    name = number_names[index - 1]
    base = f'question {name}'
    previous_name = 'one' if index == 1 else number_names[index - 2]
    next_name = number_names[index] if index < 40 else 'forty'
    accent = pastel_palette[(index - 1) % len(pastel_palette)]

    html = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Question {index}</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
    <link rel="stylesheet" href="{base}.css" />
  </head>
  <body>
    <div class="page-shell">
      <div class="top-row">
        <div class="brand-row">
          <img class="brand-mark" src="favicon.svg" alt="" />
          <div class="brand-name">BrightIQ</div>
        </div>
        <div id="profile-name" class="profile-pill">Player</div>
      </div>

      <div class="card">
        <p class="progress">Question {index} / 40</p>
        <div class="progress-meta"><span id="progress-count">0 answered</span><span>40 questions</span></div>
        <div class="progress-track" role="progressbar" aria-label="Quiz progress" aria-valuemin="1" aria-valuemax="40" aria-valuenow="{index}"><span style="width: {index * 2.5}%"></span></div>
        <h1 id="question-text">{q['prompt']}</h1>
        <div class="options" id="options"></div>
        <p id="answer-status" class="answer-status" aria-live="polite">Choose an answer to save your progress.</p>
        <div class="controls">
          <button id="prev-btn" class="nav-btn secondary">Previous</button>
          <button id="next-btn" class="nav-btn primary">Next</button>
        </div>
      </div>
    </div>
    <footer class="site-footer">
      <span class="footer-spark" aria-hidden="true">✦</span>
      <span>Made by <strong>Darin Ahmed</strong></span>
      <span class="footer-separator" aria-hidden="true">·</span>
      <span>2026</span>
    </footer>
    <script src="question-data.js"></script>
    <script src="{base}.js"></script>
  </body>
</html>
'''

    css = f'''* {{ box-sizing: border-box; }}
:root {{
  --accent: {accent};
  --card: #fff7fb;
  --text: #2d3f63;
  --muted: #536d95;
  --shadow: 0 22px 44px rgba(139, 102, 143, 0.16);
}}
html, body {{
  margin: 0;
  min-height: 100vh;
}}
body {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  padding: 22px 0 14px;
  font-family: "Segoe UI", Arial, sans-serif;
  background: linear-gradient(125deg, #dcf4e7 0%, #fff0f5 48%, #e9f4ff 100%);
  color: var(--text);
}}
.page-shell {{
  width: min(860px, 92vw);
  display: grid;
  gap: 18px;
}}
.site-footer {{ width: min(860px, 92vw); display: flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 10px 0; border-top: 1px solid rgba(139, 125, 163, 0.18); color: #718095; font-size: 0.76rem; }}
.site-footer strong {{ color: #a9527b; font-weight: 800; }}
.footer-spark {{ color: #e783aa; font-size: 1rem; }}
.footer-separator {{ color: #d184a2; }}
.top-row {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; }}
.profile-pill {{ max-width: 48%; overflow: hidden; padding: 9px 15px; border: 1px solid rgba(255,255,255,0.72); border-radius: 999px; background: #e2f4e8; color: #355f4b; font-size: 0.9rem; font-weight: 700; text-overflow: ellipsis; white-space: nowrap; }}
.brand-row {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 10px 18px;
  border-radius: 999px;
  background: rgba(255,255,255,0.64);
  box-shadow: 0 12px 26px rgba(95, 113, 185, 0.12);
  width: fit-content;
  justify-self: center;
}}
.brand-mark {{
  width: 36px;
  height: 36px;
  display: block;
  border-radius: 50%;
  box-shadow: 0 4px 11px rgba(100, 91, 135, 0.14);
}}
.brand-name {{
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}}
.card {{
  padding: 28px 22px 24px;
  background: linear-gradient(145deg, #fff4f8 0%, #fffaf0 48%, #effaf3 100%);
  border: 1px solid rgba(255,255,255,0.9);
  border-radius: 28px;
  box-shadow: var(--shadow);
}}
.progress {{
  margin: 0 0 8px;
  color: #b65f85;
  letter-spacing: 0.12em;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
}}
.progress-meta {{ display: flex; justify-content: space-between; gap: 12px; color: var(--muted); font-size: 0.78rem; }}
.progress-track {{ width: 100%; height: 8px; margin: 10px 0 24px; overflow: hidden; border-radius: 999px; background: #e7eee8; }}
.progress-track span {{ display: block; height: 100%; border-radius: inherit; background: linear-gradient(90deg, #80cfae, #ef91b2); transition: width 300ms ease; }}
h1 {{
  margin: 0 0 24px;
  font-size: clamp(1.6rem, 2.8vw, 2.7rem);
  line-height: 1.5;
  color: var(--text);
}}
.options {{
  display: grid;
  grid-template-columns: repeat(2, minmax(220px, 1fr));
  gap: 16px;
  margin-bottom: 26px;
}}
.option-btn {{
  position: relative;
  width: 100%;
  min-height: 66px;
  padding: 16px 16px 16px 56px;
  border-radius: 16px;
  border: 1px solid transparent;
  color: var(--text);
  font-size: 1rem;
  text-align: left;
  cursor: pointer;
  font-weight: 600;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
}}
.option-btn::before {{
  content: attr(data-letter);
  position: absolute;
  left: 16px;
  top: 50%;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  transform: translateY(-50%);
  border-radius: 50%;
  background: rgba(255,255,255,0.8);
  color: #5b556d;
  font-size: 0.78rem;
  font-weight: 800;
}}
.option-btn:nth-child(1) {{ background: #ffe0eb; }}
.option-btn:nth-child(2) {{ background: #d8f2e3; }}
.option-btn:nth-child(3) {{ background: #e8e1fb; }}
.option-btn:nth-child(4) {{ background: #fff0c9; }}
.option-btn:hover {{
  transform: translateY(-1px);
  border-color: rgba(105, 150, 128, 0.42);
  box-shadow: 0 10px 20px rgba(120, 130, 210, 0.12);
}}
.option-btn.selected {{
  background: linear-gradient(135deg, #f6a9c5, #bdebd2);
  border-color: #d87ca0;
  box-shadow: 0 12px 24px rgba(220, 126, 164, 0.24);
}}
.option-btn:focus-visible {{ outline: 3px solid #65b995; outline-offset: 3px; }}
.answer-status {{ min-height: 22px; margin: -10px 0 18px; color: #648374; font-size: 0.84rem; }}
.controls {{
  display: flex;
  justify-content: space-between;
  gap: 14px;
}}
.nav-btn {{
  flex: 1;
  border: none;
  border-radius: 14px;
  padding: 14px 18px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
}}
.nav-btn.primary {{ background: linear-gradient(135deg, var(--accent), #ffb3c6); color: white; }}
.nav-btn.secondary {{
  background: rgba(255,255,255,0.76);
  color: var(--text);
}}
@media (max-width: 700px) {{
  .options {{ grid-template-columns: 1fr; }}
  .controls {{ flex-direction: column; }}
}}
@media (max-width: 520px) {{
  body {{ gap: 10px; padding: 16px 0 10px; }}
  .page-shell {{ width: 94vw; gap: 14px; }}
  .site-footer {{ width: 94vw; font-size: 0.7rem; }}
  .top-row {{ gap: 8px; }}
  .card {{ padding: 24px 16px 20px; }}
  .brand-row {{ gap: 7px; padding: 7px 10px; }}
  .brand-name {{ font-size: 1rem; }}
  .profile-pill {{ padding: 8px 11px; font-size: 0.78rem; }}
  h1 {{ font-size: clamp(1.45rem, 7vw, 2rem); line-height: 1.35; }}
  .options {{ gap: 11px; margin-bottom: 20px; }}
  .option-btn {{ min-height: 58px; padding: 13px 12px 13px 50px; font-size: 0.94rem; }}
  .option-btn::before {{ left: 12px; }}
  .progress-track {{ margin-bottom: 20px; }}
}}
'''

    js = f'''const questionNumber = {index};
const totalQuestions = 40;
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options');
const nextBtn = document.getElementById('next-btn');
const prevBtn = document.getElementById('prev-btn');
const progressCount = document.getElementById('progress-count');
const answerStatus = document.getElementById('answer-status');

const profile = JSON.parse(localStorage.getItem('brightIQProfile') || 'null') || {{name: 'Player', group: '18+'}};
document.getElementById('profile-name').textContent = profile.name;
const questionOrder = JSON.parse(localStorage.getItem('iqQuestionOrder') || 'null') || Array.from({{length: totalQuestions}}, (_, questionIndex) => questionIndex);
const questionBank = QUESTION_BANKS[profile.group] || QUESTION_BANKS['18+'];
const question = questionBank[questionOrder[questionNumber - 1]];

const storageKey = 'iqQuizAnswers';
const storedAnswers = JSON.parse(localStorage.getItem(storageKey) || '[]');
const answers = Array(totalQuestions).fill(null);
for (let i = 0; i < answers.length; i++) {{
  answers[i] = storedAnswers[i] ?? null;
}}

const previousPageName = {previous_name!r};
const nextPageName = {next_name!r};
progressCount.textContent = answers.filter((answer) => answer !== null).length + ' answered';
if (answers[questionNumber - 1] !== null) answerStatus.textContent = 'Answer saved. You can change it before moving on.';

questionText.textContent = question.prompt;
question.options.forEach((option, index) => {{
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'option-btn';
  button.dataset.letter = String.fromCharCode(65 + index);
  button.textContent = option;
  button.setAttribute('aria-pressed', answers[questionNumber - 1] === index ? 'true' : 'false');
  if (answers[questionNumber - 1] === index) button.classList.add('selected');
  button.addEventListener('click', () => {{
    answers[questionNumber - 1] = index;
    localStorage.setItem(storageKey, JSON.stringify(answers));
    document.querySelectorAll('.option-btn').forEach((btn) => {{
      btn.classList.remove('selected');
      btn.setAttribute('aria-pressed', 'false');
    }});
    button.classList.add('selected');
    button.setAttribute('aria-pressed', 'true');
    progressCount.textContent = answers.filter((answer) => answer !== null).length + ' answered';
    answerStatus.textContent = 'Answer saved. You can change it before moving on.';
  }});
  optionsContainer.appendChild(button);
}});

prevBtn.style.visibility = questionNumber === 1 ? 'hidden' : 'visible';
nextBtn.textContent = questionNumber === totalQuestions ? 'See Result' : 'Next';

prevBtn.addEventListener('click', () => {{
  if (questionNumber > 1) {{
    window.location.href = 'question ' + previousPageName + '.html';
  }}
}});

nextBtn.addEventListener('click', () => {{
  if (questionNumber < totalQuestions) {{
    window.location.href = 'question ' + nextPageName + '.html';
  }} else {{
    window.location.href = 'result.html';
  }}
}});
'''

    with open(f'{base}.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open(f'{base}.css', 'w', encoding='utf-8') as f:
        f.write(css)
    with open(f'{base}.js', 'w', encoding='utf-8') as f:
        f.write(js)

print(f'Generated {len(questions)} question files successfully.')
