// Получаем элементы DOM
const button = document.getElementById('changeTextButton'); // Кнопка
const dynamicText = document.getElementById('dynamicText'); // Динамический текст
const itemList = document.getElementById('itemList'); // Список

// Добавляем обработчик события на кнопку
button.addEventListener('click', () => {
    // Меняем текст при нажатии на кнопку
    dynamicText.textContent = 'Текст успешно изменён!';
});

// Пример использования популярных методов JavaScript

// 1. Создание нового элемента списка
const newItem = document.createElement('li'); // Создаём новый элемент <li>
newItem.textContent = 'Новый элемент'; // Добавляем текст

// 2. Добавление элемента в список
itemList.appendChild(newItem); // Добавляем элемент в конец списка

// 3. Удаление первого элемента списка через 5 секунд
setTimeout(() => {
    const firstItem = itemList.firstElementChild; // Находим первый элемент
    if (firstItem) {
        itemList.removeChild(firstItem); // Удаляем его
    }
}, 5000);

// 4. Пример использования forEach для массива
const itemsArray = Array.from(itemList.children); // Преобразуем HTMLCollection в массив
itemsArray.forEach((item, index) => {
    console.log(`Элемент ${index + 1}:`, item.textContent); // Выводим текст каждого элемента
});