# Хеш таблица от 2 списъка

Във файл `hash_them.py`, напишете функция: `hash_them(keys, values)`, която:

* Взима два списъка `keys` и `values`, които може да не са с равна дължина
* Връща хеш таблица (речник), където за всеки елемент `key` от `keys`, който се намира на индекс `i`, има стойност `values[i]`
* За всeки `key`, за който нямаме съответстващо `value`, сложете `None` за стойност.
Например:

```python
>>> hash_them(["Ivan", "Maria"], [1, 2])
{ "Ivan": 1, "Maria": 2 }

>>> hash_them(["Ivan", "Maria"], [1])
{ "Ivan": 1, "Maria": None }
```
