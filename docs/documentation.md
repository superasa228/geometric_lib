# Документация
## Общее описание решения:
geometric_lib - библиотека функций, предназначенная для получения определённых параметров различных геометрических фигур

В настоящий момент готовы 4 файла:
- circle.py
- rectangle.py
- square.py
- triangle.py

Также было проведено функциональное тестирование кадого файла. Результаты тестирования хранятся в папке tests

## Описание каждой функции с примерами вызова
### circle.py
area(r) - принимает вещественное число r, возвращает площадь круга с радиусом r

area(1.0) = 3.141592653589793

area(4.5) = 63.61725123519331



perimeter(r) - принимает вещественное число r, возвращает периметр круга с радиусом r

perimeter(1.0) = 6.283185307179586

perimeter(4.5) = 28.274333882308138

---


### rectangle.py
area(a, b) - принимает вещественные числа a и b, возвращает площадь прямоугольника со сторонами a и b

area(1.0, 1.0) = 1.0

area(4.5, 7.5) = 33.75

perimeter(a, b) - принимает вещественные числа a и b, возвращает периметр прямоугольника со сторонами a и b

perimeter(1.0, 1.0) = 4.0

perimeter(4.5, 7.5) = 24.0


  ----

  
### square.py
area(a) - принимает вещественное число a, возвращает площадь квадрата со стороной a

area(1.0) = 1.0

area(4.5) = 20.25
  
perimeter(a) - принимает вещественное число a, возвращает периметр квадрата со стороной a

perimeter(1.0) = 4.0

perimeter(4.5) = 18.0


----


### triangle.py
area(a, h) - принимает вещественные числа a и h, возвращает площадь треугольника с основанием a и высотой h

area(1.0, 1.0) = 0.5

area(4.5, 7.5) = 16.875
  
perimeter(a, b, c) - принимает вещественные числа a, b и c, возвращает периметр треугольника со сторонами a, b и c

perimeter(1.0, 1.0, 1.0) = 3.0

