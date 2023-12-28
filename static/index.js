// Получаем все кнопки с классом "myButton"
var buttons = document.querySelectorAll(".button");

// Добавляем обработчик события "click" для каждой кнопки
buttons.forEach(function(button) {
  button.addEventListener("click", function() {
    var value = button.value;
    console.log("Нажата кнопка с значением: " + value);
  });
});