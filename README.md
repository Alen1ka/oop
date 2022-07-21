__Основы__

Задача 1. Необходимо реализовать код, показанный в примерах выше. Создать класс Rectangle и класс ToyClass. Для ToyClass необходимо добавить три атрибута, и метод который устанавливает их.

Задача 2. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

Задача 3. Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.

__Наследование__

Задача 2. Написать программу, в которой есть главный класс Games со статическим полем Year, опишите конструктор присваивающий значение полю Year, также опишите метод getName, который возвращает имя игры. На основе главного класса путем наследования опишите четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте каждому классу дополнительные поля и переопределите у всех классов метод getName.

Задача 3. Напишите программу с пустым классом Country. Опишите наследуемые от класса Country классы Russia, Canada, Germany. Добавьте каждому классу поле population и опишите метод setPopulation и getPopulation.

Задача 4. Напишите программу в которой есть главный класс с текстовым полем. В главное классе должен быть метод для присваивания значения полю: без аргументов и с одним текстовым аргументом. Объект главного класса создаётся передачей одного текстового аргумента конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.

Задача 2. Необходимо написать программу в которой описать один базовый класс в нем описать конструктор, и класс потомок. Описать в классе потомке конструктор с параметрами по умолчанию. Затем нужно описать класс для которого класс потомок является базовым классом и в нем переопределить конструктор. В каждом классе описать по два поля и методы — show, get, set для каждого поля.

__Работа с числами, с длиной строки и слотами__

Задача 2. Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.

Задача 3. Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг. Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений. Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.

Задача 4. Николай – оригинальный человек. 
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился. 
Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”. 
В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие», то ничего у такого хитреца не получится).

__Покупка дома__

![image](https://user-images.githubusercontent.com/57345786/179697442-e0f3cb09-7ae3-445b-95fc-a39ee21ee7c4.png)
![image](https://user-images.githubusercontent.com/57345786/179697522-299bf1b7-5c18-4dec-ac58-47e3ca7fea93.png)
![image](https://user-images.githubusercontent.com/57345786/179697635-2b7349cd-5b59-47bc-b837-65ffc6ec5a71.png)
![image](https://user-images.githubusercontent.com/57345786/179697693-3fa4208c-58d4-42e9-94a5-c48df067ed35.png)
![image](https://user-images.githubusercontent.com/57345786/179697749-a2b047f5-f31c-4a79-ae68-760f5ddb42d9.png)
![image](https://user-images.githubusercontent.com/57345786/179697786-9581838f-d40d-44d8-93f9-f2b920776dce.png)

__Алфавит__

![image](https://user-images.githubusercontent.com/57345786/180237766-8fdd7acf-fa0e-4a02-afe5-cac722a98890.png)
![image](https://user-images.githubusercontent.com/57345786/180238033-3ab25d15-0cdd-467f-8569-02ef9a1f6fda.png)


__Садовник и помидоры__

![image](https://user-images.githubusercontent.com/57345786/180238526-ea277a85-3306-4640-9169-429f1c98b742.png)
![image](https://user-images.githubusercontent.com/57345786/180238252-1ea9d37e-93be-4a68-93f7-4cf6ad15cf9e.png)
