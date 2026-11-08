const questions = [
  {
    text: 'كم العدد الذي يكمّل التسلسل: 2، 4، 8، 16، ___؟',
    options: ['24', '28', '32', '64'],
    correct: 3,
  },
  {
    text: 'أي كلمة لا تنتمي إلى المجموعة؟',
    options: ['قلم', 'كتاب', 'مكتبة', 'ممحاة'],
    correct: 2,
  },
  {
    text: 'إذا كان كل مربع يساوي 3، وكل دائرة تساوي 2، فما قيمة المربع + الدائرة؟',
    options: ['5', '6', '7', '8'],
    correct: 0,
  },
  {
    text: 'أي رقم يكمل النمط؟ 5، 10، 20، 40، ___',
    options: ['60', '70', '80', '90'],
    correct: 2,
  },
  {
    text: 'ما هو الحيوان الذي لا يندرج مع الآخرين؟',
    options: ['نمر', 'أسد', 'ذئب', 'حوت'],
    correct: 3,
  },
  {
    text: 'إذا كانت الساعة الآن 3:15، فما الزاوية بين إبرة الساعات وإبرة الدقائق؟',
    options: ['30°', '45°', '52.5°', '67.5°'],
    correct: 2,
  },
  {
    text: 'أي عبارة تعني نفس كلمة “استنتاج”؟',
    options: ['تخمين', 'تفسير', 'نتيجة', 'حبس'],
    correct: 1,
  },
  {
    text: 'اختر الكلمة التي تعبر عن العلاقة نفسها: طائر : جناح :: سمكة : ?',
    options: ['ذيل', 'زعانف', 'خطم', 'قرش'],
    correct: 1,
  },
  {
    text: 'أي رقم يملأ الفراغ؟ 9، 7، 10، 8، 11، ___',
    options: ['9', '10', '12', '13'],
    correct: 2,
  },
  {
    text: 'أي كلمة هي عكس كلمة “سريع”؟',
    options: ['بطيء', 'قوي', 'مشرق', 'صامت'],
    correct: 0,
  },
  {
    text: 'إذا كان كل حرف يساوي عدد موضعه في الأبجدية، فما قيمة “B + A”؟',
    options: ['3', '4', '5', '6'],
    correct: 2,
  },
  {
    text: 'أي عدد ليس جزءًا من النمط التالي؟ 1، 4، 9، 16، 25، 27',
    options: ['9', '16', '25', '27'],
    correct: 3,
  },
  {
    text: 'أي كلمة تعني “متفائل”؟',
    options: ['حزين', 'مستبشر', 'متوتر', 'مكتئب'],
    correct: 1,
  },
  {
    text: 'إذا كانت: 3 × 4 = 12، 4 × 5 = 20، فما قيمة 5 × 6؟',
    options: ['25', '30', '35', '40'],
    correct: 1,
  },
  {
    text: 'اختر الجملة المنطقية الصحيحة:',
    options: ['كل الطيور تسبح', 'كل الأسماك تطير', 'الكلب حيوان', 'البيت يركض'],
    correct: 2,
  },
  {
    text: 'أي شيء ينتمي إلى المجموعة؟',
    options: ['زجاجة', 'مِصْباح', 'بيانو', 'حائط'],
    correct: 2,
  },
  {
    text: 'كم عدد الحروف في كلمة “ذكاء”؟',
    options: ['4', '5', '6', '7'],
    correct: 1,
  },
  {
    text: 'أي حرف ياتي بعد A مباشرة في الحروف الأبجدية؟',
    options: ['B', 'C', 'D', 'E'],
    correct: 0,
  },
  {
    text: 'إذا كان أحمد أطول من سامي، وسامي أطول من فهد، فأيهم أطول؟',
    options: ['سامي', 'فهد', 'أحمد', 'لا يمكن معرفة'],
    correct: 2,
  },
  {
    text: 'ما هو ناتج 12 ÷ 3 + 4؟',
    options: ['6', '8', '10', '12'],
    correct: 1,
  },
  {
    text: 'أي خيار يملأ النمط: 1، 3، 6، 10، 15، ___؟',
    options: ['18', '20', '21', '22'],
    correct: 2,
  },
  {
    text: 'اختر الكلمة التي لها نفس المعنى: “حذر”',
    options: ['متهور', 'متيقظ', 'مغفور', 'مستقر'],
    correct: 1,
  },
  {
    text: 'إذا كان 2 + 2 = 5، فما قيمة 4 + 4؟',
    options: ['8', '10', '12', '16'],
    correct: 1,
  },
  {
    text: 'أي رقم لا يتناسب مع التسلسل؟ 3، 6، 9، 12، 14',
    options: ['3', '9', '12', '14'],
    correct: 3,
  },
  {
    text: 'ماذا يكون الشيء التالي في التسلسل: شمس، قمر، نجمة، ___؟',
    options: ['سماء', 'شجرة', 'غيمة', 'أرض'],
    correct: 2,
  },
  {
    text: 'أي كلمة تعني “المعرفة”؟',
    options: ['وضوح', 'علم', 'سرعة', 'قوة'],
    correct: 1,
  },
  {
    text: 'إذا كان كل تفاحة تساوي 2، وكل برتقالة تساوي 3، فما قيمة تفاحة + برتقالة؟',
    options: ['4', '5', '6', '7'],
    correct: 1,
  },
  {
    text: 'أي فكرة لا تنتمي إلى قائمة التفكير المنطقي؟',
    options: ['تحليل', 'مقارنة', 'تخمين', 'إنتاج'],
    correct: 3,
  },
  {
    text: 'كيف تكون العلاقة بين “صديق” و“عدو”؟',
    options: ['متقابلان', 'متشابهان', 'مختلفان', 'متساويان'],
    correct: 2,
  },
  {
    text: 'أي رقم يأتي بعد 64 في هذا النمط: 1، 4، 9، 16، 25، 36، 49، 64، ___؟',
    options: ['72', '81', '90', '100'],
    correct: 1,
  },
  {
    text: 'أي كلمة تقابل “مشرق”؟',
    options: ['داكن', 'واضح', 'حيوي', 'سريع'],
    correct: 0,
  },
  {
    text: 'إذا كانت النتيجة في رياضات المدرسة: 8، 10، 12، 14، فما التالي؟',
    options: ['15', '16', '18', '20'],
    correct: 1,
  },
  {
    text: 'ما ناتج 7 + 8 × 2؟',
    options: ['15', '23', '30', '32'],
    correct: 1,
  },
  {
    text: 'أي كلمة لا تنتمي إلى مجموعة الألوان؟',
    options: ['أزرق', 'أخضر', 'موز', 'أحمر'],
    correct: 2,
  },
  {
    text: 'ما نوع العلاقة بين “نص” و“مقروء”؟',
    options: ['سبب ونتيجة', 'جزء وكامل', 'عكس', 'مقارنة'],
    correct: 1,
  },
  {
    text: 'ما هو الرقم الذي يساوي 10% من 150؟',
    options: ['10', '15', '20', '25'],
    correct: 1,
  },
  {
    text: 'أي كلمة لها نفس معنى “بصيرة”؟',
    options: ['حماقة', 'فطنة', 'ضعف', 'سرعة'],
    correct: 1,
  },
  {
    text: 'إذ كان كل حرف من كلمة “حكمة” يقابل رقمه في ترتيب الحروف، فما مجموع الحروف؟',
    options: ['15', '16', '17', '18'],
    correct: 2,
  },
  {
    text: 'اختَر الإجابة الصحيحة: 8، 13، 21، 34، ___',
    options: ['44', '55', '65', '75'],
    correct: 1,
  },
  {
    text: 'أي اختيار يعبر عن نوعية التفكير السريع؟',
    options: ['التردد', 'التفكير المنطقي', 'التشتت', 'التسرع'],
    correct: 1,
  },
  {
    text: 'ما هو النتيجة المنطقية لـ: إذا كانت كل السيارات لها عجلات، وكل العجلات تدور، فهل كل السيارات تدور؟',
    options: ['نعم', 'لا', 'أحيانًا', 'غير معلوم'],
    correct: 0,
  },
  {
    text: 'أي عدد يمثل الوسط الحسابي بين 12 و 20؟',
    options: ['14', '15', '16', '17'],
    correct: 2,
  }
];

