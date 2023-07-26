document.getElementById("wheel__button").addEventListener("click", function () {
  const spinner = document.getElementById("spinner");
  const popup = document.querySelector(".popup");

  // Удаляем классы любой предыдущей анимации, чтобы сбросить позицию спиннера
  spinner.classList.remove("wheel__spinner_final", "wheel__spinner_animated_1");

  // Добавляем класс анимации для первой анимации, чтобы вращать спиннер
  spinner.classList.add("wheel__spinner_animated_1");

  // Когда первая анимация заканчивается, открываем попап
  spinner.addEventListener(
    "animationend",
    function () {
      popup.classList.add("popup__show");
    },
    { once: true } //  Обработчик сработает только один раз
  );
});