perimeter(4.5, 7.5, 10.5) = 22.5

  
## История изменения проекта с хешами комитов
[ba9aeb3cea847b63a91ac378a2a6db758682460](https://github.com/superasa228/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)

  L-03: Circle and square added
  
smartiqa committed on Mar 4, 2021

-------------------

[d078c8d9ee6155f3cb0e577d28d337b791de28e2](https://github.com/superasa228/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)

  L-03: Docs added

smartiqa committed on Mar 4, 2021

-----------
  
[53e522218da5f022d2ae3fc065e4a738485e92be](https://github.com/superasa228/geometric_lib/commit/53e522218da5f022d2ae3fc065e4a738485e92be)

  add rectangle.py
  
superasa228 committed on Sep 11, 2023

-------------
  
[bac0c271d467a408d6f5a06334b8bb0b389063b3](https://github.com/superasa228/geometric_lib/commit/bac0c271d467a408d6f5a06334b8bb0b389063b3)

  add triangle.py
  
superasa228 committed on Sep 11, 2023

----------

[0f7981f4dea7d94f2a143a9bbc58a3b6c942b28b](https://github.com/superasa228/geometric_lib/commit/0f7981f4dea7d94f2a143a9bbc58a3b6c942b28b)

  fix rectangle.py
  
superasa228 committed on Sep 11, 2023

---------

[38ce93e22713c88da887de136115eb045b66f1a6](https://github.com/superasa228/geometric_lib/commit/38ce93e22713c88da887de136115eb045b66f1a6)

  added commentary in circle.py
  
superasa228 committed on Oct 3, 2023

---------

[e9fb0a146a5cd4e41fd5c6c090c88903a2f55001](https://github.com/superasa228/geometric_lib/commit/e9fb0a146a5cd4e41fd5c6c090c88903a2f55001)

  Added commentary in rectangle.py and fix rectangle.py
  
superasa228 committed on Oct 3, 2023

--------

[2482f6ff280dd31f708c20da71c6d683a5fcce40](https://github.com/superasa228/geometric_lib/commit/2482f6ff280dd31f708c20da71c6d683a5fcce40)

  Added commentary in square.py
  
superasa228 committed on Oct 3, 2023

---------

[fc1a24dc7715089ddc6b1ee74e2c2eb9843e97bd](https://github.com/superasa228/geometric_lib/commit/fc1a24dc7715089ddc6b1ee74e2c2eb9843e97bd)

  Added commentary in triangle.py
  
superasa228 committed on Oct 3, 2023

----------

[80e485e180045c3a5cd8d9bea6eca73748c515fb](https://github.com/superasa228/geometric_lib/commit/80e485e180045c3a5cd8d9bea6eca73748c515fb)

Create documentation in docs

superasa228 committed on Oct 4, 2023

---------

[e9afbd5a488bd1654be0672d402d1a42a4a4d56b](https://github.com/superasa228/geometric_lib/commit/e9afbd5a488bd1654be0672d402d1a42a4a4d56b)

Rename documentation to documentation.md

superasa228 committed on Oct 4, 2023

--------

[35e48c46a7e23d965b0323ebc9766b7be812b233](https://github.com/superasa228/geometric_lib/commit/35e48c46a7e23d965b0323ebc9766b7be812b233)

Update documentation.md

superasa228 committed on Oct 4, 2023

-----

[9f6ce665116721275238f2c5ac721ebbdb1fc5be](https://github.com/superasa228/geometric_lib/commit/9f6ce665116721275238f2c5ac721ebbdb1fc5be)

Update documentation.md 

superasa228 committed on Oct 4, 2023

-----

[3c0b73d76e5e5e6fef363cfb6d76128a55bf8383](https://github.com/superasa228/geometric_lib/commit/3c0b73d76e5e5e6fef363cfb6d76128a55bf8383)

Update documentation.md 

superasa228 committed on Oct 9, 2023

------

[07af2821eab1ec81de146c04ae53d30f04515428](https://github.com/superasa228/geometric_lib/commit/07af2821eab1ec81de146c04ae53d30f04515428)

Update circle.py 

superasa228 committed on Oct 9, 2023

----

[525bd277c9eba001236385c4221bbdf05271ab27](https://github.com/superasa228/geometric_lib/commit/525bd277c9eba001236385c4221bbdf05271ab27)

Update rectangle.py 

superasa228 committed on Oct 9, 2023

-------

[0b3ffe1f1c8f49662d2b422939edd7d6c569211c](https://github.com/superasa228/geometric_lib/commit/0b3ffe1f1c8f49662d2b422939edd7d6c569211c)

Update rectangle.py 

superasa228 committed on Oct 9, 2023

-------

[af7a432ab4cfe3236a3a78ca2b2e490a0b0621e1](https://github.com/superasa228/geometric_lib/commit/af7a432ab4cfe3236a3a78ca2b2e490a0b0621e1)

Update square.py 

superasa228 committed on Oct 9, 2023

-----

[0258398db357981dead515d47e7d8a021a1d461f](https://github.com/superasa228/geometric_lib/commit/0258398db357981dead515d47e7d8a021a1d461f)

Update triangle.py 

superasa228 committed on Oct 9, 2023

-------

[45ceeaf1b860825dad9b92abb74569e66b971b90](https://github.com/superasa228/geometric_lib/commit/45ceeaf1b860825dad9b92abb74569e66b971b90)

Create test_circle.py

superasa228 committed on Nov 10, 2023

-------

[3c22ebae3d5bc0a389695c824f17871df0dac66e](https://github.com/superasa228/geometric_lib/commit/3c22ebae3d5bc0a389695c824f17871df0dac66e)

Create test_rectangle.py

superasa228 committed on Nov 10, 2023

-------

[db5e2d2806951608dca1e14bb1f45150a0351c72](https://github.com/superasa228/geometric_lib/commit/db5e2d2806951608dca1e14bb1f45150a0351c72)

Create test_square.py

superasa228 committed on Nov 10, 2023

------

[e81a121fc2086ac1e762d1ba853b994c668343ce](https://github.com/superasa228/geometric_lib/commit/e81a121fc2086ac1e762d1ba853b994c668343ce)

Create test_triangle.py

superasa228 committed on Nov 10, 2023

-----

[33daee2069f275d920d580b104d23168eaf82d48](https://github.com/superasa228/geometric_lib/commit/33daee2069f275d920d580b104d23168eaf82d48)

add testing report files

superasa228 committed on Nov 10, 2023

------