const screens = {
  home: document.getElementById('home-screen'),
  quiz: document.getElementById('quiz-screen'),
  result: document.getElementById('result-screen'),
};

const stepIndicator = document.getElementById('step-indicator');
const progressFill = document.getElementById('progress-fill');
const questionCard = document.getElementById('question-card');
const answersContainer = document.getElementById('answers');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const iqScore = document.getElementById('iq-score');
const iqMessage = document.getElementById('iq-message');
const startBtn = document.getElementById('start-btn');
const restartBtn = document.getElementById('restart-btn');

const state = {
  currentIndex: 0,
  answers: new Array(questions.length).fill(null),
};

function showScreen(screenName) {
  Object.values(screens).forEach((screen) => {
    screen.classList.remove('active');
  });
  screens[screenName].classList.add('active');
}

function renderQuestion() {
  const currentQuestion = questions[state.currentIndex];
  const progressPercent = ((state.currentIndex + 1) / questions.length) * 100;

  stepIndicator.textContent = `السؤال ${state.currentIndex + 1} / ${questions.length}`;
  progressFill.style.width = `${progressPercent}%`;

  questionCard.innerHTML = `<h2>${currentQuestion.text}</h2>`;
  answersContainer.innerHTML = '';

  currentQuestion.options.forEach((option, index) => {
    const button = document.createElement('button');
    button.className = 'option';

    if (state.answers[state.currentIndex] === index) {
      button.classList.add('selected');
    }

    button.textContent = option;
    button.addEventListener('click', () => {
      state.answers[state.currentIndex] = index;
      renderQuestion();
    });

    answersContainer.appendChild(button);
  });

  prevBtn.style.visibility = state.currentIndex === 0 ? 'hidden' : 'visible';
  nextBtn.textContent = state.currentIndex === questions.length - 1 ? 'إظهار النتيجة' : 'التالي';
}

