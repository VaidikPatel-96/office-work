// const questions = [
//     {
//         question :"which is larget animal in the workd?",
//         answers: [
//             {Text: "shark",correct: false},
//             {Text: "shark",correct: false},
//             {Text: "shark",correct: false},
//             {Text: "shark",correct: false},
//         ]
        

//     }

// ]
// script.js
const questions = [
    {
      question: "What is the capital of France?",
      options: ["Berlin", "Madrid", "Paris", "Lisbon"],
      answer: 2
    },
    {
      question: "Which planet is known as the Red Planet?",
      options: ["Earth", "Mars", "Jupiter", "Venus"],
      answer: 1
    },
    {
      question: "What is the largest mammal?",
      options: ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
      answer: 1
    },
    {
      question: "Who wrote 'Romeo and Juliet' ?",
      options: ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"],
      answer: 2
    },
    {
      question: "What is the chemical symbol for water?",
      options: ["H2O", "O2", "CO2", "NaCl"],
      answer: 0
    },
    {
      question: "Which continent is known as the Dark Continent?",
      options: ["Asia", "Africa", "Europe", "South America"],
      answer: 1
    },
    {
      question: "What is the smallest prime number?",
      options: ["0", "1", "2", "3"],
      answer: 2
    },
    {
      question: "Who painted the Mona Lisa?",
      options: ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Claude Monet"],
      answer: 1
    },
    {
      question: "What is the speed of light?",
      options: ["300,000 km/s", "150,000 km/s", "299,792 km/s", "400,000 km/s"],
      answer: 2
    },
    {
      question: "Which organ purifies blood in the human body?",
      options: ["Heart", "Lungs", "Kidneys", "Liver"],
      answer: 2
    }
  ];
  
  let currentQuestionIndex = 0;
  let score = 0;
  
  const questionContainer = document.getElementById("question-container");
  const questionElement = document.getElementById("question");
  const optionsContainer = document.getElementById("options");
  const resultContainer = document.getElementById("result-container");
  const scoreElement = document.getElementById("score");
  const restartButton = document.getElementById("restart-btn");
  const nextButton = document.getElementById("next-btn");
  const prevButton = document.getElementById("prev-btn");
  const finishButton = document.getElementById("finish-btn");
  
  function showQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    questionElement.textContent = currentQuestion.question;
    optionsContainer.innerHTML = "";
  
    currentQuestion.options.forEach((option, index) => {
      const button = document.createElement("button");
      button.textContent = option;
      button.addEventListener("click", () => selectAnswer(index));
      optionsContainer.appendChild(button);
    });
    updateButtonVisibility();
  }
  
  function selectAnswer(selectedIndex) {
    const currentQuestion = questions[currentQuestionIndex];
    const buttons = optionsContainer.querySelectorAll("button");
  
    if (selectedIndex === currentQuestion.answer) {
      buttons[selectedIndex].classList.add("correct");
      score++;
    } else {
      buttons[selectedIndex].classList.add("wrong");
      buttons[currentQuestion.answer].classList.add("correct");
    }
  
    buttons.forEach(button => button.disabled = true);
  }
  
  function updateButtonVisibility() {
    prevButton.style.display = currentQuestionIndex > 0 ? "inline-block" : "none";
    nextButton.style.display = currentQuestionIndex < questions.length - 1 ? "inline-block" : "none";
    finishButton.style.display = currentQuestionIndex === questions.length - 1 ? "inline-block" : "none";
  }
  
  function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
      currentQuestionIndex++;
      showQuestion();
    }
  }
  
  function prevQuestion() {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex--;
      showQuestion();
    }
  }
  
  function showResult() {
    questionContainer.classList.add("hidden");
    resultContainer.classList.remove("hidden");
    scoreElement.textContent = `Your score is ${score} out of ${questions.length}`;
  }
  
  function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    questionContainer.classList.remove("hidden");
    resultContainer.classList.add("hidden");
    showQuestion();
  }
  
  nextButton.addEventListener("click", nextQuestion);
  prevButton.addEventListener("click", prevQuestion);
  finishButton.addEventListener("click", showResult);
  restartButton.addEventListener("click", restartQuiz);
  
  showQuestion();
  