function calculateIQ() {
  const correctAnswers = state.answers.reduce((sum, answer, index) => {
    return sum + (answer === questions[index].correct ? 1 : 0);
  }, 0);

  const scoreRatio = correctAnswers / questions.length;
  return Math.min(170, Math.max(70, Math.round(75 + scoreRatio * 95)));
}

function getResultText(iq) {
  if (iq >= 140) return 'أنت ذكي جدًا ومتفوق في التحليل واتخاذ القرار. لديك قدرة قوية على الربط بين المعلومات بسرعة فائقة.';
  if (iq >= 120) return 'أنت تمتلك مستوى ذكاء مرتفعًا جدًا، وقدرات تحليل واستنتاج ممتازة، وتستطيع حل المشكلات بذكاء ومرونة.';
  if (iq >= 100) return 'مستوى ذكائك جيد، لديك قدرة على التفكير المنطقي والتحليل، وتستطيع تطوير مهاراتك أكثر في المستقبل.';
  if (iq >= 85) return 'أنت تمتلك قدرات تفكير جيدة، وبعض الأسئلة كانت تتطلب تركيزًا أكثر، لكنك على الطريق الصحيح.';
  return 'النتيجة تشير إلى أن قدراتك في التفكير والتحليل تحتاج إلى مزيد من التمرين والتطوير، وهذا ليس نقطة ضعف بل فرصة للنمو.';
}

function showResult() {
  const iq = calculateIQ();
  iqScore.textContent = `${iq}`;
  iqMessage.textContent = getResultText(iq);
  showScreen('result');
}

startBtn.addEventListener('click', () => {
  state.currentIndex = 0;
  state.answers = new Array(questions.length).fill(null);
  renderQuestion();
  showScreen('quiz');
});

prevBtn.addEventListener('click', () => {
  if (state.currentIndex > 0) {
    state.currentIndex -= 1;
    renderQuestion();
  }
});

nextBtn.addEventListener('click', () => {
  if (state.currentIndex < questions.length - 1) {
    state.currentIndex += 1;
    renderQuestion();
    return;
  }

  showResult();
});

restartBtn.addEventListener('click', () => {
  showScreen('home');
});

showScreen('home');
